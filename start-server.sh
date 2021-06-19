#!/usr/bin/env bash
# start-server.sh
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd rrs_scraper; python manage.py createsuperuser --no-input)
fi
(cd rrs_scraper; gunicorn rrs_scraper.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) & nginx -g "daemon off;"