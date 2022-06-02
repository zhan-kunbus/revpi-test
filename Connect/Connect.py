from Core.Core import Core
from modules.RevPiSSHClient import RevPiSSHClient
from modules.EthernetPort import EthernetPort

class Connect(Core):

	eth1 = None

	def __init__(self, ipAddr, userName, passWord):
		Core.__init__(self, ipAddr, userName, passWord)
		self.eth1 = EthernetPort(self.sshClient, "eth1", "192.168.101.2", 90)


	def eth1IperfConnect(self):
		return self.eth1.iperfConnect()

	def eth1PeerPing(self):
		return self.eth1.peerPing()

	def setEth1Peer(self, eth):
		self.eth1.setPeer(eth)
