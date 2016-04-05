#!/usr/bin/env bash

cd ${PH_HOME_DIR}

echo "Work dir: " ${PWD}

echo -n `bin/python --version`

PYTHON=${PWD}/bin/python

cd ${PH_HOME_DIR}/maintain/conf_utils

echo "Installing project packages:"
echo `${PYTHON} setup.py install`

cd ${PH_HOME_DIR}/polls_server
echo "Installing server: "
echo `${PYTHON} setup.py install`

cd ${PH_HOME_DIR}/polls_client
echo "Installing client: "
echo `${PYTHON} setup.py install`