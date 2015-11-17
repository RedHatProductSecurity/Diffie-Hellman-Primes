FROM alpine:3.2

RUN adduser -D generator && \
    apk add --update openssl && \
    rm -f /var/cache/apk/*

COPY generate.sh /home/generator/

USER generator
WORKDIR "/home/generator"
ENTRYPOINT ["/home/generator/generate.sh"]
