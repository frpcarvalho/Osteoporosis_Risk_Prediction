# Osteoporosis Risk Prediction Model

A stacking ensemble model for predicting osteoporosis risk using routine clinical data, developed using NHANES 2007-2014 dataset.

## Model Performance
- Accuracy: 93%
- AUC: 0.94
- Cross-validation Score: 0.929 (±0.030)

## Requirements
```bash
pip install -r requirements.txt
```

## Quick Start
```python
from src.predict import load_model, predict_osteoporosis_risk
import pandas as pd

# Load model
model = load_model()

# Load your data
data = pd.read_csv("your_data.csv")

# Make predictions
predictions, probabilities = predict_osteoporosis_risk(model, data)
```

The model requires the following features (listed by importance):

Age (DEMO_RIDAGEYR) - 6.04%
Arm Muscle Circumference (BMX_BMXARMC) - 5.61%
Body Weight (BMX_BMXWT) - 5.30%
Gender (DEMO_RIAGENDR) - 3.28%
Body Mass Index (BMI) - 2.71%
Calcium Intake (DR1TOT_DR1TCALC) - 2.42%
Folate (FOLFMS_LBDFOTSI) - 2.28%
Height (BMX_BMXHT) - 2.23%
Hand Grip Strength (MGX_MGXH2T1) - 2.21%
Alkaline Phosphatase (BIOPRO_LBXSAPSI) - 2.16%
Physical Activity Metrics (PAXDAY_PAXSSNDP) - 2.14%
Meal Timing (DR1IFF_H_DR1_020) - 2.14%
Total Saturated Fatty Acids (DR1TOT_DR1TSFAT) - 2.09%
Estradiol Levels (TST_LBXEST) - 1.95%
Previous Year Weight (WHQ_WHD050) - 1.90%

## Model Details
- Architecture: Stacking Ensemble
- Base Models: 
  - Gradient Boosting
  - Random Forest
  - XGBoost
  - LightGBM
- Meta-classifier: Logistic Regression

## Citation
If you use this model in your research, please cite:
```bibtex
@article{carvalho2024enhancing,
  title={Enhancing Osteoporosis Risk Prediction Using Machine Learning: A Holistic Approach Integrating Biomarkers and Clinical Data},
  author={Carvalho, Filipe Ricardo and Gavaia, Paulo Jorge},
  journal={Computers in Biology and Medicine},
  year={2024}
}
```

