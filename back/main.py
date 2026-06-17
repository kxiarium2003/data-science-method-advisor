from fastapi import FastAPI
from schemas import (
    RecommendationRequest,
    RecommendationResponse
)
from recommender import recommend

app = FastAPI(
    title="Data Science Method Advisor API"
)


@app.get("/")
def health_check():
    return {"message": "API is running"}


@app.post(
    "/recommend",
    response_model=RecommendationResponse
)
def get_recommendation(
    request: RecommendationRequest
):
    return recommend(request)