t = int(input())

for x in range(0, t):
	N, Q = list(map(int, input().split(" ")))
	l = []
	
	for y in range(0, N):
		S, A = input().split(" ")
		l.append([S, A])
	
	mx = None
	mxs = ""
	for s, a in l:
		a = int(a)
		if len(s) - a > a:
			s = "".join(["T" if c == "F" else "F" for c in s])
			a = len(s) - a
		if mx == None or a > mx:
			mx = a
			mxs = s

	print(f"Case #{(x + 1)}: {mxs} {mx}/1")	

