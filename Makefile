.PHONY: build start stop restart

build:
	@echo Building the image...
	docker compose build

start:
	@echo Running the container...
	docker compose up -d

stop:
	@echo Stopping and removing the container...
	docker compose down
	docker image rm anchor || true

restart: stop build start
