import json
import pandas as pd

STYLE_TAXONOMY = {
    "Streetwear": ["oversized", "hoodie", "cargo", "pants", "sneakers", "sweatshirt", "joggers", "skate", "baggy"],
    "Corporate Chic": ["blazer", "formal", "trousers", "shirt", "pinstripe", "office", "button-down", "pleated", "khaki"],
    "Cottagecore / Boho": ["floral", "summer", "maxi", "dress", "print", "sundress", "pastel", "ruffle", "linen", "midi", "wrap"],
    "Edgy / Grunge": ["leather", "combat", "boots", "jacket", "moto", "studded", "faux", "platform", "chunky", "black"]
}

# 2. Define Action Weights (Intent-based Scoring)
ACTION_WEIGHTS = {
    "bought": 3,
    "cart": 2,
    "wishlist": 1
}

def load_user_data(filepath):
    """Loads user history and converts it into a clean Pandas DataFrame."""
    with open(filepath, 'r') as f:
        data = json.load(f)     
    return pd.DataFrame(data)

def analyze_user_style(df):
    """Analyzes item titles against keywords to calculate a weighted style profile."""
    # Initialize a dictionary to hold scores for each style archetype
    style_scores = {style: 0 for style in STYLE_TAXONOMY.keys()}

    # Process every item in the user's history
    for _, row in df.iterrows():
        title = row['title'].lower()
        status = row['status']
        weight = ACTION_WEIGHTS.get(status, 1) # Default weight to 1 if status is unknown
        
        # Check title against keywords for each archetype
        for style, keywords in STYLE_TAXONOMY.items():
            for keyword in keywords:
                if keyword in title:
                    # Score = Number of keyword matches * behavioral weight of the action
                    style_scores[style] += weight

    # Calculate percentages for a cleaner output
    total_score = sum(style_scores.values())
    if total_score == 0:
        return style_scores, "Undecided"
    
    style_percentages = {style: round((score / total_score) * 100, 2) for style, score in style_scores.items()}

    # Determine dominant style
    dominant_style = max(style_scores, key=style_scores.get)

    return style_percentages, dominant_style

if __name__ == "__main__":
    # Test the script locally
    user_history_path = "data/user_history.json"
    
    print("🔄 Loading user data stream...")
    df_user = load_user_data(user_history_path)
    
    print("🧠 Analyzing text patterns and intent weights...")
    style_profile, dominant = analyze_user_style(df_user)
    
    print("\n📊 --- FASHION DASH STYLE REPORT ---")
    print(f"Dominant Aesthetic: ✨ {dominant} ✨\n")
    print("Full Breakdown:")
    for style, percentage in style_profile.items():
        print(f" - {style}: {percentage}%")
    print("------------------------------------\n")