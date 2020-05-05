def pisano_period(m):
    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if (prev == 0 and curr == 1):
            return i + 1

def fibonacci_huge(n, m):
    pisano = pisano_period(m)
    n %= pisano
    prev, curr = 0, 1
    if n <= 1:
        return n
    for i in range(n-1):
        prev,curr = curr, prev+curr
    return curr % m

if __name__ == '__main__':
  n,m = map(int,input().split())
  print(fibonacci_huge(n,m))