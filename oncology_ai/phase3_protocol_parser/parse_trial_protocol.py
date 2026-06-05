import re
import json

# -----------------------------------
# Sample Clinical Trial Criteria
# -----------------------------------

trial_protocol = """

INCLUSION CRITERIA:

- HER2 Positive patients only
- ECOG performance status 0-1
- EGFR Mutated
- Age above 18
- Prior chemotherapy allowed

EXCLUSION CRITERIA:

- Severe liver disease
- ECOG above 1

"""

print("===== TRIAL PROTOCOL =====\n")

print(trial_protocol)

# -----------------------------------
# Parse HER2 Requirement
# -----------------------------------

requires_her2 = bool(
    re.search(
        r"HER2 Positive",
        trial_protocol,
        re.IGNORECASE
    )
)

# -----------------------------------
# Parse EGFR Requirement
# -----------------------------------

egfr_required = None

if re.search(
    r"EGFR Mutated",
    trial_protocol,
    re.IGNORECASE
):
    egfr_required = "Mutated"

# -----------------------------------
# Parse ECOG Requirement
# -----------------------------------

ecog_match = re.search(
    r"ECOG.*?(\d)-(\d)",
    trial_protocol,
    re.IGNORECASE
)

max_ecog = None

if ecog_match:
    max_ecog = int(
        ecog_match.group(2)
    )

# -----------------------------------
# Parse Age Requirement
# -----------------------------------

age_match = re.search(
    r"Age above (\d+)",
    trial_protocol,
    re.IGNORECASE
)

min_age = None

if age_match:
    min_age = int(
        age_match.group(1)
    )

# -----------------------------------
# Build Trial Logic JSON
# -----------------------------------

trial_logic = {

    "requires_HER2":
    requires_her2,

    "requires_EGFR":
    egfr_required,

    "max_ECOG":
    max_ecog,

    "minimum_age":
    min_age
}

# -----------------------------------
# Print Structured Logic
# -----------------------------------

print("\n===== STRUCTURED TRIAL LOGIC =====\n")

print(
    json.dumps(
        trial_logic,
        indent=4
    )
)
