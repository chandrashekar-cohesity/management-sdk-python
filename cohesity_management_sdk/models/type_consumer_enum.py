# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

class TypeConsumerEnum(object):

    """Implementation of the 'Type_Consumer' enum.

    Specifies the type of the consumer.
    Type of the consumer can be one of the following three,
    'kViews', indicates the stats info of Views used per organization
    (tenant)
    per view box (storage domain).
    'kProtectionRuns', indicates the stats info of Protection Runs used per
    organization (tenant) per view box (storage domain).
    'kReplicationRuns', indicates the stats info of Replication In used per
    organization (tenant) per view box (storage domain).

    Attributes:
        KVIEWS: TODO: type description here.
        KPROTECTIONRUNS: TODO: type description here.
        KREPLICATIONRUNS: TODO: type description here.

    """

    KVIEWS = 'kViews'

    KPROTECTIONRUNS = 'kProtectionRuns'

    KREPLICATIONRUNS = 'kReplicationRuns'

