# logging

日志级别等级 CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

```
#!/usr/bin/env python
# coding:utf-8

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='test.log',
    filemode='w'
)

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
```

```
%(name)s Logger的名字
%(levelno)s 数字形式的日志级别
%(levelname)s 文本形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s 调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d 线程ID。可能没有
%(threadName)s 线程名。可能没有
%(process)d 进程ID。可能没有
%(message)s用户输出的消息
```

## Django logging

代码文件中，直接可以 get 到自定义的 onlyoffice logger，使用自定义的 onlyoffice logger 来处理。
```
logger = logging.getLogger('onlyoffice')
```

代码文件中(`seahub/api2/endpoints/upload_links.py`)，get logger 时，获取到的是 `__name__`（`seahub.api2.endpoints.upload_links`），按层级关系依次向上寻找 logger。
```
logger = logging.getLogger(__name__)
logger.error('in upload link')
```

如果自定义或者层级关系均未找到 logger，则使用 root（或 `''`）定义的 logger。

settins.py

```
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'upload_link_format': {
            'format': '%(lineno)s %(funcName)s %(message)s',

        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(lineno)s %(funcName)s %(message)s',

        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'upload_link_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'upload_link_format',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'seahub.log'),
            'maxBytes': 1024*1024*100,  # 100 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'onlyoffice_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'onlyoffice.log'),
            'maxBytes': 1024*1024*100,  # 100 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {  # 默认 logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'seahub.api2.endpoints': {  # 按层级关系依次向上寻找 logger
            'handlers': ['upload_link_handler', ],
            'level': 'DEBUG',
            'propagate': False
        },
        'onlyoffice': {  # 自定义的 onlyoffice logger
            'handlers': ['onlyoffice_handler', ],
            'level': 'INFO',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': ['console'],
            'level': "DEBUG",
            'propagate': False,
        },
    }
}
```
