FROM python:3.6-slim

RUN apt-get update && apt-get install -y gcc python3-dev musl-dev g++ libxslt-dev
RUN pip install --upgrade pip
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR ./
CMD python3 run.py
EXPOSE 5000