#! /bin/bash

Local_path=$1

Home_path=$2

OLD_DATE=`date +'%Y-%m-%d' -d 'now - 10 days'`

Remote_Path=$3

To_Remove_date=$4

Remote_Server_IP='7.7.1.120'

Remote_Server_User='root'

Archive_Server_IP='7.7.1.101'

Archive_Server_user='root'



echo "Backup Date : $OLD_DATE"
echo "To Remove Date : $To_Remove_date"
echo "Remote Path : $2"
echo "Local Path : $1"


size=`df -h | grep $Home_path | awk '{print $5}' | sed 's/.$//'`

if [ $size -gt 95 ]
then
        find $Local_Path -type f -mtime +$To_Remove_date  -exec rm "{}"
        ssh $Remote_Server_User@$Remote_Server_IP << EOF
                find $Remote_Path -type f -newermt $OLD_DATE -exec scp -r "{}" $Archive_Server_user@$Archive_Server_IP:$Local_path  \;
EOF

else
        ssh $Remote_Server_User@$Remote_Server_IP << EOF
                find $Remote_Path -type f -newermt $OLD_DATE -exec scp -r "{}" $Archive_Server_user@$Archive_Server_IP:$Local_path  \;
EOF

fi
