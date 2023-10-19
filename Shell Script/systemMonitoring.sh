#!/bin/bash
# Monitors the CPU and Memory usage of the system using ps
# To use, make sure to grant execute permissions to the script using:
# -> chmod +x SystemMonitoring.sh

# Get CPU Usage
cpu_usage=$(ps aux | awk 'NR > 0 { s +=$3 }; END {print s "%"}')

# Get Memory Usage
memory_usage=$(ps aux | awk 'NR > 0 { s +=$4 }; END {print s "%"}')

echo "CPU Usage: $cpu_usage"
echo "Memory Usage: $memory_usage"
