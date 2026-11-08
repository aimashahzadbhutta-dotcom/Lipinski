Lipinski – Drug Candidate Screening

Overview

This project explores a basic computational approach to drug candidate screening using Python. Inspired by the principles of Lipinski's Rule of Five, it evaluates a small dataset of compounds against four predefined criteria: molecular weight, solubility, toxicity, and biological activity.

The objective is to demonstrate how simple rule-based screening can be used to organize compound data, assess multiple properties simultaneously, and identify promising candidates for further investigation.

Project Objectives

- Evaluate compounds using predefined physicochemical and biological criteria.
- Apply data manipulation techniques to pharmaceutical-related datasets.
- Implement rule-based classification using Python.
- Identify compounds that satisfy all four screening conditions.
- Develop a foundation for more advanced computational drug discovery workflows.

Screening Criteria

Each compound is evaluated against the following conditions:

Parameter| Screening Criterion
Molecular Weight| Less than 500
Solubility| Greater than 0.4
Toxicity| Less than 0.3
Biological Activity| Greater than 0.6

Each satisfied condition contributes one point to the compound's screening score.

Classification System

Compounds are classified according to their total screening score:

Conditions Passed| Classification
4| Excellent Candidate
3| Good Candidate
2| Weak Candidate
0–1| Rejected

The program also extracts compounds classified as excellent candidates and displays their toxicity and biological activity values.

Technologies Used

- Python – Core programming language.
- Pandas – Dataset creation, manipulation, and analysis.
- NumPy – Numerical operations and conditional classification.

Project Structure

Lipinski/
│
├── lipinski.py
└── README.md

How to Run

1. Clone the repository:

git clone <https://github.com/aimashahzadbhutta-dotcom/Lipinski>

2. Navigate to the project directory:

cd Lipinski

3. Install the required libraries:

pip install pandas numpy

4. Execute the Python script:

python lipinski.py

Dataset

The project uses a small, manually defined dataset containing six hypothetical compounds. Each compound is assigned values for molecular weight, solubility, toxicity, and biological activity.

The dataset is intended for demonstrating the screening methodology and does not represent experimentally validated pharmaceutical compounds.

Scientific Considerations

Although inspired by Lipinski's Rule of Five, this implementation is a simplified screening model rather than a complete application of the original rule.

Lipinski's Rule of Five primarily considers molecular weight, lipophilicity (LogP), hydrogen bond donors, and hydrogen bond acceptors to assess the likelihood of favorable oral drug absorption.

The additional solubility, toxicity, and biological activity thresholds used here are independent screening criteria selected for this project.

The classifications should therefore be interpreted as preliminary computational assessments, not evidence of drug efficacy, safety, or clinical suitability.

Future Improvements

- Incorporate real compound datasets from publicly available chemical databases.
- Include molecular descriptors such as LogP and hydrogen bond donors and acceptors.
- Introduce molecular structure analysis using RDKit.
- Expand the screening process with additional drug-likeness properties.
- Develop data visualizations to compare compound characteristics.

Author's Note

This project represents an introductory step toward understanding how computational methods can support early-stage drug discovery. It focuses on translating compound properties into structured data and applying logical screening criteria to make the evaluation process more systematic.