# CAS 集成

测试用户名：`casuser`
密码：`Mellon`

## via python

seahub_settings.py

```
ENABLE_CAS = True
CAS_SERVER_URL = 'https://casserver.herokuapp.com/cas/'
CAS_LOGOUT_COMPLETELY = True
```

## via apache

### ubuntu 18.04

```
apt-get install libapache2-mod-auth-cas
```

```
vi /etc/apache2/mods-enabled/auth_cas.conf
```

```
CASCookiePath /var/cache/apache2/mod_auth_cas/
CASLoginURL https://casserver.herokuapp.com/cas/login
CASValidateURL https://casserver.herokuapp.com/cas/serviceValidate
```

```
vi /etc/apache2/sites-enabled/000-default.conf
```

```
<VirtualHost *:80>
    Alias /media  /home/user/haiwen/seafile-server-latest/seahub/media

    RewriteEngine On

    <Location /media>
        Require all granted
    </Location>

    <Location /sso>
        AuthType CAS
        Require valid-user
        CASAuthNHeader remote-user
    </Location>

    # seafile fileserver
    ProxyPass /seafhttp http://127.0.0.1:8082
    ProxyPassReverse /seafhttp http://127.0.0.1:8082
    RewriteRule ^/seafhttp - [QSA,L]

    # seahub
    SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
```

```
vi /opt/seafile/conf/seahub_settings.py
```

```
ENABLE_REMOTE_USER_AUTHENTICATION = True
REMOTE_USER_DOMAIN = 'your.seafile-domain.com'
```

### centos 7

```
yum install mod_auth_cas
```

```
vi /etc/httpd/conf.d/auth_cas.conf
```

其他同上

* <https://apereo.github.io/cas/6.0.x/index.html>
* <https://dacurry-tns.github.io/deploying-apereo-cas/introduction_overview.html>
