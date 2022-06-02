
from modules.RevPiHelper import RevPiHelper

class Test_Flat:


	def setup_method(self, method):
		# flash image
		# factory reset

		self.RevPiClient= RevPiSSHClient(self.HOSTNAME_DUT,self.USERNAME_DUT,self.PASSWORD_DUT)
		self.RevPiClient.Connect()
		self.scp_client = scp.SCPClient(self.RevPiClient.getTransport())
		self.intf = RevPi_Interfaces(self.RevPiClient)

	def teardown_method(self, method):
		self.RevPiClient.Disconnect()
