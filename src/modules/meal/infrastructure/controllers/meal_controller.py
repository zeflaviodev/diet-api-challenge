#pylint:disable=broad-exception-raised

class MealController:

    def __init__(self) -> None:
        pass

    def create(self, request):
        body = None
        if request.data: body = request.json

        if not body:
            raise Exception('Body is required')

        print(body)
        # Falta adicionar o validador
        # repository = MealRepository()
        # use_case = MealCreateUseCase(repository)

        # use_case.create_meal(body)

        return {'message': 'Meal created successfully'}
    