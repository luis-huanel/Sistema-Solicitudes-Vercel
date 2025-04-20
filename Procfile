web: gunicorn ProyectoWeb.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn ProyectoWeb.wsgi
