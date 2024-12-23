# Linux 命令

```
python /root/scripts/start.py >> /var/log/start.log 2>&1
```

## check Linux version

```
lsb_release -a
uname -a
cat /etc/issue

cat /etc/centos-release
```

## 查看登录信息

```
[root@node3 ~]# last

root     pts/0        43.224.44.74     Wed Nov 16 09:43   still logged in
root     pts/2        114.249.209.248  Tue Nov  1 21:40 - 23:54  (02:13)
root     pts/1        114.249.209.248  Tue Nov  1 20:41 - 23:57  (03:16)
root     pts/0        114.249.209.248  Tue Nov  1 20:35 - 23:57  (03:21)
root     pts/0        114.249.209.248  Tue Nov  1 19:42 - 20:35  (00:52)
root     pts/0        54.179.196.89    Tue Nov  1 14:55 - 19:07  (04:11)
root     pts/0        123.117.78.247   Tue Nov  1 14:52 - 14:53  (00:00)
root     pts/0        123.117.78.247   Tue Nov  1 14:13 - 14:14  (00:01)
reboot   system boot  3.10.0-1160.15.2 Tue Nov  1 22:12 - 10:04 (14+11:51)
root     pts/0        114.249.233.212  Tue Feb 23 10:02 - crash (616+12:09)
root     pts/1        114.249.233.212  Tue Feb 23 09:42 - 18:17  (08:35)
root     pts/0        43.224.44.74     Tue Feb 23 09:41 - 09:42  (00:00)
```

```
[root@node3 ~]# grep 154.91.227.231  /var/log/secure

Nov 16 08:41:24 node3 sshd[143795]: Accepted password for root from 154.91.227.231 port 55592 ssh2
```

## 快捷命令

在 `~/.bash_profile` 或者 `~/.bashrc` 中增加以下命令

```
# some more ls aliases
alias ll='ls -alF'
alias e='exit'
alias c='clear'
```

```
Ctrl+k， 用于删除从光标处开始到结尾处的所有字符
Ctrl+u， 用于删除从光标开始到行首的所有字符。一般在密码或命令输入错误时常用
Ctrl+w， 剪切光标所在处之前的一个词 (以空格、标点等为分隔符)
ctrl + 方向键左键， 光标移动到前一个单词开头
ctrl + 方向键右键， 光标移动到后一个单词结尾
```

## tcpdump

```
tcpdump -i any port 8082 -w output.pcap
```

## openssh

### Extracting the certificate and keys from a .pfx file

The .pfx file, which is in a PKCS#12 format, contains the SSL certificate (public keys) and the corresponding private keys. Sometimes, you might have to import the certificate and private keys separately in an unencrypted plain text format to use it on another system. This topic provides instructions on how to convert the .pfx file to .crt and .key files.

#### Extract .crt and .key files from .pfx file

Run the following command to extract the private key:

```
openssl pkcs12 -in [yourfile.pfx] -nocerts -out [drlive.key]
```

You will be prompted to type the import password. Type the password that you used to protect your keypair when you created the .pfx file.

You will be prompted again to provide a new password to protect the .key file that you are creating. Store the password to your key file in a secure place to avoid misuse.

Run the following command to extract the certificate:

```
openssl pkcs12 -in [yourfile.pfx] -clcerts -nokeys -out [drlive.crt]
```

Run the following command to decrypt the private key:

```
openssl rsa -in [drlive.key] -out [drlive-decrypted.key]
```

Type the password that you created to protect the private key file in the previous step.

The .crt file and the decrypted and encrypted .key files are available in the path, where you started OpenSSL.

#### Convert .pfx file to .pem format

There might be instances where you might have to convert the .pfx file into .pem format. Run the following command to convert it into PEM format.

```
openssl rsa -in [keyfile-encrypted.key] -outform PEM -out [keyfile-encrypted-pem.key]
```

## cat << EOF > file

```
cat << EOF > tmp-file
deb http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
EOF
```

## 查看文件目录大小

