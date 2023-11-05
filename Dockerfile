FROM python:3.8.18
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 5000

ENV FLASK_APP=service/__init__.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
