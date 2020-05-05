def gcd(a,b):
  if a == 0:
    return b
  if b == 0:
    return a
  a,b = b,a%b
  return gcd(a,b)

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(gcd(a,b))