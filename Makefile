all: run_server run_client

run_server:
	$ python manage.py runserver

run_client:
	cd frontend && npm start