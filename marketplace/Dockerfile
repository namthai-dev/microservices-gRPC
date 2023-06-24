FROM python:3.9

RUN mkdir /service

COPY protobufs/ /service/protobufs/

COPY marketplace/ /service/marketplace/

COPY requirements.txt /service/marketplace/

WORKDIR /service/marketplace

# RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto
EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
