import subprocess

ip = input("Enter IP to ping: ")

result = subprocess.run(
    ["ping", "-n", "1", ip],
    capture_output=True
)

if result.returncode == 0:
    print(f"{ip} is UP ✅")
else:
    print(f"{ip} is DOWN ❌")