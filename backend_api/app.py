from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# -----------------------------------
# Home Route
# -----------------------------------

@app.route("/")
def home():

    return {
        "message":
        "DarwinAI Oncology API Running"
    }

# -----------------------------------
# Match Endpoint
# -----------------------------------

@app.route("/match", methods=["POST"])
def match_patient():

    data = request.json

    report = data.get(
        "pathology_report",
        ""
    )

    matched = []

    # HER2
    if re.search(
        r"HER2:\s*Positive",
        report,
        re.IGNORECASE
    ):

        matched.append(
            "HER2 Positive"
        )

    # EGFR
    if re.search(
        r"EGFR:\s*Mutated",
        report,
        re.IGNORECASE
    ):

        matched.append(
            "EGFR Mutated"
        )

    # ECOG
    ecog = re.search(
        r"ECOG.*?(\d)",
        report
    )

    ecog_score = (
        ecog.group(1)
        if ecog else None
    )

    # Simple scoring
    score = len(matched) * 40

    if ecog_score == "1":
        score += 20

    score = min(score, 100)

    return jsonify({

        "match_score":
        score,

        "matched_rules":
        matched,

        "ECOG":
        ecog_score
    })

# -----------------------------------
# Run Server
# -----------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
