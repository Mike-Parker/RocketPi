#!/bin/sh

IP=$1
KEY=$2
TMPFILE=/tmp/rocketpi-${KEY}.tmp

trap cleanup 0 1 2 3 6 15

cleanup()
{
  if [ -e $TMPFILE ]; then  
    rm $TMPFILE; 
    exit 1
  fi
}

if [ -e /tmp/rocketpi-*.tmp ]; then
  exit 1
fi

while :
do
  ping -c 1 $IP >& /dev/null
  
  if [ $? == 0 ]; then
    echo $$ > $TMPFILE
  else
    exit 1
  fi
  
  sleep 1
  
done