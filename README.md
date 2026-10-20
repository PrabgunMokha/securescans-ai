# SecureScans AI

A Streamlit dashboard that scans pasted text and uploaded text files for potentially exposed credentials, personal information, and suspicious code patterns.

The detection engine uses 16 regular-expression rules. It runs locally without an LLM, external AI service, embeddings, or a vector database.

## Features

- Paste text or upload logs, configuration files, source code, and other supported text formats.
- Detect patterns for AWS keys, private keys, API tokens, passwords, JWTs, and generic secrets.
- Flag email addresses, Indian phone numbers, Aadhaar/PAN patterns, credit-card patterns, and UPI IDs.
- Identify IPv4 addresses, credential-bearing URLs, and SQL-like statements.
- View severity counts, category charts, a risk gauge, and remediation suggestions.
- Review session scan history and download plain-text reports.
- Try the bundled sample data.

## Quick start

From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local address displayed by Streamlit, normally [localhost:8501](http://localhost:8501).

## Usage

1. Paste text or upload a file in the Scanner view.
2. Select **INITIATE THREAT SCAN**. To explore the demo, select **Load Sample Data** first.
3. Inspect findings, severities, matched values, and suggested remediation.
4. Download a report or switch to History to review scans from the current session.

Supported upload extensions include `.txt`, `.csv`, `.log`, `.json`, `.xml`, `.yml`, `.yaml`, `.env`, `.cfg`, `.ini`, `.conf`, `.py`, and `.js`. Files are decoded as UTF-8 with undecodable bytes ignored.

## Scoring

Matches are deduplicated within each detection rule and weighted by severity: Critical = 25, High = 15, Medium = 8, and Low = 3. The total is capped at 100.

| Score | Label |
| --- | --- |
| 0 | CLEAN |
| 1–24 | LOW |
| 25–49 | MEDIUM |
| 50–74 | HIGH |
| 75–100 | CRITICAL |

The score is a rule-based indicator, not a calibrated probability of compromise. A value may match more than one rule.

## Project structure

| File | Purpose |
| --- | --- |
| `app.py` | Dashboard, input controls, history, and report export |
| `scanner_logic.py` | Detection patterns, scoring, and remediation mappings |
| `charts.py` | Plotly visualizations |
| `styles.py` | Dashboard styling |
| `sample_data.py` | Example scan input |
| `requirements.txt` | Streamlit and Plotly dependencies |

## Limitations

Pattern matches require human review. Ordinary SQL statements can trigger the SQL rule, and matching an identifier format does not validate that identifier or prove a breach. The scanner can miss obfuscated or unfamiliar secrets. It does not execute code, scan networks, inspect binary documents, or establish regulatory compliance. History is held in Streamlit session state rather than persistent storage. Findings and downloaded reports include matched values, so handle them as sensitive data.
