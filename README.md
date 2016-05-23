# minion-beedo 

To start the minion ssh into minion with raspberry pi user 
username: pi
password: raspberry

and run main.py with sudo 

To trigger alarm run command:
curl -i --data "signal=alarm" 192.168.1.65:8888/banana

To trigger random speech:
curl -i --data "signal=speech" 192.168.1.65:8888/banana
