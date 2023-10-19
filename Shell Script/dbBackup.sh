#!/bin/bash
# To backup database

username="enter username here"
password="enter password here"
database="database_name"
backup_dir="/Users/ab01/Library/CloudStorage/OneDrive-AmityUniversity/Programming/Shell"

mysqldump -u $username -p$password $database > $backup_dir/db_backup_$(date +%Y%m%d%H%M%S).sql
echo "Database backup created: db_backup_$(date +%Y%m%d%H%M%S).sql"
