from jinja2 import Environment, BaseLoader
import main

html_template = """
<html>
<head></head>
<body>
<h1>Here are your news!</h1>
{% for index in range(news_article | length) %}
        <h2>{{news_article[index][0]}}</h2>
        <p>{{news_article[index][1]}}</p>
        <p>{{news_article[index][2]}}</p>
{% endfor %}
</body>
</html>
"""

env = Environment(loader=BaseLoader).from_string(html_template)
template_vars = {"news_article": main.news_article}
html_out = env.render(template_vars)
print(html_out)
