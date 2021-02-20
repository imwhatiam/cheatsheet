# nginx

## install

```
apt update
apt install nginx
```

## SNI

[A more generic solution for running several HTTPS servers on a single IP address is TLS Server Name Indication extension (SNI, RFC 6066), which allows a browser to pass a requested server name during the SSL handshake and, therefore, the server will know which certificate it should use for the connection. ](http://nginx.org/en/docs/http/configuring_https_servers.html)

### nginx 是否支持 SNI

```
root@ubuntu-demo-com ~ # nginx -V
nginx version: nginx/1.10.3 (Ubuntu)
built with OpenSSL 1.0.2g  1 Mar 2016
TLS SNI support enabled
```

### 测试

#### 配置 nginx

Bind two different domain to the same IP.

Two nginx virtual hosts with different server name and certificate.

#### **python requests module 测试**

```
>>> import requests

>>> requests.get('https://www.imwhatiam.com')
<Response [200]>

>>> requests.get('https://demo.seafile.com')
<Response [200]
```

#### **openssl s_client 命令测试**

第一个请求加了 `-servername`  参数，请求 `www.imwhatiam.com:443` ，得到 `/CN=www.imwhatiam.com`

```
liandembp:~ lian$ openssl s_client -servername www.imwhatiam.com -connect www.imwhatiam.com:443
CONNECTED(00000005)
depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X3
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/CN=www.imwhatiam.com
   i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
 1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
   i:/O=Digital Signature Trust Co./CN=DST Root CA X3
```

第二个请求没加 `-servername`  参数，请求 `www.imwhatiam.com:443` ，得到 `/CN=demo.seafile.com`

当不加 `-servername` 参数的时候，得到的证书，和 nginx 配置中的顺序有关。哪个 server_name 的配置在文件最前，返回哪个。

```
openssl s_client  -connect www.imwhatiam.com:443
CONNECTED(00000005)
depth=1 C = US, O = Let's Encrypt, CN = Let's Encrypt Authority X3
verify error:num=20:unable to get local issuer certificate
verify return:0
---
Certificate chain
 0 s:/CN=demo.seafile.com
   i:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
 1 s:/C=US/O=Let's Encrypt/CN=Let's Encrypt Authority X3
   i:/O=Digital Signature Trust Co./CN=DST Root CA X3
```
