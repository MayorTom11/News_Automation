import requests
from openai import OpenAI
import dictionaries
import mail


client = OpenAI(
    api_key="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"
)
news_api_key = "219692c72b1f42fc9b0f73e9740b3fb9"
news_article = []


def news(title_input, sort_by, date_by):
    date_by1 = ""
    date_by2 = ""
    if sort_by in dictionaries.SORT_OPTIONS:
        sort_by = dictionaries.SORT_OPTIONS[sort_by]

    if date_by in dictionaries.DATE_OPTIONS:
        date_by1, date_by2 = dictionaries.DATE_OPTIONS[date_by]
    main_url = "https://newsapi.org/v2/everything?q='"+title_input+"&from="+date_by1.strftime('%Y-%m-%d')+"&to="+date_by2.strftime('%Y-%m-%d')+"'&sortBy="+sort_by+"&apiKey="+news_api_key
    news_request = requests.get(main_url).json()
    print(requests.get(main_url))
    print(news_request)
    article = news_request["articles"]
    for i in range(5):
        news_article.append([])
    for n in range(len(news_article)):
        news_article[n].insert(0, article[n]['title'])
        news_article[n].insert(1, article[n]['content'].replace("\r", "").replace("\n", " "))
        news_article[n].insert(2, article[n]['url'])
        summarize = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": "Summarize this article for me in 200 words: " + news_article[n][1]}
            ]
        )
        news_article[n][1] = summarize.choices[0].message.content
    # mail.send_email(title_input)
