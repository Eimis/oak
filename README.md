# oak

How to start the backend API server:

* clone this repo
* run `docker-compose up`
* Congratulations, API server is now running!
* You can visit `http://localhost:8000/game/log` to see if the API server works

To run some *very basic* tests:

open container's shell:
`docker exec -it oak_web_1 bash`
run tests:
`oak/manage.py test oak`
