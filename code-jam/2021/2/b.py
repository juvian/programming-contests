T = int(input())


def solve(N, last, sums):
	if N == 0:
		return sums
	mx = -1
	for x in range(2, N+1):
		if last * x < 3:
			continue
		if N % (last * x) == 0:
			s = solve(N - last * x, last * x, sums + 1)
			mx = max(mx, s)
		if last * x > N:
			break
	return mx



for x in range(T):
	N = int(input())
	print(f"Case #{x+1}: {solve(N, 1, 0)}")