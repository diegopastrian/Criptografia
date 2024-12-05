# Dockerfile para Ubuntu 20.10
FROM ubuntu:20.10

# Cambia los repositorios a versiones antiguas
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/g' /etc/apt/sources.list \
    && sed -i 's/http:\/\/security.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/g' /etc/apt/sources.list

# Actualiza e instala las herramientas necesarias, SSH, Wireshark y tshark
RUN apt-get update && apt-get install -y sudo net-tools openssh-server openssh-client wireshark tshark

# Crea y configura el usuario 'test'
RUN useradd -m -s /bin/bash test
RUN echo 'test:test' | chpasswd

# Configura SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expone el puerto SSH
EXPOSE 22

# Comando para iniciar SSHD
CMD ["/usr/sbin/sshd", "-D"]
