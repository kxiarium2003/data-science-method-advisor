from pydantic import BaseModel
from typing import List


class RecommendationRequest(BaseModel):
    research_topic: str
    data_type: str
    analysis_goal: str
    dataset_size: str
    label_availability: str
    user_priority: str
    explainability_importance: str
    research_domain: str


class MethodRecommendation(BaseModel):
    name: str
    score: int
    difficulty: str
    difficulty_score: int
    library: str
    example_use_case: str
    description: str


class RecommendationResponse(BaseModel):
    research_topic: str
    researcher_profile: str
    recommended_methods: List[MethodRecommendation]
    recommended_xai: List[str]
    reason_details: List[str]
    reason: str