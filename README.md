# gRPC Review - Python

## Overview

Goal is to review implementing client <-> server python communication using gRPC


## Getting Started
Activate virtual environment
```sh
source .env/bin/activate
```

Install dependencies
```sh
python -m pip install grpcio grpcio-tools
```

Compile proto file using the following command
```sh
python -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. feed.proto animal.proto
```

Start server
```sh
python feed_server.py
```

Start client
```sh
python feed_client.py
```


## Approach to Setting Up gRPC Client <-> Server Communication

1. Define .proto files. E.g. feed.proto, animal.proto
2. Generate language specific servicers, stubs, and proto types
3. Create and start a server
4. Create and use a client to call the server

Other possible implementation details may include
1. Defining DB client to read from / write to a persistent storage
2. Adding instrumentation to measure client <-> server communication
3. Introduce authentication and authorization


## Caveats

Feed server is shared by the feed and animal services. Idea is to showcase that this is possible if interested.

In production, may decide to have 2 separate deployments where clients use "dns:///feed.service:50051" to connect to the feed service and "dns:///animal.service:50051" to connect to the animal service which may be in separate pods / containers / etc.

Alternatively, may decide to split the code out across repositories to mitigate any likelihood that clients connect to "dns:///feed.service:50051" but call animal service and vice versa.

Have seen both implementations.


## Resources

- [Python gRPC Quick Start](https://grpc.io/docs/languages/python/quickstart/)
- [Compiling Protocol Buffers](https://protobuf.dev/getting-started/pythontutorial/)
- [Language Guide (proto 3)](https://protobuf.dev/programming-guides/proto3/)
- [Implementing gRPC in Python: A Step-by-step Guide](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)