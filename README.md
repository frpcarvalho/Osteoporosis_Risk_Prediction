# Osteoporosis Risk Prediction Using Machine Learning

## Overview
A machine learning approach for predicting osteoporosis risk using routine clinical data from the NHANES dataset (2007-2014), without requiring DXA measurements. Our stacking ensemble model combines multiple specialized classifiers to achieve high accuracy in osteoporosis risk assessment.

## Key Features
- **Data Source**: NHANES cycles 2007-2014 (7,924 participants aged 50+)
- **Model Architecture**: Stacking ensemble combining:
  - Gradient Boosting Classifier
  - Random Forest Classifier
  - XGBoost Classifier
  - LightGBM Classifier
  - Logistic Regression Meta-classifier
- **Performance**:
  - Accuracy: 93%
  - AUC: 0.94
  - Cross-validation score: 0.929 (±0.030)

## Top Predictors
1. Age (6.04%)
2. Arm muscle circumference (5.61%)
3. Body weight (5.30%)
4. Gender (3.28%)
5. BMI (2.71%)
6. Calcium intake (2.42%)
7. Folate (2.28%)
8. Height (2.23%)
9. Hand grip strength (2.21%)
10. Alkaline phosphatase (2.16%)

## Project Structure
```
├── preprocessing/
│   ├── reference_values_t_score.ipynb
│   └── data_preparation.ipynb
├── models/
│   ├── pipeline_selector_classifier.ipynb
│   ├── grid_search_phase_1.ipynb
│   └── stacking_ensemble.ipynb
├── evaluation/
│   └── model_evaluation.ipynb
└── utils/
    └── helper_functions.py
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from models.stacking_ensemble import StackingEnsembleCV

# Initialize model
model = StackingEnsembleCV()

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)
```

## Clinical Application
This model is designed for clinical settings where DXA access is limited, providing a cost-effective screening tool for osteoporosis risk assessment. It uses readily available clinical data and can be integrated into existing healthcare systems.

## References
For detailed methodology and results, please refer to our paper: [Link to paper when published]

## Citation
If you use this code in your research, please cite:
```bibtex
@article{carvalho2024enhancing,
  title={Enhancing Osteoporosis Risk Prediction Using Machine Learning: A Holistic Approach Integrating Biomarkers and Clinical Data},
  author={Carvalho, Filipe Ricardo and Gavaia, Paulo Jorge},
  journal={Computers in Biology and Medicine},
  year={2024}
}
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
- Filipe Ricardo Carvalho (frcarvalho@ualg.pt)
- Faculty of Medicine and Biomedical Sciences, University of Algarve, Faro, Portugal
