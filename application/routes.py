from .app import app


@app.route('/', name='index')
def hello_world(request):
    from pyramid.response import Response
    return Response('Hello world afdsafsa')
