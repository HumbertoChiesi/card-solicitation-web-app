from starlette.routing import Route

from actions.system_application import CreditCardSystem

BASE_PATH = '/sistema'


class Router:

    @staticmethod
    def get_routes() -> list:
        return [
            Route(f'{BASE_PATH}/solicitacao/', CreditCardSystem.get_cc_applications, methods=['GET']),
            Route(f'{BASE_PATH}/solicitacao/', CreditCardSystem.insert_cc_application, methods=['POST']),
            Route(f'{BASE_PATH}/solicitacao/{{application_id}}', CreditCardSystem.get_one_application,methods=['GET']),
            Route(f'{BASE_PATH}/solicitacao/{{application_id}}', CreditCardSystem.delete_cc_application, methods=['DELETE'])
        ]
