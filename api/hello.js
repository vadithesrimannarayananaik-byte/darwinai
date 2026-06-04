export default async function handler(req, res) {

  const patient = req.query.patient || "diabaties";
  const trial = req.query.trial || "Type 2 Diabetes Mellitus";

  const response = await fetch(
    "https://api.openai.com/v1/chat/completions",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${process.env.OPENAI_API_KEY}`
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages: [
          {
            role: "user",
            content: `
You are a medical AI.

Patient disease:
${patient}

Clinical trial disease:
${trial}

Decide if both diseases refer to the same or related condition.

Reply ONLY with:
MATCH
or
NO MATCH
`
          }
        ],
        max_tokens: 20
      })
    }
  );

  const data = await response.json();

  res.status(200).json(data);

}
