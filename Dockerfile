FROM python:3.8

RUN python3 -m pip install flask

#RUN mkdir project

COPY . .

#WORKDIR /project

#EXPOSE 5000

ENV FLASK_APP=app
#ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]