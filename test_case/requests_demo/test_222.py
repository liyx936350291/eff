import requests
#request发送http请求
def test_no_params():
    # 使用 requests.get 发送一个get 请求
    # r = requests.get("https://www.baidu.com/")
    # 使用 requests.get 发送一个get 请求
    # r = requests.request(method='GET',url="https://www.baidu.com/")
    sess = requests.session() #使用session建立连接
    r = sess.request(method='GET',url="https://www.baidu.com/")
    r = sess.request(method='GET',url="https://www.baidu.com/")
    print(r.text) #text 获取响应对象中，响应正文数据

def test_get_params():
    #get 请求带参数
    pa = {"accountNamee":"xuepl123"} #把“get”参数放入一个字典中
    r = requests.request("GET","http://qa.yansl.com:8084/acc/getAccInfo",params=pa)#请求时以params关键字传参
    print(r.text)


def test_get_path():
    #get请求参数再path中
    #使用.format 进行字符串格式化
    r = requests.request("get","http://qa.yansl.com:8084//acc/getAllAccs/{pageNum}/{pageSize}".format(pageNum = 1,pageSize = 1))
    print(r.text)

def test_get_file(pub_data):
    #get请求下载文件
    p = {"pridCode":"63803y"}
    h = {"token":pub_data['token']}
    r = requests.request("GET", "http://qa.yansl.com:8084/product/downProdRepertory", params=p,headers = h)
    # r.content 获取响应正文的字节码（二进制）
    with open("aa.xls","wb") as f: #with语法 打卡文件并赋值给变量f
        f.write(r.content)  #把响应中的数据写入到文件


#post 请求发送json类型数据
def test_post_json():
    data = {
  "pwd": "abc123",
  "userName": "tutu653"
}
    r = requests.post("http://qa.yansl.com:8084/login",json= data) #json关键字发送json类型数据
    print(r.text)

def test_post_formdata(pub_data):
    #post请求键值对数据
    data = {
  "userName": "qvev5957"
}
    h = {"token":pub_data['token']}
    r = requests.post("http://qa.yansl.com:8084/user/lock",data= data,headers =h) #json关键字发送json类型数据
    print(r.text)

#post请求上传文件
def test_post_upload_file(pub_data):
     data = {
         "file": open("aa.xls","rb")
     }
     h = {"token": pub_data['token']}
     r = requests.post("http://qa.yansl.com:8084/product/uploaProdRepertory", files=data, headers=h)  # files关键字发送文件类型的关键字
     print(r.text)

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