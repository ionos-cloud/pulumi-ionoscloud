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
from . import outputs

__all__ = [
    'GetNfsClusterResult',
    'AwaitableGetNfsClusterResult',
    'get_nfs_cluster',
    'get_nfs_cluster_output',
]

@pulumi.output_type
class GetNfsClusterResult:
    """
    A collection of values returned by getNfsCluster.
    """
    def __init__(__self__, connections=None, id=None, location=None, name=None, nfs=None, partial_match=None, size=None):
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nfs and not isinstance(nfs, list):
            raise TypeError("Expected argument 'nfs' to be a list")
        pulumi.set(__self__, "nfs", nfs)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetNfsClusterConnectionResult']:
        """
        A list of connections for the Network File Storage cluster. You can specify only one connection. Each connection supports the following:
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Network File Storage cluster.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location where the Network File Storage cluster is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Network File Storage cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nfs(self) -> Sequence['outputs.GetNfsClusterNfResult']:
        """
        The NFS configuration for the Network File Storage cluster. Each NFS configuration supports the following:
        """
        return pulumi.get(self, "nfs")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        return pulumi.get(self, "size")


class AwaitableGetNfsClusterResult(GetNfsClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNfsClusterResult(
            connections=self.connections,
            id=self.id,
            location=self.location,
            name=self.name,
            nfs=self.nfs,
            partial_match=self.partial_match,
            size=self.size)


def get_nfs_cluster(id: Optional[str] = None,
                    location: Optional[str] = None,
                    name: Optional[str] = None,
                    partial_match: Optional[bool] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNfsClusterResult:
    """
    Returns information about clusters of Network File Storage (NFS) on IonosCloud.


    :param str id: ID of the Network File Storage cluster.
    :param str location: The location where the Network File Storage cluster is located.
    :param str name: Name of the Network File Storage cluster.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getNfsCluster:getNfsCluster', __args__, opts=opts, typ=GetNfsClusterResult).value

    return AwaitableGetNfsClusterResult(
        connections=pulumi.get(__ret__, 'connections'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        nfs=pulumi.get(__ret__, 'nfs'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        size=pulumi.get(__ret__, 'size'))
def get_nfs_cluster_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                           location: Optional[pulumi.Input[str]] = None,
                           name: Optional[pulumi.Input[Optional[str]]] = None,
                           partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNfsClusterResult]:
    """
    Returns information about clusters of Network File Storage (NFS) on IonosCloud.


    :param str id: ID of the Network File Storage cluster.
    :param str location: The location where the Network File Storage cluster is located.
    :param str name: Name of the Network File Storage cluster.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getNfsCluster:getNfsCluster', __args__, opts=opts, typ=GetNfsClusterResult)
    return __ret__.apply(lambda __response__: GetNfsClusterResult(
        connections=pulumi.get(__response__, 'connections'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        nfs=pulumi.get(__response__, 'nfs'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        size=pulumi.get(__response__, 'size')))
