# tools/science-online.md

## Shadowsocks

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
