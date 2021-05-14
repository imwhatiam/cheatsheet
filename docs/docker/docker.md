# Docker

## install

```
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo docker run hello-world
```

## command

### login

```
# login to docker hub
docker login
```

### run

将本地的 8123 端口映射到 Docker 容器的 8000 端口。

```
docker run -it -p 127.0.0.1:8123:8000 ubuntu:latest /bin/bash
```

- `-t`: 在新容器内指定一个伪终端或终端。
- `-i`: 允许你对容器内的标准输入 (STDIN) 进行交互。
- `-P`: 是容器内部端口 **随机映射** 到主机的高端口。
- `-p`: 是容器内部端口 **绑定** 到指定的主机端口。

### ps

可用 `docker ps` 或者 `docker port {container_id}` 命令查看

```
docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS                    NAMES
fab859fcf1ad        ubuntu:latest       "/bin/bash"         4 seconds ago       Up 3 seconds                0.0.0.0:8123->8000/tcp   quirky_hopper
```

### port

```
docker port fab859fcf1ad
8000/tcp -> 0.0.0.0:8123
```

### logs

```
docker logs -f {container_id}
```

> `-f`: 像使用 `tail -f` 一样来输出容器内部的标准输出。

### top

```
docker top {container_id}
```

### commit

```
docker commit -m="update" -a="lian" container-name imwhatiam/ubuntu:v2
```

> `-m`: 提交的描述信息
> `-a`: 指定镜像作者
> `runoob/ubuntu:v2`: 指定要创建的目标镜像名

### push

```
# push local image to docker hub, must login first.
docker push imwhatiam/ubuntu-seafile:v1
```

### stop

```
docker stop $(docker ps -a -q)
```

### rm

```
docker rm $(docker ps -a -q -f status=exited)
```

### cp

```
# 将主机 /www/runoob 目录拷贝到容器 96f7f14e99ab 的 /www 目录下。
docker cp /www/runoob 96f7f14e99ab:/www/

# 将主机 /www/runoob 目录拷贝到容器 96f7f14e99ab 中，目录重命名为 www。
docker cp /www/runoob 96f7f14e99ab:/www

# 将容器 96f7f14e99ab 的 /www 目录拷贝到主机的 /tmp 目录中。
docker cp  96f7f14e99ab:/www /tmp/
```

```
docker cp foo.txt mycontainer:/foo.txt
docker cp mycontainer:/foo.txt foo.txt
```

### start

```
# restart it in the background
docker start  `docker ps -q -l`

# This will start all container which are in exited state.
docker start $(docker ps -a -q --filter "status=exited")
```

### attach

```
# reattach the terminal & stdin
docker attach `docker ps -q -l`
```

### exec

```
# This will connect to the particular container
docker exec -it <container-id> /bin/bash
```

### export

```
# 将 id 为 a404c6c174a2 的 **容器** 按日期保存为tar文件。
docker export -o mysql-`date +%Y%m%d`.tar a404c6c174a2
```

### save

```
# 将 **镜像** runoob/ubuntu:v3 生成 my_ubuntu_v3.tar
docker save -o my_ubuntu_v3.tar runoob/ubuntu:v3
```

### import

```
# 从镜像归档文件my_ubuntu_v3.tar创建镜像，命名为runoob/ubuntu:v4
docker import my_ubuntu_v3.tar runoob/ubuntu:v3
```

### search

```
docker search httpd
```

### inspect

```
# 查看 docker 底层信息
docker inspect

# 获取某个具体信息
docker inspect -f '{{.NetworkSettings.IPAddress}}' ubuntu
```

## trouble shoot

#### Error response from daemon: OCI runtime create failed: container_linux.go:348: starting container process caused "process_linux.go:297: copying bootstrap data to pipe caused \"write init-p: broken pipe\"": unknown

系统版本为 Ubuntu 14.04, 升级 docker 后，版本不一致导致的，[解决方法](https://meta.discourse.org/t/docker-copying-bootstrap-data-to-pipe-caused-write-init-p-broken-pipe/108947/32)：
```
apt remove docker-ce docker-ce-cli
apt install docker-ce=18.06.1~ce~3-0~ubuntu
```

## Dockerfile

```
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

RUN ln -s /usr/bin/python3 /usr/bin/python && \
    ln -s /usr/bin/pip3 /usr/bin/pip

RUN pip install wheel && \
    pip install --upgrade django ipython pip

RUN git config --global user.name "lian" && \
    git config --global user.email "imwhatiam123@gmail.com" && \
    git config --global core.editor "vim"

# Clean up APT when done.
RUN apt-get -qy autoremove && \
    apt-get clean
```
