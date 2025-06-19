FROM nginx:1.23-alpine
# Удаляем дефолтный конфиг
RUN rm /etc/nginx/conf.d/default.conf
# Подкидываем наш
COPY ./nginx.conf /etc/nginx/conf.d/
COPY ./fullchain.pem /etc/nginx/
COPY privkey.pem /etc/nginx/privkey.pem
RUN chmod 600 /etc/nginx/privkey.pem