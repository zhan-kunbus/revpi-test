import pytest
import sys

class test_ImageLite():
	VAR = 9
	def test_var_even(self):
		assert self.VAR % 2 == 0

	def setup_method(self, method):
		# Helper
		self.Helper= RevPiSSHClient(self.ipHelper,"pi", "raspberry")
		self.Helper.Connect()