# Ubuntu系统Daphne + Nginx + supervisor部署Django项目 

从Django 3.0开始支持ASGI应用程序运行，使Django完全具有异步功能。

Django打算在可预见的未来支持这两者。但是，异步功能将仅对在 ASGI 下运行的应用程序可用。

所以说，我们也需要适时的更新我们的技能，学会部署asgi异步服务器环境中部署django项目！

## ubuntu安装Nginx

```bash
sudo apt-get install nginx
```

> *检查nginx是否安装成功：*`nginx -v` *查看nginx的版本，如果正确显示格式如这样* `nginx version: nginx/1.18.0 (Ubuntu)`*，那么证明安装成功！*

**nginx常用命令：**

1. 启动nginx: `service nginx start`
2. 停止nginx：`service nginx stop`
3. 重启nginx：`service nginx restart`
4. 重载配置文件：`service nginx reload`
5. 查看nginx状态：`service nginx status`

## 克隆已经开发好的django项目

把我们已经开发好的django-blog博客项目从线上仓库可克隆到Nginx的项目文件，建立虚拟环境，安装项目依赖，创建数据库，同步数据，开发环境调试项目可正常运转后开始部署！

# 部署

## 一、虚拟环境中安装Daphne

> Daphne是一个纯Python编写的应用于UNIX环境的由Django项目维护的ASGI服务器。它扮演着ASGI参考服务器的角色。

你可以通过 pip 来安装 Daphne，该命令需要在激活虚拟环境的情况下运行

```python3
python -m pip install daphne
```

### 在 Daphne 中运行 Django

一旦 Daphne 安装完毕，你就可以使用 daphne 命令了，它将用来启动 Daphne 服务进程。在最简单的情形下，Daphne 加上包含一个 ASGI 应用模块的位置和应用的名称（以冒号分隔）。

对于一个典型的 Django 项目，可以像下面这样来启动 Daphne

```bash
daphne myproject.asgi:application
```

它将开启一个进程，监听 `127.0.0.1:8000`。这需要你的项目位于 Python path 上。为了确保这点，你应该在与 `manage.py` 文件相同的路径中运行这个命令。

## 二、虚拟环境中安装supervisor

Supervisor是用Python开发的一套通用的进程管理程序，能将一个普通的命令行进程变为后台daemon，并监控进程状态，异常退出时能自动重启。它是通过fork/exec的方式把这些被管理的进程当作supervisor的子进程来启动，这样只要在supervisor的配置文件中，把要管理的进程的可执行文件的路径写进去即可。也实现当子进程挂掉的时候，父进程可以准确获取子进程挂掉的信息的，可以选择是否自己启动和报警。supervisor还提供了一个功能，可以为supervisord或者每个子进程，设置一个非root的user，这个user就可以管理它对应的进程。

#### 1. 安装supervisor 的方式

安装supervisor的方式非常多，最简便的就是以下两种，直接安装在整个系统当中或者安装在python项目的虚拟环境当中！

```bash
# 直接安装在系统当中，整个环境中都有
sudo apt-get install supervisor

# 可以在虚拟环境中通过pip安装
pip3 install supervisor
```

#### 2. 生成配置文件

```ini
echo_supervisord_conf > /etc/supervisord.conf
```

**备注：**在任意文件夹下运行该命令，如果后边未指定存放配置文件的路径，而是单纯的指定了supervisord.conf的配置文件名，那么他会在当前文件夹下生成默认配置！

**修改配置文件supervisord.conf，在最后一行增加**

```ini
[include]
files = supervisord.d/*.ini
```

备注：files的路径可自行指定，不是必须非要存放在这里！

#### 3. 创建配置文件

在files指定的目录下创建一个`asgi.ini`的文件,用来设置项目的配置信息

