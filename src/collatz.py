def collatz_sequence_generator_from(n):
	last = n
	reached_termination = False
	while not reached_termination:
		last = (lambda e: 3*e+1)(last) if last%2 else (lambda e: e/2)(last)
		if last == 1:
			reached_termination = True
		else: 
			yield last

def find_longest_chain_upto(n):
	value = 1
	longest = [1]
	for i in range(2, n):
		computed = [int(c) for c in collatz_sequence_generator_from(i)]
		if len(computed) > len(longest):
			longest = computed
			value = i
	return value, longest

