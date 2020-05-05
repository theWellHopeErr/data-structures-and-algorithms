def fibonacci_last_digit(n):
  if n == 0:
    return n
  prev,curr = 0,1
  for i in range(n-1):
    prev,curr = curr%10,(prev+curr)%10
  return curr

def fibonacci_sum(n):
    last_digit = fibonacci_last_digit((n + 2) % 60)
    sum_last_digit =  last_digit_after_subtraction(last_digit, 1)
    return sum_last_digit

def fibonacci_partial_sum(a, b):
    last_digit_partial_sum = last_digit_after_subtraction(fibonacci_sum(b), fibonacci_sum(a - 1))
    return last_digit_partial_sum

def last_digit_after_subtraction(last_digit_minuend, last_digit_subtrahend):
    if (last_digit_minuend < last_digit_subtrahend):
        last_digit_minuend += 10;
    return last_digit_minuend - last_digit_subtrahend

if __name__ == '__main__':
  a,b = map(int,input().split())
  print(fibonacci_partial_sum(a,b))