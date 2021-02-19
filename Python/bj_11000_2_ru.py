import heapq

N = int(input())
h = [0]
g = [tuple(map(int, input().split())) for _ in range(N)]
g.sort()
for s, e in g:
    print(h[0], s)
    if h[0] > s:
        heapq.heappush(h, e)
    else:
        heapq.heapreplace(h, e)

print(*h)
print(len(h))
