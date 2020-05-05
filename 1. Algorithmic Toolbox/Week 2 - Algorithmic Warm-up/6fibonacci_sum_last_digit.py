def fibonacci_last_digit(n):
  if n == 0:
    return n
  prev,curr = 0,1
  for i in range(n-1):
    prev,curr = curr%10,(prev+curr)%10
  return curr

def fibonacci_sum_last_digit(n):
  last_digit = fibonacci_last_digit((n+2) % 60)
  return last_digit-1 if last_digit != 0 else 9

if __name__ == '__main__':
  print(fibonacci_sum_last_digit(int(input())))