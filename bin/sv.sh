#!/usr/bin/env bash

if [ ! -d "polls_server/static" ]; then
  python polls_server/manage.py collectstatic --noinput
fi

SUPERVISORD=${ENV_PH_HOME_DIR}bin/supervisord
SUPERVISORD_ARGS='-c etc/supervisord.conf'
SUPERVISORCTL=${ENV_PH_HOME_DIR}bin/supervisorctl

case $1 in
start)
    echo -n "Starting supervisord: "
    ${SUPERVISORD} ${SUPERVISORD_ARGS}
    echo `${ENV_PH_HOME_DIR}bin/supervisorctl pid`
    ;;
stop)
    echo -n "Stopping supervisord: "
    ${SUPERVISORCTL} shutdown
    echo
    ;;
restart)
    echo -n "Stopping supervisord: "
    ${SUPERVISORCTL} shutdown
    echo
    echo -n "Starting supervisord: "
    ${SUPERVISORD} ${SUPERVISORD_ARGS}
    echo
    ;;
esac