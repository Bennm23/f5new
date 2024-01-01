from django.conf import settings
from django.core.cache import cache
import openai

def get_rugby_fact():
    # Check if the fact is in the cache
    fact = cache.get('rugby_fact')
    
    # If the fact is not cached, fetch a new one and cache it
    if not fact:
        openai.api_key = settings.OPENAI_KEY

        # Updated API call for OpenAI using Completion.create
        response = openai.completions.create(
            model="text-davinci-003",
            prompt="Give me an interesting rugby fact about historical matches, remarkable events, or information about individual players.",
            max_tokens=60
        )

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Give me an interesting rugby fact about historical matches, remarkable events, or information about individual players."},
            ]
        )

        fact = response.choices[0].message.content

        # Cache the fact for 24 hours (86400 seconds)
        cache.set('rugby_fact', fact, 86400)

    return fact

