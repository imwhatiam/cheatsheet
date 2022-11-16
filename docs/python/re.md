# re

```
In [1]: import re

In [2]: line = 'CREATE TABLE IF NOT EXISTS `api2_tokenv2` (`key` varchar(40) NOT NULL PRIMARY KEY...'

In [3]: m = re.search('CREATE TABLE(?: IF NOT EXISTS)? [`"]?(\w+)[`"]?(\s*\(.*)', line)

In [4]: m.groups()
Out[4]: ('api2_tokenv2', ' (`key` varchar(40) NOT NULL PRIMARY KEY...')
```


`\1` `\2`分别代表什么了呢？其实代表的就是`group(1)`和`group(2)`，可以引用已经匹配出来的字符串。

```
In [1]: import re

In [2]: line = "created_at datetime NOT NULL DEFAULT `1970-01-01 00:00:00`,"

In [3]: line = re.sub(r"default `([^`]*)`", r"default '\1'", line, 0, re.IGNORECASE)

In [4]: line
Out[4]: "created_at datetime NOT NULL default '1970-01-01 00:00:00',"
```
