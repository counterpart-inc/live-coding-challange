# Earthquake API

 This is a base for the live coding challange to the Find Nearest Earthquake

## Stack used
* Python 3.11
* Django 5
* Django Rest Framework
* Postgres
* Docker
* Docker Compose
* [Haversine](https://pypi.org/project/haversine/) package to calculate the distance between two points using [Haversine Formula](https://en.wikipedia.org/wiki/Haversine_formula)

## How to run the project with Docker (recommended)

```
1. Clone the project
 $ git clone <repo_url>
 
2. Enter on the project folder
 $ cd earthquake-api
 
3. Create your .env file
 $ cp contrib/.env-sample .env
 
4. Build the project
 $ make build
 
5. Run the project
 $ make up
 
6. Run the migrations
 $ make migrate
 
7. Check the Makefile for more options
 $ make help
```
