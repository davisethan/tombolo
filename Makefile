IMAGE := ethandavisecd/tombolo:latest

.PHONY: docs
docs:
	quarto render quarto

.PHONY: docker-build
docker-build:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE) .

.PHONY: docker-push
docker-push:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(IMAGE) --push .
