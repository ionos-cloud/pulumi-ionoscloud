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
    'GetIPBlockResult',
    'AwaitableGetIPBlockResult',
    'get_ip_block',
    'get_ip_block_output',
]

@pulumi.output_type
class GetIPBlockResult:
    """
    A collection of values returned by getIPBlock.
    """
    def __init__(__self__, id=None, ip_consumers=None, ips=None, location=None, name=None, size=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_consumers and not isinstance(ip_consumers, list):
            raise TypeError("Expected argument 'ip_consumers' to be a list")
        pulumi.set(__self__, "ip_consumers", ip_consumers)
        if ips and not isinstance(ips, list):
            raise TypeError("Expected argument 'ips' to be a list")
        pulumi.set(__self__, "ips", ips)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The id of Ip Block
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipConsumers")
    def ip_consumers(self) -> Sequence['outputs.GetIPBlockIpConsumerResult']:
        """
        Read-Only attribute. Lists consumption detail of an individual ip
        """
        return pulumi.get(self, "ip_consumers")

    @property
    @pulumi.getter
    def ips(self) -> Sequence[str]:
        """
        The list of IP addresses associated with this block.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of Ip Block
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The number of IP addresses to reserve for this block.
        """
        return pulumi.get(self, "size")


class AwaitableGetIPBlockResult(GetIPBlockResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIPBlockResult(
            id=self.id,
            ip_consumers=self.ip_consumers,
            ips=self.ips,
            location=self.location,
            name=self.name,
            size=self.size)


def get_ip_block(id: Optional[str] = None,
                 location: Optional[str] = None,
                 name: Optional[str] = None,
                 size: Optional[int] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIPBlockResult:
    """
    The **IP Block data source** can be used to search for and return an existing Ip Block.
    You can provide a string for the id, the name or the location parameters which will be compared with the provisioned Ip Blocks.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By ID
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(id="ipblock_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(name="IP Block Name")
    ```

    ### By Location
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(location="us/las")
    ```

    ### By Name & Location


    :param str id: ID of an existing Ip Block that you want to search for.
    :param str location: The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
    :param str name: Name of an existing Ip Block that you want to search for.
    :param int size: The number of IP addresses to reserve for this block.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['size'] = size
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:compute/getIPBlock:getIPBlock', __args__, opts=opts, typ=GetIPBlockResult).value

    return AwaitableGetIPBlockResult(
        id=pulumi.get(__ret__, 'id'),
        ip_consumers=pulumi.get(__ret__, 'ip_consumers'),
        ips=pulumi.get(__ret__, 'ips'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        size=pulumi.get(__ret__, 'size'))
def get_ip_block_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                        location: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        size: Optional[pulumi.Input[Optional[int]]] = None,
                        opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetIPBlockResult]:
    """
    The **IP Block data source** can be used to search for and return an existing Ip Block.
    You can provide a string for the id, the name or the location parameters which will be compared with the provisioned Ip Blocks.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By ID
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(id="ipblock_id")
    ```

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(name="IP Block Name")
    ```

    ### By Location
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.compute.get_ip_block(location="us/las")
    ```

    ### By Name & Location


    :param str id: ID of an existing Ip Block that you want to search for.
    :param str location: The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
    :param str name: Name of an existing Ip Block that you want to search for.
    :param int size: The number of IP addresses to reserve for this block.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['size'] = size
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:compute/getIPBlock:getIPBlock', __args__, opts=opts, typ=GetIPBlockResult)
    return __ret__.apply(lambda __response__: GetIPBlockResult(
        id=pulumi.get(__response__, 'id'),
        ip_consumers=pulumi.get(__response__, 'ip_consumers'),
        ips=pulumi.get(__response__, 'ips'),
        location=pulumi.get(__response__, 'location'),
        name=pulumi.get(__response__, 'name'),
        size=pulumi.get(__response__, 'size')))
