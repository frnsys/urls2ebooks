from nom.html2md import html_to_markdown
from newspaper import Article
from newspaper.article import ArticleException

urls = [url.strip() for url in open('urls.txt').readlines() if url]

for i, url in enumerate(urls):
    try:
        article = Article(url, keep_article_html=True)
        article.download()
        article.parse()
        md = html_to_markdown(article.article_html)

        output = '''
{}

---

# {}

---
{}
        '''.format(url, article.title, md)

        title = '''
---
title: {}
author: {}
---
'''.format(article.title, ', '.join(article.authors))

        with open('out/{:0>2}.md'.format(i), 'w') as f:
            f.write(output)

        with open('out/{:0>2}_title.txt'.format(i), 'w') as f:
            f.write(title.strip())

    except ArticleException:
        print('could not extract: {}'.format(url))