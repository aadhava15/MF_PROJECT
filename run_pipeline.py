import os
import subprocess

def run_script(script_name):
    print(f"🚀 Running {script_name}...")
    try:
        subprocess.run(["python", script_name], check=True)
        print(f"✅ {script_name} completed successfully.\n")
    except Exception as e:
        print(f"❌ Error in {script_name}: {e}")

if __name__ == "__main__":
    print("=== Bluestock MF Analytics Pipeline Execution ===\n")
    
    # Run aaga vendiya scripts list
    scripts = [
        "etl_process.py",       
        "risk_analytics.py",     
        "recommender.py"        
    ]
    
    for s in scripts:
        if os.path.exists(s):
            run_script(s)
        else:
            print(f"⚠️ Warning: {s} not found, skipping...")

    print("🎯 All analytics tasks are ready for Power BI consumption!")