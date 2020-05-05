def dot_product(n,a,b):
  c = 0
  for i in range(n):
    c += a[i] * b[i]
  return c

if __name__ == "__main__":
  n = int(input())
  a = sorted([int(i) for i in input().split()])
  b = sorted([int(i) for i in input().split()])
  print(dot_product(n,a,b))