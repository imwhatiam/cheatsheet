## MySql

### install mariadb

```
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client
sudo mysql_secure_installation
sudo mysql -uroot
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
create database seahub charset utf8;
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

### trouble shoot

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
