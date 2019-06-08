FROM python:3.5.3
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py" ]
