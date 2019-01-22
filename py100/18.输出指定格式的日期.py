import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()) ))
#.time返回浮点数，.localtime返回日期数据，.strftime处理数据成字符串