```
du /var/www -h --max-depth=1 | sort -rn
du -sh directory

# The `-s` is size, the `-h` is human readable.
ls -sh filename

find /var/lib/docker/overlay2/ -type f -size +100M -print0 | xargs -0 du -h | sort -nr
```

```
df -hl

Filesystem Size Used Avail Capacity Mounted on
/dev/sda8  103G 9.5G 89G   10%      /home
```

HD硬盘接口的第一个硬盘（a），第二个分区（8），容量是103G，用了9.5G，可用是89，因此利用率是10%， 被挂载到（/home）

## I/O

标准输入(`stdin`)： 默认为键盘输入

标准输出(`stdout`)： 默认为屏幕输出，表示为 `1`

标准错误输出(`stderr`)： 默认也是输出到屏幕，表示为 `2`


将输出重定向到 ls_result 文件中
```
ls > ls_result
```

追加到 ls_result 文件中
```
ls -l >> ls_result
```

只有标准输出被存入 all_result 文件中
```
find /home -name lost* > all_result
```

表示将标准错误输出重定向
```
find /home -name lost* 2> err_result
```

不输出错信息
```
find /home -name lost* 2> /dev/null
```

标准错误输出和标准输入一样都被存入到文件中
```
find /home -name lost_ > all_result 2>& 1
or
find /home -name lost_ >& all_result
```
> 1. `>` 就是输出（标准输出和标准错误输出）重定向的代表符号;
> 2. 连续两个 `>` 符号，即 `>>` 则表示不清除原来的而追加输出;

## chmod

### 文字设定法

```
chmod \[--help] \[--version] mode file
chmod u+x test.sh
```

Args

- `-c` : 若该档案权限确实已经更改，才显示其更改动作
- `-f` : 若该档案权限无法被更改也不要显示错误讯息
- `-v` : 显示权限变更的详细资料
- `-R` : 对目前目录下的所有档案与子目录进行相同的权限变更(即以递回的方式逐个变更)
- `–help` : 显示辅助说明
- `–version` : 显示版本

权限范围

- `u` ：目录或者文件的当前的用户
- `g` ：目录或者文件的当前的群组
- `o` ：除了目录或者文件的当前用户或群组之外的用户或者群组
- `a` ：所有的用户及群组

权限操作

- `+` 表示增加权限
- `-` 表示取消权限
- `=` 表示唯一设定权限

权限代号：

- `r` ：读权限，用数字4表示
- `w` ：写权限，用数字2表示
- `x` ：执行权限，用数字1表示

### 数字设定法

所有者有读和写的权限，组用户只有读的权限
```
sudo chmod 644 ×××
```

只有所有者有读和写以及执行的权限
```
sudo chmod 700 ×××
```

每个人都有读和写的权限
```
sudo chmod 666 ×××
```

每个人都有读和写以及执行的权限
```
sudo chmod 777 ×××
```

其中：

- `×××` 指文件名（也可以是文件夹名，不过要在 `chmod` 后加 `-ld`）。
- 数字文字对应关系: r=4，w=2，x=1
- 若要 `rwx` 属性则 4+2+1=7
- 若要 `rw-` 属性则 4+2=6；
- 若要 `r-x` 属性则 4+1=7。
- 0 \[000] 无任何权限
- 4 \[100] 只读权限
- 6 \[110] 读写权限
- 7 \[111] 读写执行权限

## 查看端口占用

```
apt install net-tools

netstat -tlnp | grep 8000

lsof -i:8000

# for MAC
lsof -iTCP -sTCP:LISTEN -n -P
```

```
netstat
\-a (all)显示所有选项，默认不显示LISTEN相关
\-t (tcp)仅显示tcp相关选项
\-u (udp)仅显示udp相关选项
\-n 拒绝显示别名，能显示数字的全部转化成数字。
\-l 仅列出有在 Listen (监听) 的服務状态
\-p 显示建立相关链接的程序名
\-r 显示路由信息，路由表
\-e 显示扩展信息，例如uid等
\-s 按各个协议进行统计
\-c 每隔一个固定时间，执行该netstat命令。
```

