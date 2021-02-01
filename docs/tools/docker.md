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

## trouble shoot

#### Error response from daemon: OCI runtime create failed: container_linux.go:348: starting container process caused "process_linux.go:297: copying bootstrap data to pipe caused \"write init-p: broken pipe\"": unknown

系统版本为 Ubuntu 14.04, 升级 docker 后，版本不一致导致的，[解决方法](https://meta.discourse.org/t/docker-copying-bootstrap-data-to-pipe-caused-write-init-p-broken-pipe/108947/32)：
```
apt remove docker-ce docker-ce-cli
apt install docker-ce=18.06.1~ce~3-0~ubuntu
```
