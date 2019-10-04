## Motivation

Exemples d'implémentation en python pour illustrer la conférence **3 patterns de tests d’intégration avec des ressources externes**
donnée lors du [meetup crafting datascience du 25/09](https://www.meetup.com/fr-FR/crafting-datascience/events/264211988/).

[![Build Status](https://travis-ci.org/octo-cdcv/3_patterns_tests_integration.svg?branch=master)](https://travis-ci.org/octo-cdcv/3_patterns_tests_integration)

## General Information

* [Presentation - Slide deck](https://fr.slideshare.net/FabienArcellier/3-patterns-de-tests-dintgration-avec-des-ressources-externes/FabienArcellier/3-patterns-de-tests-dintgration-avec-des-ressources-externes)
* [Meetup Crafting Datascience](https://www.meetup.com/fr-FR/crafting-datascience/)
* [Blueprint de ce projet](https://github.com/FabienArcellier/blueprint-library-pip)

## Focus du meetup

Le meetup illustre 3 patterns pour effectuer des tests
qui nécessitent des ressources externes.

### Isoler les tests d'intégration qui font appels au Filesystem

### Effectuer des tests d'intégration sur elastcisearch

### Effectuer des tests d'intégration sur un émulateur S3

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-library-pip.git
```

## Usage

1 . instancier un environnement virtuel et installer les dépendances

```
virtualenv -p python3 venv
pip install .
```

2 . exécuter les tests automatiques

```
. venv/bin/activate; python -u -m unittest discover "$(TEST_MODULE)/"
```

## Developper guideline

D'autres commandes sont packagées dans le `Makefile` et viennent du blueprint de démarrage
d'une librairie python ``blueprint-lib-pip``.

```
$ make
coverage                       output the code coverage in htmlcov/index.html
freeze_requirements            update the project dependencies based on setup.py declaration
help                           provides cli help for this makefile (default)
install_requirements_dev       install pip requirements for development
install_requirements           install pip requirements based on requirements.txt
lint                           run pylint
tests                          run automatic tests
tox                            run tests described in tox.ini on multiple python environments
venv                           build a virtual env for python 3 in ./venv
```

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Install production environment

```bash
make install_requirements
```

### Initiate or update the library requirements

If you want to initiate or update all the requirements `install_requires` declared in `setup.py`
and freeze a new requirements.txt, use this command

```bash
make freeze_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
