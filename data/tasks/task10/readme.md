# Web Logs Analysis with PySpark

This project demonstrates a simple Big Data ETL pipeline for analyzing web server logs using Apache Spark and Python.

---

## Project Structure

---

## Objective

The goal is to parse and analyze a large-scale web log file to derive meaningful metrics using PySpark.

The log contains:
- IP addresses
- Timestamps
- Requested URLs
- HTTP status codes
- User agents

---

## Features Implemented

1. **Total Requests per IP**  
   Identify the most active users or bots based on IP address.

2. **Most Visited URLs**  
   Determine which endpoints are most frequently accessed.

3. **HTTP Status Distribution**  
   Check how many requests succeeded (200), failed (404, 500), etc.

---

## Requirements

- Python 3.7+
- PySpark

Install PySpark via pip:

```bash
pip install pyspark
```
**csv**
ip,timestamp,url,status,user_agent
192.168.1.1,2023-10-01 12:45:00,/home,200,Mozilla/5.0
192.168.1.2,2023-10-01 12:46:10,/about,404,Chrome/91.0
