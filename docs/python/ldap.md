# ldap

|缩写|全称|
|:----|:----|
|LDAP|Light Directory Access Portocol|
|DN|Distinguished Name|
|dc|Domain Component|
|ou|Organization Unit|
|cn|Common Name|
|uid| User ID|

```
cn=username,ou=people,dc=test,dc=com
```

是一个 DN，代表一条记录，代表一位在 test.com 公司 people 部门的用户 username。

## python3-ldap

```
apt install python3-ldap
```

```
import ldap
from pprint import pprint

ldapconn = ldap.initialize('ldap://ldap.forumsys.com:389')
ldapconn.simple_bind_s('cn=read-only-admin,dc=example,dc=com', 'password')

base_dn = 'dc=example,dc=com'

print("\nsearch_filter = 'ou=scientists'")
search_filter = 'ou=scientists'
result = ldapconn.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter, None)
pprint(result)

print("\nsearch_filter = 'uid=tesla'")
search_filter = 'uid=tesla'
result = ldapconn.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter, None)
pprint(result)
```

```
search_filter = 'ou=scientists'
[('ou=scientists,dc=example,dc=com',
  {'cn': [b'Scientists'],
   'objectClass': [b'groupOfUniqueNames', b'top'],
   'ou': [b'scientists'],
   'uniqueMember': [b'uid=einstein,dc=example,dc=com',
                    b'uid=galieleo,dc=example,dc=com',
                    b'uid=tesla,dc=example,dc=com',
                    b'uid=newton,dc=example,dc=com',
                    b'uid=training,dc=example,dc=com',
                    b'uid=jmacy,dc=example,dc=com']})]

search_filter = 'uid=tesla'
[('uid=tesla,dc=example,dc=com',
  {'cn': [b'Nikola Tesla'],
   'gidNumber': [b'99999'],
   'homeDirectory': [b'home'],
   'mail': [b'tesla@ldap.forumsys.com'],
   'objectClass': [b'inetOrgPerson',
                   b'organizationalPerson',
                   b'person',
                   b'top',
                   b'posixAccount'],
   'sn': [b'Tesla'],
   'uid': [b'tesla'],
   'uidNumber': [b'88888']})]
```

## ldap test server

### zflexldapadministrator

LDAP Server Connection Info:

```
Server: www.zflexldap.com 
Port: 389
Bind DN: cn=ro_admin,ou=sysadmins,dc=zflexsoftware,dc=com
Bind Password: zflexpass
```

Other Users IDs and their passwords are:

```
uid=guest1,ou=users,ou=guests,dc=zflexsoftware,dc=com
guest1password
uid=guest2,ou=users,ou=guests,dc=zflexsoftware,dc=com
guest2password
uid=guest3,ou=users,ou=guests,dc=zflexsoftware,dc=com
guest3password
```

- [https://www.zflexldapadministrator.com/index.php/blog/82-free-online-ldap](https://www.zflexldapadministrator.com/index.php/blog/82-free-online-ldap)

### forumsys

Here are the credentials for an Online LDAP Test Server that you can use for testing your applications that require LDAP-based authentication.  Our goal is to eliminate the need for you to download, install and configure an LDAP sever for testing. If all you need is to test connectivity and authentication against a few identities, you have come to the right place.

LDAP Server Information (read-only access):

```
Server: ldap.forumsys.com
Port: 389
Bind DN: cn=read-only-admin,dc=example,dc=com
Bind Password: password
```

All user passwords are `password`.

You may also bind to individual Users (uid) or the two Groups (ou) that include:

```
ou=mathematicians,dc=example,dc=com

riemann
gauss
euler
euclid
```

```
ou=scientists,dc=example,dc=com

einstein
newton
galieleo
tesla
```

![ldap](https://www.forumsys.com/wp-content/uploads/2014/02/LDAP-Users1.png)

- [https://www.forumsys.com/tutorials/integration-how-to/ldap/online-ldap-test-server/](https://www.forumsys.com/tutorials/integration-how-to/ldap/online-ldap-test-server/)
