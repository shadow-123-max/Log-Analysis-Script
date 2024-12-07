# Log-Analysis-Script


This Python script analyzes a log file to provide insights into the requests made by users, the most accessed endpoints, and potential suspicious activities such as failed login attempts. It is designed to help in identifying patterns such as brute force login attempts based on status codes and message patterns in the log file.

#Features

1. IP Activity Analysis: 
   - Tracks the number of requests made by each IP address.
   - Displays a list of IP addresses sorted by request count in descending order.

2. Endpoint Access Analysis: 
   - Identifies the most frequently accessed endpoint.
   - Displays the endpoint and the number of times it was accessed.

3. Suspicious Activity Detection: 
   - Detects failed login attempts based on HTTP status code `401` and the presence of "Invalid credentials" in the message.
   - Flags IP addresses that exceed a defined threshold (default is 10 failed login attempts).

4. CSV Output: 
   - The analysis results are saved to a CSV file (`log_analysis_results.csv`) for further review.

## Requirements

- Python 3.x
- `csv` and `collections` modules (These are part of Python's standard library, so no additional installations are required.)

## Installation

1. Clone the repository:
   ```bash
   https://github.com/shadow-123-max/Log-Analysis-Script
  [ git clone https://shadow-123-max/Log-Analysis-Script](https://github.com/shadow-123-max/Log-Analysis-Script)
  
2.Place your log file (e.g., sample.log) in the same directory or update the file_path in the script accordingly.
Run the script:
python log_analysis.py

3.The script will:
   Parse the log file.
   Display the analysis results in the terminal.
   Save the results to a CSV file (log_analysis_results.csv).
   
Example Output
IP Activity Summary:
IP Address          Request Count
-----------------------------------
203.0.113.5         8
198.51.100.23       8
192.168.1.1         7
10.0.0.2            6
192.168.1.100       5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Summary:
IP Address          Failed Login Count
-----------------------------------
203.0.113.5         5
192.168.1.100       3


