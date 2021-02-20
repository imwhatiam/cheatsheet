# python3-saml-demo-django

<https://github.com/imwhatiam/python3-saml-demo-django>

1. idp 使用 https://samltest.id/ 提供的服务。也可对接 onelogin 提供的 idp 服务，具体参考：https://developers.onelogin.com/saml/python 。

1. sp 使用 https://github.com/onelogin/python3-saml

## 用法

运行命令（也可下载 Dockerfile 和 settings.json 到同一目录后自行 `docker build -t imwhatiam/python3-saml-demo-django:v1 .`）：

```
docker run -it -p 8000:8000 --name test-saml2 imwhatiam/python3-saml-demo-django:v1 bash
```

进入到容器后，再运行：

```
python3 manage.py runserver 0.0.0.0:8000
```

然后浏览器中访问 http://127.0.0.1:8000/

点击 Login，之后进入到 https://samltest.id/ 的登录界面，按提示输入用户名密码后，即可跳转回本地，并显示已登录用户的信息。 

## 额外说明

### 上传 metadata 到 https://samltest.id/

我已经预先设置好，如 sp 访问地址变了，需要重新上传：

1. 访问 http{s}://new-domain-or-ip/metadata/ 并将 xml 文件下载到本地。
2. 访问 https://samltest.id/upload.php 将 xml 文件上传上去。

### 配置 settings.json

我已预先配置好:

sp 部分使用 onelogin 默认配置 https://github.com/onelogin/python3-saml/blob/master/demo-django/saml/settings.json#L4 ，但注意需要改为自己的域名或IP。

sp 使用自签名证书：`openssl req -new -x509 -days 3652 -nodes -out sp.crt -keyout sp.key`

idp 部分参考 https://samltest.id/download/#SAMLtest%E2%80%99s_IdP

### logout

这部分未配置成功，点击 Logout 后页面显示：

```
Errors:
invalid_response
Reason: The status code of the Response was not Success, was Responder -> unexpected
```

查看 https://samltest.id/logs/idp.log 上的 [log](./logout-error-from-idp.log)，估计是签名、加密的问题，未做进一步调测。
