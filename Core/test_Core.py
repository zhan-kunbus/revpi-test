
import os
import sys
from Core import Core
from modules.RevPiHelper import RevPiHelper

class Test_Core:
	core = None
	helper = None

	def setup_method(self, method):
		self.core = Core("192.168.168.105", "pi", "raspberry")
		self.helper = RevPiHelper("192.168.168.1", "pi", "raspberry")
		self.core.setEth0Peer(self.helper.getEtherPort("eth0"))

	def test_IperfEth0(self):
		self.helper.iperfListen("eth0")
		r = self.core.iperfConnect()
		if (r != 0):
			raise Exception("Failed")

	def test_PingEth0(self):
		r = self.core.peerPing()