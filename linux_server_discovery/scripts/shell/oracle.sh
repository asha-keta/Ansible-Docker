if id oracle >/dev/null 2>&1; then
/bin/ps -ef|grep pmon
else
echo "oracle user does not exist on $(hostname)"
fi
