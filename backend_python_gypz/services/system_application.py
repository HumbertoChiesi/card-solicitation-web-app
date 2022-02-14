from models.cc_application import CreditCardApplication
from repository.system_application import SystemApplicationRepository
from services.credit_approved import credit_approved


class CreaditCardSystemServices:

    @staticmethod
    def get_all_system_applications() -> dict:
        try:
            system_applications_repository = SystemApplicationRepository()
            system_applications = system_applications_repository.get_all_system_applications()
        finally:
            del system_applications_repository
        return system_applications

    @staticmethod
    def get_one_system_application(application_id) -> dict:
        try:
            system_applications_repository = SystemApplicationRepository()
            system_application = system_applications_repository.get_one_system_application(application_id)
        finally:
            del system_applications_repository
        return system_application

    @staticmethod
    def insert_one_application(application: CreditCardApplication) -> dict:
        try:
            system_applications_repository = SystemApplicationRepository()
            application.credit = credit_approved(application.income)
            inserted_application = system_applications_repository.insert_application(application)
        finally:
            del system_applications_repository
        return inserted_application

    @staticmethod
    def delete_application(application_id) -> bool:
        try:
            system_applications_repository = SystemApplicationRepository()
            deleted = system_applications_repository.delete_application(application_id)
            return deleted
        finally:
            del system_applications_repository
