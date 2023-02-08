#! /bin/bash
source /srv/web/venv/bin/activate
python qr_site/qrcoder.py &
python manage.py runserver 0.0.0.0:8010 --insecure
