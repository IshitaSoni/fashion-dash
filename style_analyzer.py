import json
import pandas as pd
import re

# 1. Configuration Constants
STYLE_TAXONOMY = {
    "Streetwear": ["oversized", "hoodie", "cargo", "pants", "sneakers", "sweatshirt", "joggers", "skate", "baggy"],
    "Corporate Chic": ["blazer", "formal", "trousers", "shirt", "pinstripe", "office", "button-down", "pleated", "khaki"],
    "Cottagecore / Boho": ["floral", "summer", "maxi", "dress", "print", "sundress", "pastel", "ruffle", "linen", "midi", "wrap"],
    "Edgy / Grunge": ["leather", "combat", "boots", "jacket", "moto", "studded", "faux", "platform", "chunky", "black"]
}

ACTION_WEIGHTS = {
    "bought": 3,
    "cart": 2,
    "wishlist": 1
}

# ==========================================================
# 🧪 PURE LOGIC FUNCTION (100% Testable, No File I/O)
# ==========================================================
def calculate_style_scores(items_list, taxonomy, weights):
    """
    Pure Function: Takes a raw list of dictionaries, matches keywords,
    applies weights, and returns the raw point distribution.
    """
    style_scores = {style: 0 for style in taxonomy.keys()}
    
    for item in items_list:
        title = item.get('title', '').lower()
        status = item.get('status', 'wishlist')
        weight = weights.get(status, 1)
        
        matched_styles = set()
        
        for style, keywords in taxonomy.items():
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', title):
                    matched_styles.add(style)
                    break
        
        for style in matched_styles:
            style_scores[style] += weight
                    
    return style_scores


# ==========================================================
# 📥 DATA INGESTION & FORMATTING WRAPPER
# ==========================================================
def load_user_data(filepath):
    """Loads user history from disk into a Pandas DataFrame."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def analyze_user_style(df):
    """
    Acts as the interface for the rest of the application.
    Converts DataFrame to records, runs pure logic, and profiles percentages.
    """
    # Convert DataFrame back to a list of dicts to feed the pure function
    items_list = df.to_dict(orient='records')
    
    # Call our pure function
    style_scores = calculate_style_scores(items_list, STYLE_TAXONOMY, ACTION_WEIGHTS)
        
    total_score = sum(style_scores.values())
    if total_score == 0:
        return {style: 0.0 for style in STYLE_TAXONOMY.keys()}, "Undecided"
        
    style_percentages = {style: round((score / total_score) * 100, 2) for style, score in style_scores.items()}
    dominant_style = max(style_scores, key=style_scores.get)
    
    return style_percentages, dominant_style


# ==========================================================
# 🖥️ LOCAL TESTING BLOCK
# ==========================================================
if __name__ == "__main__":
    user_history_path = "data/user_history.json"
    
    print("🔄 Loading data via wrapper...")
    df_user = load_user_data(user_history_path)
    
    print("🧠 Processing style profiles...")
    style_profile, dominant = analyze_user_style(df_user)
    
    print("\n📊 --- TERMINAL VISUAL CHECK ---")
    print(f"Dominant Vibe: {dominant}")
    for style, percentage in style_profile.items():
        print(f" - {style}: {percentage}%")