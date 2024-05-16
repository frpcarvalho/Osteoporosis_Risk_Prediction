Osteoporosis Prediction Model

Osteoporosis, characterized by decreased bone mineral density and compromised bone structure, affects approximately 18% worldwide, with osteoporosis-associated fractures impacting up to 37 million people annually. Despite the World Health Organization's recommendation of dual-energy X-ray absorptiometry (DXA) for bone mineral density assessment, limitations such as availability, radiation exposure, and the inability to detect fracture risk in patients with subclinical conditions persist.

Artificial intelligence has emerged as a promising solution in various medical fields, including orthopedics. However, there remains a need for a reliable, cost-effective, and practical tool for osteoporosis prediction.

Objective

Our aim was to develop a machine learning model to predict osteoporosis using patient data such as biomarkers and clinical history, eliminating the need for additional diagnostic exams, simplifying the process, and improving accessibility for clinicians.

Methodology

We conducted a pipeline of different algorithm combinations and identified Gradient Boosting as the most effective estimator and classifier. Unlike previous models that relied on BMD and T-scores features, our approach utilizes biomarkers and historical clinical data.

Results

The model achieved 90% accuracy, an AUC of 92%, and a mean cross-validation score of 91%. Quantification of feature importance revealed Magnesium, Coronary Artery Disease, fracture, Hypertension, Chronic Obstructive Pulmonary Disease, and the ratio of high-density lipoprotein cholesterol with alanine aminotransferase and blood urea nitrogen to uric acid as influential factors.

Availability

The code and model were developed in Python utilizing major machine learning libraries and are openly available on GitHub. This accessibility ensures seamless integration into existing hospital software systems.

Conclusion

Our research underscores the importance of incorporating traditional risk factors and novel biomarkers in health risk assessment. This approach holds potential to introduce innovative forecasting methods for osteoporosis, gradually superseding established strategies like FRAX.
