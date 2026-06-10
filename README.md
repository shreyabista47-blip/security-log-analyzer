# Security Log Analyzer

## Overview

Security Log Analyzer is a Python-based tool that processes authentication logs and identifies suspicious login activity.

The tool analyzes failed login attempts, groups them by source IP address, and generates alerts for potential brute-force attacks.

## Features

- Parse authentication logs
- Count failed login attempts by IP address
- Detect potential brute-force attacks
- Assign severity levels
- Generate security analysis reports

## Technologies Used

- Python
- File Handling
- Dictionaries
- Conditional Logic

## Sample Detection

Input:

FAILED LOGIN - user: admin - IP: 192.168.1.100

Output:

IP Address: 192.168.1.100
Failed Logins: 5
Severity: HIGH
ALERT: Possible Brute Force Attack

## Future Improvements

- Export reports to CSV
- Email alerting
- Real-time log monitoring
- Integration with SIEM platforms
