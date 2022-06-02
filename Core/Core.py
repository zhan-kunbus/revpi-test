
from modules.RevPiSSHClient import RevPiSSHClient
from modules.EthernetPort import EthernetPort

class Core:
	eth0 = None
	sshClient = None

	def __init__(self, ipAddr, userName, passWord):
		self.sshClient = RevPiSSHClient(ipAddr, userName, passWord)
		self.sshClient.Connect()
		self.eth0 = EthernetPort(self.sshClient, "eth0", "192.168.100.2", 90)

	def iperfConnect(self):
		return self.eth0.iperfConnect()

	def peerPing(self):
		return self.eth0.peerPing()

	def setEth0Peer(self, eth):
		self.eth0.setPeer(eth)