# Base image
FROM python:3.12-slim

# Cài đặt các package system cần thiết
RUN apt-get update && apt-get install build-essential -y
RUN apt-get install -y curl wget git

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy toàn bộ thư mục code và các file từ root của repo
COPY code ./code
COPY requirements.txt .
COPY .env .

# Cài đặt dependencies
RUN pip install -r requirements.txt

# Expose port cho Streamlit
EXPOSE 8501

# Khởi chạy ứng dụng 
ENTRYPOINT ["streamlit", "run", "/app/code/app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#docker build -t chatbot-app .
#docker run -p 8501:8501 --env-file .env chatbot-app
