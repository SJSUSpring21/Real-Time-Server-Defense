FROM python:3.8

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

ENV PATH=/root/.local:$PATH

RUN pip3 install -r requirements.txt
CMD ["./main.py"]
ENTRYPOINT [ "python3" ]