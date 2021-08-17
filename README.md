# Sahay
**Sahay** is a Q&A application with grievances/questions being posted as tokens. An open source application developed by the students at IEEE ComSoc VIT Chennai student chapter.

## Development
- Developed using Test Driven Development approach. The testing is automated using TravisCI ([travis-ci](https://travis-ci.com/))
- The backend is developed using django-rest-framework([drf](https://pypi.org/project/djangorestframework/)), with [flake8](https://pypi.org/project/flake8/) as the linter.
- The frontend uses flutter and dart.

## Docker Setup
- First install docker desktop from [docker-home](https://www.docker.com/get-started)
- Then set up git in your local folder using `git init`
- Add the git repository to remote 
				`git remote add origin <code-url>`
- Pull code from the remote origin `git pull origin main`
- Setup docker `docker-compose build`
- Run django command on docker image using the syntax 
`docker-compose run --rm app sh -c "<your piece of code>"`
ex:
`docker-compose run --rm app sh -c "python manage.py test"`

## Contributing
- If you want to use/install any library don't use pip install directly. Add the said library to `requirements.txt`.
	- Add the library in the format: 
	- `'library name'>='used version',<'version rounded to first decimal '` 
	- ex: `djangorestframework>=3.12.4,<3.13.0`
- We will have a main `djangoapp` which will contain all user models.
- For any functions/models, implement tests first in `.\tests\`.
- Use proper headers and prefixes for commits and Pull Requests
	- `[tests]` for testing changes
	- `[docker]` for docker changes
	- `[models]` for models and serializers related PRs
	- `[views]` for functions and permissions related PRs
	- `[urls]` for urls and routing related PRs
	- `[tickets]` for commits dealing with ticket class
	- `[user]` for commits dealing with user class
	- `[service]` for commits dealing with service class
	- `[role]` for commits dealing with role class