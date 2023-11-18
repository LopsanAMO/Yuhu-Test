# Yuhu Test

yuhu Test. Check out the project's [documentation](http://3.131.60.191/api/doc/).

Postman Collection - [collection](https://api.postman.com/collections/1986978-f887f8c2-9d7c-4edc-ba22-c426d29988a6?access_key=PMAT-01HFGKVF25TBA6P485XB17Y64E)
# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

# Initialize the project

Copy the .env.sample file to a new file called .env.

```bash
cp .env.sample .env
```
The slack bot token prevously saved, you'll need to set on your new .env, the variable is called ```SLACK_API_KEY```

update the .env entries to real values:

```bash
DB_NAME=postgres
DB_USER=postgres
DB_PASS=postgres
SECRET_KEY=AUniqueSecretKey
ALLOWED_HOSTS=*
SLACK_API_KEY=xxx-xxxxxxx
```

Start the dev server for local development:

```bash
docker-compose up
```

Create a superuser to login to the system as nora:

```bash
docker-compose run --rm web ./app/manage.py createsuperuser
```

# Documentation (running locally) 

- API Documentation  ```http://localhost:8000/api/doc/``` or ``` http://3.131.60.191/api/doc/```
