cd /home/mrk/novalab-notify &&
source conf &&
source venv/bin/activate  &&
gunicorn config.wsgi
