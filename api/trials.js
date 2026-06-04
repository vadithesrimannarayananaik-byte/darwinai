export default async function handler(req, res) {

  const disease = req.query.disease || "diabetes";

  try {

    const response = await fetch(
      `https://clinicaltrials.gov/api/query/full_studies?expr=${encodeURIComponent(disease)}&min_rnk=1&max_rnk=5&fmt=json`
    );

    const data = await response.json();

    res.status(200).json(data);

  } catch (error) {

    res.status(500).json({
      success: false,
      error: error.message
    });

  }

}
