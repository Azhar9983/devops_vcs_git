import math
def ip(n):
	if n<2:
		return False
	for i in range(2, int(math.sqrt(n))+1 ):
		if not n%i:
			return False
	return True

