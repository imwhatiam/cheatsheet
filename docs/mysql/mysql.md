# MySql

[图解SQL的Join](http://coolshell.cn/articles/3463.html)

## install mariadb

```
sudo apt-get update
sudo apt-get install mariadb-server mariadb-client
sudo mysql_secure_installation
sudo mysql -uroot
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
