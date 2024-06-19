from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

topics = [
	{'id':1, 'title':'routing', 'body':'Routing is ..'},
	{'id':2, 'title':'view', 'body':'View is ..'},
	{'id':3, 'title':'model', 'body':'Model is ..'}
]

def HTMLTemplate(articleTag):
	global topics
	ol = ''
	for topic in topics:
		ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
	
	return f'''
		<html>
		<body>
			<h1><a href="/">Django</a></h1>
			<ul>
				{ol}
			</ul>
			{articleTag}
			<ul>
				<a href="/create/">create</a>
			</ul>
		</body>
		</html>		 
	'''

def index(request):
	article = '''
	<h2>Welcome</h2>
	Hello, Django
	'''
	return HttpResponse(HTMLTemplate(article))

def read(request, id): #url로 들어온 id 자료형은 string.
	global topics
	article = ''
	for topic in topics:
		print(type(topic['id']))
		if topic['id'] == int(id):
			article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

	return HttpResponse(HTMLTemplate(article))

@csrf_exempt
def create(request):
	article = '''
		<form action="/create/" method="post">
			<p><input type="text" name="title" placeholder="title"></p>
			<p><textarea name="body" placeholder="body"></textarea></p>
			<p><input type="submit"></p>
		</form>
	'''
	return HttpResponse(HTMLTemplate(article))

