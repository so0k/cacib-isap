
# Docker Tech Talk Demo Script

Ensure backup cluster in AWS is available

## Docker CLI

Using Docker For Mac / Docker For Windows

```
docker run -it --rm alpine /bin/sh
```

```
hostname
ps -a
ls -l
uptime
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

```
docker image ls
```

```
docker run -it --rm busybox 
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

```
docker run -d -p 80:80 --name webserver -v $PWD/static_site:/usr/share/nginx/html:ro nginx:alpine
```

```
docker stop webserver
docker rm webserver
```

```
docker run -it --name test ubuntu:latest /bin/bash
```

```
apt-get install rolldice
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

```
docker ps -a
```

```
docker commit -t so0k:rolldice test
```

Instead, use a Dockerfile... `static-site\Dockerfile`

```
docker build -t so0k/static-site:latest .
```

```
docker run --name static-site -e AUTHOR="Docker Singapore" -d -p 80:80 so0k/static-site
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

## Docker Compose

Run a simple Flask app with a Redis cache.

```
cd counter/
docker-compose up
```

Change the code
```
vim app.py
```
Notice application code reloaded.


Another simple Python app (Master-Slave)

```
cd ../locust/
docker-compose up -d
```

Start the swarm
```
curl -XPOST http://127.0.0.1:8089/swarm -d"locust_count=20&hatch_rate=10"
```

Watch the status
```
watch -n 1 "curl -s http://127.0.0.1:8089/stats/requests | jq -r '[.user_count, .total_rps, .state] | @tsv'
```

Stop the swarm
```
curl http://127.0.0.1:8089/stop
```

Clean up
```
cd ../counter
docker-compose down --volume
```

```
cd ../locust
docker-compose down --volume
```

## Using Docker-Machine:

- Manage remote hosts
- Provision multiple hosts locally
- .. 

```
docker-machine create --driver xhyve manager
```

```
docker-machine ls
```

```
docker-machine ssh manager
uname -a
```

```
docker-machine env manager
eval $(docker-machine env manager)
```

```
docker run -d --name static-site -e AUTHOR="Docker Singapore!" -d -p 80:80 so0k/static-site
```

```
docker-machine ip manager
```

open website

```
docker system info
```

## Docker Swarm

```
docker-machine create --driver xhyve worker
```

```
docker swarm init
```

```
eval $(docker-machine env worker)
```

```
docker swarm join \
     --token SWMTKN-?? \
     192.168.64.24:2377
```

Unset docker environment:

```
eval $(docker-machine env -u)
```

[What's New in 1.13](https://gist.github.com/so0k/872b798db710e0cb6b4bfc12550a63e0)
