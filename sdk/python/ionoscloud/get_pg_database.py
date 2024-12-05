# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
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

__all__ = [
    'GetPgDatabaseResult',
    'AwaitableGetPgDatabaseResult',
    'get_pg_database',
    'get_pg_database_output',
]

@pulumi.output_type
class GetPgDatabaseResult:
    """
    A collection of values returned by getPgDatabase.
    """
    def __init__(__self__, cluster_id=None, id=None, name=None, owner=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner and not isinstance(owner, str):
            raise TypeError("Expected argument 'owner' to be a str")
        pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")


class AwaitableGetPgDatabaseResult(GetPgDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPgDatabaseResult(
            cluster_id=self.cluster_id,
            id=self.id,
            name=self.name,
            owner=self.owner)


def get_pg_database(cluster_id: Optional[str] = None,
                    name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPgDatabaseResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getPgDatabase:getPgDatabase', __args__, opts=opts, typ=GetPgDatabaseResult).value

    return AwaitableGetPgDatabaseResult(
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        owner=pulumi.get(__ret__, 'owner'))
def get_pg_database_output(cluster_id: Optional[pulumi.Input[str]] = None,
                           name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPgDatabaseResult]:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getPgDatabase:getPgDatabase', __args__, opts=opts, typ=GetPgDatabaseResult)
    return __ret__.apply(lambda __response__: GetPgDatabaseResult(
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        owner=pulumi.get(__response__, 'owner')))
