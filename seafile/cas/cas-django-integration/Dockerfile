FROM imwhatiam/ubuntu:base

# for warning of "falling back to frontend: Teletype"
ARG DEBIAN_FRONTEND=noninteractive

RUN apt install -y libapache2-mod-auth-cas

RUN mkdir /var/www/html/secured-by-cas

# apt install pip
COPY index.php /var/www/html/index.php
COPY secured-by-cas/index.php /var/www/html/secured-by-cas/index.php

COPY auth_cas.conf /etc/apache2/mods-available/auth_cas.conf
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

RUN cd; \
    django-admin startproject cas_django_integration
