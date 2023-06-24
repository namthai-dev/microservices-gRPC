# microservices-gRPC
Microservices with high performance Remote Procedure Call (RPC)

Install dependencies

    pip install -r requirements.txt

To generate Python code from the protobufs

    python -m grpc_tools.protoc -I ./protobufs --python_out=./recommendations --grpc_python_out=./recommendations ./protobufs/recommendations.proto
    python -m grpc_tools.protoc -I ./protobufs --python_out=./marketplace --grpc_python_out=./marketplace ./protobufs/recommendations.proto

Copy `.env-example` to `.env`

Run Docker

    docker compose up
