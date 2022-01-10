FROM python:latest

WORKDIR /app
COPY /bot bot
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "-m", "bot" ]