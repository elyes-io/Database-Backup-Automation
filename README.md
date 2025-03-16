# Database Backup Automation

## Description

The **Database Backup Automation** project is a Python-based tool that automatically backs up the structure of your MySQL database every day. This ensures your database schema (tables and relationships) is regularly saved, with each backup file named based on the date and time it was created. This project helps prevent data loss and allows for easy restoration of your database structure when needed.

## Features
- **Automated Daily Backups**: Runs automatically every day at a specified time.
- **Time-Stamped Backup Files**: Backup files are named with the current date and time
- **Easy Restoration**: The backup file can be used to restore the database schema if needed.

## Requirements
- `Python 3.x`
- `MySQL Database`
- `mysql-connector-python` library
- `.env` file containing ( DATABASE_USER=... , DATABASE_PASSWORD=... , DATABASE_NAME=... , PORT=... , HOST=... )

## How to Use

1. **Install Dependencies**  
   Make sure you have Python 3.x installed, then install the required packages :
   ```bash
   pip -r install requirements.txt 
   ```
2. **Containerize The Application**  
   a- Create an image
   ```bash
   docker build -t dataabse_image .
   ```
   
   b- Run a container
   ```bash
   docker run --name database_container -dt -p 5000:5000 --restart unless-stopped --network bridge database_image
   ```
   
   c- List the container
   ```bash
   docker ps database_container
   ```
