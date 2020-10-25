FROM python:3.8

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*


COPY . /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
