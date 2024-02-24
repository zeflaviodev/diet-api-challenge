# from src.adapters.http_types.http_response import HttpResponse
# from .types import  BadRequestError, UnprocessableEntityError

# def handle_errors(error: Exception) -> HttpResponse:
#     if isinstance(error, (BadRequestError, UnprocessableEntityError)):
#         return HttpResponse(
#             status_code=error.status_code,
#             body={
#                 "errors": [{
#                     "title": error.name,
#                     "detail": error.message,
#                 }]
#             }
#         )
#     return HttpResponse(
#             status_code=500,
#             body={
#                 "errors": [{
#                     "title": "Server Error",
#                     "detail": str(error),
#                 }]
#             }
#         )
