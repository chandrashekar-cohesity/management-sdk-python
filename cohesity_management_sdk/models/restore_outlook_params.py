# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.restore_outlook_params_mailbox
import cohesity_management_sdk.models.entity_proto

class RestoreOutlookParams(object):

    """Implementation of the 'RestoreOutlookParams' model.

    TODO: type model description here.

    Attributes:
        mailbox_vec (list of RestoreOutlookParamsMailbox): In a RestoreJob ,
            user will provide the list of mailboxes to be restored. Provision
            is there for restoring full AND partial mailbox recovery.
        target_folder_path (string): TODO: type description here.
        target_mailbox (EntityProto): Specifies the attributes and the latest
            statistics about an entity.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mailbox_vec":'mailboxVec',
        "target_folder_path":'targetFolderPath',
        "target_mailbox":'targetMailbox'
    }

    def __init__(self,
                 mailbox_vec=None,
                 target_folder_path=None,
                 target_mailbox=None):
        """Constructor for the RestoreOutlookParams class"""

        # Initialize members of the class
        self.mailbox_vec = mailbox_vec
        self.target_folder_path = target_folder_path
        self.target_mailbox = target_mailbox


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
        mailbox_vec = None
        if dictionary.get('mailboxVec') != None:
            mailbox_vec = list()
            for structure in dictionary.get('mailboxVec'):
                mailbox_vec.append(cohesity_management_sdk.models.restore_outlook_params_mailbox.RestoreOutlookParamsMailbox.from_dictionary(structure))
        target_folder_path = dictionary.get('targetFolderPath')
        target_mailbox = cohesity_management_sdk.models.entity_proto.EntityProto.from_dictionary(dictionary.get('targetMailbox')) if dictionary.get('targetMailbox') else None

        # Return an object of this model
        return cls(mailbox_vec,
                   target_folder_path,
                   target_mailbox)


