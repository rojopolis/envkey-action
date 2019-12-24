FROM alpine:latest

COPY . /tmp/envkey-action

RUN apk add --no-cache\
        ca-certificates\
        python3;\
        pip3 install /tmp/envkey-action;\
        rm -rf /tmp/envkey-action

ENTRYPOINT ["envkey-action"]