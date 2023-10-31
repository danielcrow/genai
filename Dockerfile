FROM registry.access.redhat.com/ubi9/python-311@sha256:6760d1fb9617b2af8bbfcc33a7591cabbc1e416775c7187b1a71b830ffc6cb0c

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]