import json

# -----------------------------------
# Sample Patient JSON
# -----------------------------------

patient = {

    "HER2_Status":
    "Positive",

    "EGFR_Status":
    "Mutated",

    "ECOG_Score":
    1,

    "Age":
    58
}

# -----------------------------------
# Sample Trial Logic
# -----------------------------------

trial = {

    "requires_HER2":
    True,

    "requires_EGFR":
    "Mutated",

    "max_ECOG":
    1,

    "minimum_age":
    18
}

print("===== PATIENT =====\n")

print(
    json.dumps(
        patient,
        indent=4
    )
)

print("\n===== TRIAL =====\n")

print(
    json.dumps(
        trial,
        indent=4
    )
)

# -----------------------------------
# Matching Engine
# -----------------------------------

score = 0

max_score = 4

reasons = []

# HER2 Match

if (
    trial["requires_HER2"]
    and patient["HER2_Status"]
    == "Positive"
):

    score += 1

    reasons.append(
        "HER2 requirement matched"
    )

# EGFR Match

if (
    patient["EGFR_Status"]
    == trial["requires_EGFR"]
):

    score += 1

    reasons.append(
        "EGFR mutation matched"
    )

# ECOG Match

if (
    patient["ECOG_Score"]
    <= trial["max_ECOG"]
):

    score += 1

    reasons.append(
        "ECOG eligible"
    )

# Age Match

if (
    patient["Age"]
    >= trial["minimum_age"]
):

    score += 1

    reasons.append(
        "Age eligible"
    )

# -----------------------------------
# Final Match %
# -----------------------------------

match_score = int(
    (score / max_score) * 100
)

# -----------------------------------
# Final Output
# -----------------------------------

result = {

    "match_score":
    match_score,

    "matched_rules":
    reasons
}

print("\n===== MATCH RESULT =====\n")

print(
    json.dumps(
        result,
        indent=4
    )
)
