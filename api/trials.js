export default async function handler(req, res) {
  const disease = req.query.disease || "diabetes";

  try {
    const response = await fetch(
      `https://clinicaltrials.gov/api/v2/studies?query.term=${encodeURIComponent(disease)}&pageSize=5`,
      {
        headers: {
          "Accept": "application/json",
        },
      }
    );

    if (!response.ok) {
      const errorText = await response.text();
      return res.status(response.status).json({
        success: false,
        error: `API responded with status ${response.status}`,
        details: errorText,
      });
    }

    const data = await response.json();

    res.status(200).json({
      success: true,
      data,
    });

  } catch (error) {
    res.status(500).json({
      success: false,
      error: error.message,
    });
  }
}
