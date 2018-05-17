# coding:utf-8

import re

# re.match(pattern, string, flags=0)
# pattern 匹配的正则表达式 string 要匹配的字符串
# flags 标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
# group(num=0) 匹配的整个表达式的字符串，
# group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。

# groups() 返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

#  r'(.*) are (.*?) .*'
#  首先，这是一个字符串，前面的一个 r 表示字符串为非转义的原始字符串，让编译器忽略反斜杠，
# 也就是忽略转义字符。但是这个字符串里没有反斜杠，所以这个 r 可有可无。
#
#  (.*) 第一个匹配分组，.* 代表匹配除换行符之外的所有字符。
#  (.*?) 第二个匹配分组，.*? 后面多个问号，代表非贪婪模式，也就是说只匹配符合条件的最少字符
#  后面的一个 .* 没有括号包围，所以不是分组，匹配效果和第一个一样，但是不计入匹配结果中。
#  matchObj.group() 等同于 matchObj.group(0)，表示匹配到的完整文本字符
#
#  matchObj.group(1) 得到第一组匹配结果，也就是(.*)匹配到的
#
#  matchObj.group(2) 得到第二组匹配结果，也就是(.*?)匹配到的
#
#  因为只有匹配结果中只有两组，所以如果填 3 时会报错。