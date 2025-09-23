import os

import requests
base_url = "http://127.0.0.1:8080"


"""请求体参数 请求方法"""
user_data = {
    "name" : "a张三",
    "age" : 25,
    "sex" : "男",
    "addr" :{
        "province" : "广东",
        "city" : "深圳"
    }
}
# 通过json封装请求体参数
# response =  requests.post(f"{base_url}/data",json = user_data)
# print("请求结果：")
# print("状态码：",response.status_code)
# print("响应报文：",response.json())
# print()


"""表单参数 请求方法"""
# form_data = {
#     "username" : "admin",
#     "password" : "123456"
# }
# # 通过data封装表单参数
# response =  requests.put(f"{base_url}/regin",data = form_data)
# print("请求结果：")
# print("状态码：",response.status_code)
# print("响应报文：",response.json())
# print()

"""上传单个文件 小文件和大文件的请求方式是一样的"""
# with open('./images/1.png','rb') as f:
#     # files参数是一个字典  键为接口中定义的参数名
#     # 值是一个元组 ("文件名", 文件对象, "MIME类型")
#     files = {"file":("1.png",f,"image/png")}
#     response =  requests.post(f"{base_url}/uploadfile",files=files)
#
# print("请求结果：")
# print("状态码：",response.status_code)
# print("响应报文：",response.json())
# print()


"""上传多个文件 """
# with open('./images/1.png','rb') as f1,open('./images/2.png','rb') as f2:
#     # 多个文件需要打包成元组
#     files = [
#         ("files",("1.png", f1, "image/png")),
#         ("files",("2.png", f2, "image/png")),
#     ]
#     response = requests.post(f"{base_url}/files", files=files)
#
# print("请求结果：")
# print("状态码：",response.status_code)
# print("响应报文：",response.json())
# print()
#


"""获取静态文件"""

# 1、获取文本文件并读取内容
# response =  requests.get(f"{base_url}/staticVideo/1.txt")
# if response.status_code == 200:
#     print("请求结果：")
#     print("响应报文：",response.text)  # 文本文件直接用 .text 获取内容
#     print()

# 2、获取图片文件并保存到本地

# file = "2.png"
# download_dir = r"C:\Users\33122\Desktop\2507Code\03FastApi\download"
# response =  requests.get(f"{base_url}/staticImages/{file}")
#
# print("请求结果：")
# if response.status_code == 200:
#     with open(os.path.join(download_dir,file),'wb') as f:
#         f.write(response.content)
#         print(f"图片已保存：{file}")
# else:
#     print("图片请求失败",response.status_code)

# 3、请求视频文件并保存到本地(大文件建议流式下载)
file = "3.MP4"
download_dir = r"C:\Users\33122\Desktop\2507Code\03FastApi\download"
# 流式下载大文件 （避免一次性加载到内存）
with requests.get(f"{base_url}/staticVideo/{file}",stream=True) as reponse_video:
    if reponse_video.status_code == 200:
        with open(os.path.join(download_dir,file),'wb') as f:
           # 迭代下载
          for chunk in reponse_video.iter_content(chunk_size=2*1024*1024): # 2M chunk
              if chunk:
                  f.write(chunk)

        print(f"视频已保存：{file}")
    else:
        print("视频请求失败",reponse_video.status_code)
