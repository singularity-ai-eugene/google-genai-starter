from google import genai
from authentication import CREDENTIALS

# Access specific service credentials
GOOGLE_API_KEY = CREDENTIALS['GOOGLE_API_KEY']['password']


# Pass the API key to the client
client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Who founded Google and when was it founded?",
)

print(response.text)