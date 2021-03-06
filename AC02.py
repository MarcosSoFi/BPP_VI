
import pytest
import unittest

# 	Functions
#	----------------------------------------------------------------
def string_ToInt1(data):
	return int(data)

def string_ToInt2(data):
	if not isinstance(data, str):
		raise TypeError("Input must be a string")
	return int(data)

def string_ToInt3(data):
	output = []
	if not isinstance(data, str):
		raise TypeError("Input must be a string")
	else:
		try:
			output.append(int(data))
		except:
			if data.startswith("'") and data.endswith("'"):
				output.append(int(data[1:-1]))
			else:
				output.append(0)
	return output

def total(lst):
	return sum(lst)


#   [1] pytest
#	----------------------------------------------------------------
def test_string_ToInt1():
	assert string_ToInt1("1")    == 1
	assert string_ToInt1(True)   == 1
	assert string_ToInt1(1)	 	 == 1  
	#assert string_ToInt1("'1'") == 1   # Error

def test_string_ToInt2():
	assert string_ToInt2("1")   == 1
	#assert string_ToInt2(True) == 1  # Error
	with pytest.raises(TypeError):
		string_ToInt2(1)
		string_ToInt2(True)

def test_string_ToInt31():
	assert string_ToInt3("1")   == [1]

def test_string_ToInt32():	
	assert string_ToInt3("'1'") == [1]

def test_string_ToInt33():		
	assert string_ToInt3("a")   == [0]

def test_total1():
	assert total([1,2,3]) == 6

def test_total2():
	assert total([1,2,3]) > 5


#   [2] unittest
#	----------------------------------------------------------------
class Tests(unittest.TestCase):
	def test_1(self):
		self.assertEqual(string_ToInt1("1"),1)

	def test_2(self):
		self.assertIsInstance(string_ToInt1("1"),int)

	def test_3(self):
		self.assertIsInstance(string_ToInt1(True),int)

	def test_4(self):
		self.assertIsInstance(string_ToInt2("6"),int)

	def test_5(self):
		self.assertIsInstance(string_ToInt3("'1'")[0],int)

	def test_6(self):
		self.assertIsInstance(string_ToInt3("a")[0],int)

	def test_7(self):
		self.assertEqual(total([1,2,3]),6)

	def test_8(self):
		self.assertGreater(total([1,2,3]),5)


if __name__ == "__main__":
     unittest.main()