FROM ubuntu:latest

RUN apt update && apt install  openssh-server sudo -y

RUN apt install net-tools sudo -y

RUN groupadd --gid 1000 ubuntu

RUN useradd -rm -d /home/ubuntu -s /bin/bash -g ubuntu -u 1000 ubuntu 

RUN echo 'ubuntu:jctf2022!' |chpasswd

RUN sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

RUN service ssh start

EXPOSE 2222

CMD ["/usr/sbin/sshd","-D"]

COPY flag.txt /root

RUN chmod 4755 /usr/bin/date

RUN chmod a-w /tmp

RUN chmod a-w /home/ubuntu

RUN chown -R root:root /home/ubuntu
