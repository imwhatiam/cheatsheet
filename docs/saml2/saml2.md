# saml2

saml，Security Assertion Markup Language，安全断言标记语言。

SP，Service Provider 服务提供方。

IdP，Identity Provider 身份认证方。

通过浏览器 GET 或者 POST 请求来转发请求、交互信息。

IAM，Identity and Access Management.

## IDP Metadata.xml

|参数|含义|
|----|----|
|entityID|IdP 唯一标识。 建议使用域名形式，确保全局唯一。取值中要包含“https://”。 示例：https://www.idp.com|
|两个<ds:X509Certificate></ds:X509Certificate>内的值|是一份包含公钥的证书，该证书用于验证签名。为了确保安全性，建议使用长度大于等于2048位的公钥。SP通过IDP元数据文件中的签名证书来确认认证过程中断言消息的可信性、完整性。|
|<md:SingleLogoutService中Location的值|会话注销功能。示例：https://www.idp.com/saml/logout|
|<md:SingleSignOnService中Location的值|IDP处理SAML请求认证的地址，用以接收处理SAMLRequest，并生成SAMLResponse，示例：https://www.idp.com/saml/login|

## 登录流程

未登录时，浏览器会将页面重定向到 IdP，

`https://www.idp.com/saml/login?SAMLRequest={SAMLRequest}&RelayState={RelayState}&SigAlg={SigAlg}&Signature={Signature}`

并带上以下参数：

1. `SAMLRequest`。

2. `RelayState`，an URL parameter that we use to say to our Identity Provider where he should send the response back。

3. `SigAlg`，签名算法（比如：`http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`）。

4. `Signature`，签名值。SP 发起请求前，会将请求中的 `SAMLRequest={SAMLRequest}&RelayState={RelayState}&SigAlg={SigAlg}` 使用 SP 私钥签名（签名算法为 `SigAlg` 字段指定的算法），之后再做一次 Base64 编码作为签名值。


IdP 收到请求后通过 SP 公钥（SP Metadata.xml文件中 `<ds:X509Certificate></ds:X509Certificate>` 标签内的值）来验证签名。签名验证通过，则表明是合法 SP 发送的请求可以进行后续操作，否则请求非法。

显示 Idp 登录页面，用户登录成功后，IdP 发送 POST 请求给 SP（AssertionConsumerService）并带上以下参数：

1. `SAMLResponse`。

2. `RelayState`，samlRequest中相同参数值。


SP 收到 `SAMLResponse` 后，解析出用户信息，进行后续操作。

## Saml Tech Overview

![saml-tech-overview.png](./saml-tech-overview.png)

## Referer

- [Reloading SAML: Do you really need SAML?](https://sagarag.medium.com/reloading-saml-do-you-really-need-saml-931976b3b5e3)
- [Reloading SAML : SAML Basics](https://sagarag.medium.com/reloading-saml-saml-basics-b8999995c73e)
- [华为云 IDP Metadata.xml](https://support.huaweicloud.com/devg-bpconsole/access_00001.html)
- [华为云 saml 认证](https://support.huaweicloud.com/api-bpconsole/jac_00001.html)

## Tools

- [decode SAML requests](https://developer.pingidentity.com/en/tools/saml-decoder.html)
- <https://developers.onelogin.com/saml/online-tools/x509-certs/obtain-self-signed-certs>

----------

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