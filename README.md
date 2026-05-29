# 🔐 SSH Brute Force Attack Detector

A Python-based security monitoring tool that analyzes Linux authentication logs to detect failed SSH login attempts, monitor user sessions, and identify potential brute-force attacks.

## 📖 Overview

SSH brute-force attacks are one of the most common methods attackers use to gain unauthorized access to Linux systems. This project automates the analysis of authentication logs (`auth.log`) to identify suspicious login activity and generate alerts when multiple failed login attempts are detected.

The tool helps security analysts and system administrators monitor authentication events and quickly identify potential attacks.

---

## 🚀 Features

* Detects failed SSH login attempts
* Extracts usernames from authentication logs
* Extracts timestamps of failed login events
* Monitors user session openings
* Monitors user session closures
* Counts failed authentication attempts
* Generates alerts for suspicious login activity
* Detects potential SSH brute-force attacks
* Creates a security report file
* Lightweight and easy to use

---

## 🛠️ Technologies Used

* Python 3
* Regular Expressions (Regex)
* Linux Authentication Logs
* File Handling

---

## 📂 Project Structure

```text
SSH-BruteForce-Detector/
│
├── ssh_bruteforce_detector.py
├── Log_file.txt
├── README.md
└── sample_auth.log
```

---

## ⚙️ Installation

Clone the repository:

```bash
https://github.com/vigneshVG20/SSH-Brute-Force-Attack-Detector.git
cd SSH-BruteForce-Detector
```

No additional Python libraries are required.

---

## ▶️ Usage

Run the script with appropriate permissions:

```bash
sudo python3 ssh_bruteforce_detector.py
```

The script reads:

```text
/var/log/auth.log
```

and generates:

```text
Log_file.txt
```

containing detected events and statistics.

---

## 🔍 Detection Logic

### Failed Login Detection

The script searches for authentication failures containing:

```text
password check failed
```

When a failed login is detected:

* Username is extracted
* Timestamp is extracted
* Security alert is generated
* Event is written to the report file

### Session Monitoring

The tool tracks:

```text
session opened for user
```

and

```text
session closed for user
```

to monitor authentication activity.

### Brute Force Detection

If failed login attempts exceed:

```text
5 attempts
```

the tool generates the following alert:

```text
Possible Brute Force Attack
```

---

## 📊 Sample Output

```text
[Alert] Login attempt for user admin is detected
Timestamp 2026-05-20T15:21:33.456+00:00

[Alert] Login attempt for user root is detected
Timestamp 2026-05-20T15:22:10.123+00:00

Total session opened: 12
Total session closes: 11
Total failed attempt: 7

Possible Brute Force Attack
```

---

## 📝 Generated Report

Example report:

```text
[Alert] Login attempt for user admin is detected
Timestamp 2026-05-20T15:21:33.456+00:00

[Alert] Login attempt for user root is detected
Timestamp 2026-05-20T15:22:10.123+00:00

Total session opened: 12
Total session closes: 11
Total failed attempt: 7
```

---

## 🎯 Skills Demonstrated

This project demonstrates:

* Security Log Analysis
* SSH Authentication Monitoring
* Threat Detection
* Brute Force Attack Detection
* Regular Expressions (Regex)
* Python Automation
* Linux Security
* Incident Monitoring
* SOC Analyst Fundamentals

---

## 🔮 Future Enhancements

* Detect source IP addresses of attackers
* Track repeated failures per IP address
* Real-time log monitoring
* Email alert notifications
* CSV and JSON report export
* Dashboard visualization
* SIEM integration
* Automatic IP blocking using firewall rules
* Geo-location analysis of attacker IPs

---

## ⚠️ Disclaimer

This project is intended for educational and defensive cybersecurity purposes only. Use it only on systems and logs that you own or are authorized to analyze.

---

## 👨‍💻 Author

**Vignesh S**

Aspiring SOC Analyst | Cybersecurity Enthusiast

### Connect With Me

* LinkedIn: linkedin.com/in/vignesh-s20
* GitHub: github.com/vigneshVG20

---

## ⭐ If you found this project useful, consider giving it a star!
