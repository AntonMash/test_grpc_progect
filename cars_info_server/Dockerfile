FROM python

RUN mkdir /service
COPY protos /service/protos/
COPY cars_info_server/ /service/cars_info_server/
WORKDIR /service/cars_info_server
RUN python -m pip install --upgrade pip
RUN python -m pip install -r req.txt
RUN python -m grpc_tools.protoc -I ../protos --python_out=. --grpc_python_out=. ../protos/cars_info.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]