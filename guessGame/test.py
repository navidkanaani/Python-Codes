import unittest
import script

class scriptTest(unittest.TestCase):
	def test_input1(self):
		result=script.check(5,5)
		self.assertTrue(result)

	def test_input_wrong_guess(self):
		result=script.check(5,0)
		self.assertFalse(result)

	def test_input_wrong_number(self):
		result=script.check(5,11)
		self.assertFalse(result)

	def test_input_wrong_type(self):
		result=script.check(5,'dafsfsd')
		self.assertFalse(result)


if __name__=='__main__':
	unittest.main()