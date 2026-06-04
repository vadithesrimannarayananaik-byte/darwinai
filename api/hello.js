export default async function handler(req, res) {

  const patient = req.query.patient || "diabaties";
  const trial = req.query.trial || "Type 2 Diabetes Mellitus";

  const response = await fetch(
    "https://api.anthropic.com/v1/messages",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": process.env.CLAUDE_API_KEY,
        "anthropic-version": "2023-06-01"
      },
      body: JSON.stringify({
        model: "claude-3-5-haiku-20241022",
        max_tokens: 100,
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
        ]
      })
    }
  );

  const data = await response.json();

  res.status(200).json(data);

}
