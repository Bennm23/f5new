from django.conf import settings
from django.core.cache import cache
import openai

def get_blog_ideas():
    # Check if the idea is in the cache
    idea = cache.get('rugby_idea')
    
    # If the idea is not cached, fetch a new one and cache it
    if not idea:
        openai.api_key = settings.OPENAI_KEY

        # Updated API call for OpenAI using Completion.create
        response = openai.completions.create(
            model="text-davinci-003",
            prompt="Tell me an interesting idea about rugby or about a rugby player's statistics, or the rugby world cup.",
            max_tokens=60
        )

        idea = response.choices[0].text.strip()

        # Cache the idea for 24 hours (86400 seconds)
        cache.set('rugby_idea', idea, 86400)

    return idea