import parse
import ipaddress
import re
import paramiko

class EthernetPort:
	IfName = None
	Speed = None
	Duplex = None
	AutoNego = None
	IPAddress = None
	peerPort = None
	sshClient = None

	strSetIp = "sudo ip address add {} dev {}"
	strAddRoute = "sudo ip route add {} dev {}"

	def __init__(self, client, ifname, ipaddr, speed):
		self.sshClient = client
		self.IfName = ifname
		self.setIPAddress(ipaddr)
		self.Speed = speed

	def setSSHClient(client):
		self.sshClient = client

	def setIPAddress(self, ip):
		self.IPAddress = ip
		cmd = self.strSetIp.format(self.IPAddress, self.IfName)
		self.sshClient.SSHExecute(cmd)

		cmd = self.strAddRoute.format(str(ipaddress.ip_interface(self.IPAddress +"/24").network), self.IfName)
		self.sshClient.SSHExecute(cmd)


	def getIPAddress(self):
		return self.IPAddress

	def setPeer(self, peer):
		self.peerPort = peer

	def peerPing(self):
		targetIP = self.peerPort.getIPAddress()
		cmd = "ping -c 5 {}".format(targetIP)
		out = self.sshClient.SSHExecute(cmd).decode("utf-8")
		r = out.find("bytes from {}".format(targetIP))
		if r == -1:
			raise Exception("Destination Host Unreachable")
		strPat = '[{}-9][.][0-9]* ms'.format(1)#TODO pat reg

		m = re.search(strPat, out)
		if m != None:
			return 1
		return 0

	def iperfConnect(self):
		ipServer = self.peerPort.getIPAddress()
		cmd = "iperf3 -R -B {0} -c {1} -t 10 | tee ~/iperf-{0}-output.log".format(self.IPAddress, ipServer)
		out = self.sshClient.SSHExecute(cmd).decode("utf-8")
		print(out)
		r = out.find("iperf Done")
		if r == -1:
			raise Exception("iperf3: error - unable to connect to server: No route to host")

		maxBW = self.Speed - 1
		strPat = '[0-{}][0-{}][.][0-9] Mbits/sec'.format(maxBW//10, maxBW % 10)
		m = re.search(strPat, out)
		if m != None:
			return 1
		return 0

	def iperfListen(self):
		cmd = "pkill iperf3; iperf3 -sD | tee ~/iperf3-server-output.log"
		self.sshClient.SSHExecute(cmd)

		return 0

	def ethtoolCheck():
		cmd = "ethtool {}".format(IfName)
		out = self.sshClient.SSHExecute(cmd)
		parse('Speed: {:d}Mb/s', out)
		if (self.Speed != speed):
			return -1
		return 0

	def setupDhcp():
		pass
	def connectDhcp():
		pass
