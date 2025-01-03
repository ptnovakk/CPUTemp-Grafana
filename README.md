# CPUTemp-Grafana
Raspberry Pi CPU Temperature Logger

This repository contains a Python script designed for logging the CPU temperature of a Raspberry Pi 3B to an SQLite database. The project includes:

Temperature Reading: Utilizes the Pi's thermal zone to fetch real-time CPU temperature.
Database Integration: Stores temperature data in an SQLite database with automatic timestamping for each entry.
Scheduled Logging: Example setup for running temperature logging via cron jobs for automated, regular updates.

Key Features:
Simple setup with minimal dependencies.
Continuous logging with configurable intervals.
SQL queries for data retrieval included.

Usage:
Install SQLite on your Raspberry Pi.
Clone this repository, adjust the Python script if necessary, and run it either manually or through cron for automatic logging.

Contributions: 
Feel free to fork this repo, make enhancements, or report issues.

License: Creative Commons Zero 1.0 (CC0 1.0)

Tags: Raspberry Pi, CPU Temperature, IoT, SQLite, Python, Data Logging
