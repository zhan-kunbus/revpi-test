from modules.RevPiSSHClient import RevPiSSHClient
from modules.EthernetPort import EthernetPort

class RevPiHelper:
	eth0 = None
	eth1 = None
	sshClient = None

	def __init__(self, ipAddr, userName, passWord):
		self.sshClient = RevPiSSHClient(ipAddr, userName, passWord)
		self.sshClient.Connect()
		self.eth0 = EthernetPort(self.sshClient, "eth0", "192.168.100.1", 90)
		self.eth1 = EthernetPort(self.sshClient, "eth1", "192.168.101.1", 90)

	def iperfListen(self, port):
		if (port == "eth0"):
			self.eth0.iperfListen()
		if (port == "eth1"):
			self.eth1.iperfListen()

	def getEtherPort(self, port):
		if (port == "eth0"):
			return self.eth0
		if (port == "eth1"):
			return self.eth1