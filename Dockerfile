FROM python:3.8

EXPOSE $PORT

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install streamlit

RUN pip install pyqrcode

CMD ["streamlit", "run", "app.py", "--server.port", $PORT]