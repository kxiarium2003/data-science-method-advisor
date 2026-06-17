METHODS = {
    "Logistic Regression": {
        "difficulty": "★☆☆☆☆",
        "difficulty_score": 20,
        "library": "scikit-learn",
        "example": "Customer Churn Prediction",
        "description": "Simple and interpretable linear classification model."
    },
    "Decision Tree": {
        "difficulty": "★☆☆☆☆",
        "difficulty_score": 20,
        "library": "scikit-learn",
        "example": "Loan Approval Classification",
        "description": "Tree-based model that is easy to visualize and explain."
    },
    "Random Forest": {
        "difficulty": "★★☆☆☆",
        "difficulty_score": 40,
        "library": "scikit-learn",
        "example": "Fraud Detection",
        "description": "Ensemble model with strong performance and stability."
    },
    "XGBoost": {
        "difficulty": "★★★☆☆",
        "difficulty_score": 60,
        "library": "xgboost",
        "example": "Credit Risk Prediction",
        "description": "High-performance boosting algorithm for tabular data."
    },
    "LightGBM": {
        "difficulty": "★★★☆☆",
        "difficulty_score": 60,
        "library": "lightgbm",
        "example": "Large Scale Classification",
        "description": "Fast gradient boosting framework optimized for large datasets."
    },
    "K-Means": {
        "difficulty": "★☆☆☆☆",
        "difficulty_score": 20,
        "library": "scikit-learn",
        "example": "Customer Segmentation",
        "description": "Popular clustering algorithm for unlabeled data."
    },
    "TF-IDF + Logistic Regression": {
        "difficulty": "★★☆☆☆",
        "difficulty_score": 40,
        "library": "scikit-learn",
        "example": "Spam Detection",
        "description": "Lightweight and effective baseline for text classification."
    },
    "BERT": {
        "difficulty": "★★★★☆",
        "difficulty_score": 80,
        "library": "transformers",
        "example": "Sentiment Analysis",
        "description": "Pretrained language model with strong NLP performance."
    },
    "CNN": {
        "difficulty": "★★★☆☆",
        "difficulty_score": 60,
        "library": "tensorflow",
        "example": "Image Classification",
        "description": "Deep learning model specialized for image data."
    },
    "LSTM": {
        "difficulty": "★★★★☆",
        "difficulty_score": 80,
        "library": "tensorflow",
        "example": "Stock Price Forecasting",
        "description": "Sequential deep learning model for time-dependent data."
    },
    "Transformer": {
        "difficulty": "★★★★★",
        "difficulty_score": 100,
        "library": "transformers",
        "example": "Time Series Forecasting",
        "description": "State-of-the-art architecture for sequence modeling."
    }
}


DATA_TYPE_CANDIDATES = {
    "Tabular": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost",
        "LightGBM",
        "K-Means"
    ],
    "Text": [
        "TF-IDF + Logistic Regression",
        "BERT"
    ],
    "Image": [
        "CNN"
    ],
    "Time Series": [
        "LSTM",
        "Transformer"
    ]
}


def recommend(req):

    candidates = DATA_TYPE_CANDIDATES.get(req.data_type, [])

    scores = {method: 0 for method in candidates}

    # ==================================================
    # Analysis Goal
    # ==================================================

    if req.analysis_goal == "Classification":

        for model in candidates:
            scores[model] += 20

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 20

        if "Decision Tree" in scores:
            scores["Decision Tree"] += 20

        if "Random Forest" in scores:
            scores["Random Forest"] += 20

        if "XGBoost" in scores:
            scores["XGBoost"] += 20

        if "LightGBM" in scores:
            scores["LightGBM"] += 20

        if "BERT" in scores:
            scores["BERT"] += 30

        if "CNN" in scores:
            scores["CNN"] += 30

    elif req.analysis_goal == "Regression":

        if "Random Forest" in scores:
            scores["Random Forest"] += 20

        if "XGBoost" in scores:
            scores["XGBoost"] += 30

        if "LightGBM" in scores:
            scores["LightGBM"] += 30

    elif req.analysis_goal == "Clustering":

        if "K-Means" in scores:
            scores["K-Means"] += 100

    elif req.analysis_goal == "Forecasting":

        if "LSTM" in scores:
            scores["LSTM"] += 40

        if "Transformer" in scores:
            scores["Transformer"] += 50

    elif req.analysis_goal == "Feature Importance Analysis":

        if "Random Forest" in scores:
            scores["Random Forest"] += 50

        if "XGBoost" in scores:
            scores["XGBoost"] += 50

    elif req.analysis_goal == "Model Interpretation":

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 50

        if "Decision Tree" in scores:
            scores["Decision Tree"] += 50

    # ==================================================
    # Dataset Size
    # ==================================================

    if req.dataset_size == "Small (<10K samples)":

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 20

        if "Decision Tree" in scores:
            scores["Decision Tree"] += 20

    elif req.dataset_size == "Large (>100K samples)":

        if "LightGBM" in scores:
            scores["LightGBM"] += 30

        if "Transformer" in scores:
            scores["Transformer"] += 30

    # ==================================================
    # Label Availability
    # ==================================================

    if req.label_availability == "No":

        if "K-Means" in scores:
            scores["K-Means"] += 60

    # ==================================================
    # User Priority
    # ==================================================

    if req.user_priority == "High Performance":

        if "XGBoost" in scores:
            scores["XGBoost"] += 30

        if "LightGBM" in scores:
            scores["LightGBM"] += 30

        if "BERT" in scores:
            scores["BERT"] += 30

        if "Transformer" in scores:
            scores["Transformer"] += 30

    elif req.user_priority == "Interpretability":

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 30

        if "Decision Tree" in scores:
            scores["Decision Tree"] += 30

        if "Random Forest" in scores:
            scores["Random Forest"] += 20

    elif req.user_priority == "Fast Training":

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 20

        if "LightGBM" in scores:
            scores["LightGBM"] += 30

    # ==================================================
    # Explainability Importance
    # ==================================================

    if req.explainability_importance == "High":

        if "Logistic Regression" in scores:
            scores["Logistic Regression"] += 20

        if "Decision Tree" in scores:
            scores["Decision Tree"] += 20

        if "Random Forest" in scores:
            scores["Random Forest"] += 20

    # ==================================================
    # XAI Recommendation
    # ==================================================

    if (
        req.explainability_importance == "High"
        or req.analysis_goal == "Model Interpretation"
    ):
        xai = ["SHAP", "LIME"]
    else:
        xai = ["SHAP"]

    # ==================================================
    # Top 3
    # ==================================================

    ranked = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    recommendations = []

    for method, score in ranked:

        info = METHODS[method]

        recommendations.append({
            "name": method,
            "score": score,
            "difficulty": info["difficulty"],
            "difficulty_score": info["difficulty_score"],
            "library": info["library"],
            "example_use_case": info["example"],
            "description": info["description"]
})
        
    if req.user_priority == "High Performance":
        researcher_profile = "🚀 Performance-Oriented Researcher"

    elif req.user_priority == "Interpretability":
        researcher_profile = "🔍 Explainability-Oriented Researcher"

    else:
        researcher_profile = "⚡ Efficiency-Oriented Researcher"
        
    return {
        "research_topic": req.research_topic,
        "researcher_profile": researcher_profile,
        "recommended_methods": recommendations,
        "recommended_xai": xai,
        "reason": (
            f"Recommendations for '{req.research_topic}' "
            f"were generated using "
            f"{req.data_type} data, "
            f"{req.analysis_goal} goal, "
            f"{req.user_priority} priority, "
            f"and {req.explainability_importance} explainability."
        )
    }