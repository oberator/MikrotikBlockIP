# MikrotikBlockIP
This python script sends a ip address to the Mikrotik router, which has to be dropped in the firewall.

# Usage
Call the script with droplist.py <IPtoBeBlocked> <TimeoutOfBlockinMinutes>
  
e.g. droplist.py 10.10.10.44 10
This will add the IP Adress 10.10.10.44 to the drop_traffic AdressList for 10 Minutes.

Of course it is neccessary to build a Firewall Droproule for incomming traffic from the Adresslist "drop_traffic".
