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
   git clone https://shadow-123-max/Log-Analysis-Script
