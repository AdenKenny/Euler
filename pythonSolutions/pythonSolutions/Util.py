class Util:
	@staticmethod
	def is_pal(n: int) -> bool:
		num_str = str(n)
		
		if num_str == num_str[::-1]:
			return True
		
		return False

	def is_pal(n: str) -> bool:
		if str == str[::-1]:
			return True

		return False

	@staticmethod
	def is_prime(n: int) -> bool:
		for i in range(2, int(n ** 0.5) + 1):
			if n % i == 0:
				return False
		
		return True
	
		
