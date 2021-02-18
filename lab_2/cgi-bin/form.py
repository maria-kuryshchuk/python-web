#!/usr/bin/env python3
import cgi
import html
import os
from http import cookies

form = cgi.FieldStorage()
text1 = form.getfirst("fname", "not specified")
text2 = form.getfirst("lname", "not specified")

text1 = html.escape(text1)
text2 = html.escape(text2)

if form.getvalue('language'):

    languages = form.getvalue('language')
    if type(languages) == list and len(languages) != 1:
        languages = ', '.join(languages)
else:  
    languages = "not specified"

if form.getvalue('gender'):
  
    gender = form.getvalue('gender')
else:
    gender = "not specified"
#counting cookies
cookie = cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))

if cookie.get("counter") is None:
    cookie['counter'] = '1'
    print(cookie)
else:
    cookie['counter'] = str(1 + int(cookie['counter'].value))
    print(cookie)
counter = cookie['counter'].value



print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обробка даних форми</title>
        </head>
        <body>""")

print("<h1>Обробка даних форми</h1>")
print("<p>First name: {}</p>".format(text1))
print("<p>Last name: {}</p>".format(text2))
print("<p>I know {}</p>".format(languages))
print("<p>I am a {}</p>".format(gender))
print("<br><p>Total count of submitted forms: {}</p>".format(counter))

print("""</body>
        </html>""")
