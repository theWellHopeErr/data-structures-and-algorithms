def change(n):
  denominations = [10, 5, 1]
  no_of_coins = 0
  for i in denominations:
    if n // i > 0:
      no_of_coins += n // i
      n%=i
      # print(i,no_of_coins,n)
  return no_of_coins

if __name__ == "__main__":
  print(change(int(input())))
