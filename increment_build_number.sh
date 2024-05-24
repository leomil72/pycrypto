#!/bin/sh
# get build number from file
arr=()
while IFS= read -r line; do
arr+=("$line")
done < build_number
date_today=$(date '+%Y%m%d')
date_file=${arr[0]}
number=${arr[1]}
if [ "$date_today" != "$date_file" ]; then
number=1
date_file=${date_today}
else
number=$(($number+1))
fi
echo $date_file > build_number
echo $number >> build_number

