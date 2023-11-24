# MySql

## 大小敏感

需要设置collate（校对） 。 collate规则：

`*_bin`: 表示的是binary case sensitive collation，也就是说是区分大小写的
`*_cs`: case sensitive collation，区分大小写
`*_ci`: case insensitive collation，不区分大小写

[图解SQL的Join](http://coolshell.cn/articles/3463.html)

## install mariadb

```
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client
sudo mysql_secure_installation
sudo mysql -uroot
```

```
sudo apt install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
sudo add-apt-repository "deb [arch=amd64,arm64,ppc64el] http://mariadb.mirror.liquidtelecom.com/repo/10.4/ubuntu $(lsb_release -cs) main"
sudo apt update
sudo apt -y install mariadb-server mariadb-client
```

## config mariadb

vi `/etc/mysql/mariadb.conf.d/50-server.cnf`

```
[mysqld]

lower_case_table_names=1
```

```
service mysql restart
```

## commands

### login mysql

```
mysql -u root -p
```

### list databases/tables

```
show databases;
show tables;
```

### create database

```
CREATE DATABASE liantest CHARACTER SET utf8;
```

### switch database

```
use mysql;
```

### delete database

```
mysqladmin -u root -p drop mytestdb;
drop database mytestdb;
```

### export database

```
mysqldump -u user -p password -d seahub > seahub.sql
```

### export data in all tables

```
mysqldump -u user -p password seahub > seahub.sql
```

### export data in two tables

```
mysqldump -u user -p password seahub profile_profile api2_token > table.sql
```

### show table schema

```
show create table table_name
```

or

```
describe dbname.table_name
```

### create user

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost';

FLUSH PRIVILEGES;
```

### change a user's password

```
use mysql;
update user set password=PASSWORD('password') where User='user';
flush privileges;
quit
```

### delete user

```
drop user 'root'@'114.249.235.35';
```

### allow remote connect

```
GRANT ALL ON *.* TO root@'192.168.255.221' IDENTIFIED BY 'root';
```

or

```
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password' WITH GRANT OPTION;
```

then

```
FLUSH PRIVILEGES;
```

### sort table by size

```
select TABLE_NAME, concat(truncate(data_length/1024/1024,2), ' MB') as data_size,
concat(truncate(index_length/1024/1024,2), ' MB') as index_size
from information_schema.tables where TABLE_SCHEMA = 'seahub-demo'
group by TABLE_NAME
order by data_length desc;
```

### select

```
select count(distinct username) from UserActivityStat where timestamp>='2022-01-01 00:00:00' and timestamp<="2022-12-31 23:59:59";

select count(distinct user) from api2_token where created>='2022-01-01 00:00:00' and created<="2022-12-31 23:59:59";

select count(distinct user) from api2_tokenv2 where created_at>='2022-01-01 00:00:00' and created_at<="2022-12-31 23:59:59";

select count(distinct username) from base_userlastlogin where last_login>='2022-01-01 00:00:00' and last_login<="2022-12-31 23:59:59";

select count(distinct op_user) from Activity where timestamp>='2022-01-01 00:00:00' and timestamp<="2022-12-31 23:59:59";
```
