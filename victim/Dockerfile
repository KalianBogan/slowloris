FROM nginx

RUN echo "* soft nofile 102400" >> /etc/security/limits.conf \
    echo "* hard nofile 102400" >> /etc/security/limits.conf

COPY ./volumes/nginx.conf /etc/nginx/nginx.conf
COPY ./volumes/conf.d/default.conf /etc/nginx/conf.d/default.conf