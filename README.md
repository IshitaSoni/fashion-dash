# Fashion Dash 👗🚀

**Fashion Dash** is a Python-based data pipeline and recommendation engine that solves the problem of style choice paralysis. By aggregating a user's digital fashion footprint (wishlists, carts, and purchase history from platforms like Myntra, Amazon, and Flipkart), the system analyzes text patterns, categorizes the user's distinct "fashion archetypes," and suggests new products they are highly likely to love.

---

## ✨ Features

- **Data Aggregation Pipeline:** Simulates incoming data streams from multiple e-commerce platforms (`Myntra`, `Amazon`, `Flipkart`).
- **Weighted Style Archetype Tagging:** Uses basic NLP (Natural Language Processing) and keyword mapping to categorize items into distinct fashion vibes (e.g., _Streetwear, Corporate Chic, Cottagecore, Edgy_).
- **Behavioral Weighting System:** Weights items based on user intent (e.g., a _Purchased_ item impacts the style score more heavily than a _Wishlisted_ item).
- **Content-Based Recommendation Engine:** Filters a master catalog to predict and recommend products matching the user's dominant style persona.

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.10+
- **Data Manipulation:** `pandas`
- **Machine Learning / NLP:** `scikit-learn` (TF-IDF Vectorization)
- **Dashboard / UI (Planned):** `Streamlit` & `Plotly`

---

## 📂 Project Structure

```text
fashion_dash/
│
├── data/
│   ├── user_history.json       # Simulated cart/wishlist/purchase data
│   └── product_catalog.json    # Mock items available for recommendation
│
├── src/
│   ├── __init__.py
│   ├── data_pipeline.py        # Loads, cleans, and merges user data
│   ├── style_analyzer.py       # Core NLP logic & style categorization
│   └── recommender.py          # Predictive suggestion model
│
├── main.py                     # The orchestrator that executes the workflow
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```
