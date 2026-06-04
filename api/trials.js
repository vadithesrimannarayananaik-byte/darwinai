export default async function handler(req, res) {
  const disease = req.query.disease || "diabetes";

  try {
    const url = `https://clinicaltrials.gov/api/v2/studies?query.term=${encodeURIComponent(disease)}&pageSize=5`;

    const response = await fetch(url, {
      method: "GET",
      headers: {
        "accept": "application/json"
      }
    });

    // Check if response is OK
    if (!response.ok) {
      const errorText = await response.text();
      return res.status(response.status).json({
        success: false,
        error: `ClinicalTrials API error: ${response.status}`,
        details: errorText
      });
    }

    const data = await response.json(); // ✅ parse as JSON directly

    return res.status(200).json({
      success: true,
      totalCount: data.totalCount,
      studies: data.studies  // ✅ return only what you need
    });

  } catch (error) {
    return res.status(500).json({
      success: false,
      error: error.message
    });
  }
}
