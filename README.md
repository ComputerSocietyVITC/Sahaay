# Sahaay
**Sahaay** is a Q&A application with grievances/questions being posted as tokens. An open source application developed by the students at IEEE ComSoc VIT Chennai student chapter.

## Development
- Developed using Test Driven Development approach. The testing is automated using TravisCI ([travis-ci](https://travis-ci.com/)) and Github Actions
- The backend is developed using FastAPI([fastapi](https://fastapi.tiangolo.com/))
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
`docker-compose run --rm app sh -c "pytest"`

To test a particular file (`test_user.py`), use 
`docker-compose run --rm app sh -c "pytest tests\test_user.py"`

To setup the live test server, run `docker-compose up -d` after building the docker image. The live image will then be hosted at `https://localhost:3000`. The api could be tested using the FastAPI testing interface provided at `https://localhost:3000/docs`.

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

### Writing Tests
All tests should be written before starting to create endpoint routes, to setup constraints to be satisfied by the function/endpoint beforehand.

All tests are stored in the [app/tests](https://github.com/ComputerSocietyVITC/Sahaay/tree/main/app/tests) folder with every separate test file (for every new testing family like user, tickets, etc.) named starting with `test_`. Similar naming convention is also followed for every test function, following standard pytest naming convention.

While writing tests for unsafe requests(`POST`, `PATCH`) use fixtures which are to be defined in the [app/tests/fixtures](https://github.com/ComputerSocietyVITC/Sahaay/tree/main/app/tests/fixtures) folder.
The fixtures are then imported in the [`conftest.py`](https://github.com/ComputerSocietyVITC/Sahaay/tree/main/app/tests/conftest.py) file. These fixtures are then used for test functions using the `@pytest.fixtures.usefixtures` decorator.

The tests themselves are of two types:
- **Dependency tests** : to test dependency functions like password hashing, backend processing, etc. These are standard python tests and require no special knowledge.
- **Endpoint tests**: These are written using the `FastAPI testclient` library, which in itself uses libraries like starlette, asyncio and pytest-mongodb for setting up a asynchronous endpoint testing environment. 
A sample endpoint test could be found [here](https://github.com/ComputerSocietyVITC/Sahaay/blob/User/app/tests/test_user.py).