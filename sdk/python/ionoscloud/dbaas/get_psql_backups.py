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
from .. import _utilities
from . import outputs

__all__ = [
    'GetPSQLBackupsResult',
    'AwaitableGetPSQLBackupsResult',
    'get_psql_backups',
    'get_psql_backups_output',
]

@pulumi.output_type
class GetPSQLBackupsResult:
    """
    A collection of values returned by getPSQLBackups.
    """
    def __init__(__self__, cluster_backups=None, cluster_id=None, id=None):
        if cluster_backups and not isinstance(cluster_backups, list):
            raise TypeError("Expected argument 'cluster_backups' to be a list")
        pulumi.set(__self__, "cluster_backups", cluster_backups)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="clusterBackups")
    def cluster_backups(self) -> Sequence['outputs.GetPSQLBackupsClusterBackupResult']:
        """
        List of backups.
        """
        return pulumi.get(self, "cluster_backups")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The unique ID of the cluster
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetPSQLBackupsResult(GetPSQLBackupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPSQLBackupsResult(
            cluster_backups=self.cluster_backups,
            cluster_id=self.cluster_id,
            id=self.id)


def get_psql_backups(cluster_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPSQLBackupsResult:
    """
    The **DbaaS Postgres Backups data source** can be used to search for and return existing DbaaS Postgres Backups for a specific Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_backups(cluster_id="cluster_id")
    ```


    :param str cluster_id: The unique ID of the cluster.
           
           `cluster_id` must be provided. If it is not provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:dbaas/getPSQLBackups:getPSQLBackups', __args__, opts=opts, typ=GetPSQLBackupsResult).value

    return AwaitableGetPSQLBackupsResult(
        cluster_backups=pulumi.get(__ret__, 'cluster_backups'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'))
def get_psql_backups_output(cluster_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPSQLBackupsResult]:
    """
    The **DbaaS Postgres Backups data source** can be used to search for and return existing DbaaS Postgres Backups for a specific Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.dbaas.get_psql_backups(cluster_id="cluster_id")
    ```


    :param str cluster_id: The unique ID of the cluster.
           
           `cluster_id` must be provided. If it is not provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:dbaas/getPSQLBackups:getPSQLBackups', __args__, opts=opts, typ=GetPSQLBackupsResult)
    return __ret__.apply(lambda __response__: GetPSQLBackupsResult(
        cluster_backups=pulumi.get(__response__, 'cluster_backups'),
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        id=pulumi.get(__response__, 'id')))
