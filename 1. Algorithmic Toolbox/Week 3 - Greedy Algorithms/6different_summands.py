def different_sumands(n):
  prizes = []
  if n == 1:
    prizes.append(1)
    return prizes
  W = n
  for i in range(1, n):
      if W>2*i:
          prizes.append(i)
          W -= i
      else:
          prizes.append(W)
          break
  return prizes

if __name__ == "__main__":
  prizes = different_sumands(int(input()))
  print(len(prizes))
  print(*prizes)