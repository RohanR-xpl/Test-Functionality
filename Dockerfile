FROM python:3.11
WORKDIR /app
RUN pip install flask flask_sqlalchemy psycopg2
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
