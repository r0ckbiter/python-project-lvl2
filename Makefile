install:
	poetry install
	
gendiff:
	poetry run gendiff
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl
	
lint:
	poetry run flake8 gendiff
	
package-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl
	
test:
	poetry run pytest tests


coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
