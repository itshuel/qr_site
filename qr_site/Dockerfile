FROM python:3

RUN apt-get update
WORKDIR /srv/web
COPY ./qr_site ./srv/web
RUN pip install --upgrade pip

EXPOSE 8010

CMD ["source", "venv/bin/activate"]
CMD ["python", "qr_site/qrcoder.py", "&"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8010", '--insecure']
