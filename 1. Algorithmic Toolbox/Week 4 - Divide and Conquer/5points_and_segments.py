arr = list()
s, p = [int(i) for i in input().split()]

for i in range(s):
    a, b = [int(i) for i in input().split()]
    arr.append((a,'l'))
    arr.append((b,'r'))

points = input().split()
for i in points:
    arr.append((int(i),'p'))

arr.sort()

segment_count = 0
point_segment_map = dict()
for i in arr:
    if i[1] == 'l': segment_count += 1
    elif i[1] == 'r': segment_count -= 1
    else:
        point_segment_map[i[0]] = segment_count

t = ''
for i in points:
    t += str(point_segment_map[int(i)]) + ' '
print(t[:-1])