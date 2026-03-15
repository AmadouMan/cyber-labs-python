import subprocess

print("\n=== SOC Registry Persistence Hunter v3 ===\n")

run_keys = [
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run",
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce",
    r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run",
    r"HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce"
]

suspicious_paths = [
    "appdata",
    "temp",
    "public",
    "downloads",
    ".ps1",
    ".vbs",
    ".bat",
    "powershell",
    "cmd.exe",
    "wscript",
    "mshta"
]

alerts = []

for key in run_keys:
    print(f"\n[*] Checking: {key}")

    try:
        output = subprocess.check_output(
            f'reg query "{key}"',
            shell=True,
            text=True,
            errors="ignore"
        )

        lines = output.splitlines()

        for line in lines:
            for indicator in suspicious_paths:
                if indicator.lower() in line.lower():
                    alerts.append((key, line.strip()))
    except:
        pass


print("\n====== Registry Persistence Report ======\n")

if alerts:
    for key, entry in alerts:
        print("🚨 Suspicious Registry Autorun Found")
        print("Key:", key)
        print("Entry:", entry)
        print("-" * 50)
else:
    print("No obvious suspicious registry persistence detected.")