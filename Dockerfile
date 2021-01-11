FROM ubuntu:18.04

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
&& apt-get clean \
&& apt-get update \
&& apt-get install -y python3-pip python3-dev

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


RUN mkdir /jixiao
WORKDIR /jixiao
COPY requirements.txt /usr
COPY . /jixiao
RUN pip3 install -r requirements.txt  -i  https://pypi.tuna.tsinghua.edu.cn/simple  --no-cache-dir
CMD ["gunicorn", "jixiao:app", "-c", "gunicorn_conf.py"]
