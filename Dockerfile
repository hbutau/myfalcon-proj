FROM python:3.7-alpine
# Let us copy our requirements file so that we can install our python dependencies.

RUN set -ex \
    && apk add --no-cache --virtual \
    libpq-dev \
    linux-headers \
    postgresql-dev \
    libxslt-dev \
    musl-dev \
    libgcc \
    zlib-dev \
    jpeg-dev \
    gcc

# Copy our source code to the working directory
COPY ./requirements.txt   /code/requirements.txt

RUN pip install -U -r /code/requirements.txt 

COPY . /CODE/

WORKDIR /CODE/

EXPOSE 8000

CMD ["uwsgi uwsgi.ini]
