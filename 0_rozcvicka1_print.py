def is_prime(number):
	if number < 2:
		return False

	divisor = 2
	while divisor * divisor <= number:
		if number % divisor == 0:
			return False
		divisor += 1

	return True


primes = []
number = 2

while len(primes) < 100:
	if is_prime(number):
		primes.append(number)
	number += 1

print(*primes)
