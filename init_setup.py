#!/bin/bash
git init
git add .
git commit -a -m 'first commit'
python manage.py startapp frontend
mv apache/django.py apache/django.wsgi
touch logs/access.log
touch logs/access.log
cp /usr/local/Cellar/python/2.7.1/lib/python2.7/site-packages/django/conf/project_template/reset.sh .
cp /usr/local/Cellar/python/2.7.1/lib/python2.7/site-packages/django/conf/project_template/.gitignore .
touch initial_data.json
echo [] > initial_data.json
./manage.py syncdb --noinput
./manage.py schemamigration frontend --initial
./manage.py migrate
./reset.sh
rm init_setup.py
git add .
git commit -a -m 'after init'