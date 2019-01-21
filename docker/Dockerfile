# My Site
# Version: 1.0
# Modified by Valentin Faria Oliveira
# Following https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/modwsgi/
# and https://docs.djangoproject.com/en/2.1/howto/static-files/
FROM python:3.5

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean && DEBIAN_FRONTEND=noninterractive apt-get install -yq apache2 mysql-server libapache2-mod-wsgi-py3 && rm -rf /var/lib/apt/lists/*

# Project Files and Settings
ARG REQUIREMENTS=requirements.txt
ARG GITADRESS=https://github.com/tgraveleau/GreenStarter
ARG PROJECT=GreenStarter
ARG USER=djangoadmin
ARG PASSWORD=django
ARG BDDNAME=makeOurPlanetGreatAgain

# install django project and set apache2 conf
WORKDIR /var/www/html
RUN git clone $GITADRESS && pip3 install -r $PROJECT/$REQUIREMENTS && $PROJECT/manage.py collectstatic --noinput && mv $PROJECT/docker/apache2.conf /etc/apache2 && rm -fr $PROJECT/$REQUIREMENTS $PROJECT/docker

# mysql
RUN service mysql start \
&& mysql -u root --execute="CREATE DATABASE $BDDNAME" \
&& mysql -u root --execute="CREATE USER '$ADMIN'@'%' IDENTIFIED BY '$PASSWORD'" \
&& mysql -u root --execute="GRANT ALL PRIVILEGES ON $BDDNAME.* TO '$ADMIN'@'%' WITH GRANT OPTION" \
&& mysql -u root --execute="FLUSH PRIVILEGES" \
&& $PROJECT/manage.py makemigrations && $PROJECT/manage.py migrate && $PROJECT/manage.py loaddata $PROJECT/fixtures/initial_data.json

# Server
EXPOSE 80
STOPSIGNAL SIGINT
CMD /usr/sbin/apache2ctl start && /usr/sbin/mysqld

# docker build . --tag="django"
# docker run -d -p 8000:80 --mount source=django-vol,destination=/var/www/html/GreenStarter --mount source=mysql-vol,destination=/var/lib/mysql --name="conteneur_django" django
