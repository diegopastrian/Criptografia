# Dockerfile para Ubuntu 14.10
FROM ubuntu:14.10

# Cambia los repositorios a versiones antiguas
RUN sed -i 's/http:\/\/archive.ubuntu.com\/ubuntu/http:\/\/old-releases.ubuntu.com\/ubuntu/g' /etc/apt/sources.list

# Instala las herramientas necesarias y SSH
RUN apt-get update && apt-get install -y sudo net-tools openssh-server openssh-client

# Crea y configura el usuario
RUN useradd -m -s /bin/bash ubuntu
RUN echo 'ubuntu:password' | chpasswd

# Configura SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Expone el puerto SSH
EXPOSE 22

# Comando para iniciar SSHD
CMD ["/usr/sbin/sshd", "-D"]
