install:
	pipenv install

runserver:
	bash -c "pushd arti/ && pipenv run ./manage.py runserver && popd"

shell:
	bash -c "pushd arti/ && pipenv run ./manage.py shell_plus && popd"

pipenv-shell:
	pipenv shell


clean:
	pipenv --rm