## crontab

```
# 1. Entry: Minute when the process will be started [0-60]
# 2. Entry: Hour when the process will be started [0-23]
# 3. Entry: Day of the month when the process will be started [1-28/29/30/31]
# 4. Entry: Month of the year when the process will be started [1-12]
# 5. Entry: Weekday when the process will be started [0-6] [0 is Sunday]
#
# all x min = */x

*  *  *  *  *  command to be executed
┬  ┬  ┬  ┬  ┬
│  │  │  │  │
│  │  │  │  │
│  │  │  │  └───── day of week (0 - 6) (0 is Sunday, or use names)
│  │  │  └────────── month (1 - 12)
│  │  └─────────────── day of month (1 - 31)
│  └──────────────────── hour (0 - 23)
└───────────────────────── min (0 - 59)
```

To open crontab

```
crontab -e
```

To list crontab content

```
crontab -l
```

To remove all your cron jobs

```
crontab -r
```

Run mycommand at 5:09am on January 1st plus every Monday in January

```
09 05 1 1 1  mycommand
```

Run mycommand at 05 and 35 past the hours of 2:00am and 8:00am on the 1st through the 28th of every January and July.

```
05,35 02,08 1-28 1,7 *  mycommand
```

Run mycommand every 5 minutes

```
*/5 * * * *  mycommand
```

## 查看文档

### head

show the first **n** lines of the file, **n=10** default
```
head -n ~/solar.html
```

### tail

show the last **n** lines of the file, **n=10** default
```
tail -n ~/solar.html
```

show the changes of the file ontime
```
tail -f ~/solar.html
```

filter out lines includes `HEAD`
```
tail -f /opt/seafile/logs/*.log /var/log/nginx/*.log | grep -v HEAD
```

## grep

```
grep -r search-string .
```

## find

find \<指定目录> \<指定条件> \<指定动作>

* \<指定目录>： 所要搜索的目录及其所有子目录。默认为当前目录。
* \<指定条件>： 所要搜索的文件的特征。
* \<指定动作>： 对搜索结果进行特定的处理。

recursively delete all files of a specific extension in the current dir

```
find . -type f -name "*.bak"
```

```
seafile-data# find . -type f | wc -l
1721980
seafile-data# find . -size +10M -type f | wc -l
2169
seafile-data# find . -size +1M -type f | wc -l
33583
```

## tree

```
tree -P '*.py|*.html' -L 2
```

## sed 字符串替换

```
sed -i 's/old-string/new-string/g' /path/to/file.txt
```

## iptables

For CentOS

```
sudo iptables -I INPUT 1 -p tcp --dport 8082 -j ACCEPT
sudo iptables -I INPUT 1 -p tcp --dport 8000 -j ACCEPT
```

## tar

* `-c`：`-c` 或 `--create` 建立新的备份文件。
* `-x`：`-x` 或 `--extract` 或 `--get` 从备份文件中还原文件。将打包文件解压。
* `-z`：`-z` 或 `--gzip` 或 `--ungzip` 通过 `gzip` 指令处理备份文件。将打包文件压缩。 
* `-v`：`-v` 或`--verbose` 显示指令执行过程。
* `-f`：`-f <备份文件>` 或 `--file=<备份文件>` 指定备份文件。

### 压缩

打包目录下的workspace（不压缩）

```
tar -cvf workspace.tar workspace
```

打包并压缩目录下的worksapce

```
tar -czvf workspace.tar.gz.$(date +%Y-%m-%d) workspace
```

### 解压

```
tar -xzvf workspace.tar.gz
```

## trouble shoot

### Permissions 0644 for ‘/root/.ssh/id_rsa’ are too open.

```
chmod 0600 /root/.ssh/id_rsa
```

### LC_ALL is not set in ENV

```
export  LC_ALL=en_US.UTF-8
```
