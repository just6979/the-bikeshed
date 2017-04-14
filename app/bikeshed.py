from werkzeug.wrappers import Request, Response


@Request.application
def app(request):
    return Response(
        'Hello World! This will soon be a place to record and share your bikes and their components. ' +
        'Show off your sweet ride to the world, keep track of maintenance schedules, find compatible upgrades.'
    )
