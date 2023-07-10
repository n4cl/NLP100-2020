FROM python:3.11.4-buster

RUN apt-get -y update && apt-get -y install mecab libmecab-dev git make curl xz-utils file sudo
RUN pip install --upgrade pip
RUN pip install mecab-python3

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd && \
    ./bin/install-mecab-ipadic-neologd -n -y && \
    cd .. && \
    rm -rf mecab-ipadic-neologd && \
    echo `mecab-config --dicdir`"/mecab-ipadic-neologd" && \
    export MECABRC=/etc/mecabrc
