FROM python:3.9-slim-bullseye
WORKDIR /app
COPY app /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app", "--log-level", "debug"]