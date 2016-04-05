# Install

* Config global env
```
export PH_HOME_DIR=/path/to/project/polls_hub
export PH_ENV_ID=dev
```
* Config venv & install apps
```
./init_venv.sh && ./install_apps.sh
```
* Post install configuration
```
bin/python configure.py
```
* Create db
```
bin/manage.py migrate
```
* Create admin user
```
bin/manage.py createsuperuser --username admin --email admin@admin.com --noinput
```

* Build static
```
bin/python polls_server/manage.py collectstatic --noinput
```

* Start supervisord
```
./bin/sv.sh start
```

* Verify status
```
./bin/supervisorctl status
```
Should return:
```
polls_client                     RUNNING   pid 2845, uptime 0:00:34
polls_server                     RUNNING   pid 2844, uptime 0:00:34
```