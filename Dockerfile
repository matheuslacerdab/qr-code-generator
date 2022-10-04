FROM python:3.8

#EXPOSE 8501

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

#CMD ["streamlit", "run", "app.py"]
CMD streamlit run --server.port $PORT app.py