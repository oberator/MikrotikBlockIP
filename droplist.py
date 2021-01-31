import paramiko
import sys

if len(sys.argv) != 3:
    raise ValueError('Please provide at least ip adress an timeout like droplist.py 192.168.1.1 5')

IPtoBlocK = sys.argv[1]
IPTimeout = sys.argv[2]

ip_mik = '10.10.10.1'
user= 'proxyUsr'
password='mysecretpassword'


def blockIP(ipaddr,timeoutInMin):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip_mik,username=user,password=password)
    print (f"Sucessfull login to {ip_mik}")
    print ("")
    #stdin,stdout,stderr= ssh.exec_command('ip firewall address-list add list=drop_traffic address={ipaddr} ')
    stdin,stdout,stderr= ssh.exec_command(f'ip firewall address-list add list=drop_traffic address={ipaddr} timeout={timeoutInMin}m')

    print(stdout.read())


blockIP(IPtoBlocK,IPTimeout)

