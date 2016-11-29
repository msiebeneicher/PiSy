# PiSy [![Build Status](https://travis-ci.org/msiebeneicher/PiSy.svg?branch=master)](https://travis-ci.org/msiebeneicher/PiSy)

salt pillar sync tool for easy synchronization of secret pillars with dummy values

## Usage

```sh
usage: main.py [-h] [-v] source target

synchronise pillars from source to destination folder with dummy values

positional arguments:
  source      Pillar source path
  target      Pillar target path

optional arguments:
  -h, --help  show this help message and exit
  -v          Verbosity
```

## Requirements

* PyYAML
* six

# Installation

```sh
# Install pisy v0.1.0
wget https://github.com/msiebeneicher/PiSy/releases/download/v0.1.0/pisy-0.1.0-py2.7.egg
easy_install pisy-0.1.0-py2.7.egg
```

## Unittests

Execute unittests by `./runtests,py`