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

## sudo docker build -t image_name

## It is important to run the container read-only so others cannot leave scripts behind or leak flags
## sudo docker run -dp 2222:2222 --read-only image_name 