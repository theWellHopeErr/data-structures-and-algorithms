def optimal_points(segments):
  index = 0
  coordinates = []
  segments.sort(key = lambda x: x[1])
  while index < len(segments):
    curr = segments[index]
    while index < len(segments)-1 and curr[1]>=segments[index+1][0]:
        index += 1
    coordinates.append(curr[1])
    index += 1
  return coordinates

if __name__ == '__main__':
  segments = []
  for _ in range(int(input())):
    segments.append([int(i) for i in input().split()])
  points = optimal_points(segments)
  print(len(points))
  print(*points)