import sys

input = sys.stdin.readline


def main():
	N = int(input())
	K = int(input())
	
	left = 1
	right = N * N
	
	while left <= right:
		mid = (left + right) // 2
		
		count = 0
		for i in range(1, N + 1):
			count += min(mid // i, N)
		
		if count >= K:
			right = mid - 1
		else:
			left = mid + 1
	
	print(left)


main()
