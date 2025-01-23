# docker image
# install python
FROM python
#install dependency
RUN pip install Flask gunicorn
#copy all local files
WORKDIR /app
COPY . .
# RUN the webserver on a container startup, here use the gunicorm
# webserver, with one worker process and 8 threads
# for enviroment with mupltiple CPU cores, increase the number
# of threads to be equal to the core avaliable
CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 app:app