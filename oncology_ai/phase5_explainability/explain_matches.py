import json
import re

# -----------------------------------
# Sample Pathology Report
# -----------------------------------

report = """

Patient diagnosed with
Breast Cancer.

TNM staging demonstrates
T2N1M0.

ECOG performance status:
1

HER2: Positive

EGFR: Mutated

Prior chemotherapy administered.

"""

print("===== PATHOLOGY REPORT =====\n")

print(report)

# -----------------------------------
# Match Evidence Extraction
# -----------------------------------

matched_text = []

# HER2 Evidence

her2_match = re.search(
    r"HER2:\s*Positive",
    report,
    re.IGNORECASE
)

if her2_match:

    matched_text.append(
        her2_match.group()
    )

# EGFR Evidence

egfr_match = re.search(
    r"EGFR:\s*Mutated",
    report,
    re.IGNORECASE
)

if egfr_match:

    matched_text.append(
        egfr_match.group()
    )

# ECOG Evidence

ecog_match = re.search(
    r"ECOG.*?(\d)",
    report,
    re.IGNORECASE
)

if ecog_match:

    matched_text.append(
        f"ECOG performance status: {ecog_match.group(1)}"
    )

# TNM Evidence

tnm_match = re.search(
    r"T\dN\dM\d",
    report
)

if tnm_match:

    matched_text.append(
        f"TNM Stage: {tnm_match.group()}"
    )

# -----------------------------------
# Final Explainability Output
# -----------------------------------

explanation = {

    "match_score":
    100,

    "matched_evidence":
    matched_text
}

print("\n===== EXPLAINABILITY RESULT =====\n")

print(
    json.dumps(
        explanation,
        indent=4
    )
)
