import requests
import pandas as pd
import os

# Target directory irukka nu check pannikka
os.makedirs("data/raw", exist_ok=True)

def fetch_nav_data(scheme_code):
    """Oru specific AMFI scheme code-oda historical NAV data-va fetch pannum."""
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and len(data['data']) > 0:
            df = pd.DataFrame(data['data'])
            df['scheme_code'] = scheme_code
            df['fund_house'] = data['meta'].get('fund_house', 'Unknown')
            df['scheme_name'] = data['meta'].get('scheme_name', 'Unknown')
            return df
        else:
            print(f"Scheme {scheme_code}-ku yentha data-vum kedaikkala")
            return None
    else:
        print(f"{scheme_code} fetch panna mudiyala. Status: {response.status_code}")
        return None

# INTHA PART THAAN ROMBA MUKKIYAM (Ithu illana code run aagathu)
if __name__ == "__main__":
    schemes = [125497, 119551, 120503, 118632, 119092, 120841]
    all_nav_data = []
    
    print("API vazhiya data fetch aaguthu, konjam wait pannunga...")
    for code in schemes:
        print(f"AMFI Code {code}-kaga data fetch aaguthu...")
        df = fetch_nav_data(code)
        if df is not None:
            all_nav_data.append(df)
            
    if all_nav_data:
        final_df = pd.concat(all_nav_data, ignore_index=True)
        output_path = "data/raw/live_nav_data.csv"
        final_df.to_csv(output_path, index=False)
        print(f"\n✅ SUPER! NAV data '{output_path}'-la success-a save aayiduchu!")