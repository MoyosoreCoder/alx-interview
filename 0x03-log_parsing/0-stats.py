#!/usr/bin/python3
"""Python script that reads stdin line by line and computes metrics"""
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    """Print the statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption"""
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) != 10:
                continue
            ip, dash, date, method, resource, protocol, status, size = parts[0], parts[1], parts[3] + parts[4], parts[5], parts[6], parts[7], parts[8], parts[9]
            if method != '"GET' or resource != '/projects/260' or protocol != 'HTTP/1.1"':
                continue

            # Compute file size
            total_size += int(size)
            # Count status codes
            if status in status_codes:
                status_codes[status] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

        except Exception:
            continue

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
