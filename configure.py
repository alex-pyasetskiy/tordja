#!/usr/bin/env bin/python
# encoding: utf-8

import sys
import os
import os.path
import argparse

import configobj

PH_HOME_DIR = os.environ["PH_HOME_DIR"]
PH_ENV_ID = os.environ["PH_ENV_ID"]


def _make_config_file_name(environment, out=False):
    """
    Make config file name with abs path depends on environment id

    :param environment: current environment id from OS ENV
    :type

    :return: path
    """
    return os.path.join(PH_HOME_DIR, "etc/config", "%s.conf" % environment) if out else \
        os.path.join(PH_HOME_DIR, "config", "%s.conf.in" % environment)


def _expand_env_vars(section, key):
    """
    This will make config lines like:

    .. code-block:: config.in

        ADMINS = %(ADMINS)s
        DIR = %(DIR)s
        CERTS_PATH = %(DIR)s/etc/dev-certs

    to be substituted properly.

    """
    section[key] = section[key] % os.environ


def _expand_file(config):
    with file(config) as config_file:
        first_line = config_file.readline().strip()
        if first_line.startswith("#$include"):
            _, __, include = first_line.partition(" ")
            data = _expand_file(_make_config_file_name(include))
        else:
            data = configobj.ConfigObj(list_values=False)
    config_data = configobj.ConfigObj(config, interpolation=False, list_values=False)
    config_data.walk(_expand_env_vars)
    data.update(config_data)
    return data


def main():
    parser = argparse.ArgumentParser(
        description=u"""Performs post-deploy configuration of the platform
        filling variables in corresponding environment configs""")
    parser.add_argument("--config", required=False, default=None)
    args = parser.parse_args()

    # noinspection PyUnresolvedReferences
    out_config_file = args.config if args.config is not None else _make_config_file_name(PH_ENV_ID, out=True)
    in_config_file = args.config if args.config is not None else _make_config_file_name(PH_ENV_ID)

    print >> sys.stdout, u"\nCreating config file %s, for %s environment\n" % (out_config_file, PH_ENV_ID.upper())

    if not in_config_file.endswith(u".conf.in"):
        print >> sys.stderr, u"Specified file must end with '.conf.in', exiting"
    else:
        config = _expand_file(in_config_file)
        with file(out_config_file, "w") as out_config:  # This removes '.in' at the end of input file name)
            config.write(outfile=out_config)


if __name__ == "__main__":
    main()