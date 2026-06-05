import random
import pandas as pd
from faker import Faker

fake = Faker()

# -----------------------------------
# Oncology Data Pools
# -----------------------------------

cancers = [
    "Non-Small Cell Lung Cancer",
    "Breast Cancer",
    "Colorectal Cancer",
    "Melanoma",
    "Pancreatic Adenocarcinoma"
]

tnm_stages = [
    "T1N0M0",
    "T2N1M0",
    "T3N2M0",
    "T4N3M1"
]

ecog_scores = [0, 1, 2, 3]

her2_status = [
    "Positive",
    "Negative"
]

egfr_status = [
    "Mutated",
    "Wild Type"
]

pdl1_levels = [
    "<1%",
    "1-49%",
    ">=50%"
]

alk_status = [
    "Rearranged",
    "Negative"
]

kras_status = [
    "G12C",
    "Wild Type"
]

treatments = [
    "Carboplatin",
    "Paclitaxel",
    "Pembrolizumab",
    "Radiation Therapy",
    "Trastuzumab",
    "Osimertinib",
    "FOLFOX",
    "Nivolumab"
]

symptoms = [
    "fatigue",
    "weight loss",
    "dyspnea",
    "persistent cough",
    "bone pain",
    "nausea"
]

# -----------------------------------
# Generate Synthetic Patient
# -----------------------------------

def generate_patient():

    age = random.randint(35, 85)

    sex = random.choice([
        "Male",
        "Female"
    ])

    cancer = random.choice(cancers)

    tnm = random.choice(tnm_stages)

    ecog = random.choice(ecog_scores)

    her2 = random.choice(her2_status)

    egfr = random.choice(egfr_status)

    pdl1 = random.choice(pdl1_levels)

    alk = random.choice(alk_status)

    kras = random.choice(kras_status)

    prior_tx = random.sample(
        treatments,
        k=2
    )

    symptom = random.choice(symptoms)

    patient_name = fake.name()

    pathology_report = f"""
    PATIENT: {patient_name}

    AGE: {age}

    SEX: {sex}

    PATHOLOGY REPORT:

    Patient diagnosed with
    {cancer}.

    TNM staging demonstrates
    {tnm}.

    ECOG performance status:
    {ecog}

    Biomarker Testing:

    HER2: {her2}

    EGFR: {egfr}

    PD-L1 Expression:
    {pdl1}

    ALK: {alk}

    KRAS: {kras}

    Clinical symptoms include
    {symptom}.

    Prior therapies administered:
    - {prior_tx[0]}
    - {prior_tx[1]}

    Impression:
    Advanced oncologic disease
    requiring systemic therapy
    evaluation.
    """

    clinical_note = f"""
    ONCOLOGY FOLLOW-UP NOTE:

    {patient_name} is a
    {age}-year-old {sex.lower()}

    with history of
    {cancer}.

    ECOG score remains
    {ecog}.

    Patient reports
    {symptom}.

    Molecular profiling confirms:

    HER2 {her2}

    EGFR {egfr}

    PD-L1 {pdl1}

    ALK {alk}

    KRAS {kras}

    Prior treatment exposure:
    {prior_tx[0]}
    and
    {prior_tx[1]}.

    Plan:
    Evaluate eligibility
    for targeted therapy
    and immunotherapy
    clinical trials.
    """

    return {

        "patient_name": patient_name,

        "age": age,

        "sex": sex,

        "cancer_type": cancer,

        "tnm_stage": tnm,

        "ecog": ecog,

        "HER2": her2,

        "EGFR": egfr,

        "PDL1": pdl1,

        "ALK": alk,

        "KRAS": kras,

        "prior_treatments": prior_tx,

        "pathology_report":
        pathology_report.strip(),

        "clinical_note":
        clinical_note.strip()
    }

# -----------------------------------
# Generate Dataset
# -----------------------------------

def generate_dataset(
    num_patients=25
):

    records = []

    for _ in range(num_patients):

        patient = generate_patient()

        records.append(patient)

    return pd.DataFrame(records)

# -----------------------------------
# Main
# -----------------------------------

if __name__ == "__main__":

    df = generate_dataset(
        num_patients=10
    )

    print(df[[
        "patient_name",
        "cancer_type",
        "tnm_stage",
        "ecog"
    ]])

    # Save CSV
    df.to_csv(
        "synthetic_oncology_patients.csv",
        index=False
    )

    print("\n====================")
    print("SAMPLE REPORT")
    print("====================\n")

    print(
        df.iloc[0][
            "pathology_report"
        ]
    )

    print(
        "\n✅ CSV GENERATED"
    )
