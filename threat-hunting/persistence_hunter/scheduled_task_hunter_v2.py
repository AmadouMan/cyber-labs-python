import subprocess

print("\n=== SOC Scheduled Task Persistence Hunter v2 ===\n")

suspicious_keywords = [
    "powershell",
    "cmd.exe",
    "wscript",
    "cscript",
    "mshta",
    "temp",
    "appdata",
    "public",
    ".ps1",
    ".vbs",
    ".bat",
    ".exe"
]

print("[*] Enumerating Scheduled Tasks...\n")

try:
    output = subprocess.check_output(
        "schtasks /query /fo LIST /v",
        shell=True,
        text=True,
        errors="ignore"
    )

    tasks = output.split("HostName:")

    alerts = []

    for task in tasks:
        for keyword in suspicious_keywords:
            if keyword.lower() in task.lower():
                alerts.append(task)
                break

    print("====== Threat Hunting Report ======\n")

    if alerts:
        for a in alerts:
            print("🚨 Suspicious Scheduled Task Found:\n")
            print(a[:800])
            print("-" * 50)
    else:
        print("No suspicious scheduled tasks detected.")

except Exception as e:
    print("Error running schtasks:", e)