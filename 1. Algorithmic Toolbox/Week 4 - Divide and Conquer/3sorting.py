import random
def sorting(arr, l, r):
    if l + 1 >= r:
        return
    m = l #random.randint(l, r-1)
    arr[l], arr[m] = arr[m], arr[l]
    m1, m2 = partition(arr, l, r)
    sorting(arr, l, m1)
    sorting(arr, m2+1, r)

def partition(arr, l, r):
    m2 = l
    for i in range(l+1, r):
        if arr[i] <= arr[l]:
            arr[m2+1], arr[i] = arr[i], arr[m2+1]
            m2 += 1
    arr[l], arr[m2] = arr[m2], arr[l]
    m1 = l
    for i in range(l, m2):
        if arr[i] < arr[m2]:
            arr[i], arr[m1] = arr[m1], arr[i]
            m1 += 1
    return m1, m2

if __name__ == "__main__":
  n = int(input())
  seq = [int(i) for i in input().split()]
  # sorting(seq,0,n-1)
  seq.sort()
  for x in seq:
      print(x, end=' ')