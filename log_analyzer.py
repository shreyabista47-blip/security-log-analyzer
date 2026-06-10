print("Security Log Analyzer Started\n")

log_file = open("sample_logs.txt", "r")
logs = log_file.readlines()
log_file.close()

ip_counts = {}

for line in logs:

    if "FAILED LOGIN" in line:

        ip = line.split("IP: ")[1].strip()

        if ip in ip_counts:
            ip_counts[ip] += 1
        else:
            ip_counts[ip] = 1

report = "=== Security Analysis Report ===\n\n"

for ip, count in ip_counts.items():

    report += f"IP Address: {ip}\n"
    report += f"Failed Logins: {count}\n"

    if count >= 5:
        report += "Severity: HIGH\n"
        report += "ALERT: Possible Brute Force Attack\n"

    elif count >= 3:
        report += "Severity: MEDIUM\n"
        report += "Suspicious Activity Detected\n"

    else:
        report += "Severity: LOW\n"

    report += "\n"

print(report)

report_file = open("report.txt", "w")
report_file.write(report)
report_file.close()

print("Report saved to report.txt")