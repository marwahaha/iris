# iris
Iris is a Google Play Store metadata scraper mean to run in a container

# Setup
Install Docker (https://docs.docker.com/engine/installation/)
Install docker-compose (https://docs.docker.com/compose/install/)


# Run

Cloning this repo gets you the source code and the docker setup files necessary to build/run it.

```
cd compose
docker-compose up
```

## History
Iris is almost entirely forked from an abondoned project Manoj Saha (https://github.com/manojps/google-play-apps-crawler-scrapy) -- so credit goes to him for most of this.  My intentions are do dockerize both it and the postgresql storage into one easy to run application.
