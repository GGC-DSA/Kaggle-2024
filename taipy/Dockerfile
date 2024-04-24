FROM python:3.11
WORKDIR /app
RUN pip install taipy
RUN pip install numpy
RUN pip install pandas
RUN pip install tensorflow
RUN pip install spacy
RUN pip install transformers
RUN pip install pathlib
RUN pip install datasets
RUN pip install torch
RUN pip install matplotlib
RUN pip install plotly
COPY . /app
ENV TAIPY_APP=./app/taipy/main.py
CMD ["python3", "./app/taipy/main.py", "--host=0.0.0.0", "--port=8888"]