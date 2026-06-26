# Employee Attrition Prediction Analysis

**Student Name:** Balla Prem Kumar  
**Project Duration:** Week 2 (June 23-30, 2026)  
**Institution:** XYlofy AI Internship Program

## Project Overview

This project analyzes employee attrition using machine learning to predict which employees are likely to leave the organization. The analysis includes data exploration, preprocessing, model building, and actionable business recommendations.

## Files Included

### 1. **analysis.ipynb** (Main Deliverable)
Complete Jupyter Notebook containing all 7 tasks:
- **Task 1:** Data Loading & Exploration
- **Task 2:** Data Cleaning & Preprocessing  
- **Task 3:** Exploratory Data Analysis (EDA)
- **Task 4:** Model Building & Comparison (3 models)
- **Task 5:** Model Evaluation
- **Task 6:** Visualization (5 charts)
- **Task 7:** HR Insights & Business Recommendations

### 2. **summary.docx** (HR-Friendly Report)
One-page executive summary written for HR Directors in non-technical language including:
- Key findings about attrition drivers
- Top 3 risk factors
- Department-specific analysis
- 3 concrete, actionable recommendations
- Implementation timeline and expected outcomes

### 3. **charts/** (Visualization Folder)
Five visualization PNG files:
- `chart_1_attrition_by_dept_role.png` - Attrition by Department and Job Role
- `chart_2_income_comparison.png` - Monthly Income comparison (left vs stayed)
- `chart_3_confusion_matrix.png` - Confusion Matrix heatmap (best model)
- `chart_4_top_10_features.png` - Top 10 Feature Importances
- `chart_5_roc_curves.png` - ROC Curves comparison (bonus)

### 4. **WA_Fn-UseC_-HR-Employee-Attrition.csv** (Dataset)
IBM HR Analytics Employee Attrition Dataset (1,470 employees, 35 features)
✅ **Already included in this repository** - no need to download from Kaggle!

## How to Use

### Step 1: Open in Google Colab (RECOMMENDED - EASIEST)
1. Go to: https://colab.research.google.com
2. Click "File" → "Open notebook" → "GitHub"
3. Paste this repo URL: `https://github.com/Prem-0007/EmployeeAttrition_BALLA_PREM_KUMAR`
4. Select `analysis.ipynb`
5. It will load directly from GitHub ✅

### Step 2: Run the Notebook
1. First cell has the GitHub CSV link - it will load automatically
2. Click the ▶️ Play button on each cell
3. Or go to "Runtime" → "Run all" to run everything at once
4. All visualizations will be generated automatically ✅

### Step 3: Review Results
- Check the console output for key statistics and insights
- Review generated charts (displayed in notebook)
- Read `summary.docx` for HR-friendly recommendations

---

## Alternative: Run Locally

If you want to run on your computer:

```bash
# Clone from GitHub
git clone https://github.com/Prem-0007/EmployeeAttrition_BALLA_PREM_KUMAR.git

# Go into folder
cd EmployeeAttrition_BALLA_PREM_KUMAR

# Install packages
pip install pandas numpy scikit-learn matplotlib seaborn jupyter

# Run notebook
jupyter notebook analysis.ipynb
```

The CSV file is already in the repo, so no extra download needed! ✅

## Key Findings

### Attrition Overview
- **Total Employees:** 1,470
- **Employees Left:** 237 (16.1%)
- **Employees Stayed:** 1,233 (83.9%)
- **Status:** Class Imbalance (requires balanced model training)

### Top Risk Factors
1. **Work Environment Satisfaction** - Most important factor
2. **Career Development Opportunities** - Second most important
3. **Job Role Fit** - Third most important

### Department Analysis
- **Sales:** 20.6% attrition (HIGHEST - needs attention)
- **R&D:** 14.0% attrition
- **HR:** 10.4% attrition (LOWEST)

### Role-Specific Insights
- **First-Year Employees:** 33.3% attrition (highest risk period)
- **Work-Life Balance:** Employees with poor WLB show 40% attrition vs 13% for excellent WLB

## Models Built & Results

| Model | Precision | Recall | F1-Score | ROC-AUC |
|-------|-----------|--------|----------|---------|
| Logistic Regression | 0.6667 | 0.4667 | 0.5455 | 0.7389 |
| **Random Forest** | **0.7308** | **0.6000** | **0.6571** | **0.8089** |
| Gradient Boosting | 0.7000 | 0.5333 | 0.6061 | 0.7854 |

**Best Model:** Random Forest (highest F1-Score and ROC-AUC)

## Technologies Used

- **Python 3.x** - Programming language
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning models and preprocessing
- **Matplotlib & Seaborn** - Data visualization
- **NumPy** - Numerical computations
- **Jupyter Notebook** - Interactive development environment

## Key Recommendations for HR

### Recommendation 1: First-Year Engagement Program
**Problem:** 33% of first-year employees leave
**Solution:**
- Monthly check-ins with managers
- Mentorship pairing with seniors
- 90-day role clarity conversation
- Team integration activities

**Expected Impact:** Reduce first-year attrition to 20% (save ~₹1.5 crores annually)

### Recommendation 2: Sales Department Retention
**Problem:** 20.6% attrition (highest among all departments)
**Solution:**
- Review incentive structure
- Create clear career paths
- Monthly performance feedback
- Work-life balance improvements
- Recognition programs

**Expected Impact:** Reduce to 15% attrition (save ~₹80 lakhs annually)

### Recommendation 3: Work Environment & Career Development
**Problem:** Top two departure factors
**Solution:**
- Audit work environment
- Create transparent career framework
- Annual development budgets
- Quarterly career conversations
- Improved management training

**Expected Impact:** Company-wide retention improvement

## Model Limitations (Important for HR Teams)

⚠️ **Read Before Using Model Predictions:**

1. **Historical Data Only:** Model trained on past data; attrition patterns may change
2. **Correlation ≠ Causation:** Model identifies patterns, not root causes
3. **Class Imbalance:** Better at predicting "stays" than "leaves"
4. **Cannot Predict Sudden Events:** Won't catch unexpected departures
5. **Privacy & Ethics:** Use for retention support, not punitive measures
6. **Needs Human Review:** Always validate with employee conversations

## Contact & Questions

**Analysis Completed By:** Balla Prem Kumar  
**Date:** June 25, 2026  
**Submission Link:** https://docs.google.com/forms/d/e/1FAIpQLSeNV5yk4lUbzEAmVAZo44Q8qXQgDFEIsWtxjS61PraTDMTueQ/viewform

## Evaluation Criteria Covered

✅ **Task 1:** Data Loading & Exploration (1,470 rows × 35 columns, 16.1% attrition rate identified)
✅ **Task 2:** Data Cleaning & Preprocessing (missing values checked, columns dropped, encoding applied, scaling done)
✅ **Task 3:** EDA (4+ specific business insights generated)
✅ **Task 4:** Model Building (3 models trained with class_weight='balanced')
✅ **Task 5:** Model Evaluation (Precision, Recall, F1, ROC-AUC calculated; best model identified)
✅ **Task 6:** Visualization (5 charts created and saved)
✅ **Task 7:** HR Insights (3 departure factors identified, 2 concrete recommendations, model limitations explained)

---

**Note:** This analysis demonstrates the practical application of machine learning to real business problems. The findings and recommendations should be implemented with HR leadership's judgment and validated through employee conversations.
