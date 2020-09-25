import requests

# def test_post_join():
#     data ={
#   "pwd": "abc123",
#   "userName": "tuu653"
# }
#     r=requests.post("http://qa.yansl.com:8084/login",json=data)#join关键字发送json类型数据
#     print(r.text)
#
# def test_post_formdata(pub_data):
#     #post请求键值对数据
#     data ={
#   "userName": "tan242743"
# }
#     h = {"token":pub_data["token"]}
#     r=requests.post("http://qa.yansl.com:8084/user/lock",data=data,headers=h)#join关键字发送json类型数据
#     print(r.text)
#



# def test_post_upload_file(pub_data):
#     data ={
#         "file": open("aa.xls","rb")
# }
#     h = {"token":pub_data["token"]}
#     r=requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory",files=data,headers=h)#join关键字发送json类型数据
#     print(r.text)

#
# def test_post_upload_file(pub_data):
#
#     data ={
#   "file": open("aa.xls","rb")
# }
#     h = {"token":pub_data["token"]}
#     r=requests.post("http://qa.yansl.com:8084/user/lock",files=data,headers=h)#join关键字发送json类型数据
#     print(r.text)





def test_post_json_1(pub_data):
    data = {
  "pwd": "wh123456",
  "userName": "wh1kxd82"
}
    h = {"token": pub_data["token"]}
    r = requests.post("http://qa.yansl.com:8084/login",json=data,headers=h) # json关键字发送json类型数据

    # 请求信息
    # 请求方法
    print("请求方法:",r.request.method)
    # url
    print("url:", r.request.url)
    # 请求头
    print("请求头:", r.request.headers)
    # 请求正文
    print("请求正文:", r.request.body)


    # 响应信息
    # 响应状态码
    print("响应状态码 :", r.status_code)
    # 响应头
    print("响应头 :", r.headers)
    # 响应正文
    print("响应正文 :", r.text) # 获取响应文本
    print("响应正文 :", r.content) # 获取响应字节码
    print("响应正文 :", r.json()["message"]) # 获取响应字典
