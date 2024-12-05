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
    'GetIpfailoverResult',
    'AwaitableGetIpfailoverResult',
    'get_ipfailover',
    'get_ipfailover_output',
]

@pulumi.output_type
class GetIpfailoverResult:
    """
    A collection of values returned by getIpfailover.
    """
    def __init__(__self__, datacenter_id=None, id=None, ip=None, lan_id=None, nicuuid=None):
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip and not isinstance(ip, str):
            raise TypeError("Expected argument 'ip' to be a str")
        pulumi.set(__self__, "ip", ip)
        if lan_id and not isinstance(lan_id, str):
            raise TypeError("Expected argument 'lan_id' to be a str")
        pulumi.set(__self__, "lan_id", lan_id)
        if nicuuid and not isinstance(nicuuid, str):
            raise TypeError("Expected argument 'nicuuid' to be a str")
        pulumi.set(__self__, "nicuuid", nicuuid)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The ID of a Data Center.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ip(self) -> str:
        """
        The reserved IP address to be used in the IP failover group.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        The ID of a LAN.
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter
    def nicuuid(self) -> str:
        """
        The ID of a NIC.
        """
        return pulumi.get(self, "nicuuid")


class AwaitableGetIpfailoverResult(GetIpfailoverResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpfailoverResult(
            datacenter_id=self.datacenter_id,
            id=self.id,
            ip=self.ip,
            lan_id=self.lan_id,
            nicuuid=self.nicuuid)


def get_ipfailover(datacenter_id: Optional[str] = None,
                   ip: Optional[str] = None,
                   lan_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpfailoverResult:
    """
    The **IP Failover data source** can be used to search for and return an existing IP Failover object.
    You need to provide the datacenter_id and the id of the lan to get the ip failover object for the provided datacenter.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.


    :param str datacenter_id: The ID of the datacenter containing the ip failover datasource
    :param str ip: The reserved IP address to be used in the IP failover group.
    :param str lan_id: The ID of a LAN.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['ip'] = ip
    __args__['lanId'] = lan_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getIpfailover:getIpfailover', __args__, opts=opts, typ=GetIpfailoverResult).value

    return AwaitableGetIpfailoverResult(
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        id=pulumi.get(__ret__, 'id'),
        ip=pulumi.get(__ret__, 'ip'),
        lan_id=pulumi.get(__ret__, 'lan_id'),
        nicuuid=pulumi.get(__ret__, 'nicuuid'))
def get_ipfailover_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                          ip: Optional[pulumi.Input[str]] = None,
                          lan_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpfailoverResult]:
    """
    The **IP Failover data source** can be used to search for and return an existing IP Failover object.
    You need to provide the datacenter_id and the id of the lan to get the ip failover object for the provided datacenter.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.


    :param str datacenter_id: The ID of the datacenter containing the ip failover datasource
    :param str ip: The reserved IP address to be used in the IP failover group.
    :param str lan_id: The ID of a LAN.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['ip'] = ip
    __args__['lanId'] = lan_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getIpfailover:getIpfailover', __args__, opts=opts, typ=GetIpfailoverResult)
    return __ret__.apply(lambda __response__: GetIpfailoverResult(
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        id=pulumi.get(__response__, 'id'),
        ip=pulumi.get(__response__, 'ip'),
        lan_id=pulumi.get(__response__, 'lan_id'),
        nicuuid=pulumi.get(__response__, 'nicuuid')))
