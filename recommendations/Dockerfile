FROM python:3.9

RUN mkdir /service

COPY protobufs/ /service/protobufs/

COPY recommendations/ /service/recommendations/

COPY requirements.txt /service/recommendations/

WORKDIR /service/recommendations

# RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051

ENTRYPOINT [ "python", "main.py" ]
