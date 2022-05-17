from collatz import collatz_sequence_generator_from as seq_gen, find_longest_chain_upto as flcu



"""
https://oeis.org/A006877

1, 2, 3, 6, 7, 9, 18, 25, 
27, 54, 73, 97, 129, 171, 
231, 313, 327, 649, 703, 
871, 1161, 2223, 2463, 2919, 
3711, 6171, 10971,
13255, 17647, 23529, 26623, 
34239, 35655, 52527, 77031, 
106239, 142587, 156159, 216367 ...
"""

def test_longest_chain_under_35000():
	s, _ = flcu(35000)
	assert s == 34239

def test_longest_chain_under_36000():
	s, _ = flcu(36000)
	assert s == 35655

def test_longest_chain_under_53000():
	s, _ = flcu(53000)
	assert s == 52527

def test_longest_chain_under_77032():
	s, _ = flcu(77032)
	assert s == 77031

def test_longest_chain_under_156160():
	s, _ = flcu(156160)
	assert s == 156159

def test_longest_chain_under_2():
	s, _ = flcu(2)
	assert s == 1

def test_longest_chain_under_4():
	s, _ = flcu(4)
	assert s == 3

def test_longest_chain_under_5():
	s, _ = flcu(5)
	assert s == 3

def test_longest_chain_under_7():
	s, _ = flcu(7)
	assert s == 6

def test_longest_chain_under_8():
	s, _ = flcu(8)
	assert s == 7

def test_longest_chain_under_9():
	s, _ = flcu(9)
	assert s == 7


def test_longest_chain_under_129():
	s, _ = flcu(129)
	assert s == 97

def test_longest_chain_under_130():
	s, _ = flcu(130)
	assert s == 129

def test_longest_chain_under_500():
	s, _ = flcu(500)
	assert s == 327


def test_longest_chain_under_700():
	s, _ = flcu(700)
	assert s == 649


def test_longest_chain_under_750():
	s, _ = flcu(750)
	assert s == 703

def test_longest_chain_under_4000():
	s, _ = flcu(4000)
	assert s == 3711


def test_longest_chain_under_6200():
	s, _ = flcu(6200)
	assert s == 6171


def test_longest_chain_under_11000():
	s, _ = flcu(11000)
	assert s == 10971
