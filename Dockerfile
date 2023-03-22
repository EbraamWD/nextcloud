FROM python:3.8

RUN python3 -m pip install flask


COPY . /

#WORKDIR /project

EXPOSE 5000

ENV FLASK_APP=app
#ENV FLASK_ENV=development

CMD ["python", "app.py"]

#"--host=0.0.0.0