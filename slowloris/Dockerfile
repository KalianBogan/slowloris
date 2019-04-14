FROM ubuntu

RUN apt-get update \
    && apt-get install -y python3-pip \
    && apt-get install -y git \
    && git clone https://github.com/gkbrk/slowloris.git /usr/games/slowloris \
    && mkdir -p /usr/games/attack/

COPY /volumes/run.py /usr/games/attack/

ENTRYPOINT ["python3", "/usr/games/attack/run.py", "10", "-s 10000", "-ua"]