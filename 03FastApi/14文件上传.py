import uvicorn
from fastapi import FastAPI,File,UploadFile
from typing import List


app = FastAPI(title="文件上传接口",description="文件上传接口",version="0.0.1")

# 文件以请求体方式上传文件  multipart/form-data
# 单文件上传接口(小文件)
# 使用bytes类型接收文件，会将整个文件内容读入内存
@app.post('/file',tags=["文件上传接口"])
def upload_single_small_file(file:bytes = File()):
    # File() 表示这是一个文件上传参数
    # bytes 类型适合小文件，因为会一次性加载到内存
    print("接收到的文件字节数:",len(file))  # 打印内存信息

    return{
        "message" : "小文件上传成功",
        "file_size": f"{len(file)} bytes"
    }

# 多文件上传接口(小文件)
@app.post('/files',tags=["文件上传接口"])
def data(files:List[bytes] = File()):
    return {
        "message": "小文件上传成功",
        "file_size": f"上传了{len(files)}个文件 "
    }

# 单文件上传接口(大文件)
@app.post('/uploadfile',tags=["文件上传接口"])
def upload_single_big_file(file:UploadFile):
    # UploadFile适合大文件上传，因为它使用流式处理
    # 可以获取文件的相关属性
    print("接收到文件名:",file.filename,"文件类型:",file.content_type,"文件大小:",file.size)

    # 流式写入文件，避免一次性加载大文件到内存
    with open (f"./images/{file.filename}","wb") as f:
        # 逐行读取上传的文件并写入本地文件  file.file为文件句柄
        for line in file.file:
            f.write(line)

    return{
        "message":"大文件上传成功",
        "file_name":file.filename,
        "save_path" : f"./images/{file.filename}"
    }

if __name__ == "__main__":
    uvicorn.run(
        app,   # 应用实例
        host='0.0.0.0', # 监听地址{"method":"get方法"}
        port=8080,   # 监听端口
        log_level="debug"  # 日志级别
    )
