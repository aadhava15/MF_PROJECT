import pandas as pd

print("Fixing fund_master.csv...")

correct_data = {
    'scheme_code': [125497, 119551, 120503, 118632, 119092, 120841],
    'fund_house': ['HDFC', 'SBI', 'ICICI', 'Nippon', 'Axis', 'Kotak'],
    'category': ['Equity', 'Equity', 'Equity', 'Equity', 'Equity', 'Equity'],
    'sub_category': ['Large Cap', 'Large Cap', 'Large Cap', 'Large Cap', 'Large Cap', 'Large Cap'],
    'risk_grade': ['High', 'High', 'High', 'High', 'High', 'High']
}

# Correct data-va thirumbavum save pandrom
pd.DataFrame(correct_data).to_csv("data/raw/fund_master.csv", index=False)

print("✅ fund_master.csv success-a fix aayiduchu!")