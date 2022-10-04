FROM python:3.8

EXPOSE "$PORT"

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install streamlit

RUN pip3 install pyqrcode

CMD ["streamlit", "run", "app.py", "--server.port", "$PORT"]