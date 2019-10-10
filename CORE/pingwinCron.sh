var=$1
# delete previous scheduled tasks for pingwinServer if exists:
crontab -l | grep -v pingwinServer | crontab - 
# add  scheduled task with values given from user:
(crontab -l 2>/dev/null; echo "$var sudo python3 /PingWin/CORE/pingwinServer.py") | crontab - 


