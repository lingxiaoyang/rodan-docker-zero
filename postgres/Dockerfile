FROM postgres:11.5

# PostgreSQL Python language
RUN apt-get update
RUN apt-get -y install postgresql-plpython-11

# Redis-Python binding
RUN apt-get -y install python-pip
RUN pip install 'redis>=3.3,<3.3.99'
