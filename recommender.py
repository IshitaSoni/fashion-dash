import json
import pandas as pd
import re
from style_analyzer import load_user_data, analyze_user_style, STYLE_TAXONOMY

def load_catalog_data(filepath):
    """Loads the master product catalog into a Pandas DataFrame."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def recommend_products(catalog_df, style_profile, top_n=3):
    """
    Scores products in the catalog based on the user's style profile
    and returns the top N recommendations.
    """
    recommendations = []
    
    for _, row in catalog_df.iterrows():
        title = row['title'].lower()
        product_score = 0
        
        matched_styles = set()
        
        # Calculate how well this item matches the user's style layout
        for style, percentage in style_profile.items():
            keywords = STYLE_TAXONOMY[style]
            # If a keyword matches, add points weighted by how much the user likes that style
            for keyword in keywords:
                if re.search(r'\b' + re.escape(keyword) + r'\b', title):
                    matched_styles.add(style)
                    break
        
        for style in matched_styles:
            product_score += style_profile[style]
        
        # Add the computed score to our item metadata
        item_data = row.to_dict()
        item_data['match_score'] = round(product_score, 2)
        recommendations.append(item_data)
        
    # Convert to DataFrame, sort by highest match score, and drop items with 0 match
    rec_df = pd.DataFrame(recommendations)
    rec_df = rec_df[rec_df['match_score'] > 0]
    rec_df = rec_df.sort_values(by='match_score', ascending=False)
    
    return rec_df.head(top_n)

if __name__ == "__main__":
    # 1. Pipeline: Load and analyze user data to fetch their profile
    user_df = load_user_data("data/user_history.json")
    style_profile, dominant_style = analyze_user_style(user_df)
    
    # 2. Ingest the product database catalog
    print("📦 Crawling the master product catalog...")
    catalog_df = load_catalog_data("data/product_catalog.json")
    
    # 3. Predict & Recommend items matching their profile
    print("🔮 Running predictive style matchmaking...")
    top_picks = recommend_products(catalog_df, style_profile, top_n=3)
    
    print("\n🛍️ --- FASHION DASH RECOMMENDATIONS ---")
    print(f"Based on your profile, we curated these top pieces for you:\n")
    
    for i, (_, row) in enumerate(top_picks.iterrows(), 1):
        print(f"{i}. {row['title']} by '{row['brand']}'")
        print(f"   💰 Price: ₹{row['price']} | 🎯 Match Score: {row['match_score']}")
        print("-" * 40)