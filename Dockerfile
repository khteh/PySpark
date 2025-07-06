FROM khteh/ubuntu:latest
MAINTAINER Kok How, Teh <funcoolgeek@gmail.com>
WORKDIR /app
ADD . /app
RUN pipenv install
#ENTRYPOINT ["pipenv", "run", "hypercorn", "--config=/etc/hypercorn.toml", "--reload", "src.main:app"]
# Define the default command to run your PySpark application
CMD ["pipenv", "run", "spark-submit", "--master", "local[*]", "TextFile.py"]
