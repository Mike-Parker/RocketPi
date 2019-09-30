#!/bin/sh

echo 'Content-type: text/html'
echo ''

read QUERY_STRING

IFS="&"

for i in $QUERY_STRING ; do
  IFS="="
  set -- $i
  eval "$(echo $1)=$2"
  IFS="&"
done

if [ $start_link == "START" ]
  then
  
  #IP_ADDR=`netstat -tn 2>/dev/null | grep ':80' | sed -e 's/:/ /g' | awk '{print $6}' | sort  -u`
  #KEY=`date | md5sum | awk '{print $1}'`
  
  ### DEBUG ###
  IP_ADDR='192.168.0.187'
  #IP_ADDR='192.168.0.187 192.168.0.99'
  KEY=`date | md5 | awk '{print $1}'`
  ### END DEBUG ###

  CNT=`echo $IP_ADDR | grep -c ' '`
 
  ### DEBUG ###
  #echo "IP Address = $IP_ADDR"
  #echo "Client count = $CNT"
  #echo "Key = $KEY"
  ### END DEBUG ###
  
  if [ $CNT != 0 ]; then
    echo "ERROR: No than one client connected"
    exit 1
  else
    # Invoke ping process and redirect STDOUT & STDERR.
    # Otherwise script waits for invoked process to complete
    ./ping.sh $IP_ADDR $KEY >& /dev/null &
  fi
else if [ $stop_link == "STOP" ]
  then
    PID=`cat /tmp/rocketpi-$KEY.tmp`
    kill $PID
    KEY=""
  fi
fi

sleep 2

if ( [ ! -z $KEY ] && [ -f /tmp/rocketpi-$KEY.tmp ] ) || [ -z $KEY ]
  then
  echo '<html>'
  echo '<head>'
  echo '<script type="text/javascript">'
  echo 'window.onload = function(){'
  echo 'document.forms["form"].submit();'
  echo '}'
  echo '</script>'
  echo '<link rel="stylesheet" href="../rocketpi.css" type="text/css">'
  echo '</head>'
  echo '<body>'
  echo '<form action="home.cgi" method="POST" id="form">'
  echo '<input type="hidden" name="KEY" value="'$KEY'">'
  echo '</form>'
  echo '</body>'
  echo '</html>'
else
  echo "ERROR: Link not established"
  exit 1
fi


