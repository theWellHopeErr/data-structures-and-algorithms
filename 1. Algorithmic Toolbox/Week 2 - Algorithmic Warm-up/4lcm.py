def gcd(a,b):
  if a == 0:
    return b
  if b == 0:
    return a
  a,b = b,a%b
  return gcd(a,b)

def lcm(a,b):
  return (a*b) // gcd(a,b)

if __name__ == "__main__":
    a,b = map(int,input().split())
    print(lcm(a,b))