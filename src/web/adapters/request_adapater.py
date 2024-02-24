from typing import Callable
from flask import request as FlaskRequest
from src.modules.shares.http.http_response import HttpResponse
from src.modules.shares.http.http_request import HttpRequest

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:
    body = None
    if request.data: body = request.json

    http_request = HttpRequest(
        headers=request.headers,
        body=body,
        query_params=request.args,
        path_params=request.view_args,
        url=request.full_path
    )

    http_response = controller(http_request)

    return http_response
