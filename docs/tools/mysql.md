## MySql

### install mariadb

```
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client
sudo mysql_secure_installation
sudo mysql -uroot
```

### config mariadb

vi `/etc/mysql/mariadb.conf.d/50-server.cnf`

```
[mysqld]

lower_case_table_names=1
```

```
service mysql restart
```

### commands

login mysql

```
mysql -u root -p
```

list databases/tables

```
show databases;
show tables;
```

create database

```
CREATE DATABASE liantest CHARACTER SET utf8;
```

switch database

```
use mysql;
```

delete database

```
mysqladmin -u root -p drop mytestdb;
drop database mytestdb;
```

export database

```
mysqldump -u user -p password -d seahub > seahub.sql
```

export database and data in tables

```
mysqldump -u user -p password seahub > seahub.sql
```

show table schema

```
show create table table_name
```

or

```
describe dbname.table_name
```

create user

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';

FLUSH PRIVILEGES;
```

change a user's password

```
mysql -u root -p
mysql> use mysql;
mysql> update user set password=PASSWORD('password') where User='user';
mysql> flush privileges;
mysql> quit
```

delete user

```
drop user 'root'@'114.249.235.35';
```

allow remote connect

```
GRANT ALL ON *.* TO root@'192.168.255.221' IDENTIFIED BY 'root';
```

### trouble shoot

#### ERROR 1044 (42000): Access denied for user 'seafile'@'localhost' to database 'ifile'

```
mysql -u root -p

grant all privileges on *.* to 'seafile'@'localhost' identified by 'IeKi8aht';

flush privileges;
```

#### Specified key was too long; max key length is 767 bytes

系统变量 `innodb_large_prefix` 开启了，则对于使用 `DYNAMIC` 或 `COMPRESSED` 行格式的 `InnoDB` 表，索引键前缀限制为3072字节。如果禁用 `innodb_large_prefix` ，不管是什么表，索引键前缀限制为767字节。

上述的bug很明显是索引超出了限制的长度767（我司生产上 `innodb_large_prefix` 禁用了）：

我发现报错的那张表建立了一个 `varchar` 类型的索引， `varchar(255)` ，觉得没什么问题，其实不然，上述的767是字节，而 `varchar` 类型是字符，同时我发现我使用的字符集为（`utf8mb4`），这个指每个字符最大的字节数为4，所以很明显 `4*255 > 767`。

所以就报上述错了 `（Specified key was too long; max key length is 767 bytes）`。

解决方法：

改变 `varchar` 的字符数，我改成了64就可以了。 `varchar(64)` 

或者启用 `innodb_large_prefix` ，那么限制值会增加到3072


#### access to Mysql database from remote server

```
mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
mysql> FLUSH PRIVILEGES;
```

#### [MySQL Error 1170 (42000): BLOB/TEXT Column Used in Key Specification Without a Key Length](http://stackoverflow.com/questions/1827063/mysql-error-key-specification-without-a-key-length)

#### [图解SQL的Join](http://coolshell.cn/articles/3463.html)

#### 数据库外键问题

阿里巴巴定制的数据库中，创建表需要使用字符集`CHARSET=utf8mb4` 。

```
CREATE TABLE `tags_fileuuidmap` (
  ...
  `uuid` char(32) NOT NULL COMMENT 'uuid',
  ...
) ENGINE=InnoDB AUTO_INCREMENT=396 DEFAULT CHARSET=utf8mb4 COMMENT='tags_fileuuidmap'
;
```

Seahub 的数据库中，创建表时使用的字符集为`CHARSET=utf8` 。

```
CREATE TABLE `related_files_relatedfiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `o_uuid_id` char(32) NOT NULL,
  `r_uuid_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `related_files_relate_o_uuid_id_aaa8e613_fk_tags_file` (`o_uuid_id`),
  KEY `related_files_relate_r_uuid_id_031751df_fk_tags_file` (`r_uuid_id`),
  CONSTRAINT `related_files_relate_o_uuid_id_aaa8e613_fk_tags_file` FOREIGN KEY (`o_uuid_id`) REFERENCES `tags_fileuuidmap` (`uuid`),
  CONSTRAINT `related_files_relate_r_uuid_id_031751df_fk_tags_file` FOREIGN KEY (`r_uuid_id`) REFERENCES `tags_fileuuidmap` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8
