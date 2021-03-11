# tt-CiberC
Technical Test CiberC


# Requirements
- docker
- docker-compose
- django 2.2.19
- mysql8

# Steps to reproduce

## Deploy db
- `sudo docker-compose up -d`
- `mysql -h 127.0.0.1 -P 3306 -u ciberc -pciberc ciberc < database.sql`
