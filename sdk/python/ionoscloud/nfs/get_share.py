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
from ._inputs import *

__all__ = [
    'GetShareResult',
    'AwaitableGetShareResult',
    'get_share',
    'get_share_output',
]

@pulumi.output_type
class GetShareResult:
    """
    A collection of values returned by getShare.
    """
    def __init__(__self__, client_groups=None, cluster_id=None, gid=None, id=None, location=None, name=None, nfs_path=None, partial_match=None, quota=None, uid=None):
        if client_groups and not isinstance(client_groups, list):
            raise TypeError("Expected argument 'client_groups' to be a list")
        pulumi.set(__self__, "client_groups", client_groups)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if gid and not isinstance(gid, int):
            raise TypeError("Expected argument 'gid' to be a int")
        pulumi.set(__self__, "gid", gid)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nfs_path and not isinstance(nfs_path, str):
            raise TypeError("Expected argument 'nfs_path' to be a str")
        pulumi.set(__self__, "nfs_path", nfs_path)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if quota and not isinstance(quota, int):
            raise TypeError("Expected argument 'quota' to be a int")
        pulumi.set(__self__, "quota", quota)
        if uid and not isinstance(uid, int):
            raise TypeError("Expected argument 'uid' to be a int")
        pulumi.set(__self__, "uid", uid)

    @property
    @pulumi.getter(name="clientGroups")
    def client_groups(self) -> Sequence['outputs.GetShareClientGroupResult']:
        """
        The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
        """
        return pulumi.get(self, "client_groups")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        The ID of the Network File Storage cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def gid(self) -> int:
        """
        The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the Network File Storage share.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location where the Network File Storage share is located.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Network File Storage share.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nfsPath")
    def nfs_path(self) -> str:
        """
        Path to the NFS export. The NFS path is the path to the directory being exported.
        """
        return pulumi.get(self, "nfs_path")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def quota(self) -> int:
        """
        The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def uid(self) -> int:
        """
        The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
        """
        return pulumi.get(self, "uid")


class AwaitableGetShareResult(GetShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShareResult(
            client_groups=self.client_groups,
            cluster_id=self.cluster_id,
            gid=self.gid,
            id=self.id,
            location=self.location,
            name=self.name,
            nfs_path=self.nfs_path,
            partial_match=self.partial_match,
            quota=self.quota,
            uid=self.uid)


def get_share(client_groups: Optional[Sequence[Union['GetShareClientGroupArgs', 'GetShareClientGroupArgsDict']]] = None,
              cluster_id: Optional[str] = None,
              gid: Optional[int] = None,
              id: Optional[str] = None,
              location: Optional[str] = None,
              name: Optional[str] = None,
              partial_match: Optional[bool] = None,
              quota: Optional[int] = None,
              uid: Optional[int] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShareResult:
    """
    Returns information about shares of Network File Storage (NFS) on IonosCloud.


    :param Sequence[Union['GetShareClientGroupArgs', 'GetShareClientGroupArgsDict']] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
    :param str cluster_id: The ID of the Network File Storage cluster.
    :param int gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
    :param str id: ID of the Network File Storage share.
    :param str location: The location where the Network File Storage share is located.
    :param str name: Name of the Network File Storage share.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
    :param int quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
    :param int uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
    """
    __args__ = dict()
    __args__['clientGroups'] = client_groups
    __args__['clusterId'] = cluster_id
    __args__['gid'] = gid
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    __args__['quota'] = quota
    __args__['uid'] = uid
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:nfs/getShare:getShare', __args__, opts=opts, typ=GetShareResult).value

    return AwaitableGetShareResult(
        client_groups=pulumi.get(__ret__, 'client_groups'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        gid=pulumi.get(__ret__, 'gid'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        nfs_path=pulumi.get(__ret__, 'nfs_path'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        quota=pulumi.get(__ret__, 'quota'),
        uid=pulumi.get(__ret__, 'uid'))
def get_share_output(client_groups: Optional[pulumi.Input[Optional[Sequence[Union['GetShareClientGroupArgs', 'GetShareClientGroupArgsDict']]]]] = None,
                     cluster_id: Optional[pulumi.Input[str]] = None,
                     gid: Optional[pulumi.Input[Optional[int]]] = None,
                     id: Optional[pulumi.Input[Optional[str]]] = None,
                     location: Optional[pulumi.Input[str]] = None,
                     name: Optional[pulumi.Input[Optional[str]]] = None,
                     partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                     quota: Optional[pulumi.Input[Optional[int]]] = None,
                     uid: Optional[pulumi.Input[Optional[int]]] = None,
                     opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetShareResult]:
    """
    Returns information about shares of Network File Storage (NFS) on IonosCloud.


    :param Sequence[Union['GetShareClientGroupArgs', 'GetShareClientGroupArgsDict']] client_groups: The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
    :param str cluster_id: The ID of the Network File Storage cluster.
    :param int gid: The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
    :param str id: ID of the Network File Storage share.
    :param str location: The location where the Network File Storage share is located.
    :param str name: Name of the Network File Storage share.
    :param bool partial_match: Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
    :param int quota: The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
    :param int uid: The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
    """
    __args__ = dict()
    __args__['clientGroups'] = client_groups
    __args__['clusterId'] = cluster_id
    __args__['gid'] = gid
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    __args__['quota'] = quota
    __args__['uid'] = uid
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:nfs/getShare:getShare', __args__, opts=opts, typ=GetShareResult)
    return __ret__.apply(lambda __response__: GetShareResult(
        client_groups=pulumi.get(__response__, 'client_groups'),
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        gid=pulumi.get(__response__, 'gid'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        nfs_path=pulumi.get(__response__, 'nfs_path'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        quota=pulumi.get(__response__, 'quota'),
        uid=pulumi.get(__response__, 'uid')))
