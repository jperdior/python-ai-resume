# AI Resume

## Introduction

This is an interactive AI powered resume built on top of Django Rest Framework and a very simple vue.js frontend.
In a few steps and with an OpenAI API key, you can set up your own interactive resume.

## Requirements

- docker
- docker-compose
- make
- python3
- OpenAI API key
- Ports 8080 and 3306 available

## Get it running

1. Clone this repository
2. Set your OpenAI API key in the ops/docker/docker-compose.dev.yml file line 8
3. Run `make start`
4. To have the libraries locally available in a virtual environment run `cd code/aiResume && python3 -m venv venv && source venv/bin/activate`, remember to run `deactivate` when you finish working in this project

## How to use

TODO
