# TED
This security application uses facial recognition to detect and send an email alert to the user of unrecognized visitors.

## User Stories
* As a user, I to assign trusted visitors to be recognized by the camera.
* As a user, I want the system to take a picture and email me an image of an unrecognized visitor so I can review any potential threats.
* As a developer, I want to create a simple web application interface for a user to be able to easily add names and images of trusted visitors.
* As a developer, I want seemless automation of capturing an image of an unrecongized visitor through sending an email with the image as an attachment.
* As a developer, I want to delete any .png that are created as a result of camera training or frame capturing after processing the images in order to maintain memory space.
* As a student, I want to create a project that is unique to what we have done in the past. 
* As a student, I want to deploy with AWS and Docker in keeping with standard practices of the field.

**Stretch Goal**

* As a developer I want to utilize a Raspberry Pi to handle the camera, facial recognition, and email scripts.

## Getting Started

- Clone the repository and install the dependencies.
- In a .env file, include the following details:

```
# For email alerts:
FROM_ADDR= <gmail address from which to send alerts>
FROM_PASSWORD= <password for the above gmail address>
TO_ADDR= <gmail address to send alerts to>

# For Django app:
SECRET_KEY= <secret key received from Django>
ALLOWED_HOSTS= <host site (AWS EC2 instance or other)>

# For database access, fill in your information to the following fields:
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_SERVICE=
DB_PORT=
DB_HOST=
DATABASE_URL=

# If deploying to AWS, add these fields with your AWS instance information:
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_S3_CUSTOM_DOMAIN=
```

### Installing

In a virtual environment, run `pipenv install --dev` and `pipenv run pip freeze > requirements.txt` to install and apply the necessary dependencies.

## Running the tests

Tests for the Django app can be run within the Docker container using the command `./manage.py test`

## Deployment

Deployed on AWS with Docker, utilizing RDS and S3.

## Built With

* Python
* Django
* Docker
* PostgreSQL
* OpenCV
* Watchdog
* Psycopg2-binary
* Gunicorn
* NginX
* AWS
* RDS
* S3

## Authors

* **Tim Schoen** 
* **Dan Le** 
* **Evy Haan** 

## Versioning
_April 2019:_ Version 1.0.0

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
