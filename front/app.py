import os
import requests
import streamlit as st

API_URL = os.getenv(
    "API_URL",
    "http://localhost:8000/recommend"
)

st.set_page_config(
    page_title="Research Method Advisor",
    page_icon="📊",
    layout="wide"
)

st.title("📊 데이터 분석 방법 추천 시스템")

st.info(
    """
    🎓 26-1 오픈소스소프트웨어실습 기말고사 대체과제

    정보융합학부 김민지 (2023510005)
    """
)

st.markdown(
    """
    연구 주제와 데이터 특성을 입력하면

    적합한 머신러닝·딥러닝·설명가능 인공지능(XAI) 기법을 추천합니다.
    """
)

st.divider()

st.subheader("📝 연구 정보 입력")

col1, col2 = st.columns(2)

with col1:

    research_topic = st.text_input(
        "연구 주제",
        placeholder="예: Customer Churn Prediction"
    )
    
    data_type = st.selectbox(
        "데이터 유형",
        [
            "Tabular",
            "Text",
            "Image",
            "Time Series"
        ]
    )

    analysis_goal = st.selectbox(
        "분석 목적",
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
        "데이터 규모",
        [
            "Small (<10K samples)",
            "Medium (10K~100K samples)",
            "Large (>100K samples)"
        ]
    )

    label_availability = st.selectbox(
        "라벨 유무",
        [
            "Yes",
            "No"
        ]
    )

    user_priority = st.selectbox(
        "우선 고려사항",
        [
            "High Performance",
            "Interpretability",
            "Fast Training"
        ]
    )

    explainability_importance = st.selectbox(
        "설명 가능성 중요도",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    research_domain = st.selectbox(
        "연구 분야",
        [
            "Business",
            "Finance",
            "Healthcare",
            "Marketing",
            "Social Science",
            "Engineering"
        ]
    )

if st.button("🧐 분석 방법 추천 결과 확인", use_container_width=True):

    payload = {
        "research_topic": research_topic,
        "data_type": data_type,
        "analysis_goal": analysis_goal,
        "dataset_size": dataset_size,
        "label_availability": label_availability,
        "user_priority": user_priority,
        "explainability_importance": explainability_importance,
        "research_domain": research_domain
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        result = response.json()

        st.divider()

        st.subheader("👤 연구자 성향")
        st.success(result["researcher_profile"])

        st.divider()

        st.subheader("🏆 추천 분석 기법 top3")

        cols = st.columns(len(result["recommended_methods"]))

        for idx, method in enumerate(result["recommended_methods"]):

            with cols[idx]:

                with st.container(border=True):

                    st.metric(
                        label=f"#{idx+1} {method['name']}",
                        value=f"{method['score']}점"
                    )

                    st.progress(
                        method["difficulty_score"] / 100
                    )

                    st.write(
                        f"⭐ 난이도: {method['difficulty']}"
                    )

                    st.write(
                        f"📚 추천 라이브러리: {method['library']}"
                    )

                    st.caption(
                        method["description"]
                    )

                    st.write(
                        f"💡 활용 예시: {method['example_use_case']}"
                    )

        st.divider()

        st.subheader("🧠 추천 XAI 기법")

        xai_cols = st.columns(
            len(result["recommended_xai"])
        )

        for i, xai in enumerate(
            result["recommended_xai"]
        ):
            with xai_cols[i]:
                st.success(xai)

        st.divider()

        st.subheader("📋 추천 근거")

        for item in result["reason_details"]:
            st.write(f"✅ {item}")

        st.info(result["reason"])

    except Exception as e:

        st.error(
            f"서버 연결 오류: {e}"
        )