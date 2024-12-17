# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs

__all__ = [
    'GetMariadbBackupsResult',
    'AwaitableGetMariadbBackupsResult',
    'get_mariadb_backups',
    'get_mariadb_backups_output',
]

@pulumi.output_type
class GetMariadbBackupsResult:
    """
    A collection of values returned by getMariadbBackups.
    """
    def __init__(__self__, backup_id=None, backups=None, cluster_id=None, id=None, location=None):
        if backup_id and not isinstance(backup_id, str):
            raise TypeError("Expected argument 'backup_id' to be a str")
        pulumi.set(__self__, "backup_id", backup_id)
        if backups and not isinstance(backups, list):
            raise TypeError("Expected argument 'backups' to be a list")
        pulumi.set(__self__, "backups", backups)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[str]:
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter
    def backups(self) -> Sequence['outputs.GetMariadbBackupsBackupResult']:
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[str]:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")


class AwaitableGetMariadbBackupsResult(GetMariadbBackupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMariadbBackupsResult(
            backup_id=self.backup_id,
            backups=self.backups,
            cluster_id=self.cluster_id,
            id=self.id,
            location=self.location)


def get_mariadb_backups(backup_id: Optional[str] = None,
                        cluster_id: Optional[str] = None,
                        location: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMariadbBackupsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['clusterId'] = cluster_id
    __args__['location'] = location
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getMariadbBackups:getMariadbBackups', __args__, opts=opts, typ=GetMariadbBackupsResult).value

    return AwaitableGetMariadbBackupsResult(
        backup_id=pulumi.get(__ret__, 'backup_id'),
        backups=pulumi.get(__ret__, 'backups'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'))
def get_mariadb_backups_output(backup_id: Optional[pulumi.Input[Optional[str]]] = None,
                               cluster_id: Optional[pulumi.Input[Optional[str]]] = None,
                               location: Optional[pulumi.Input[Optional[str]]] = None,
                               opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetMariadbBackupsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['backupId'] = backup_id
    __args__['clusterId'] = cluster_id
    __args__['location'] = location
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getMariadbBackups:getMariadbBackups', __args__, opts=opts, typ=GetMariadbBackupsResult)
    return __ret__.apply(lambda __response__: GetMariadbBackupsResult(
        backup_id=pulumi.get(__response__, 'backup_id'),
        backups=pulumi.get(__response__, 'backups'),
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location')))
