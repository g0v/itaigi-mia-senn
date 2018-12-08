FROM i3thuan5/tai5-uan5_gian5-gi2_kang1-ku7
MAINTAINER Sing-hong

RUN pip3 install django kau3-tian2_iong7-ji7 gunicorn django-cors-headers

COPY . .
RUN python3 manage.py test
CMD gunicorn miasenn.wsgi --log-level debug -b 0.0.0.0:8000
