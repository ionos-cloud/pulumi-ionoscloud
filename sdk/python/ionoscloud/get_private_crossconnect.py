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
    'GetPrivateCrossconnectResult',
    'AwaitableGetPrivateCrossconnectResult',
    'get_private_crossconnect',
    'get_private_crossconnect_output',
]

@pulumi.output_type
class GetPrivateCrossconnectResult:
    """
    A collection of values returned by getPrivateCrossconnect.
    """
    def __init__(__self__, connectable_datacenters=None, description=None, id=None, name=None, peers=None):
        if connectable_datacenters and not isinstance(connectable_datacenters, list):
            raise TypeError("Expected argument 'connectable_datacenters' to be a list")
        pulumi.set(__self__, "connectable_datacenters", connectable_datacenters)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if peers and not isinstance(peers, list):
            raise TypeError("Expected argument 'peers' to be a list")
        pulumi.set(__self__, "peers", peers)

    @property
    @pulumi.getter(name="connectableDatacenters")
    def connectable_datacenters(self) -> Sequence['outputs.GetPrivateCrossconnectConnectableDatacenterResult']:
        """
        Lists datacenters that can be joined to this cross connect
        """
        return pulumi.get(self, "connectable_datacenters")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of cross connect
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The UUID of the connectable datacenter
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the connectable datacenter
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def peers(self) -> Sequence['outputs.GetPrivateCrossconnectPeerResult']:
        """
        Lists LAN's joined to this cross connect
        """
        return pulumi.get(self, "peers")


class AwaitableGetPrivateCrossconnectResult(GetPrivateCrossconnectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateCrossconnectResult(
            connectable_datacenters=self.connectable_datacenters,
            description=self.description,
            id=self.id,
            name=self.name,
            peers=self.peers)


def get_private_crossconnect(description: Optional[str] = None,
                             id: Optional[str] = None,
                             name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateCrossconnectResult:
    """
    The **Cross Connect data source** can be used to search for and return existing cross connects.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_private_crossconnect(name="Cross Connect Example")
    ```


    :param str description: Description of cross connect
    :param str id: ID of the cross connect you want to search for.
           
           Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str name: Name of an existing cross connect that you want to search for.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect', __args__, opts=opts, typ=GetPrivateCrossconnectResult).value

    return AwaitableGetPrivateCrossconnectResult(
        connectable_datacenters=pulumi.get(__ret__, 'connectable_datacenters'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        peers=pulumi.get(__ret__, 'peers'))
def get_private_crossconnect_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                                    id: Optional[pulumi.Input[Optional[str]]] = None,
                                    name: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetPrivateCrossconnectResult]:
    """
    The **Cross Connect data source** can be used to search for and return existing cross connects.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_private_crossconnect(name="Cross Connect Example")
    ```


    :param str description: Description of cross connect
    :param str id: ID of the cross connect you want to search for.
           
           Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
    :param str name: Name of an existing cross connect that you want to search for.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getPrivateCrossconnect:getPrivateCrossconnect', __args__, opts=opts, typ=GetPrivateCrossconnectResult)
    return __ret__.apply(lambda __response__: GetPrivateCrossconnectResult(
        connectable_datacenters=pulumi.get(__response__, 'connectable_datacenters'),
        description=pulumi.get(__response__, 'description'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        peers=pulumi.get(__response__, 'peers')))
