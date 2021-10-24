FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install flask
COPY ./main.py ./main.py
COPY ./flag.txt ./flag.txt

CMD python3 main.py
