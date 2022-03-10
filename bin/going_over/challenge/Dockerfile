FROM ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9 AS build

RUN apt-get update -y && \
    apt-get install -y gcc && \
    rm -rf /var/lib/apt/lists/*

COPY /files/src.c .
RUN gcc src.c -o going-over -fno-stack-protector -no-pie

FROM ubuntu@sha256:86ac87f73641c920fb42cc9612d4fb57b5626b56ea2a19b894d0673fd5b4f2e9

RUN useradd -m -d /home/jersey -u 12345 jersey
WORKDIR /home/jersey

RUN mkdir /home/jersey/bin && \
    cp /bin/sh /home/jersey/bin && \
    cp /bin/ls /home/jersey/bin && \
    cp /bin/cat /home/jersey/bin

COPY ynetd .
RUN chmod +x ynetd

COPY --from=build going-over going-over
COPY /files/flag.txt /home/jersey/

RUN chown -R root:root /home/jersey

USER jersey
EXPOSE 9999
CMD ./ynetd -p 9999 ./going-over