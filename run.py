#!/usr/bin/env python3
"""
Quick Start Script for Employee Attrition Analysis
This script helps you run the analysis locally
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = {
        'pandas': 'pandas',
        'numpy': 'numpy',
        'sklearn': 'scikit-learn',
        'matplotlib': 'matplotlib',
        'seaborn': 'seaborn',
        'jupyter': 'jupyter'
    }
    
    print("Checking dependencies...\n")
    missing = []
    
    for module, package_name in required_packages.items():
        try:
            __import__(module)
            print(f"✓ {package_name} installed")
        except ImportError:
            print(f"✗ {package_name} NOT installed")
            missing.append(package_name)
    
    if missing:
        print(f"\nMissing packages: {', '.join(missing)}")
        print("\nRun this command to install:")
        print(f"pip install {' '.join(missing)}")
        return False
    
    print("\n✓ All dependencies installed!")
    return True

def check_dataset():
    """Check if dataset exists"""
    csv_files = [
        'WA_Fn-UseC_-HR-Employee-Attrition.csv',
        'HR_Attrition.csv'
    ]
    
    print("\nChecking for dataset...\n")
    
    for csv_file in csv_files:
        if os.path.exists(csv_file):
            print(f"✓ Found: {csv_file}")
            return True
    
    print("✗ Dataset NOT found!")
    print("\nTo download the dataset:")
    print("1. Go to: https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset")
    print("2. Download: WA_Fn-UseC_-HR-Employee-Attrition.csv")
    print("3. Place it in this folder")
    return False

def run_notebook():
    """Launch Jupyter notebook"""
    print("\n" + "="*80)
    print("Launching Jupyter Notebook...")
    print("="*80 + "\n")
    
    try:
        subprocess.run(['jupyter', 'notebook', 'analysis.ipynb'])
    except FileNotFoundError:
        print("Jupyter not found. Run: pip install jupyter")
        sys.exit(1)

def run_colab_instructions():
    """Print instructions for Google Colab"""
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                    RUNNING IN GOOGLE COLAB (RECOMMENDED)                   ║
╚════════════════════════════════════════════════════════════════════════════╝

Google Colab is easier and requires no installation! Here's how:

1. Go to: https://colab.research.google.com
2. Click "File" → "Open notebook" → "GitHub"
3. Or upload the analysis.ipynb file directly
4. Upload the CSV dataset to Colab:
   - In the first cell, add:
     from google.colab import files
     files.upload()
5. Run all cells!

Benefits of Colab:
✓ Free GPU/TPU access
✓ No setup required
✓ Automatic visualization display
✓ Easy to share results

For more info: https://colab.research.google.com
    """)

def main():
    """Main execution"""
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║          EMPLOYEE ATTRITION PREDICTION - QUICK START                       ║
║                     Analyst: Balla Prem Kumar                              ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Check dependencies
    deps_ok = check_dependencies()
    
    # Check dataset
    dataset_ok = check_dataset()
    
    if not dataset_ok:
        print("\n" + "="*80)
        run_colab_instructions()
        sys.exit(1)
    
    if deps_ok and dataset_ok:
        print("\n" + "="*80)
        print("✓ All requirements met!")
        print("="*80)
        
        print("\nOptions:")
        print("1. Run locally with Jupyter (type: python run.py)")
        print("2. Run in Google Colab (recommended)")
        print("3. View README for more information")
        
        response = input("\nRun Jupyter locally? (y/n): ").strip().lower()
        if response == 'y':
            run_notebook()
        else:
            run_colab_instructions()

if __name__ == "__main__":
    main()
