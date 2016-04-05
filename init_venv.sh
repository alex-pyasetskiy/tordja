#!/usr/bin/env bash

VERSION=15.0.1

INITIAL_ENV=.

PYTHON=python2.7

URL_BASE=https://pypi.python.org/packages/source/v/virtualenv

wget ${URL_BASE}/virtualenv-${VERSION}.tar.gz

tar xzf virtualenv-${VERSION}.tar.gz

${PYTHON} virtualenv-${VERSION}/virtualenv.py --distribute ${INITIAL_ENV}

rm -rf virtualenv-${VERSION}

${PH_HOME_DIR}/bin/pip install virtualenv-${VERSION}.tar.gz

${PH_HOME_DIR}/bin/pip install -r requirements.txt

rm -rf virtualenv-${VERSION}.tar.gz

${PH_HOME_DIR}/bin/virtualenv --relocatable .

# TODO: separate this ugly implementation

${PH_HOME_DIR}/bin/pip install git+https://github.com/django-nonrel/django@nonrel-1.5
${PH_HOME_DIR}/bin/pip install git+https://github.com/django-nonrel/djangotoolbox
${PH_HOME_DIR}/bin/pip install git+https://github.com/django-nonrel/mongodb-engine