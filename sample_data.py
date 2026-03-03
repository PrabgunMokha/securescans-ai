"""
sample_data.py — Sample vulnerable data for testing SecureScan AI.
Contains realistic examples of every threat type the scanner detects.
"""

SAMPLE_DATA = """# Sample Vulnerable Data — For Testing
# ====================================

# AWS Credentials (leaked in config)
AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# API Tokens
api_key = "sk-proj-abc123def456ghi789jkl012mno345"
auth_token = "ghp_AB1CDeFgHiJkLmNoPqRsTuVwXyZ012345"
SECRET_TOKEN=superSecretTokenValue1234567890abcdef

# JWT Token
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiYWRtaW4iOnRydWV9.dyt0CoTl4WoVjAHI9Q_CwSKhl6d_9rhM3NrXuJttkao

# Database password
password = "MyS3cur3P@ssw0rd!"

# Private Key
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Z3VS5JJcds3xfn/ygWyF...
-----END RSA PRIVATE KEY-----

# PII - Indian Documents
Aadhaar: 2345 6789 0123
PAN: ABCDE1234F
Phone: +91 9876543210
Phone: 8765432109

# Email Addresses
john.doe@gmail.com
admin@securescans.ai
test.user@company.org

# Financial
UPI: user.name@okaxis
UPI: payment@ybl

# Credit Card Numbers
4532015112830366
5425233430109903

# Network
Internal Server: 192.168.1.105
Database Host: 10.0.0.42
URL: https://admin:password123@internal.server.com/api

# SQL Queries
SELECT * FROM users WHERE role = 'admin'
DELETE FROM sessions WHERE expired = true
"""
