sudo -s
apt-get update && apt-get -y upgrade && apt-get -y install dnsutils curl sudo git && curl -sSL https://get.docker.com/ | sh && git clone https://github.com/ahmednitul/netflix-proxy /opt/netflix-proxy && cd /opt/netflix-proxy && ./build.sh
