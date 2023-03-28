FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

# https://developer.aliyun.com/mirror/ubuntu
# RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# COPY ubuntu-source.list /etc/apt/sources.list

RUN mkdir /root/.pip
COPY pip.conf /root/.pip/
COPY tmux.conf /root/.tmux.conf

RUN apt-get -q update && \
    apt-get -qy upgrade

RUN apt-get install -qy --no-install-recommends pkg-config \
    python3 python3-dev python3-pip python3-setuptools \
    curl less vim wget git net-tools tmux tzdata

# RUN rm -rf /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip install wheel && \
    pip install --upgrade django ipython pip

RUN git config --global user.name "lian" && \
    git config --global user.email "imwhatiam123@gmail.com" && \
    git config --global core.editor "vim"

# Clean up APT when done.
RUN apt-get -qy autoremove && \
    apt-get clean

