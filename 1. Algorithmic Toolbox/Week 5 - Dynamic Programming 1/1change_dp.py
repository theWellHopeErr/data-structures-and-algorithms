import sys

def change_dp(money):
  denominations = [1, 3, 4]
  min_coins = [0] + [sys.maxsize]*money

  for i in range(1, money+1):
    for j in denominations:
        if i>=j:
            coins = min_coins[i-j]+1
            if coins < min_coins[i]:
                min_coins[i] = coins
  return min_coins[money]

if __name__ == "__main__":
  print(change_dp(int(input())))