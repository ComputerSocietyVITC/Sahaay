#!/usr/bin/env bash
while [ ! -f /var/tmp/hypercorn.sock ]
do
     sleep 1
done

python3 manage.py migrate 

cd Core
hypercorn -b 'unix:/var/tmp/hypercorn.sock' -w 4 Core.asgi:fastapi 

chmod 777 /var/tmp/hypercorn.sock && service nginx start

exit
