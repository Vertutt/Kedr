FROM nginx:1.23-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY ./nginx.conf /etc/nginx/conf.d/
COPY ./fullchain.pem /etc/nginx/
COPY privkey.pem /etc/nginx/privkey.pem
RUN chmod 600 /etc/nginx/privkey.pem