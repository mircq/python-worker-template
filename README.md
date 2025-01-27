# python-worker-template

This repo is still a work in progress!

#### Python version
[![python](https://img.shields.io/badge/Python-3.12-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

#### Package and project manager
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&style=flat&logoColor=white&label=uv&color=yellow)](https://github.com/astral-sh/uv)

#### Brokers
[![rabbitmq](https://img.shields.io/badge/rabbitmq-4.0.5-%23FF6600?style=flat&logo=rabbitmq&logoColor=white)](https://www.rabbitmq.com/)
[![pulsar](https://img.shields.io/badge/ApachePulsar-4.0.2-188FFF?style=flat&logo=apachepulsar&logoColor=white)](https://pulsar.apache.org/)

#### Data Modelling
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json&logoColor=white&labelColor=grey)](https://pydantic.dev)

#### Linter
[![Ruff](https://img.shields.io/badge/ruff-0.7.2-41B5BE?style=flat&logoColor=white)](https://docs.astral.sh/ruff/)

#### Static code analysis
[![MyPy](https://img.shields.io/badge/mypy-1.13.0-blue?style=flat)](https://mypy-lang.org/)

#### Docs
[![Sphinx](https://img.shields.io/badge/Sphinx-8.1.3-F7C942?style=flat&logo=sphinx&logoColor=white)](https://www.sphinx-doc.org/en/master/)


## Project description
This project is intended to be as a template worker. This worker consumes messages from a given queue and execute tasks 
according to the content of the messages, writing results into another (specified) queue.

## Install dependencies 

In order to run the project, you need to install _UV_ first.

On Linux and MacOS environments, launch the following command:

```shell
curl -LsSf https://astral.sh/uv/0.5.6/install.sh | sh
```

On Windows environments, launch the following command.

```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/0.5.6/install.ps1 | iex"
```

After _UV_ has been installed, you are ready to install project dependencies:

```shell
uv sync 
```

## Launching the application

To start the server, launch the following command:

```shell
python main.py
```

## Code quality

To perform code linting (e.g. remove unused dependencies and similar) launch the following command:
```shell
ruff check --fix
```

To format the code, launch the following command:

```shell
ruff format 
```