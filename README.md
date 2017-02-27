
# Docker Tech Talk Demo Script

This Repository contains the code I used for the live demonstration during the
tech talk at Credit Agricole - Feb 27, 2016.

The code samples come from exising Docker labs material (see references below).

The [slides are available](https://docs.google.com/presentation/d/1eoj4GNbK256tBYwhZ6U4pW8nfl31FmYc6KJuPZRH4ns/edit?usp=sharing) as well

## Docker CLI

Using Docker For Mac / Docker For Windows

```
docker pull alpine
```

```
docker image ls
```

Do this multipe times
```
docker run -it alpine /bin/sh
```

```
hostname
ps -a
ls -l
uptime
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

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

Clean up containers
```
docker container prune
```

```
docker run -it --name test ubuntu:latest /bin/bash
```

```
apt-get install rolldice
```

<kbd>CTRL</kbd>+<kbd>D</kbd>

```
docker container ls -a
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
Notice application code reloaded...


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

```bash
docker-machine create --driver xhyve manager
```
Note: If network is a concern, do this in advance as well as

```bash
(cd vote;docker-compose pull)
```

```bash
docker-machine ls
```

```bash
docker-machine ssh manager
uname -a
```

```bash
docker-machine env manager
eval $(docker-machine env manager)
```

```
docker run -d --name static-site -e AUTHOR="Docker Singapore!" -d -p 80:80 so0k/static-site
```

```
docker-machine ip manager
```

open website on manager IP..

Notice also:

```
docker system info
```

## Docker Swarm

Create a Swarm of Nodes

Create another node for the swarm

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


## Deploy Stack across swarm

Talk to manager
```
eval $(docker-machine env manager)
```

```bash
docker stack -h
```

```bash
cd vote/
docker-compose config | less
docker stack deploy -c docker-compose.yaml vote
```

```bash
docker service ls
```

Ports:

- 8080 for node viz
- 5000 for voting app
- 5001 for result app

## Clean up

```
docker stack rm vote
```

```bash
docker-machine rm manager worker
```

Unset docker environment:

```
eval $(docker-machine env -u)
```

## References

- [Static site](https://github.com/docker/labs/tree/master/beginner/static-site)
- [Compose](https://docs.docker.com/compose/gettingstarted/)
- [Locust](https://github.com/honestbee/distributed-load-testing)
- [xhyve driver](https://github.com/zchee/docker-machine-driver-xhyve)
- [aws driver](https://docs.docker.com/machine/drivers/aws/)
- [Voting App](https://docs.docker.com/engine/getstarted-voting-app/)
- [What's New in 1.13](https://gist.github.com/so0k/872b798db710e0cb6b4bfc12550a63e0)

