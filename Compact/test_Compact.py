from Compact import Compact
from modules.RevPiHelper import RevPiHelper
#from tests.system_tests.RevPi_Interfaces import RevPi_Interfaces

class Test_Compact:
	compact = None

	def setup_method(self, method):
		self.compact = Compact("192.168.0.102", "pi", "raspberry")
		self.helper = RevPiHelper("192.168.0.101", "pi", "raspberry")
		self.compact.setEth0Peer(self.helper.getEtherPort("eth1"))
		self.compact.setEth1Peer(self.helper.getEtherPort("eth1"))
		return 0

	def test_EtherAIperf(self):
		self.helper.iperfListen("eth1")
		r = self.compact.iperfConnect()
		if (r != 0):
			raise Exception("Failed")

	def test_EtherAPing(self):
		r = self.compact.peerPing()

	def test_EtherBIperf(self):
		self.helper.iperfListen("eth1")
		r = self.compact.eth1IperfConnect()
		if (r != 0):
			raise Exception("Failed")

	def test_EtherBPing(self):
		r = self.compact.eth1PeerPing()
