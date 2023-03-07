

## 使用
构建镜像&使用
```
docker build -t woltzz/mitm-redis:0.1 .

docker run -it -p 8080:8080 woltzz/mitm-redis mitmdump
```

配置代理指向程序所指向的主机ip和8888端口即可进行拦截。

## 配置说明
config/config.ini默认配置中含义为：将请求url包含有bing.com/search的返回数据都会发到redis stream队列中。
