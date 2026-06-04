export default async function handler(req, res) {

  const disease = req.query.disease || "diabetes";

  const response = await fetch(
    `https://clinicaltrials.gov/api/query/study_fields?expr=${disease}&fields=BriefTitle,ConditionName,LocationCity,NCTId&min_rnk=1&max_rnk=5&fmt=json`
  );

  const data = await response.json();

  res.status(200).json(data);

}
