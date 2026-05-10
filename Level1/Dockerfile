FROM python:3.9-slim

WORKDIR /app

# 安装依赖
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple

# 拷贝代码
COPY app.py .

# 暴露端口
EXPOSE 5000

CMD ["python", "app.py"]
