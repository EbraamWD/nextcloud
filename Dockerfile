FROM python:alpine as build

RUN apk upgrade --no-cache && \
    apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev cargo

WORKDIR /source

COPY requirements.txt /source/

RUN python3 -m venv /source/venv && \
    . /source/venv/bin/activate && \
    python3 -m ensurepip --upgrade && \
    python3 -m pip install -r /source/requirements.txt 

COPY app.py .
    
# Build the final image

FROM python:alpine as final

WORKDIR /source

COPY --from=build /source /source

ENV FLASK_APP=app.py

CMD . /source/venv/bin/activate && python3 app.py