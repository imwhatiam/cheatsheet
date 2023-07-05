```
docker run -t -d -p 0.0.0.0:9980:9980 -e "aliasgroup1=http://192.168.0.44:8000" -e "extra_params=--o:ssl.enable=false" --name code -e "username=lian" -e "password=lian" --restart always collabora/code
```
