import sys

def primitive_calculator(n):
  num_operations = [0, 0] + [sys.maxsize]*(n-1)

  for i in range(2, n+1):
      temp1, temp2, temp3 = [sys.maxsize]*3

      temp1 = num_operations[i-1] + 1 
      if i%2 == 0: temp2 = num_operations[i//2] + 1
      if i%3 == 0: temp3 = num_operations[i//3] + 1
      min_ops = min(temp1, temp2, temp3)
      num_operations[i] = min_ops

  nums = [n]
  while n!=1:
      if n%3 ==0 and num_operations[n]-1 == num_operations[n//3]:
          nums += [n//3]
          n = n//3
      elif n%2 ==0 and num_operations[n]-1 == num_operations[n//2]:
          nums += [n//2]
          n = n//2
      else:
          nums += [n-1]
          n = n - 1
  return nums[::-1]

if __name__ == "__main__":
  res = primitive_calculator(int(input()))
  print(len(res)-1)
  print(*res)