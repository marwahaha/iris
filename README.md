# iris
Iris is a Google Play Store metadata scraper meant to run in a docker container

# Setup
Install Docker (https://docs.docker.com/engine/installation/)

Install docker-compose (https://docs.docker.com/compose/install/)


# Run

Cloning this repo gets you the source code and the docker setup files necessary to build/run it. The compose file pulls from dockerhub (it does NOT build from the given Dockefile here, but that may be used instead if desired).


You will need to configure the crawler to point to the correct postgresql server (the IP your host running docker) within the docker-compose.yml

```
gplay-crawler:
   image: behren/gplaycrawler
   environment:
    - POSTGRES_HOST=<DOCKER_IP_HOST_HERE>
```

```
cd compose
docker-compose up
```

# Storage

PostgreSQL storage persists in a docker volume.  The PostgreSQL server can be found at <DOCKER_IP_HOST_HERE>:5432

## History
Iris is almost entirely forked from an abandoned project Manoj Saha (https://github.com/manojps/google-play-apps-crawler-scrapy) -- so credit goes to him for most of this.  My intentions are do dockerize both it and the postgresql storage into one easy to run application.

docker build . -t behren/gplaycrawler && docker push behren/gplaycrawler
docker-compose up --scale gplay-crawler=2
