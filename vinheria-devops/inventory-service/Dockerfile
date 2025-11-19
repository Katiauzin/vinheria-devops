FROM python:3.9-slim

WORKDIR /usr/src/app

RUN pip install flask requests

COPY app.py .

CMD ["python", "app.py"]