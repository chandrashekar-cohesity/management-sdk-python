# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.file_folder_search_result

class FileFolderSearchResult1(object):

    """Implementation of the 'File/Folder Search Result.1' model.

    Specifies an array of found files and folders. In addition, a count is
    provided to indicate if additional requests must be made to get
    the full result.

    Attributes:
        files (list of FileFolderSearchResult): Array of Files and Folders.
            Specifies the list of files and folders returned by this request
            that match the specified search and filter criteria. The number of
            files returned is limited by the pageCount field.
        total_count (long|int): Specifies the total number of files and
            folders that match the filter and search criteria. Use this value
            to determine how many additional requests are required to get the
            full result.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "files":'files',
        "total_count":'totalCount'
    }

    def __init__(self,
                 files=None,
                 total_count=None):
        """Constructor for the FileFolderSearchResult1 class"""

        # Initialize members of the class
        self.files = files
        self.total_count = total_count


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
        files = None
        if dictionary.get('files') != None:
            files = list()
            for structure in dictionary.get('files'):
                files.append(cohesity_management_sdk.models.file_folder_search_result.FileFolderSearchResult.from_dictionary(structure))
        total_count = dictionary.get('totalCount')

        # Return an object of this model
        return cls(files,
                   total_count)