```

所以直接使用 Seahub 的创建语句，给阿里巴巴创建新表时，会报错：

```
ERROR 1005 (HY000): Can't create table `ali_seahub`.`related_files_relatedfiles` (errno: 150 "Foreign key constraint is incorrectly formed")
```

解决方法

根据 MySQL 的 [外键文档](https://dev.mysql.com/doc/refman/5.6/en/create-table-foreign-keys.html)

> Corresponding columns in the foreign key and the referenced key must have similar data types. The size and sign of integer types must be the same. The length of string types need not be the same. For nonbinary (character) string columns, the character set and collation must be the same.

将 Seahub 建表语句中的 CHARSET 改为 utf8mb4，经测试可创建新表成功。


#### [Err] 1005 - Can't create table (errno: 150 "Foreign key constraint is incorrectly formed")

该错误一般出现原因如下：

1、外键的引用类型不一样，如主键是int外键是char

2、找不到主表中引用的列

3、主键和外键的字符编码不一致，也可能存储引擎不一样

```
CREATE TABLE t_employee(
    emp_id INT(3) PRIMARY KEY,
    emp_no INT(3) UNIQUE NOT NULL,
    emp_name VARCHAR(10) NOT NULL,
    emp_age tinyint(4) NOT NULL DEFAULT 25 CHECK (emp_age BETWEEN 20 AND 60),
    sex VARCHAR(1) CHECK (sex in ('男','女')),
    job VARCHAR(20),
    sal INT(10),
    -- inline写法
    -- REFERENCES 主表（主表字段）
    -- dept_no int  REFERENCES t_dept(dept_no)
    -- outline写法
    dept_no int NOT NULL ,
    FOREIGN KEY(dept_no) REFERENCES t_dept(dept_no) ON DELETE SET NULL
);
```

格式为 `dept_no int NOT NULL`, 但是外键却为 `FOREIGN KEY(dept_no) REFERENCES t_dept(dept_no) ON DELETE SET NULL`，删除格式的 `NOT NULL` 即可

#### errno: 150 "Foreign key constraint is incorrectly formed"

建立外键的字段必须和引用表的字段一模一样的类型。

<https://upliu.net/foreign-key-constraint-is-incorrectly-formed.html>

#### ERROR 1698 (28000): Access denied for user 'root'@'localhost'

<https://stackoverflow.com/questions/39281594/error-1698-28000-access-denied-for-user-rootlocalhost>

Some systems like Ubuntu, mysql is using by default the UNIX auth_socket plugin.

Basically means that: db_users using it, will be "auth" by the system user credentias. You can see if your root user is set up like this by doing the following:

```
$ sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> SELECT User, Host, plugin FROM mysql.user;

+------------------+-----------------------+
| User             | plugin                |
+------------------+-----------------------+
| root             | auth_socket           |
| mysql.sys        | mysql_native_password |
| debian-sys-maint | mysql_native_password |
+------------------+-----------------------+
```

As you can see in the query, the root user is using the auth_socket plugin

There are 2 ways to solve this:

You can set the root user to use the mysql_native_password plugin
You can create a new db_user with you system_user (recommended)
Option 1:

```
$ sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> UPDATE user SET plugin='mysql_native_password' WHERE User='root';
mysql> FLUSH PRIVILEGES;
mysql> exit;

$ sudo service mysql restart
```

Option 2: (replace YOUR_SYSTEM_USER with the username you have)

```
$ sudo mysql -u root # I had to use "sudo" since is new installation

mysql> USE mysql;
mysql> CREATE USER 'YOUR_SYSTEM_USER'@'localhost' IDENTIFIED BY 'YOUR_PASSWD';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'YOUR_SYSTEM_USER'@'localhost';
mysql> UPDATE user SET plugin='auth_socket' WHERE User='YOUR_SYSTEM_USER';
mysql> FLUSH PRIVILEGES;
mysql> exit;

$ sudo service mysql restart
```

Remember that if you use option #2 you'll have to connect to mysql as your system username (mysql -u YOUR_SYSTEM_USER)

Note: On some systems (e.g., Debian stretch) 'auth_socket' plugin is called 'unix_socket', so the corresponding SQL command should be: UPDATE user SET plugin='unix_socket' WHERE User='YOUR_SYSTEM_USER';

Update: from @andy's comment seems that mysql 8.x.x updated/replaced the auth_socket for caching_sha2_password I don't have a system setup with mysql 8.x.x to test this, however the steps above should help you to understand the issue. Here's the reply:

One change as of MySQL 8.0.4 is that the new default authentication plugin is 'caching_sha2_password'. The new 'YOUR_SYSTEM_USER' will have this auth plugin and you can login from the bash shell now with "mysql -u YOUR_SYSTEM_USER -p" and provide the password for this user on the prompt. No need for the "UPDATE user SET plugin" step. For the 8.0.4 default auth plugin update see, https://mysqlserverteam.com/mysql-8-0-4-new-default-authentication-plugin-caching_sha2_password/
