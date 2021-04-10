t = int(input())

def solve(primes, suma, prod, idx):
	if prod == suma:
		return suma

	if prod > suma or idx == len(primes) or prod * primes[idx][0] > suma - primes[idx][0]:
		return -1

	sol = solve(primes, suma, prod, idx + 1)	

	for qty in range(1, primes[idx][1] + 1):
		if  prod * primes[idx][0]**qty <= suma - primes[idx][0] * qty:
			sol = max(sol, solve(primes, suma - primes[idx][0] * qty, prod * primes[idx][0]**qty, idx + 1))
		else:
			break

	return sol

for x in range(0, t):
	M = int(input())
	primes = []
	total = 0

	for y in range(0, M):
		P, N = list(map(int, input().split(" ")))
		primes += [[P, N]]
		total += P * N

	s = solve(primes, total, 1, 0)
	
	if s < 2:
		s = 0

	print(f"Case #{(x + 1)}: {s}")
