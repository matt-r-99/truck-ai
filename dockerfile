FROM python:3.11-slim

WORKDIR /app
#install dependencies first

COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#copy app code

COPY . .
#run script
CMD ["python", "main.py"]
