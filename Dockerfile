FROM python:3.6-slim-buster


COPY . /app

WORKDIR /app

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
#ENV FLASK_ENV=development
CMD ["python", "app.py"]
#CMD ["python3", "flask", "run", "--host=0.0.0.0"]

