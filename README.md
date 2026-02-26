# Cybersecurity Log Monitoring System

## Overview
This project builds a **data warehouse-driven cybersecurity log monitoring system** with ETL pipelines, advanced SQL queries, Spark processing, Snowflake optimization, and interactive dashboards.

## Features
- ✅ Star & Snowflake schema design
- ✅ Advanced SQL (CTEs, Window Functions, Partitioning)
- ✅ Python ETL/ELT pipelines
- ✅ Apache Spark batch + streaming
- ✅ Snowflake clustering, time travel, semi-structured data
- ✅ Security: RBAC, Data Masking, Governance
- ✅ Performance tuning
- ✅ Interactive dashboard

## Project Structure
```
├── etl/                    # Python ETL pipelines
│   ├── extract.py         # Data extraction
│   ├── transform.py       # Data transformation
│   └── load.py            # Data loading
├── spark/                  # Apache Spark processing
│   ├── batch_processing.py
│   └── streaming_processing.py
├── sql/                    # SQL schemas & queries
│   ├── schema_star.sql    # Star schema
│   ├── schema_snowflake.sql
│   ├── advanced_queries.sql
│   └── optimization.sql
├── security/               # Security configurations
│   └── snowflake_security.sql
├── dashboard/              # Interactive dashboard
│   └── dashboard.ipynb
├── docs/                   # Documentation
│   ├── architecture-diagram.png
│   ├── final-report.pdf
│   └── Cybersecurity-Log-Monitoring-System.pptx
└── requirements.txt
```

## Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/raaji9/cybersecurity-log-monitoring-system.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment:
   - Set up Snowflake credentials in .env
   - Configure Spark if using local processing

## Technologies Used
- **Python 3.x** - ETL pipelines
- **Apache Spark** - Batch & Streaming processing
- **Snowflake** - Data warehouse
- **Plotly** - Interactive dashboards
- **SQL** - Advanced queries & optimization

## Security Features
- Role-Based Access Control (RBAC)
- Data Masking for sensitive fields (IP addresses)
- Column-level security

## Performance Optimizations
- Table clustering by date and severity
- Window functions for time-series analysis
- CTE for complex queries

---

**Project by:** Raaji Patel  
**GitHub:** https://github.com/raaji9/cybersecurity-log-monitoring-system
