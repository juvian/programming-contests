t = int(input())


def solve(l):
	ops = 0
	#print(l)
	for idx, x in enumerate(l):
		if idx == 0 or x > l[idx - 1]:
			continue
	#	print(idx, x, l[idx - 1])
		d1 = list(map(int, list(str(l[idx - 1]))))
		d2 = list(map(int, list(str(x))))

		if all([dd1 == dd2 for dd1, dd2 in zip(d1, d2)]) and len(d1) > len(d2):
			if not all([d == 9 for d in d1[len(d2):]]):
				t = list(map(int, list(str(l[idx - 1] + 1))))
				#print(idx, x, t, len(d2), t[len(d2):])
				for digit in t[len(d2):]:
					l[idx] = l[idx] * 10 + digit
					ops += 1
				continue

		ll = (len(d1) - len(d2) + 1)

		for dd1, dd2 in zip(d1, d2):
			if dd2 < dd1:
				break
			if dd2 > dd1:
				ll = (len(d1) - len(d2))
				break

		ops += ll
		l[idx] = x * (10**ll)
	#print(l)
	return ops

for i in range(0, t):
	N = int(input())
	l = list(map(int, input().split(" ")))

	print(f"Case #{(i + 1)}: {solve(l)}")	
	#print(l)


