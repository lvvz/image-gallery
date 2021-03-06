#!/usr/bin/env python3

import os
from setuptools import setup, find_packages
import content_gallery

FILE_TYPES = [
    ".js",
    ".css",
    ".png",
    ".gif",
    ".html"
]

def has_required_files(files):
    for f in files:
        name, ext = os.path.splitext(f)
        if ext in FILE_TYPES:
            return True
    return False

def find_data_dirs(path):
    dirs = []
    for name, dlist, files in os.walk(path):
        if has_required_files(files):
            relpath = os.path.relpath(name, 'content_gallery')
            dirs.append(os.path.join(relpath, '*'))
    return dirs


setup(
    name="django-content-gallery",
    version=content_gallery.__version__,
    fullname="Django Content Gallery",
    description=" The Django application allows to attach a collection of images to objects of any model of any app",
    author="Oleksii Vovchok",
    author_email="a.vovchok.169@gmail.com",
    keywords="django image gallery photo",
    long_description=open('README.rst').read(),
    url="https://github.com/Kemaweyan/django-content-gallery",
    license="BSD-3-Clause",
    package_data={"content_gallery": find_data_dirs('content_gallery')},
    packages=find_packages(exclude=["content_gallery.tests", "content_gallery_testapp", "content_gallery_testapp.*"]),
    test_suite='runtests.runtests',
    install_requires=[
        'Django>=1.10',
        'Pillow>=3.0.0',
        'python-magic>=0.4.2',
        'awesome-slugify>=1.6',
        'django-admin-jqueryui112',
    ],
    classifiers=[
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
