export PROJECT_NAME := python-ai-resume
export CURRENT_PATH := $(shell pwd)
export BACK_CONTAINER := back
export FRONT_CONTAINER := vue
export GITHUB_TOKEN := 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
export DOCKER_REGISTRY := ghcr.io


PHP_CS_FIXER_ARGS = --show-progress=dots --rules=@PSR12
DOCKER_COMPOSE=docker-compose -p ${PROJECT_NAME} -f ${CURRENT_PATH}/ops/docker/docker-compose.yml -f ${CURRENT_PATH}/ops/docker/docker-compose.dev.yml

restart: stop start

start: docker-build docker-up

start-no-cache: docker-build-no-cache docker-up

stop:
	@${DOCKER_COMPOSE} down --remove-orphans

docker-build:
	@${DOCKER_COMPOSE} build

docker-build-no-cache:
	@${DOCKER_COMPOSE} build --no-cache

docker-up:
	@${DOCKER_COMPOSE} up -d

logs:
	@${DOCKER_COMPOSE} logs -f

# PIP

pip-install:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} pip install -r requirements.txt

pip-upgrade:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} pip install --upgrade -r requirements.txt

pip-add:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} pip install ${package}

pip-remove:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} pip uninstall ${package}

# MIGRATIONS

generate-migrations:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} python manage.py makemigrations

execute-migrations:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} python manage.py migrate

# LINTING

lint-preview:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} black --check --diff .

lint-apply:
	@${DOCKER_COMPOSE} exec ${BACK_CONTAINER} black .