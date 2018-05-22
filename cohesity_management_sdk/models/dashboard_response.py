# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.dashboard

class DashboardResponse(object):

    """Implementation of the 'DashboardResponse' model.

    TODO: type model description here.

    Attributes:
        dashboard (Dashboard): Data shown on Dashboard.
        dashboards (list of Dashboard): Specifies a list of dashboards of all
            the clusters in the SPOG setup if the query parameter allClusters
            is set to true. Otherwise this field is not populated. When
            populated the dashboard field is also populated with aggregated
            dashboard values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dashboard":'dashboard',
        "dashboards":'dashboards'
    }

    def __init__(self,
                 dashboard=None,
                 dashboards=None):
        """Constructor for the DashboardResponse class"""

        # Initialize members of the class
        self.dashboard = dashboard
        self.dashboards = dashboards


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
        dashboard = cohesity_management_sdk.models.dashboard.Dashboard.from_dictionary(dictionary.get('dashboard')) if dictionary.get('dashboard') else None
        dashboards = None
        if dictionary.get('dashboards') != None:
            dashboards = list()
            for structure in dictionary.get('dashboards'):
                dashboards.append(cohesity_management_sdk.models.dashboard.Dashboard.from_dictionary(structure))

        # Return an object of this model
        return cls(dashboard,
                   dashboards)


