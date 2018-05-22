# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.key_value_pair_1

class AttributesDescriptor(object):

    """Implementation of the 'Attributes Descriptor.' model.

    Specifies a list of attributes about an entity.

    Attributes:
        attribute_vec (list of KeyValuePair1): Array of Attributes.  List of
            attributes about an entity.
        key_attribute_name_index (int): Specifies the attribute to use as a
            unique identifier for the entity. This value is returned in
            entityId when the GET public/statistics/entities operation is
            run.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "attribute_vec":'attributeVec',
        "key_attribute_name_index":'keyAttributeNameIndex'
    }

    def __init__(self,
                 attribute_vec=None,
                 key_attribute_name_index=None):
        """Constructor for the AttributesDescriptor class"""

        # Initialize members of the class
        self.attribute_vec = attribute_vec
        self.key_attribute_name_index = key_attribute_name_index


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
        attribute_vec = None
        if dictionary.get('attributeVec') != None:
            attribute_vec = list()
            for structure in dictionary.get('attributeVec'):
                attribute_vec.append(cohesity_management_sdk.models.key_value_pair_1.KeyValuePair1.from_dictionary(structure))
        key_attribute_name_index = dictionary.get('keyAttributeNameIndex')

        # Return an object of this model
        return cls(attribute_vec,
                   key_attribute_name_index)


