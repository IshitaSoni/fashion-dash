import sys
from style_analyzer import load_user_data, analyze_user_style
from recommender import load_catalog_data, recommend_products

def run_fashion_dash_pipeline():
    print("🚀 --- STARTING FASHION DASH PIPELINE --- 🚀\n")
    
    # Define file paths
    USER_DATA_PATH = "data/user_history.json"
    CATALOG_DATA_PATH = "data/product_catalog.json"
    
    # Step 1: Ingest and clean user data
    try:
        print("📥 Step 1: Aggregating user data streams...")
        user_df = load_user_data(USER_DATA_PATH)
        print(f"✅ Successfully ingested {len(user_df)} user interactions.\n")
    except FileNotFoundError:
        print("❌ Error: 'user_history.json' not found. Please run your mock data generator first.")
        sys.exit(1)
        
    # Step 2: Run the style categorization analytics
    print("🧠 Step 2: Analyzing fashion archetypes & action weights...")
    style_profile, dominant_style = analyze_user_style(user_df)
    
    print("\n📊 --- USER STYLE PROFILE REPORT ---")
    print(f"👑 Dominant Vibe: {dominant_style}")
    sorted_profile = sorted(style_profile.items(), key=lambda x: x[1], reverse=True)
    for style, percentage in style_profile.items():
        print(f"   • {style}: {percentage}%")
    print("------------------------------------\n")
    
    # Step 3: Predictive Recommendation
    try:
        print("📦 Step 3: Crawling product catalogs...")
        catalog_df = load_catalog_data(CATALOG_DATA_PATH)
        
        print("🔮 Predicting top product affinity scores...")
        top_picks = recommend_products(catalog_df, style_profile, top_n=3)
        
        print("\n🛍️ --- CURATED PERSONAL FEED ---")
        for i, (_, row) in enumerate(top_picks.iterrows(), 1):
            print(f"{i}. {row['title']} ({row['brand']})")
            print(f"   Price: ₹{row['price']} | Match Score: {row['match_score']}%")
            print("   " + "-" * 35)
            
    except FileNotFoundError:
        print("❌ Error: 'product_catalog.json' not found.")
        sys.exit(1)

    print("\n🏁 --- PIPELINE EXECUTION COMPLETE --- 🏁")

if __name__ == "__main__":
    run_fashion_dash_pipeline()