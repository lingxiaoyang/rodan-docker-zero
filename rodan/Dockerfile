FROM python:2.7

COPY ./Rodan/requirements.txt /
RUN pip install -r /requirements.txt

# Manually upgrade psycopg2 version to fix the following error:
# ImportError('/usr/local/lib/python2.7/site-packages/psycopg2/.libs/libresolv-2-c4c53def.5.so: symbol __res_maybe_init version GLIBC_PRIVATE not defined in file libc.so.6 with link time reference',)
RUN pip install 'psycopg2>=2.7,<2.7.99' --upgrade

RUN pip install uwsgi

WORKDIR /srv/Rodan
