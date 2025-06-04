# ===== CONFIG ======
POETRY=poetry
DOCKER_COMPOSE=docker compose

# ===== TASKS ======
build:
	$(DOCKER_COMPOSE) up --build

up:
	$(DOCKER_COMPOSE) up -d


down:
	$(DOCKER_COMPOSE) down --volumes --remove-orphans

add:
	@echo "請輸入套件名稱，ex: make add name=redis"
	@exit 1


add-%:
	$(POETRY) add $*
	$(POETRY) export --without-hashes -f requirements.txt > requirements.txt
	$(DOCKER_COMPOSE) build $(SERVICE)

##重新輸出requirements.txt
export:
	$(POETRY) export --without-hashes -f requirements.txt > requirements.txt



show:
	$(POETRY) show


shell:
	${DOCKER_COMPOSE} exec $(SERVICE) /bin/sh