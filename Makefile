all: build run_server 
	

run_server:
	npm run build
	$ python manage.py runserver --nostatic

run_client:
	cd frontend && npm start