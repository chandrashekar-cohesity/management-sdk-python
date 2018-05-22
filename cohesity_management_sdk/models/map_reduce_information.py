# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.map_reduce_info_app_property
import cohesity_management_sdk.models.map_reduce_aux_data
import cohesity_management_sdk.models.map_reduce_info_required_property

class MapReduceInformation(object):

    """Implementation of the 'Map Reduce Information.' model.

    This will be used to encapsulate information about mapper and reducer
    only.
    On UI this will be used to show the list of available apps to the user.

    Attributes:
        app_property (MapReduceInfoAppProperty): AppProperty message
            encapsulates properties that are same across all run instances of
            an app.
        aux_data (MapReduceAuxData): This message encapsulates auxillary data
            for a MapReduce. One example of such data is saved patterns for
            Pattern finder app.
        description (string): Map reduce job description.
        excluded_data_source_vec (list of int): List of all excluded data
            sources for this app.
        id (long|int): ID of map reduce job.
        is_system_defined (bool): Flag to denote if this is system pre-defined
            app or user has written this app.
        mapper_id (long|int): ID of the mapper to process the input.
        name (string): Map reduce job name.
        reducer_id (long|int): ID of the reducer.
        required_property_vec (list of MapReduceInfoRequiredProperty): TODO:
            type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_property":'appProperty',
        "aux_data":'auxData',
        "description":'description',
        "excluded_data_source_vec":'excludedDataSourceVec',
        "id":'id',
        "is_system_defined":'isSystemDefined',
        "mapper_id":'mapperId',
        "name":'name',
        "reducer_id":'reducerId',
        "required_property_vec":'requiredPropertyVec'
    }

    def __init__(self,
                 app_property=None,
                 aux_data=None,
                 description=None,
                 excluded_data_source_vec=None,
                 id=None,
                 is_system_defined=None,
                 mapper_id=None,
                 name=None,
                 reducer_id=None,
                 required_property_vec=None):
        """Constructor for the MapReduceInformation class"""

        # Initialize members of the class
        self.app_property = app_property
        self.aux_data = aux_data
        self.description = description
        self.excluded_data_source_vec = excluded_data_source_vec
        self.id = id
        self.is_system_defined = is_system_defined
        self.mapper_id = mapper_id
        self.name = name
        self.reducer_id = reducer_id
        self.required_property_vec = required_property_vec


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        app_property = cohesity_management_sdk.models.map_reduce_info_app_property.MapReduceInfoAppProperty.from_dictionary(dictionary.get('appProperty')) if dictionary.get('appProperty') else None
        aux_data = cohesity_management_sdk.models.map_reduce_aux_data.MapReduceAuxData.from_dictionary(dictionary.get('auxData')) if dictionary.get('auxData') else None
        description = dictionary.get('description')
        excluded_data_source_vec = dictionary.get('excludedDataSourceVec')
        id = dictionary.get('id')
        is_system_defined = dictionary.get('isSystemDefined')
        mapper_id = dictionary.get('mapperId')
        name = dictionary.get('name')
        reducer_id = dictionary.get('reducerId')
        required_property_vec = None
        if dictionary.get('requiredPropertyVec') != None:
            required_property_vec = list()
            for structure in dictionary.get('requiredPropertyVec'):
                required_property_vec.append(cohesity_management_sdk.models.map_reduce_info_required_property.MapReduceInfoRequiredProperty.from_dictionary(structure))

        # Return an object of this model
        return cls(app_property,
                   aux_data,
                   description,
                   excluded_data_source_vec,
                   id,
                   is_system_defined,
                   mapper_id,
                   name,
                   reducer_id,
                   required_property_vec)


