def fibonacci (n):
  if n == 0:
    return n
  prev,curr = 0,1
  for i in range(n-1):
    prev,curr = curr,(prev+curr)
  return curr

if __name__ == "__main__":
    print(fibonacci(int(input())))