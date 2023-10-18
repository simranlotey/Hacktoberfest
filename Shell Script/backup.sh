#!/bin/bash
#
# To use, make sure you have rsync pkg
# And then,
# -> backup folderName folderNameForBackup
#
# Check to make sure the user has entered exactly two arguements.
  if [ $# -ne 2 ]
  then
	  echo "Usage: backup.sh <source_directory> <target_directory>"
	  echo "Please try again."
	  exit 1
  fi

# Check rsync installation
if ! command -v rsync > /dev/null 2>&1  
# command -v packageName, to check for package and send msgs to /dev/null
then
	echo "This script requires rsync to be installed."
	echo "Please use your distribution's package manager to install it"
	exit 2
fi

# get date and store in the format YYYY-MM-DD
current_date=$(date +%Y-%m-%d)

rsync_options="-avb --backup-dir $2/$current_date --delete"
# -a(archieve) v(verbose) b( Creates backups), $2/$current_date -> our fileName , --delete will sync with files ( meaning, if we delete one script that has backup, then backup file will be deleted too

$(which rsync) $rsync_options $1 $2/current >> backup_$current_date.log  # $(which rsync) runs rsync in sub-shell

