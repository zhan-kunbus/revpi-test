import pytest
import sys

class ImageCommon:
	VAR = 9

	def test_var_positive(self):
		assert self.VAR >= 0
