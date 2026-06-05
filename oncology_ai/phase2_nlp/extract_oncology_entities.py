import pandas as pd
import re
import json

# Load oncology dataset
df = pd.read_csv(
    "../data/synthetic_oncology_patients.csv"
)

# Select first pathology report
report = df.iloc[0]["pathology_report"]

print("===== PATHOLOGY REPORT =====\n")
print(report)

# -----------------------------------
# Extract TNM Stage
# -----------------------------------

tnm = re.search(
    r"T\dN\dM\d",
    report
)

# -----------------------------------
# Extract ECOG Score
# -----------------------------------

ecog = re.search(
    r"ECOG.*?(\d)",
    report
)

# -----------------------------------
# Extract HER2 Status
# -----------------------------------

her2 = re.search(
    r"HER2:\s*(Positive|Negative)",
    report
)

# -----------------------------------
# Extract EGFR Status
# -----------------------------------

egfr = re.search(
    r"EGFR:\s*(Mutated|Wild Type)",
    report
)

# -----------------------------------
# Extract Prior Treatments
# -----------------------------------

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

        treatments.append(
            treatment
        )

# -----------------------------------
# Create Structured JSON
# -----------------------------------

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

# -----------------------------------
# Print Structured Data
# -----------------------------------

print("\n===== STRUCTURED PATIENT JSON =====\n")

print(
    json.dumps(
        patient_json,
        indent=4
    )
)
