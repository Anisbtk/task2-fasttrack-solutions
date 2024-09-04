
# Web Health Check Script

## Overview

This Python script is designed to check the health of a web application by sending an HTTP request and verifying the returned status code. If the status code is not 200, it triggers an alert via email. The script can be easily automated using cron or integrated with AWS CloudWatch for advanced monitoring.

## Features

- Sends an HTTP GET request to check the health of a specified web application.
- Sends an email alert if the status code is not 200 or if the connection fails.
- Customizable to include the URL and recipient email address.
- Includes error handling for network failures.
- Easily integratable with AWS CloudWatch or any other monitoring tool for automation.

## File Structure

```
/web-health-check-script/
│
├── /scripts/
│   └── health_check.py                     # The main Python script
│
├── .github/
│   └── workflows/
│       └── health-check-ci.yml             # GitHub Actions workflow (optional for CI/CD)
│
├── README.md                               # Documentation for how to use the script
```

## Prerequisites

- Python 3.x
- `requests` library
- A valid Gmail account for sending alert emails (can be modified to use other email providers).

To install dependencies, run:
```
pip install -r requirements.txt
```

## Usage

1. Clone this repository and navigate to the project folder:
```
git clone 
cd task2
```

2. Modify the `health_check.py` script to specify the URL you want to check and the email recipient for alerts:
```python
url_to_check = "https://web.com"
recipient_email = "email"
```

3. Run the Python script:
```
python scripts/health_check.py
```

4. To automate execution, set up a cron job or integrate with AWS CloudWatch.

### Example Cron Job (Linux)
To run the script every 5 minutes:
```
*/5 * * * * /usr/bin/python3 /path/to/your/script.py
```


