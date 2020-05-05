def fractional_knapsack(n,W,items):
  items.sort(reverse=True, key = lambda a: a[0]/a[1])
  tot = 0
  for item in items:
    if W > 0:
      v,w = item
      a = min(w,W)
      tot += a*v/w
      W -= w
  return round(tot,4)

if __name__ == "__main__":
  n,W = map(int,input().split())
  items = []
  for _ in range(n):
    items.append([int(i) for i in input().split()])
  print(fractional_knapsack(n,W,items))