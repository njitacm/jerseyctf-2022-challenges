FROM python:3.10.2-slim

WORKDIR /app

RUN pip install --no-cache-dir gunicorn

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY static static
COPY templates templates

EXPOSE 80

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
