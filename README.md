# iris
Iris is a Google Play Store metadata scraper mean to run in a container

# Setup
Install Docker (https://docs.docker.com/engine/installation/)

Install docker-compose (https://docs.docker.com/compose/install/)


# Run

Cloning this repo gets you the source code and the docker setup files necessary to build/run it. The compose file pulls from dockerhub (it does NOT build from the given Dockefile here, but that may be used instead if desired).


You will need to configure the crawler to point to the correct postgresql server (the IP your host running docker)

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

## History
Iris is almost entirely forked from an abondoned project Manoj Saha (https://github.com/manojps/google-play-apps-crawler-scrapy) -- so credit goes to him for most of this.  My intentions are do dockerize both it and the postgresql storage into one easy to run application.
