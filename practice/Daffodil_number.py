# coding:utf-8

result = []

for n in xrange(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        result.append(n)

print "方法1：", result

result=[]
for x in  range(1,10):
    for y in  range(0,10):
        for z in  range(0,10):
            n = x * 100 + y * 10 + z
            if n == x ** 3 + y ** 3 + z ** 3:
                result.append(n)
print "方法2：", result
