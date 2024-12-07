import csv
from collections import defaultdict, Counter


def analyze_log_file(file_path, threshold=10):
    try:
        ip_activity = Counter()
        endpoint_stats = Counter()
        login_failures = defaultdict(int)

        with open(file_path, 'r') as log_file:
            for line in log_file:
                fields = line.strip().split()
                if len(fields) < 9:
                    continue  # Skip lines that don't contain enough data

                ip = fields[0]
                endpoint = fields[6]
                status_code = fields[8]
                message = line.split('"')[-1].strip()

                # Tally requests by IP address
                ip_activity[ip] += 1

                # Tally endpoint access (excluding login attempts)
                endpoint_stats[endpoint] += 1

                # Record failed login attempts
                if status_code == "401" or "Invalid credentials" in message:
                    login_failures[ip] += 1

        # Sort IP activity in descending order
        sorted_ip_activity = sorted(ip_activity.items(), key=lambda x: x[1], reverse=True)

        # Identify the most accessed endpoint
        most_accessed = max(endpoint_stats.items(), key=lambda x: x[1])

        # Flag IPs with failed login attempts above threshold
        suspicious_ips = [(ip, count) for ip, count in login_failures.items() if count >= threshold]

        # Display the results in a human-readable format
        print("\nIP Activity Summary:")
        print(f"{'IP Address':<20}{'Request Count':<15}")
        print("-" * 35)
        for ip, count in sorted_ip_activity:
            print(f"{ip:<20}{count:<15}")

        print("\nMost Frequently Accessed Endpoint:")
        print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

        print("\nSuspicious Activity Summary:")
        if suspicious_ips:
            print(f"{'IP Address':<20}{'Failed Login Count':<15}")
            print("-" * 35)
            for ip, count in suspicious_ips:
                print(f"{ip:<20}{count:<15}")
        else:
            print("No suspicious activity found.")

        # Write the analysis results to a CSV file
        with open("log_analysis_results.csv", "w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            # Write IP activity summary
            writer.writerow(["IP Activity Summary"])
            writer.writerow(["IP Address", "Request Count"])
            writer.writerows(sorted_ip_activity)
            writer.writerow([])

            # Write most accessed endpoint
            writer.writerow(["Most Accessed Endpoint"])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow(most_accessed)
            writer.writerow([])

            # Write suspicious activity
            writer.writerow(["Suspicious Activity Summary"])
            writer.writerow(["IP Address", "Failed Login Count"])
            writer.writerows(suspicious_ips)

        print("\nAnalysis results saved to 'log_analysis_results.csv'.")

    except FileNotFoundError:
        print("Error: The log file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Trigger log analysis
analyze_log_file("sample.log")
