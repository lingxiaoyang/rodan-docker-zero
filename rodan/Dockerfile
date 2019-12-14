FROM python:2.7

COPY ./Rodan/requirements.txt /
RUN pip install -r /requirements.txt

# Manually upgrade psycopg2 version to fix the following error:
# ImportError('/usr/local/lib/python2.7/site-packages/psycopg2/.libs/libresolv-2-c4c53def.5.so: symbol __res_maybe_init version GLIBC_PRIVATE not defined in file libc.so.6 with link time reference',)
RUN pip install 'psycopg2>=2.7,<2.7.99' --upgrade

RUN pip install uwsgi

# Fix pybagit permissions (see Rodan .travis.yml)
RUN chmod -R 755 /usr/local/lib/python2.7/site-packages/pybagit

# We want to override a few Django settings, but we don't want to touch the upstream setting.py,
# so we create this local_settings.py elsewhere and add its directory `dev_settings` to PYTHONPATH
# so that Django can call `import local_settings` to load it (DJANGO_SETTINGS_MODULE).
#
# The mirrored_rodan_settings.py is a symlink to the original settings.py, and we create it
# because we cannot call `from rodan.settings import *` due to the Celery loading code in
# `/srv/Rodan/rodan/__init__.py` that gets loaded when Python discovers `rodan.settings`.
ENV PYTHONPATH /dev_settings:/mirrored_settings:$${PYTHONPATH}
RUN mkdir /mirrored_settings
RUN ln -s /srv/Rodan/rodan/settings.py /mirrored_settings/mirrored_rodan_settings.py
ENV DJANGO_SETTINGS_MODULE local_settings

WORKDIR /srv/Rodan
