def fibonacci_last_digit(n):
  if n == 0:
    return n
  prev,curr = 0,1
  for i in range(n-1):
    prev,curr = curr%10,(prev+curr)%10
  return curr

def fibonacci_sum_squares(n):
  vertical = fibonacci_last_digit(n % 60)
  horizontal = fibonacci_last_digit((n+1) % 60)
  return (vertical*horizontal) % 10

if __name__ == '__main__':
  print(fibonacci_sum_squares(int(input())))