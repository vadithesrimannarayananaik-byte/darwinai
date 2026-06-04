export default async function handler(req, res) {

  const disease = req.query.disease || "diabetes";

  try {

    const url =
      `https://clinicaltrials.gov/api/v2/studies?query.term=${encodeURIComponent(disease)}&pageSize=5`;

    const response = await fetch(url, {
      method: "GET",
      headers: {
        "accept": "application/json"
      }
    });

    const text = await response.text();

    return res.status(200).json({
      success: true,
      status: response.status,
      url,
      raw: text
    });

  } catch (error) {

    return res.status(500).json({
      success: false,
      error: error.message,
      stack: error.stack
    });

  }

}
