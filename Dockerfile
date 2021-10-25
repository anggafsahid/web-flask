# Python 3.6.7
FROM python:3.6.7-alpine3.6
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]