TAG?=test

fetch:
	git clone https://github.com/dagster-io/dagster.git temp-dagster
	cp -r temp-dagster/python_modules/libraries/dagster-k8s/helm/dagster/ dagster-chart
	rm -r temp-dagster

template:
	helm template --output-dir templates dagster-chart --name dagster

build:
	docker build -f docker/Dockerfile . -t pymetrics/dagster:$(TAG)


setup:
	pip install -r requirements-dev.txt

test-pipelines:
	flake8
	pytest -v -rsx pipelines/tests

docker-compose-reload:
	docker-compose build
	docker-compose restart dagster

apply:
	kubectl apply -k kuztomise/overlays/local

delete:
	kubectl delete -k kuztomise/overlays/local
