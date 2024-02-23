FROM python:3.10

COPY keystone/requirements.txt  /keystone/
RUN pip install -r /keystone/requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
RUN pip install uwsgi pymysql -i https://mirrors.cloud.tencent.com/pypi/simple
COPY keystone/ /keystone/
COPY dockerfiles/keystone.conf /etc/keystone/keystone.conf
RUN mkdir /var/log/keystone/
WORKDIR /keystone
RUN python /keystone/setup.py install
ENV OS_KEYSTONE_CONFIG_DIR /etc/keystone

CMD uwsgi --http :5000 --wsgi-file $(which keystone-wsgi-public) --master --processes 4 --threads 2