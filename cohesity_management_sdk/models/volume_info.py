# -*- coding: utf-8 -*-
# Copyright 2019 Cohesity Inc.

import cohesity_management_sdk.models.volume_info_disk_info
import cohesity_management_sdk.models.volume_info_logical_volume_info

class VolumeInfo(object):

    """Implementation of the 'VolumeInfo' model.

    TODO: type model description here.

    Attributes:
        disk_vec (list of VolumeInfoDiskInfo): Information about all the disks
            and partitions needed to mount this logical volume.
        display_name (string): Display name.
        filesystem_type (string): Filesystem on this volume.
        fs_uuid (string): Filesystem uuid.
        is_bootable (bool): Is this volume bootable?
        is_dedup (bool): Is this a dedup volume? Currently, set to true only
            for ntfs dedup volume.
        is_supported (bool): Is this a supported Volume (filesystem)?
        lv_info (VolumeInfoLogicalVolumeInfo): This is extra attribute which
            uniquely identifies a logical volume in LVM or LDM.
        volume_guid (string): The guid of the volume represented by this
            virtual disk. This information will be originally populated by
            magneto for physical environments.
        volume_type (int): Whether this volume is simple, lvm or ldm.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "disk_vec":'diskVec',
        "display_name":'displayName',
        "filesystem_type":'filesystemType',
        "fs_uuid":'fsUuid',
        "is_bootable":'isBootable',
        "is_dedup":'isDedup',
        "is_supported":'isSupported',
        "lv_info":'lvInfo',
        "volume_guid":'volumeGuid',
        "volume_type":'volumeType'
    }

    def __init__(self,
                 disk_vec=None,
                 display_name=None,
                 filesystem_type=None,
                 fs_uuid=None,
                 is_bootable=None,
                 is_dedup=None,
                 is_supported=None,
                 lv_info=None,
                 volume_guid=None,
                 volume_type=None):
        """Constructor for the VolumeInfo class"""

        # Initialize members of the class
        self.disk_vec = disk_vec
        self.display_name = display_name
        self.filesystem_type = filesystem_type
        self.fs_uuid = fs_uuid
        self.is_bootable = is_bootable
        self.is_dedup = is_dedup
        self.is_supported = is_supported
        self.lv_info = lv_info
        self.volume_guid = volume_guid
        self.volume_type = volume_type


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
        disk_vec = None
        if dictionary.get('diskVec') != None:
            disk_vec = list()
            for structure in dictionary.get('diskVec'):
                disk_vec.append(cohesity_management_sdk.models.volume_info_disk_info.VolumeInfoDiskInfo.from_dictionary(structure))
        display_name = dictionary.get('displayName')
        filesystem_type = dictionary.get('filesystemType')
        fs_uuid = dictionary.get('fsUuid')
        is_bootable = dictionary.get('isBootable')
        is_dedup = dictionary.get('isDedup')
        is_supported = dictionary.get('isSupported')
        lv_info = cohesity_management_sdk.models.volume_info_logical_volume_info.VolumeInfoLogicalVolumeInfo.from_dictionary(dictionary.get('lvInfo')) if dictionary.get('lvInfo') else None
        volume_guid = dictionary.get('volumeGuid')
        volume_type = dictionary.get('volumeType')

        # Return an object of this model
        return cls(disk_vec,
                   display_name,
                   filesystem_type,
                   fs_uuid,
                   is_bootable,
                   is_dedup,
                   is_supported,
                   lv_info,
                   volume_guid,
                   volume_type)


