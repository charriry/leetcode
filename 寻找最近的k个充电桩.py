def distance(x,y,cx,cy):
    return abs(x-cx) + abs(y-cy)
def Solution(grid,k):
    grid = sorted(grid,key=lambda x:(x[0],x[1]))
    result = [str(grid[i][1]) for i in range(k)]
    return " ".join(result)

if __name__ == "__main__":
    print(0.25 + 0.25 == 0.5)
    k , n = map(int,input().split(" "))
    x,y = map(int,input().split(" "))
    grid = []
    for i in range(n):
        temp = map(int,input().split())
        #grid.append(temp)
        dis = distance(temp[0],temp[1],x,y)
        info = (dis,i)
        grid.append(info)
    print(Solution(grid,k))
