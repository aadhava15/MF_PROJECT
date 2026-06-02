import pandas as pd
import glob
import os

print("🚀 Data Ingestion Start Aaguthu...\n")

# 1. Load all CSV datasets and print initial stats
print("--- DATASET EXPLORATION ---")
csv_files = glob.glob("data/raw/*.csv")

if not csv_files:
    print("⚠️ data/raw folder-la entha CSV files-um kedaikkala!")
else:
    for file in csv_files:
        filename = os.path.basename(file)
        print(f"\nLoading: {filename}")
        try:
            df = pd.read_csv(file)
            print(f"Shape: {df.shape}")
            print(f"Data Types:\n{df.dtypes.to_dict()}")
            print(f"Head:\n{df.head(2)}\n")
            # Anomaly checking: missing values irukka nu paakka
            missing = df.isnull().sum().sum()
            if missing > 0:
                print(f"⚠️ Anomaly Note: {filename}-la {missing} missing values irukku.")
        except Exception as e:
            print(f"{filename} read pannumbothu error: {e}")

print("\n--- FUND MASTER EXPLORATION ---")
# 2. Explore Fund Master & Validate AMFI Codes
fund_master_path = "data/raw/fund_master.csv"
nav_history_path = "data/raw/live_nav_data.csv" 

if os.path.exists(fund_master_path) and os.path.exists(nav_history_path):
    fund_master = pd.read_csv(fund_master_path)
    nav_history = pd.read_csv(nav_history_path)
    
    try:
        print(f"Unique Fund Houses: {fund_master['fund_house'].nunique()}")
        print(f"Categories: {fund_master['category'].unique()}")
        print(f"Sub-categories: {fund_master['sub_category'].unique()}")
        print(f"Risk Grades: {fund_master['risk_grade'].unique()}")
        
        # 3. AMFI codes validate panna
        master_codes = set(fund_master['scheme_code'].astype(str))
        nav_codes = set(nav_history['scheme_code'].astype(str))
        
        missing_in_nav = master_codes - nav_codes
        
        print("\n--- DATA QUALITY SUMMARY ---")
        if len(missing_in_nav) == 0:
            print("✅ Validation Passed: fund_master-la irukka ella AMFI codes-um nav_history-la irukku.")
        else:
            print(f"⚠️ Validation Failed: fund_master-la irukka {len(missing_in_nav)} codes nav_history-la miss aaguthu.")
            print(f"Sample missing codes: {list(missing_in_nav)[:5]}")
            
    except KeyError as e:
        print(f"Exploration-ku intha column kedaikkala: {e}. Unga CSV column names check pannunga.")
else:
    print("\n⚠️ Master/History validation skip aaguthu: fund_master.csv allathu live_nav_data.csv kedaikkala")