apt-get update -y
apt-get -y install libgtk2.0-dev
apt-get -y install libjpeg-dev zlib1g-dev
gunicorn --bind=0.0.0.0 --timeout 600 --chdir Front-end app:app