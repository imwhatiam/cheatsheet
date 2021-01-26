## memcached

### install

for ubuntu

```
sudo apt-get install memcached
sudo pip install python-memcached
```

### clear memcached

```
echo 'flush_all' | nc localhost 11211
```

or

```
echo 'flush_all' | netcat localhost 11211
```

or

```
$ telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
flush_all
OK
quit
Connection to localhost closed by foreign host.
$
```

### restart/start/stop...

restart memcached

```
systemctl restart memcached
```

start memcached
```
systemctl start memcached
```

stop memcached
```
systemctl stop memcached
```

start memcached at boot
```
systemctl enable memcached
```

check the status of memcached
```
systemctl status memcached
```
