export flaskroot=$(readlink -e ../testunk/)
# python run.py
FLASK_APP=run.py flask run -p 80
