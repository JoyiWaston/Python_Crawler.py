import urllib.request
# # 向京东发送HTTP GET请求，urlopen函数既可以用http，也可以用https
# response = urllib.request.urlopen('https://www.jd.com')
# # 输入urlopen函数返回值的数据类型
# print('response的类型: ', type(response))
# # 输出响应状态码，响应消息和HTTP版本
# print('status:', response.status, ' msg:', response.msg, ' version:', response.version)
# # 输出所有响应头信息
# print('headers:', response.getheaders())
# # 输出名为Content-Type的响应头信息
# print('headers.Content-Type', response.getheader('Content-Type'))
# # 输出京东商场首页所有的HTML代码(经过utf-8 解码)
# print(response.read().decode('utf-8'))

# 将表单数据转换成bytes类型，用utf-8编码
data = bytes(urllib.parse.urlencode({'name': 'Bill', 'age': 30}), encoding='utf-8')
# 提交HTTP POST请求
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# 输出响应数据
print(response.read().decode('utf-8'))

