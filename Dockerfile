FROM alpine:3.12.1

COPY . /tmp/envkey-action

RUN apk add --no-cache\
        ca-certificates\
        python3\
        py3-pip
RUN pip3 install /tmp/envkey-action;\
    rm -rf /tmp/envkey-action

ENTRYPOINT ["envkey-action"]
