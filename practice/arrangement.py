# coding:utf-8

print ["%d%d%d" % (x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5)  if(x!=y)
       and (x!=z) and (y!=z)]