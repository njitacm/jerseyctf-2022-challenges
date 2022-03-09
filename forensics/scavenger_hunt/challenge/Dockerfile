FROM ubuntu:20.04 AS build

RUN apt-get update -y && apt-get install -y gcc
COPY package/ /tmp/build
WORKDIR /tmp/build

RUN mkdir -p notaflag_1.0-1/usr/local/bin
RUN gcc src.c -o notaflag_1.0-1/usr/local/bin/jersey
RUN chmod 555 notaflag_1.0-1/usr/local/bin/jersey

RUN gzip notaflag_1.0-1/usr/share/man/man1/notaflag.1

RUN dpkg-deb --build notaflag_1.0-1

FROM ubuntu:20.04

RUN apt update && apt install -y openssh-server
RUN yes | unminimize
RUN mkdir /var/run/sshd
RUN echo 'root:$(< /dev/urandom tr -cd "[:print:]" | head -c 32; echo)' | chpasswd

RUN sed -i 's/#LogLevel INFO/LogLevel VERBOSE/' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication no/' /etc/ssh/sshd_config
RUN sed -i 's/X11Forwarding yes/X11Forwarding no/' /etc/ssh/sshd_config
RUN echo "AllowUsers jersey" >> /etc/sshd_config
RUN sed -i 's/session\s*required\s*pam_loginuid.so/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN sed -i 's/session\s*optional\s*pam_motd.so/#/g' /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN useradd --create-home --shell /bin/bash jersey
RUN echo 'jersey:securepassword' | chpasswd
RUN passwd jersey --mindays 9999

RUN touch /home/jersey/.hushlogin
RUN chown -R jersey:jersey /home/jersey
RUN chmod -w -R /home/jersey

WORKDIR /tmp
COPY --from=build /tmp/build/notaflag_1.0-1.deb .
RUN apt install -y man less ./notaflag_1.0-1.deb
RUN rm ./notaflag_1.0-1.deb

COPY files /home/jersey/jersey
RUN echo "cd /home/jersey/jersey" >> /home/jersey/.bashrc

RUN chmod -x /usr/bin/ssh*

RUN useradd --system hey_that_package_is_sus

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]