from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def score_listing(listing):

    prompt = f"""
Evaluate this truck listing for reliability and value.

Focus:
- 2003–2015 trucks
- 4WD required
- gas engines only
- prioritize Nissan Frontier 4.0L, Toyota Tundra 5.7L, Honda Ridgeline 3.5L

Listing:
{listing}

Return:
- engine guess
- score 1–10
- BUY / CONSIDER / AVOID
- notes
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
