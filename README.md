# Network Speed Tester

Automated docker-compose setup for running regular timed network speed tests in a 10-minute interval.

## Usage

The database and python script are wrapped in docker containers, managed via docker-compose.

### Start

``` shell
docker-compose up -d 
```

### Stop

``` shell
docker-compose down
```

### Reset the database

``` shell
docker-compose down -v 
```