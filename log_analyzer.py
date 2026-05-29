import re

log_file = open("/var/log/auth.log", "r")

failed_attempt = 0
session_opened = 0
session_closed = 0

with open("Log_file.txt", "w") as f:

    for line in log_file:

        if "password check failed" in line:
            failed_attempt += 1

            match = re.search(
                r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+\+\d{2}:\d{2}).*user \(([^)]+)\)',
                line
            )

            if match:
                print(f"[Alert] Login attempt for user {match.group(2)} is detected")
                print(f"Timestamp {match.group(1)}")

                f.write(f"[Alert] Login attempt for user {match.group(2)} is detected\n")
                f.write(f"Timestamp {match.group(1)}\n")

        elif "session opened for user" in line:
            session_opened += 1

        elif "session closed for user" in line:
            session_closed += 1

    f.write(f"\nTotal session opened: {session_opened}\n")
    f.write(f"Total session closes: {session_closed}\n")
    f.write(f"Total failed attempt: {failed_attempt}\n")

print("Total session opened", session_opened)
print("Total session closes", session_closed)
print("Total failed attempt:", failed_attempt)
if failed_attempt > 5:
    print("Possible Brute Force Attack")
log_file.close()
