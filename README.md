# rodan-docker-zero

Build Rodan docker images from zero.


## Background

[Rodan](https://ddmal.music.mcgill.ca/Rodan/) is a web-based workflow engine developed by the Distributed Digital Music Archives Libraries (DDMAL) lab, McGill University.

A Rodan installation includes one Django server for backend APIs, several Celery workers and one frontend app server.


## Steps to follow

1. Install Docker CE (community edition) and docker-compose onto your system.

2. Put your Rodan repo into `./rodan/Rodan`. For example:

````
cd rodan; git clone git@github.com:studio-theyang/Rodan.git
````

3. Put your rodan-client repo into `./rodan-client/rodan-client`. For example:

````
cd rodan-client; git clone git@github.com:studio-theyang/rodan-client.git
````

4. Run `docker-compose build`.

5. Run `docker-compose up`.

6. Wait until things set up. If successful, the server is available at `http://localhost:8080` and the client at `http://localhost:8081`.

## Storage

- `./var/log`: logs
- `./var/postgres`: PostgreSQL database
- `./var/projects`: Rodan projects and resources

## Quick links

Create a super user for web login:

- While containers are running, run `docker-compose exec rodan-server /bin/bash`.
- Type `./manage.py createsuperuser` and follow the instructions.

## Troubleshoot

If you encounter "GitHub rate limit" error during the build of `rodan-client`, please follow these steps:

1. Check out the intermediate Docker image of last successful step. For example, `17e501b2b329` in following case.

````
Step 12/15 : RUN yarn install
 ---> Using cache
 ---> 17e501b2b329
````

2. Launch a disposable Docker container upon this image and enter into its console:

````
docker run --rm -it 17e501b2b329 /bin/bash
````

3. Run `/code/rodan-client/node_modules/.bin/jspm registry config github` and follow the instructions to enter your GitHub account, generate an API token and paste it back.

4. Run `/code/rodan-client/node_modules/.bin/jspm registry export github` and find the line like:

````
jspm config registries.github.auth YOUR_AUTH_TOKEN
````

5. Export this final token as a bash env:

````
export DEV_JSPM_GITHUB_AUTH_TOKEN=YOUR_AUTH_TOKEN docker-compose build
````

6. Finally, get back to where you were interrupted. You'll need to store this token somewhere safe, and be prepared to `export` again when you switch to another bash console.

````
docker-compose build
````

IMPORTANT: DON'T SHARE THIS TOKEN! IT CONTAINS YOUR ACCOUNT INFO!
