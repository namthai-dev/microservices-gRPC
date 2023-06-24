import os
from fastapi import FastAPI

import grpc
from google.protobuf.json_format import MessageToJson

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = FastAPI()

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.get("/marketplace")
async def get_marketplace():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    serialized = MessageToJson(recommendations_response)
    return eval(serialized)
