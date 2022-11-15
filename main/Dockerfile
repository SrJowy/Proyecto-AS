FROM ubuntu

RUN apt -qq update
RUN apt -y -qq install python3
RUN apt -y -qq install python3-pip
RUN pip3 -qq install crate
RUN mkdir /cliente

COPY ./app.py /cliente/app.py

WORKDIR /cliente

CMD python3 app.py