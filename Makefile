DOCKER                     ?= docker
DOCKER_COMPOSE             ?= docker-compose
AMAZON_SERVICE              = amazon

start:
	${DOCKER_COMPOSE} build ${AMAZON_SERVICE}
	${DOCKER_COMPOSE} up -d ${AMAZON_SERVICE}
stop:
	${DOCKER_COMPOSE} down
