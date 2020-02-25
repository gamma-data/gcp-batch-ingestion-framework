# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Table(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, table_name: str=None):  # noqa: E501
        """Table - a model defined in Swagger

        :param id: The id of this Table.  # noqa: E501
        :type id: int
        :param table_name: The table_name of this Table.  # noqa: E501
        :type table_name: str
        """
        self.swagger_types = {
            'id': int,
            'table_name': str
        }

        self.attribute_map = {
            'id': 'id',
            'table_name': 'table name'
        }
        self._id = id
        self._table_name = table_name

    @classmethod
    def from_dict(cls, dikt) -> 'Table':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Table of this Table.  # noqa: E501
        :rtype: Table
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Table.


        :return: The id of this Table.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Table.


        :param id: The id of this Table.
        :type id: int
        """

        self._id = id

    @property
    def table_name(self) -> str:
        """Gets the table_name of this Table.


        :return: The table_name of this Table.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name: str):
        """Sets the table_name of this Table.


        :param table_name: The table_name of this Table.
        :type table_name: str
        """

        self._table_name = table_name
