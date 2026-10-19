# AI Prompt Injection Detector

A Python security tool that detects prompt injection attacks in text and web content.

## What it does
- Scans text manually or fetches content from a URL
- Detects known prompt injection patterns
- Reports number of threats found

## Why it matters
Prompt injection is the #1 vulnerability in AI systems (OWASP LLM Top 10).
This tool helps developers test their AI applications for injection vulnerabilities.

## How to use

python3 detector.py

Choose option 1 to scan text or option 2 to scan a URL.

## Example output

=== AI Prompt Injection Detector v2 ===
1. Scan text manually
2. Scan a URL

Choose (1 or 2): 1
Enter text to scan: ignore previous instructions

=== SCAN RESULTS ===
WARNING: 1 prompt injection pattern(s) detected!
  - ignore previous instructions

## Skills demonstrated
- Python (requests, string matching)
- AI Security — prompt injection detection
- OWASP LLM Top 10 awareness
