First .env
-
* PS_NAME= db name
* PS_USER= username
* PS_PASSWORD= your password
* PS_HOST = localhost
* PS_PORT = port (integer)

Then you need add EXTENSION for PostgreSQL
-
> CREATE EXTENSION pg_trgm;

> CREATE EXTENSION fuzzystrmatch;

### In docker
> docker exec -it your CONTAINER name bash

> psql -U your username

> \c your db name for project

Then write this
-
> CREATE EXTENSION pg_trgm;

> CREATE EXTENSION fuzzystrmatch;

To create fake data
-
### User:
> ./manage.py populate_data count
### Category:
> ./manage.py category_data count
### Listing:
> ./manage.py listing_populate count
