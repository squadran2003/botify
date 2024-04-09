FROM nginx:1.25

USER root
RUN apt-get update

RUN apt-get install -y --no-install-recommends certbot python3-certbot-nginx
RUN certbot certonly --webroot -w /usr/src/app -d botifyapp.com
RUN cp -r /usr/src/app/live/botifyapp.com /etc/letsencrypt/live/
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
