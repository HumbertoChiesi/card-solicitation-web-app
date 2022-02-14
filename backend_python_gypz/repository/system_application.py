from enum import unique
from uuid import UUID

from bson import ObjectId
from pymongo import MongoClient

from utils.serialize_data import serialize_data


class SystemApplicationRepository:
    def __init__(self):
        self.__client = MongoClient()
        self.__db = self.__client.applications
        self.__collections = self.__db.applications

    def get_all_system_applications(self) -> dict:
        system_applications = self.__collections.find({})
        return serialize_data(system_applications, is_list=True)

    def get_one_system_application(self, application_id: UUID) -> dict:
        system_applications = self.__collections.find_one({"_id": ObjectId(application_id)})
        return serialize_data(system_applications, is_list=False)

    def insert_application(self, application):
        self.__collections.insert_one(application.dict())
        return serialize_data(application.dict(), is_list=False)

    def delete_application(self, application_id: UUID) -> bool:
        deleted = self.__collections.delete_one({"_id": ObjectId(application_id)})
        return bool(deleted.deleted_count)
