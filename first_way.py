import time

def power(x, y, n):
    if (y == 0):
        return 1
    z = power(x % n, y // 2, n) % n
    if (y % 2 == 0):
           return (z * z) % n
    else:
         return ((x % n) * ((z * z) % n)) % n
def rects(n):
    rects = []
    for i in range(n):
        rects.append([10 * i, 10 * i, 10 *(2 * n - i), 10 * (2 * n-  i)])
    return rects
def points(n):
    p_x, p_y, m = 277, 193, 31
    points = []
    for i in range(2 * n):
        x = power(p_x * i, m, 20 * n)
        y = power(p_y * i, m, 20 * n)
        points.append([x, y])
    return points
def checked(x1, y1, x2, y2, x, y):
    if ((x1 <= x) and (x < x2) and (y1 <= y) and (y < y2)):
         return 1
    return 0

n = 1
for i in range(1, 11):
    n *= 2
    Rects = rects(n)
    Points = points(n)
    #print(*Rects)
    start = time.perf_counter()
    for j in range(len(Points)):
        ans = 0
        for i in range(n):
            ans += checked(Rects[i][0], Rects[i][1], Rects[i][2], Rects[i][3], Points[j][0], Points[j][1])
        #print("(" + str(Points[j][0]) + ", " + str(Points[j][1]) + "): " + str(ans))
    end = time.perf_counter()
    print(n, (end - start) * 1000)
