#!/bin/bash

#variables
backup_dir="/home/hkranjan"
db_name="new_db"
DATE=$(date +"%F_%H-%M-%S")
backup_file="$backup_dir/${db_name}_$date.sql"

#create a backup
mysqldump -u root -pHimanshu@423 $db_name > $backup_file

#optional: delete backups older than 7 days
find $backup_dir -type f -name "*.sql" -mtime +7 -exec rm {} \;

echo "backup completed: $backup_file"
