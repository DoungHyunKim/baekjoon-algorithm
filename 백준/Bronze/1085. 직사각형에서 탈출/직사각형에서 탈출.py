x, y, w, h = map(int,input().split())

xw = abs(x-w)
yh = abs(y-h)

list = [x,y,xw,yh]

list = sorted(list)

print(min(list))