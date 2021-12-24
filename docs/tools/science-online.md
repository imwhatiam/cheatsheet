# tools/science-online.md

## create ssh tunnel
```
ssh -qTfnN -D 1080 root@demo.seafile.com
```

- -q: quiet模式，忽视大部分的警告和诊断信息（比如端口转发时的各种连接错误）
- -T: 禁用tty分配(pseudo-terminal allocation)
- -f: 登录成功后即转为后台任务执行
- -n: 重定向stdin为/dev/null，用于配合-f后台任务
- -N: 不执行远程命令（专门做端口转发）

## install and configure privoxy

to redirect http{s} requests to socks5
```
apt install privoxy
vim /etc/privoxy/config
```

```
forward-socks5t   /               127.0.0.1:1080 .
```

```
systemctl restart privoxy
```

## configure proxy
```
export http_proxy="127.0.0.1:8118"
export https_proxy="127.0.0.1:8118"
```
