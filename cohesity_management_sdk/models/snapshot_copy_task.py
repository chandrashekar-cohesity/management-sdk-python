# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.snapshot_target_1

class SnapshotCopyTask(object):

    """Implementation of the 'Snapshot Copy Task.' model.

    Specifies information about copy tasks such as replication and archival
    tasks.

    Attributes:
        copy_status (string): Specifies the status of the copy task.
        expiry_time_usecs (long|int): Specifies when the Snapshot expires on
            the target.
        message (string): Specifies warning or error information when the copy
            task is not successful.
        snapshot_target (SnapshotTarget1): Specifies settings about a target
            where a copied Snapshot is stored. A target can be a Remote
            Cluster or an Archival External Target such as AWS or Tape.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "copy_status":'copyStatus',
        "expiry_time_usecs":'expiryTimeUsecs',
        "message":'message',
        "snapshot_target":'snapshotTarget'
    }

    def __init__(self,
                 copy_status=None,
                 expiry_time_usecs=None,
                 message=None,
                 snapshot_target=None):
        """Constructor for the SnapshotCopyTask class"""

        # Initialize members of the class
        self.copy_status = copy_status
        self.expiry_time_usecs = expiry_time_usecs
        self.message = message
        self.snapshot_target = snapshot_target


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
        copy_status = dictionary.get('copyStatus')
        expiry_time_usecs = dictionary.get('expiryTimeUsecs')
        message = dictionary.get('message')
        snapshot_target = cohesity_management_sdk.models.snapshot_target_1.SnapshotTarget1.from_dictionary(dictionary.get('snapshotTarget')) if dictionary.get('snapshotTarget') else None

        # Return an object of this model
        return cls(copy_status,
                   expiry_time_usecs,
                   message,
                   snapshot_target)


