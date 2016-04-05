from setuptools import setup, find_packages
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polls_server.settings")

setup(
    name="polls_server",
    version="1.0",
    author="Alex",
    author_email="some@email.com",
    description="polls_server",
    long_description="polls_server",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=['manage.py']
)