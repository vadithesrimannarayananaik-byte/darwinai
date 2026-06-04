export default async function handler(req, res) {

  const disease = req.query.disease || "diabetes";

  try {

    const response = await fetch(
      `https://clinicaltrials.gov/api/query/studies?query.term=${encodeURIComponent(disease)}&pageSize=5`
    );

    const text = await response.text();

    res.status(200).send(text);

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }

}
