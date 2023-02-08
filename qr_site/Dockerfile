FROM python:3

RUN apt-get update && apt-get install libgl1 -y
WORKDIR /srv/web/
COPY . /srv/web/
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8010

ENTRYPOINT ["sh","/srv/web/run.sh"]
