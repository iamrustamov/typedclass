pip:
	pip install -r requirements.txt

test:
	py.test -s -vv

testcov:
	py.test -s -vv --cov=typedclass

testhtml:
	rm -r htmlcov/ || true
	py.test -s -vv --cov=typedclass --cov-report html

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d | xargs rm -fr
