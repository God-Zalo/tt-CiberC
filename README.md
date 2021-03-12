# tt-CiberC
Technical Test CiberC


# Requirements
- docker
- docker-compose
- django 2.2.19
- mysql8

# Steps to reproduce

## Setup environment
- move venv one folder up `mv venv37/ ../`
- `source venv37/bin/activate` (manual installation may be needed)
- Install `mysqlclient` `pip install mysqlclient`

## Deploy db
- `cd databases`
- `sudo docker-compose up -d`
- `mysql -h 127.0.0.1 -P 3306 -u root -pciberc ciberc < database.sql`

## Migrate db
- create superuser may be needed
- `cd ciberc`
- `python manage.py makemigrations && pyton manage.py migrate`

## Deploy service
- `cd ciberc`
- `python manage.py runserver`

# Usage
- `http://127.0.0.1/` directs to Inventory page
- From admin site, models can be modified manually
- `http://127.0.0.1/fileupload` directs to FileUpload page
