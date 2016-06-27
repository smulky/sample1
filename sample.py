import paramiko
import re

def ping_device(from_ip,to_ip):
	result = "Down"
	s = paramiko.SSHClient()
	s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	s.connect(from_ip,username = 'user', password = 'password')
	print "Sucessfully loggedin device " + from_ip
	print "pinging " + to_ip
	stdin,stdout,sderr = s.exec_command( 'cli ping count 2 ' + to_ip )
	list = stdout.readlines()
	for line in list:
		match = re.search(r'(\d+)\s*packets\s*received',line)
		if (match):
			find_status = match.group(1)
			if (int(find_status) > 0):
				result = "Up"
	s.close()
	return result
