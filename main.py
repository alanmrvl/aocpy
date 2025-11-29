import sys

filename = sys.argv[1]

left = []
right = []

with open(filename) as file:
    for line in file:
        [l, r] = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

sum = 0

for i in range(0, len(left)):
    sum += abs(left[i] - right[i])

print(sum)
