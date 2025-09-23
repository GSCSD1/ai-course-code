import requests

# 基础 URL
base_url = "http://127.0.0.1:8080"

"""post 表单参数请求方法  """

# 定义表单参数（包含username和password）
form_data1 = {
    "username": "testuser",
    "password": "testpass123"
}
# 通过data封装表单参数
response1 = requests.put(f"{base_url}/regin", data=form_data1)
print("1. 完整表单参数提交：")
print("状态码：", response1.status_code)
print("响应内容：", response1.text)
print()

