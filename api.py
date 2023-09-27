import wikipediaapi

# Specify a user agent
user_agent = "MyWikiBot/1.0 (arseny_void@email.com)"

wikipedia_en = wikipediaapi.Wikipedia('en', user_agent=user_agent)

page = wikipedia_en.page('Python_(programming_language)')
print(page.summary)
