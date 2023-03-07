FROM mitmproxy/mitmproxy:9.0.1

ADD ./ /mitm-redis

RUN pip install -r /mitm-redis/requirements.txt

WORKDIR /mitm-redis/app

ENTRYPOINT ["mitmdump", "-s", "main.py"]

EXPOSE 8080 8081