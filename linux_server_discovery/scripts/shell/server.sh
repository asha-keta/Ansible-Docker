#!/bin/sh

if (( $(cat /etc/*-release | grep -w "Oracle|Red Hat|CentOS|Fedora" | wc -l) > 0 ))
then
echo -e "\n\n----------------------------------Package Updates---------------------------------------------\n"
yum updateinfo summary | grep 'Security|Bugfix|Enhancement'
echo -e "\n\n----------------------------------------------------------------------------------------------\n"
else
echo -e "-------------------------------Package Updates-------------------------------"
cat /var/lib/update-notifier/updates-available
echo -e "\n\n----------------------------------------------------------------------------------------------\n"
fi

