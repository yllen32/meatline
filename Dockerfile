FROM python:3.10.7-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir 
COPY meet_line/ /app
WORKDIR /app
CMD ["gunicorn", "meet_line.wsgi:application", "--bind", "0:8000" ]