```ini
[fcgi-program:asgi]
# TCP socket used by Nginx backend upstream
socket=tcp://0.0.0.0:8000

# 项目文件所在目录
directory=/home/qbc/webproject/django-blog

# 每个进程需要有一个单独的socket文件，所以我们使用process_num
# 确保更新“mysite.asgi”以匹配您的项目名称
command=daphne -u /run/daphne/daphne%(process_num)d.sock --fd 0 --access-log - --proxy-headers mysite.asgi:application

# 要启动的进程数，大致为您拥有的 CPU 数
numprocs=4

# 给每个进程一个唯一的名称，以便它们可以被区分
process_name=asgi%(process_num)d

# 自动启动和恢复进程
autostart=true
autorestart=true

# 选择您希望日志存放的位置
stdout_logfile=/home/qbc/webproject/django-blog/deploy/asgi.log
redirect_stderr=true
```

#### 4. 启动supervisor

```bash
supervisord -c /etc/supervisord.conf
```

**备注：**-c后边的路径为存放第二步生成的配置文件目录

**错误甄别及处理：**

错误1：

```bash
Error: Another program is already listening on a port that one of our HTTP servers is configured to use.  Shut this program down first before starting supervisord.
For help, use /usr/bin/supervisord -h
```

如果启动项目发生如上错误提示，说明supervisor进程已经启动了，端口被占用，我们可以运行以下命令，查看与supervisord有关的所有进程

```bash
ps -ef | grep supervisord
```

输出如下：

```bash
root        3652       1  0 08:26 ?        00:00:00 /usr/bin/python3 /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
root        6365       1  0 08:42 ?        00:00:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisord.conf
root        7201    4201  0 08:48 pts/1    00:00:00 grep --color=auto supervisord
```

杀死supervisord的进程即可

```bash
kill -s SIGTERM 3652
```

杀死之后重新启动supervisord，运行启动命令，不出意外就可以成功了！

通过supervisorctl命令查看进程状态

```bash
asgi:asgi0                       RUNNING   pid 61400, uptime 0:26:15
asgi:asgi1                       RUNNING   pid 61401, uptime 0:26:15
asgi:asgi2                       RUNNING   pid 61402, uptime 0:26:15
asgi:asgi3                       RUNNING   pid 61403, uptime 0:26:15
```

如果状态均为RUNNING说明成功，否则可去看看我们配置得日志文件提示的错误原因！

## 三、创建项目的Nginx配置文件

进入：`cd /etc/nginx/sites-enabled`
创建：`touch asgi`
用vim编辑打开刚才创建的`asgi`文件,将下边的内容填写进去，具体参考注释说明：

**有负载均衡的配置：**

```ini
upstream asgi {
    server 127.0.0.1:8001;  # 转发到服务器
}
server {
    listen 80;
    server_name 192.168.174.128;
    charset     utf-8;
    # max upload size  
    client_max_body_size 75M;    # adjust to taste
    
    # location 配置请求静态文件多媒体文件。
    location /media  {
        alias  /www/wwwroot/django-blog/media/;  
    }
    # 静态文件访问的url
    location /static {
        # 指定静态文件存放的目录
        alias /www/wwwroot/django-blog/static/;
    }
    
    location / {
        try_files $uri @proxy_to_app;
    }
    location @proxy_to_app {
        proxy_pass http://0.0.0.0:8000;

        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";

        proxy_redirect off;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Host $server_name;
    }
}
```

无负载均衡的配置

```ini
server {
  listen 80;
  server_name example.com #i just want to hide domain name..
  charset utf-8;
  client_max_body_size 20M;

  # location 配置请求静态文件多媒体文件。
    location /media  {
        alias  /www/wwwroot/django-blog/media/;  
    }
  # 静态文件访问的url
  location /static {
        # 指定静态文件存放的目录
        alias /www/wwwroot/django-blog/static/;
  }

  location / {
    proxy_pass http://0.0.0.0:8000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";

    proxy_redirect off;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Host $server_name;
  }
}
```

重载nginx配置文件：service nginx reload，重载如果不报错，说明我们已经启动成功！



