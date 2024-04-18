FROM python:3.11
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
ENV TAIPY_APP=main.py
CMD ["Python3.11", "run", "--host=0.0.0.0", "--port=8888"]