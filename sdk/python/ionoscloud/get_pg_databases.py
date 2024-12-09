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
    'GetPgDatabasesResult',
    'AwaitableGetPgDatabasesResult',
    'get_pg_databases',
    'get_pg_databases_output',
]

@pulumi.output_type
class GetPgDatabasesResult:
    """
    A collection of values returned by getPgDatabases.
    """
    def __init__(__self__, cluster_id=None, databases=None, id=None, owner=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if databases and not isinstance(databases, list):
            raise TypeError("Expected argument 'databases' to be a list")
        pulumi.set(__self__, "databases", databases)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def databases(self) -> Sequence['outputs.GetPgDatabasesDatabaseResult']:
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def owner(self) -> Optional[str]:
        return pulumi.get(self, "owner")


class AwaitableGetPgDatabasesResult(GetPgDatabasesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPgDatabasesResult(
            cluster_id=self.cluster_id,
            databases=self.databases,
            id=self.id,
            owner=self.owner)


def get_pg_databases(cluster_id: Optional[str] = None,
                     owner: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPgDatabasesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['owner'] = owner
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getPgDatabases:getPgDatabases', __args__, opts=opts, typ=GetPgDatabasesResult).value

    return AwaitableGetPgDatabasesResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        databases=pulumi.get(__ret__, 'databases'),
        id=pulumi.get(__ret__, 'id'),
        owner=pulumi.get(__ret__, 'owner'))
def get_pg_databases_output(cluster_id: Optional[pulumi.Input[str]] = None,
                            owner: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPgDatabasesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['owner'] = owner
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getPgDatabases:getPgDatabases', __args__, opts=opts, typ=GetPgDatabasesResult)
    return __ret__.apply(lambda __response__: GetPgDatabasesResult(
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        databases=pulumi.get(__response__, 'databases'),
        id=pulumi.get(__response__, 'id'),
        owner=pulumi.get(__response__, 'owner')))
