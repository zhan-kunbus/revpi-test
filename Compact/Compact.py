
from modules.RevPiSSHClient import RevPiSSHClient
from modules.EthernetPort import EthernetPort

class Compact:
	eth0 = None
	eth1 = None
	sshClient = None

	def __init__(self, ipAddr, userName, passWord):
		self.sshClient = RevPiSSHClient(ipAddr, userName, passWord)
		self.sshClient.Connect()
		self.eth0 = EthernetPort(self.sshClient, "eth0", "192.168.100.2", 90)
		self.eth1 = EthernetPort(self.sshClient, "eth1", "192.168.101.2", 16)

	def iperfConnect(self):
		return self.eth0.iperfConnect()

	def peerPing(self):
		return self.eth0.peerPing()

	def setEth0Peer(self, eth):
		self.eth0.setPeer(eth)

	def eth1IperfConnect(self):
		return self.eth1.iperfConnect()

	def eth1PeerPing(self):
		return self.eth1.peerPing()

	def setEth1Peer(self, eth):
		self.eth1.setPeer(eth)