# 26-1-oss-final-project

2026학년도 1학기 오픈소스소프트웨어실습 기말고사 대체과제입니다.

Streamlit 프론트엔드, FastAPI 백엔드, Docker, AWS EC2를 활용하여 **데이터 분석 방법 추천 시스템(Data Science Method Advisor)** 을 구현하였습니다.

사용자는 연구 주제와 데이터 특성을 입력하면, 적합한 머신러닝·딥러닝·설명가능 인공지능(XAI) 기법을 추천받을 수 있습니다.

---

## 프로젝트 소개

본 프로젝트는 연구자 또는 데이터 분석가가 연구 문제에 적합한 분석 기법을 선택할 수 있도록 지원하는 추천 웹 애플리케이션입니다.

사용자는 다음과 같은 정보를 입력합니다.

* 연구 주제
* 데이터 유형
* 분석 목적
* 데이터 규모
* 라벨 유무
* 우선 고려사항
* 설명 가능성 중요도
* 연구 분야

입력된 정보를 기반으로 FastAPI 백엔드가 점수 기반(rule-based) 추천을 수행하고, Streamlit 프론트엔드에서 결과를 시각적으로 제공합니다.

---

## 시스템 구조

```text
사용자 입력
      ↓
Streamlit Frontend
      ↓ HTTP Request
FastAPI Backend
      ↓
추천 결과(JSON)
      ↓
Streamlit 결과 출력
```

---

## 구현 기능

### 입력 정보

* Research Topic

* Data Type

  * Tabular
  * Text
  * Image
  * Time Series

* Analysis Goal

  * Classification
  * Regression
  * Clustering
  * Forecasting
  * Feature Importance Analysis
  * Model Interpretation

* Dataset Size

  * Small (<10K samples)
  * Medium (10K~100K samples)
  * Large (>100K samples)

* Label Availability

  * Yes
  * No

* User Priority

  * High Performance
  * Interpretability
  * Fast Training

* Explainability Importance

  * Low
  * Medium
  * High

* Research Domain

  * Business
  * Finance
  * Healthcare
  * Marketing
  * Social Science
  * Engineering

---

### 추천 결과

#### 추천 분석 기법 Top 3

추천 가능한 분석 기법

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* LightGBM
* K-Means
* TF-IDF + Logistic Regression
* BERT
* CNN
* LSTM
* Transformer

각 기법에 대해 다음 정보를 제공합니다.

* 추천 점수
* 난이도
* 추천 라이브러리
* 활용 예시
* 기법 설명

#### 추천 XAI 기법

* SHAP
* LIME

#### 연구자 성향 분석

예시

* 🚀 Performance-Oriented Researcher
* 🔍 Explainability-Oriented Researcher
* ⚡ Efficiency-Oriented Researcher

#### 추천 근거 제공

추천 결과가 생성된 이유를 Bullet 형태로 제공합니다.

---

## 프로젝트 구조

```text
data-science-method-advisor/
│
├── front/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── back/
│   ├── main.py
│   ├── recommender.py
│   ├── schemas.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 실행 방법

### 1. 저장소 클론

```bash
git clone https://github.com/kxiarium2003/data-science-method-advisor.git
cd data-science-method-advisor
```

---

### 2. Docker Compose 실행

```bash
docker compose up --build
```

백엔드(FastAPI)와 프론트엔드(Streamlit)가 동시에 실행됩니다.

---

### 3. 서비스 접속

#### Streamlit

```text
http://localhost:8501
```

#### FastAPI Swagger UI

```text
http://localhost:8000/docs
```

---

## API 명세

### POST /recommend

연구 정보를 입력받아 추천 결과를 반환합니다.

#### Request Body

```json
{
  "research_topic": "Customer Churn Prediction",
  "data_type": "Tabular",
  "analysis_goal": "Classification",
  "dataset_size": "Medium (10K~100K samples)",
  "label_availability": "Yes",
  "user_priority": "High Performance",
  "explainability_importance": "High",
  "research_domain": "Business"
}
```

#### Response Example

```json
{
  "research_topic": "Customer Churn Prediction",
  "researcher_profile": "🚀 Performance-Oriented Researcher",
  "recommended_methods": [
    {
      "name": "XGBoost",
      "score": 90
    }
  ],
  "recommended_xai": [
    "SHAP",
    "LIME"
  ]
}
```

---

## Docker 구성

본 프로젝트는 Docker Compose를 사용하여 프론트엔드와 백엔드를 각각 별도 컨테이너로 실행합니다.

### Container

* method-advisor-frontend
* method-advisor-backend

### Port

| Service   | Port |
| --------- | ---- |
| Streamlit | 8501 |
| FastAPI   | 8000 |

---

## 개발 환경

* Python 3.11
* FastAPI
* Uvicorn
* Streamlit
* Requests
* Docker
* Docker Compose
* AWS EC2 (Learner Lab)
* VS Code

---


## 배포 주소

Streamlit: http://54.162.138.222:8501

Swagger: http://54.162.138.222:8000/docs
