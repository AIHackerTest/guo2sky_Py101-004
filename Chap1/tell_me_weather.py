#这一步将城市和天气所对应的信息转换成字典文件，使用的方法是with as 句式
dict = {}
with open("weather_info.txt") as f:
  for line in f:
    (key, val) = line.split(',')
    dict[key]= val
#这一步我要开始判断，这里的history_list列表是为了后面方便打印历史记录
history_list = []
while True:#一直运行input
  code_or_city = input("您输入的指令或者要查询天气的城市是：")
  if  code_or_city in dict.keys():
    weather ='{0}的天气是:{1}'.format(code_or_city,dict[code_or_city])
    print (weather)
    history_list.append(weather)
  elif code_or_city == "help":
    print ('''
      输入城市名，查询该城市的天气；
      输入help，显示帮助文档；
      输入history，显示查询历史；
      输入quit，退出程序；
      ''')
  elif code_or_city == "history":
      print("您的查阅历史记录如下:")
      for item in history_list:
        print(item)
  elif code_or_city == "quit":
      quit()
  else:#这个是根据战友的例子自己加的，当输入不是以上四种情况时，跳出提示语
      print ("您的输入有误，请尝试输入help获得帮助文档")
