FROM alpine

RUN apk -qq update
RUN apk -qq add python3
RUN apk -qq add py3-pip
RUN pip3 -qq install crate
RUN pip3 -qq install flask
RUN pip3 -qq install flask_cors
RUN pip3 -qq install docker
RUN mkdir /cliente

COPY ./app.py /cliente/app.py

WORKDIR /cliente

CMD python3 app.py