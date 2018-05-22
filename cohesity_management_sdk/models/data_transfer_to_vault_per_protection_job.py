# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-


class DataTransferToVaultPerProtectionJob(object):

    """Implementation of the 'Data Transfer to Vault Per Protection Job.' model.

    Specifies statistics about the transfer of data from this Cohesity
    Cluster to this Vault for a Protection Job.

    Attributes:
        num_logical_bytes_transferred (long|int): Specifies the total number
            of logical bytes that are transferred from this Cohesity Cluster
            to this Vault for this Protection Job. The logical size is when
            the data is fully hydrated or expanded.
        num_physical_bytes_transferred (long|int): Specifies the total number
            of physical bytes that are transferred from this Cohesity Cluster
            to this Vault for this Protection Job.
        protection_job_name (string): Specifies the name of the Protection
            Job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_logical_bytes_transferred":'numLogicalBytesTransferred',
        "num_physical_bytes_transferred":'numPhysicalBytesTransferred',
        "protection_job_name":'protectionJobName'
    }

    def __init__(self,
                 num_logical_bytes_transferred=None,
                 num_physical_bytes_transferred=None,
                 protection_job_name=None):
        """Constructor for the DataTransferToVaultPerProtectionJob class"""

        # Initialize members of the class
        self.num_logical_bytes_transferred = num_logical_bytes_transferred
        self.num_physical_bytes_transferred = num_physical_bytes_transferred
        self.protection_job_name = protection_job_name


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
        num_logical_bytes_transferred = dictionary.get('numLogicalBytesTransferred')
        num_physical_bytes_transferred = dictionary.get('numPhysicalBytesTransferred')
        protection_job_name = dictionary.get('protectionJobName')

        # Return an object of this model
        return cls(num_logical_bytes_transferred,
                   num_physical_bytes_transferred,
                   protection_job_name)


