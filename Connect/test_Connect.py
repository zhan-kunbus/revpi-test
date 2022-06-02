from Connect import Connect
from modules.RevPiHelper import RevPiHelper
#from tests.system_tests.RevPi_Interfaces import RevPi_Interfaces

class Test_Connect:
	connect = None

	def setup_method(self, method):
		self.connect = Connect("192.168.0.101", "pi", "raspberry")
		self.helper = RevPiHelper("192.168.0.102", "pi", "raspberry")
		self.connect.setEth0Peer(self.helper.getEtherPort("eth0"))
		self.connect.setEth1Peer(self.helper.getEtherPort("eth1"))
		return 0

	def test_EtherAIperf(self):
		self.helper.iperfListen("eth0")
		r = self.connect.iperfConnect()
		if (r != 0):
			raise Exception("Failed")

	def test_EtherAPing(self):
		r = self.connect.peerPing()

	def test_EtherBIperf(self):
		self.helper.iperfListen("eth1")
		r = self.connect.eth1IperfConnect()
		if (r != 0):
			raise Exception("Failed")

	def test_EtherBPing(self):
		r = self.connect.eth1PeerPing()
