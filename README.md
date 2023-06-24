# microservices-gRPC
Microservices with high performance Remote Procedure Call (RPC)

![image](https://github.com/namthai-dev/microservices-gRPC/assets/102452878/c3914a58-116d-4768-bc89-8cf4e740b0af)

## Install dependencies

    pip install -r requirements.txt

To generate Python code from the protobufs

    python -m grpc_tools.protoc -I ./protobufs --python_out=./recommendations --grpc_python_out=./recommendations ./protobufs/recommendations.proto
    python -m grpc_tools.protoc -I ./protobufs --python_out=./marketplace --grpc_python_out=./marketplace ./protobufs/recommendations.proto

Copy `.env-example` to `.env`

## Run Docker

    docker compose up

## Access

    http://127.0.0.1:8000/docs

# Screenshots

![image](https://github.com/namthai-dev/microservices-gRPC/assets/102452878/19b33193-1f49-4d0d-ad57-56051617c770)
