from python:3.7-alpine
workdir /app
env FLASK_APP=app.py
env FLASK_RUN_HOST=0.0.0.0
run apk add --no-cache gcc musl-dev linux-headers
run apk add --no-cache build-base
copy requirements.txt requirements.txt
copy app_12.py app.py
copy test.db test.db
copy templates ./templates
copy static ./static
run pip install -r requirements.txt
expose 5000
cmd ["flask", "run"]
