import sys
T = int(input())
sys.setrecursionlimit(10000000)

N = 10**5+5
 
# array to store inverse of 1 to N
factorialNumInverse = [None] * (N + 1)
 
# array to precompute inverse of 1! to N!
naturalNumInverse = [None] * (N + 1)
 
# array to store factorial of
# first N numbers
fact = [None] * (N + 1)

# Function to precompute inverse of numbers
def InverseofNumber(p):
    naturalNumInverse[0] = naturalNumInverse[1] = 1
    for i in range(2, N + 1, 1):
        naturalNumInverse[i] = (naturalNumInverse[p % i] *
                                   (p - int(p / i)) % p)
 
# Function to precompute inverse
# of factorials
def InverseofFactorial(p):
    factorialNumInverse[0] = factorialNumInverse[1] = 1
 
    # precompute inverse of natural numbers
    for i in range(2, N + 1, 1):
        factorialNumInverse[i] = (naturalNumInverse[i] *
                                  factorialNumInverse[i - 1]) % p
 
# Function to calculate factorial of 1 to N
def factorial(p):
    fact[0] = 1
 
    # precompute factorials
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % p
 
# Function to return nCr % p in O(1) time
def ncr(N, R, p):
    # n C r = n!*inverse(r!)*inverse((n-r)!)
    ans = ((fact[N] * factorialNumInverse[R])% p *
                      factorialNumInverse[N - R])% p
    return ans


import bisect

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect.bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def solve(nums, start, end, lookup, indexes):
	if start == end:
		return 1
	try:	
		idx = find_lt(indexes[lookup], end)
		if idx < start or idx >= end:
			return 0
	except Exception:
		return 0
	#print(idx)
	l = solve(nums, start, idx, lookup, indexes)
	r = solve(nums, idx + 1, end, lookup + 1, indexes)
	s = (ncr(end - start - 1, idx - start, 10**9+7) * l * r) % (10**9 + 7)
	#print(start, end, lookup, idx, s, factorialMod((end - start - 1), 10**9+7), factorialMod(idx - start, 10**9+7), factorialMod(end - idx, 10**9+7), l, r)
	return s


p = 10**9+7
InverseofNumber(p)
InverseofFactorial(p)
factorial(p)

for x in range(T):
	N = int(input())
	nums = list(map(int, input().split()))

	indexes = [[] for n in range((N + 1))]

	for idx, num in enumerate(nums):
		indexes[num].append(idx)

	print(f"Case #{x+1}: {solve(nums, 0, len(nums), 1, indexes)}")
