all_code = src

install:
	pip install -e .
	pre-commit install

clean:
	git clean -fdx

format:
	isort ${all_code} --profile black
	black ${all_code}

check: format
	black ${all_code} --check
	isort ${all_code} --check --profile black
	pylint ${all_code}
