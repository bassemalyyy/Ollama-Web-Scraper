FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt
RUN pip install chainlit

EXPOSE 8000

CMD ["chainlit", "run", "main.py", "-h", "0.0.0.0", "-p", "8000"]
