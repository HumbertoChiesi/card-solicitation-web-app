from starlette.requests import Request

from starlette.responses import JSONResponse

from models.cc_application import CreditCardApplication
from services.system_application import CreaditCardSystemServices


class CreditCardSystem:

    @staticmethod
    async def get_cc_applications(request: Request) -> JSONResponse:
        try:
            system_applications = CreaditCardSystemServices.get_all_system_applications()
            return JSONResponse(system_applications)
        except Exception as err:
            return JSONResponse({"ERROR": str(err)}, status_code=400)

    @staticmethod
    async def get_one_application(request: Request) -> JSONResponse:
        try:
            application_id = request.path_params['application_id']
            system_application = CreaditCardSystemServices.get_one_system_application(application_id)
            return JSONResponse(system_application)
        except Exception as err:
            return JSONResponse({"ERROR": str(err)}, status_code=400)

    @staticmethod
    async def insert_cc_application(request: Request) -> JSONResponse:
        try:
            body_payload = await request.json()
            cc_application = CreditCardApplication(**body_payload)
            inserted_application = CreaditCardSystemServices.insert_one_application(cc_application)
            return JSONResponse(inserted_application)
        except Exception as err:
            return JSONResponse({"ERROR": str(err)}, status_code=400)

    @staticmethod
    async def delete_cc_application(request: Request) -> JSONResponse:
        try:
            application_id = request.path_params['application_id']
            deleted = CreaditCardSystemServices.delete_application(application_id)
            return JSONResponse(deleted)
        except Exception as err:
            return JSONResponse({"ERROR": str(err)}, status_code=400)
