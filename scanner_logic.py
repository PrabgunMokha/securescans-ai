"""
scanner_logic.py — SecureScan AI Detection Engine
Scans text for 16 types of security threats using regex patterns.
"""

import re
from datetime import datetime

PATTERNS = [
    ("AWS Access Key",      r'(?:A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}',  "Critical", "Credentials"),
    ("AWS Secret Key",      r'(?i)aws[_\-\s]*secret[_\-\s]*(?:access)?[_\-\s]*key[\s]*[=:]\s*["\']?([A-Za-z0-9/+=]{40})',  "Critical", "Credentials"),
    ("Private Key",         r'-----BEGIN\s(?:RSA|DSA|EC|OPENSSH|PGP)?\s?PRIVATE KEY(?:\sBLOCK)?-----',  "Critical", "Credentials"),
    ("API Key / Token",     r'(?i)(?:api[_\-\s]*key|api[_\-\s]*token|access[_\-\s]*token|auth[_\-\s]*token|secret[_\-\s]*key|secret[_\-\s]*token)[\s]*[=:]\s*["\']?([A-Za-z0-9\-._~+/]{20,})',  "Critical", "Credentials"),
    ("Hardcoded Password",  r'(?i)(?:password|passwd|pwd)[\s]*[=:]\s*["\']([^"\']{6,})["\']',  "Critical", "Credentials"),
    ("JWT Token",           r'eyJ[A-Za-z0-9_-]{10,}\.eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}',  "High", "Credentials"),
    ("Generic Secret",      r'(?i)(?:secret|token|bearer)[\s]*[=:]\s*["\']?([A-Za-z0-9\-._~+/]{16,})',  "High", "Credentials"),
    ("Email Address",       r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}',  "Medium", "PII"),
    ("Phone Number",        r'\b(?:\+91[\s\-]?)?[6-9]\d{9}\b',  "Medium", "PII"),
    ("Aadhaar Number",      r'\b[2-9]\d{3}\s?\d{4}\s?\d{4}\b',  "High", "PII"),
    ("PAN Number",          r'\b[A-Z]{5}[0-9]{4}[A-Z]\b',  "High", "PII"),
    ("Credit Card",         r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})\b',  "Critical", "PII"),
    ("UPI ID",              r'[a-zA-Z0-9.\-_]+@(?:okaxis|okhdfc|upi|apl|axl|ybl|okicici|oksbi|paytm|ibl)',  "High", "Financial"),
    ("IP Address",          r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b',  "Low", "Network"),
    ("URL with Credentials", r'https?://[^\s:]+:[^\s@]+@[^\s]+',  "Critical", "Network"),
    ("SQL Injection",       r"(?i)(?:SELECT|INSERT|UPDATE|DELETE|DROP|UNION)\s+.*(?:FROM|INTO|TABLE|SET|ALL)\s",  "High", "Code Vulnerability"),
]

WEIGHTS = {"Critical": 25, "High": 15, "Medium": 8, "Low": 3}

REMEDIATIONS = {
    "Credentials": [
        "🔑 Rotate all exposed keys/tokens immediately",
        "🔒 Use environment variables or a secrets manager",
        "📝 Add sensitive files to .gitignore",
    ],
    "PII": [
        "🛡️ Encrypt PII at rest and in transit",
        "🗑️ Remove PII from logs and config files",
        "📋 Ensure GDPR / data protection compliance",
    ],
    "Financial": [
        "💳 Never store financial IDs in plaintext",
        "🔒 Use tokenization for payment data",
    ],
    "Network": [
        "🌐 Avoid hardcoding IPs in source code",
        "🔒 Never embed credentials in URLs",
    ],
    "Code Vulnerability": [
        "🛡️ Use parameterized queries / prepared statements",
        "🔍 Implement input validation and sanitization",
    ],
}


def read_uploaded_file(uploaded_file):
    """Read text from an uploaded file."""
    try:
        content = uploaded_file.read()
        return content.decode("utf-8", errors="ignore") if isinstance(content, bytes) else content
    except Exception as e:
        return f"[Error reading file: {e}]"


def run_scan(text):
    """Scan text for all 16 threat patterns. Returns a results dictionary."""
    findings = []
    severity_counts = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0}
    category_counts = {}

    for name, pattern, severity, category in PATTERNS:
        matches = list(dict.fromkeys(re.findall(pattern, text)))  # find + deduplicate
        if matches:
            findings.append({"name": name, "category": category, "severity": severity,
                             "description": name, "matches": matches, "count": len(matches)})
            severity_counts[severity] += len(matches)
            category_counts[category] = category_counts.get(category, 0) + len(matches)

    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    findings.sort(key=lambda f: order[f["severity"]])
    risk_score = min(100, sum(WEIGHTS[f["severity"]] * f["count"] for f in findings))
    risk_level = "CRITICAL" if risk_score >= 75 else "HIGH" if risk_score >= 50 else "MEDIUM" if risk_score >= 25 else "LOW" if risk_score > 0 else "CLEAN"
    remediation = []
    for cat in category_counts:
        remediation.extend(REMEDIATIONS.get(cat, []))

    return {
        "findings": findings,
        "severity_counts": severity_counts,
        "category_counts": category_counts,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "total_findings": sum(f["count"] for f in findings),
        "remediation": remediation,
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input_length": len(text),
    }