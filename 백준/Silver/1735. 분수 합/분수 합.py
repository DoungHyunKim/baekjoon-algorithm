import math

a, b = map(int, input().split())
x, y = map(int, input().split())

d_num = math.lcm(b,y)

a_num = d_num // b 
x_num = d_num // y

sum1 = (a * a_num) + (x * x_num)

num = math.gcd(sum1, d_num)

print(sum1//num, d_num//num)