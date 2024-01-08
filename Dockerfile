FROM python:3.10
USER root
RUN mkdir /app
ADD . /app

WORKDIR /app



RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm ./google-chrome-stable_current_amd64.deb && \
    apt-get clean

RUN pip install -r requirements.txt

CMD ["python", "app.py"]