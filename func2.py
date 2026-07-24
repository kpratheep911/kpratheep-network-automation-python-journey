def check_router(hostname):
    print("\nChecking:", hostname)
    print("Step 1: Check interface status on", hostname)
    print("Step 2: Check the logs on", hostname)
    print("Step 3: Ping the gateway from", hostname)
    print("Step 4: Send alert email for", hostname)

check_router(R1)
check_router(R2)
check_router("R3")
check_router(h1)
