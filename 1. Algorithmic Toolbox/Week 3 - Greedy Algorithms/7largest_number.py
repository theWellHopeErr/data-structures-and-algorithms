def is_greater_or_equal(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))

def largest_number(n,nums):
  ans = []
  while len(nums) > 0:
    # print(nums)
    # print(ans)
    max_num = 0
    for num in nums:
      if is_greater_or_equal(num, max_num):
        max_num = num
    # print(max_num)
    ans.append(max_num)
    nums.remove(max_num)
  return ans

if __name__ == "__main__":
  n = int(input())
  nums = [int(i) for i in input().split()]
  # print(is_greater_or_equal(111111,12))
  print(''.join(map(str,largest_number(n,nums))))