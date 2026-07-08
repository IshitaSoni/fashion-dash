import pytest
from style_analyzer import calculate_style_scores

# 1. Arrange: Define static test fixtures
MOCK_TAXONOMY = {
    "Streetwear": ["hoodie", "sneakers"],
    "Corporate": ["blazer", "trousers"]
}
MOCK_WEIGHTS = {"bought": 3, "wishlist": 1}

def test_streetwear_dominance():
    # 2. Act: Simulate a clean user input packet
    sample_user_history = [
        {"title": "Oversized graphic hoodie", "status": "bought"}, # Streetwear: 3pts
        {"title": "White leather sneakers", "status": "wishlist"}  # Streetwear: 1pt
    ]
    
    scores = calculate_style_scores(sample_user_history, MOCK_TAXONOMY, MOCK_WEIGHTS)
    
    # 3. Assert: Programmatically verify expectations
    assert scores["Streetwear"] == 4, f"Expected 4 points, got {scores['Streetwear']}"
    assert scores["Corporate"] == 0, "Corporate points should be zero for this dataset."

def test_empty_user_history():
    scores = calculate_style_scores([], MOCK_TAXONOMY, MOCK_WEIGHTS)
    assert all(value == 0 for value in scores.values()), "Empty profile should yield 0 scores."