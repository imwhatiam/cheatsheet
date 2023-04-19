# tools/science-online.md

## Shadowsocks

### ss-local

https://github.com/shadowsocks/ShadowsocksX-NG

test if ss-local works
```
curl --socks5 127.0.0.1:1080 http://cip.cc
```

### ssserver

#### pip install shadowsocks

tested on ubuntu 18.04

```
pip install shadowsocks
```

create configuration file
```
vim /etc/shadowsocks.json
{
    "server":"server ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"yourpassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

start ssserver
```
ssserver -c /etc/shadowsocks.json -d start
```

if the following error occurs
```
AttributeError: /usr/lib/x86_64-linux-gnu/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup
```

then
```
vi /usr/local/lib/python3.6/dist-packages/shadowsocks/crypto/openssl.py

%s/EVP_CIPHER_CTX_cleanup/EVP_CIPHER_CTX_reset/gc
```

#### apt install shadowsocks-libev

```
sudo apt update
sudo apt upgrade
sudo apt install vim git wget curl tmux
sudo apt install shadowsocks-libev

reboot

vi /etc/shadowsocks-libev/config.json

sudo systemctl restart shadowsocks-libev
sudo systemctl status shadowsocks-libev
sudo systemctl enable shadowsocks-libev

cat /etc/shadowsocks-libev/config.json

sudo iptables -I INPUT -p tcp --dport 8388 -j ACCEPT
sudo iptables -I INPUT -p udp --dport 8388 -j ACCEPT
sudo ufw allow 8388
```

## create ssh tunnel

```
ssh -qTfnN -D 1080 root@demo.seafile.com
```

- -q: quiet模式，忽视大部分的警告和诊断信息（比如端口转发时的各种连接错误）
- -T: 禁用tty分配(pseudo-terminal allocation)
- -f: 登录成功后即转为后台任务执行
- -n: 重定向stdin为/dev/null，用于配合-f后台任务
- -N: 不执行远程命令（专门做端口转发）
```
