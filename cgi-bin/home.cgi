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

if [ -z "$KEY" ]; then
  KEY="LINK NOT ESTABLISHED"
  LINK_START_EN=""
  LINK_STOP_EN="disabled"
  SYNC_EN="disabled"
else
  LINK_START_EN="disabled"
  LINK_STOP_EN=""
  SYNC_EN=""
fi

cat <<EOF

<!DOCTYPE html>
<html>
  <head>
    <meta name="mobile-web-app-capable" content="yes">
    <script type="text/javascript" src="../rocketpi.js"></script>
    <link rel="stylesheet" href="../rocketpi.css" type="text/css">
    <title>RocketPi Homepage</title>
  </head>
  <body>
    <h1>ROCKETPI MISSION CONTROL</h1>
    <form action="handler.cgi" method="POST" id="form" onsubmit="add_dt_field()">
      <table summary="RocketPi control interface" align="center">
        <tr><td colspan=2><hr></td></tr>
        <tr>
          <td class="row_headings">Secure link key</td>
          <td>
            <input type="text" name="KEY" value="$KEY" readonly size="100">
          </td>
        </tr>
        <tr>
          <td></td><td>
            <input type="submit" class="block_button half green" name="start_link" value="START" $LINK_START_EN>
            <input type="submit" class="block_button half red" name="stop_link" value="STOP" $LINK_STOP_EN>
          </td>
        </tr>
        <tr><td colspan=2><hr></td></tr>
        <tr>
          <td>Current datetime</td>
          <td>
            <input type="text" name="current_dt" value="`date '+%Y-%m-%d %H:%M:%S'`" readonly>
          </td></tr><tr><td></td><td>
            <input type="submit" class="block_button full blue" name="time_sync" value="SYNC TIME" $SYNC_EN>
          </td>
        </tr>
        <tr><td colspan=2><hr></td></tr>
        <tr>
          <td>GPS Altitude (m)</td>
          <td>
            <input type="text" name="altitude" value="" disabled>
            </td></tr><tr><td></td><td>
            <input type="submit" class="block_button full blue" name="alt_sync" value="SET ALTITUDE" disabled>
          </td>
        </tr>
        <tr><td colspan=2><hr></td></tr>
        <tr>
          <td>Data acquisition</td>
          <td>
            <input type="submit" class="block_button half green" name="start_data" value="START" disabled>
            <input type="submit" class="block_button half red" name="stop_data" value="STOP" disabled>
          </td>
        </tr>
       <tr><td colspan=2><hr></td></tr>
        <tr>
          <td colspan=2 class="centered">
            <input type="reset" class="block_button full blue" value="RESET"/>
          </td>
        </tr>   
      </table>
      <input type="hidden" name="datetime" id="datetime" value="">
    </form>
  </body>
</html>
EOF