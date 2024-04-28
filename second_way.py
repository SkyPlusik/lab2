import time

def Power(x, y, n):
    if (y == 0):
        return 1
    z = Power(x % n, y // 2, n) % n
    if (y % 2 == 0):
           return (z * z) % n
    else:
         return ((x % n) * ((z * z) % n)) % n
def Rects(n):
    rects = []
    for i in range(n):
        rects.append([10 * i, 10 * i, 10 *(2 * n - i), 10 * (2 * n-  i)])
    return rects
def Points(n):
    p_x, p_y, m = 277, 193, 31
    points = []
    for i in range(2 * n):
        x = Power(p_x * i, m, 20 * n)
        y = Power(p_y * i, m, 20 * n)
        points.append([x, y])
    return points
def Checked(x1, y1, x2, y2, x, y):
    if ((x1 <= x) and (x < x2) and (y1 <= y) and (y < y2)):
         return 1
    return 0
def CompressedCoords(rects):
    coordsX, coordsY = [], []
    for rect in rects:
        coordsX.append(rect[0])
        coordsX.append(rect[2])
        coordsY.append(rect[0])
        coordsY.append(rect[2])
    coordsX = list(set(coordsX))
    coordsX.sort()
    coordsY = list(set(coordsY))
    coordsY.sort()
    return coordsX, coordsY
def CreateMatrix(rects, coordsX, coordsY):
    n, m = len(coordsY), len(coordsX)
    matrix = []
    for i in range(n):
        matrix.append([0] * m)
    for i in range(n):
        for j in range(m):
            x, y = coordsX[j], coordsY[i]
            for rect in rects:
                matrix[i][j]  += Checked(rect[0], rect[1], rect[2], rect[3], x, y)
    return matrix
def BinSearch(coords, goal):
    left, right = 0, len(coords) - 1
    if goal < coords[left] or goal > coords[right]:
        return -1
    while right >= left:
        mid = left + (right - left) // 2
        if coords[mid] == goal:
            return mid
        if coords[mid] > goal:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1

N = 1
for i in range(1, 11):
    N *= 2
    rects = Rects(N)
    points = Points(N)
    # подготовка
    start_preproc = time.perf_counter()
    coordsX, coordsY = CompressedCoords(rects)
    matrix = CreateMatrix(rects, coordsX, coordsY)
    end_preproc = time.perf_counter()
    n, m = len(coordsY), len(coordsX)
    # поиск
    start_query =  time.perf_counter()
    for point in points:
        x, y = BinSearch(coordsX, point[0]), BinSearch(coordsY, point[1])
        #print("(", point[0], ", ", point[1], "): ", matrix[y][x])
    end_query =  time.perf_counter()
    print(N)
    print("preprocessing: ", (end_preproc - start_preproc) * 1000)
    print("query processing: ", (end_query - start_query) * 1000)
    print("total: ", (end_query - start_preproc) * 1000)
