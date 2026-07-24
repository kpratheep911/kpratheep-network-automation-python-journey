import subprocess

ip = "8.8.8.8"
result = subprocess.run(["ping", "-n", "1", ip], capture_output=True)

print(result.returncode)