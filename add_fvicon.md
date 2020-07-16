1. create a folder called `img` in `/var/www/`

`sudo mkdir /var/www/img`
copy the icon from react build folder to the above folder

edit django config
`sudo nano /etc/nginx/sites-available/yourconfig`

edit and add the following

```
location = /youricon.extention {
    alias /var/www/mysite/img/youricon.extention; .....
}
```

the above line is already in the cofig you can edit it but dont delete whats already there in the curly braces
