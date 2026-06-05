import pandas as pd
import re
import json

# Load dataset
df = pd.read_csv(
    "synthetic_oncology_patients.csv"
)

# Select first report
report = df.iloc[0]["pathology_report"]

print("===== PATHOLOGY REPORT =====")
print(report)

# Extract TNM Stage
tnm = re.search(
    r"T\dN\dM\d",
    report
)

# Extract ECOG
ecog = re.search(
    r"ECOG.*?(\d)",
    report
)

# Extract HER2
her2 = re.search(
    r"HER2:\s*(Positive|Negative)",
    report
)

# Extract EGFR
egfr = re.search(
    r"EGFR:\s*(Mutated|Wild Type)",
    report
)

# Extract Treatments
treatments = []

possible_treatments = [
    "chemotherapy",
    "radiation",
    "immunotherapy",
    "trastuzumab",
    "osimertinib"
]

report_lower = report.lower()

for treatment in possible_treatments:
    if treatment in report_lower:
        treatments.append(treatment)

# Build structured JSON
patient_json = {

    "TNM_Stage":
    tnm.group() if tnm else None,

    "ECOG_Score":
    ecog.group(1) if ecog else None,

    "HER2_Status":
    her2.group(1) if her2 else None,

    "EGFR_Status":
    egfr.group(1) if egfr else None,

    "Prior_Treatments":
    treatments
}

print("\n===== STRUCTURED PATIENT JSON =====")

print(
    json.dumps(
        patient_json,
        indent=4
    )
)
