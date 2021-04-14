# Django

## USE_TZ and TIME_ZONE

### 当配置了 `USE_TZ = True`

数据库中记录 UTC 时间，Django 从数据库中取出时间后，会生成 `tzinfo` 为 `UTC` 的 `datetime` 对象。

### 当没有配置 `USE_TZ = True`

数据库中记录的是根据 `TIME_ZONE` 得到的本地时间，Django 从数据库中取出时间后，会生成 `tzinfo` 为 `None` 的 `datetime` 对象。

### 举例说明

比如，在 **北京时间 2021-04-10 14点左右** 创建的数据，在数据中存的时间为：

|数据库中存的时间|配置|说明|
|----------------|----|----|
|2021-04-10 13:53:40|`TIME_ZONE = 'Asia/Shanghai'`|存的是上海当地时间|
|2021-04-10 05:57:18|`USE_TZ = True` and `TIME_ZONE = 'Asia/Shanghai'`|忽略 `TIME_ZONE` 配置，存的是 UTC 时间| 
|2021-04-10 01:05:29|`TIME_ZONE = America/Chicago`|存的是芝加哥当地时间|

- <https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-USE_TZ>

### 问题及解决方案

#### TypeError: can’t compare offset-naive and offset-aware datetimes

对比两个 `datetime` 对象时，如果一个有 `tzinfo`、一个没有 `tzinfo` 则会报以上错误，解决方法：

将 `datetime` 对象统一 `make_naive`（`make_aware` 也可以）后，再对比。

```
from django.utils.timezone import make_naive, is_aware

# before make_naive
# 2021-04-09 05:32:30+00:00
# tzinfo: UTC

# after make_naive
# 2021-04-09 13:32:30
# tzinfo: None

if is_aware(last_login_time):
    last_login_time = make_naive(last_login_time)
```

- <https://docs.djangoproject.com/en/3.2/ref/utils/#django.utils.timezone.is_aware>
