FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "ml.py", "--ip=0.0.0.0", "--port=5000", "--allow-root", ]
