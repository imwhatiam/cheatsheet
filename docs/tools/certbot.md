# Certbot

## install

Nginx on Ubuntu 20.04

```
sudo apt update
sudo apt install snapd
sudo snap install core
sudo snap refresh core
sudo apt-get remove certbot
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```

- <https://snapcraft.io/docs/installing-snap-on-ubuntu>
- <https://certbot.eff.org/lets-encrypt/ubuntufocal-nginx>
