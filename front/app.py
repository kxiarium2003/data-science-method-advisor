import requests
import streamlit as st

st.set_page_config(
    page_title="Research Method Advisor",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Research Method Advisor")

st.markdown(
    """
    Discover the most suitable machine learning,
    deep learning, and explainable AI methods
    for your research problem.
    """
)

st.divider()

st.subheader("📝 Research Information")

col1, col2 = st.columns(2)

with col1:

    research_topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Customer Churn Prediction"
    )

    data_type = st.selectbox(
        "Data Type",
        [
            "Tabular",
            "Text",
            "Image",
            "Time Series"
        ]
    )

    analysis_goal = st.selectbox(
        "Analysis Goal",
        [
            "Classification",
            "Regression",
            "Clustering",
            "Forecasting",
            "Feature Importance Analysis",
            "Model Interpretation"
        ]
    )

with col2:

    dataset_size = st.selectbox(
        "Dataset Size",
        [
            "Small (<10K samples)",
            "Medium (10K~100K samples)",
            "Large (>100K samples)"
        ]
    )

    label_availability = st.selectbox(
        "Label Availability",
        [
            "Yes",
            "No"
        ]
    )

    user_priority = st.selectbox(
        "User Priority",
        [
            "High Performance",
            "Interpretability",
            "Fast Training"
        ]
    )

    explainability_importance = st.selectbox(
        "Explainability Importance",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    research_domain = st.selectbox(
        "Research Domain",
        [
            "Business",
            "Finance",
            "Healthcare",
            "Marketing",
            "Social Science",
            "Engineering"
        ]
    )

if st.button("🚀 Generate Recommendation", use_container_width=True):

    payload = {
        "research_topic": research_topic,
        "data_type": data_type,
        "analysis_goal": analysis_goal,
        "dataset_size": dataset_size,
        "label_availability": label_availability,
        "user_priority": user_priority,
        "explainability_importance": explainability_importance
        "research_domain": research_domain
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/recommend",
            json=payload
        )

        result = response.json()

        st.divider()

        st.subheader("👤 Researcher Profile")
        st.success(result["researcher_profile"])

        st.divider()

        st.subheader("🏆 Top Recommended Methods")

        cols = st.columns(len(result["recommended_methods"]))

        for idx, method in enumerate(result["recommended_methods"]):

            with cols[idx]:

                st.metric(
                    label=f"#{idx+1} {method['name']}",
                    value=f"{method['score']} pts"
                )

                st.progress(method["difficulty_score"])

                st.write(
                    f"⭐ Difficulty: {method['difficulty']}"
                )

                st.write(
                    f"📚 Library: {method['library']}"
                )

                st.caption(
                    method["description"]
                )

                st.write(
                    f"💡 Example: {method['example_use_case']}"
                )

        st.divider()

        st.subheader("🧠 Recommended XAI Techniques")

        xai_cols = st.columns(
            len(result["recommended_xai"])
        )

        for i, xai in enumerate(
            result["recommended_xai"]
        ):
            with xai_cols[i]:
                st.success(xai)

        st.divider()

        st.subheader("📋 Recommendation Reason")

        st.info(result["reason"])

    except Exception as e:

        st.error(
            f"Connection Error: {e}"
        )