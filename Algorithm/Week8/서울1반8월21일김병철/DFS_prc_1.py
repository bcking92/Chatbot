arr = [[0] * 7 for i in range(7)]

arr[0][1] = 1
arr[1][0] = 1
arr[0][2] = 1
arr[2][0] = 1
arr[1][3] = 1
arr[3][1] = 1
arr[1][4] = 1
arr[4][1] = 1
arr[2][6] = 1
arr[6][2] = 1
arr[3][5] = 1
arr[5][3] = 1
arr[4][5] = 1
arr[5][4] = 1
arr[5][6] = 1
arr[6][5] = 1

node = ['1','2','3','4','5','6','7']
visited = [0, 0, 0, 0, 0, 0, 0]
stack = []
result = ''

x = 0
result += node[x]
visited[x] = 1
while sum(visited) < 7:
    for n, i in enumerate(arr[x]):
        if i == 1:
            if not visited[n]:
                stack.append(n)
                result += node[n]
                visited[n] = 1
                x = n
                break
            else:
                continue
        else:
            continue
    else:
        if stack:
            x = stack.pop()
print(result)
