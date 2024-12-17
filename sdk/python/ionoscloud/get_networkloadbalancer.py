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
    'GetNetworkloadbalancerResult',
    'AwaitableGetNetworkloadbalancerResult',
    'get_networkloadbalancer',
    'get_networkloadbalancer_output',
]

@pulumi.output_type
class GetNetworkloadbalancerResult:
    """
    A collection of values returned by getNetworkloadbalancer.
    """
    def __init__(__self__, central_logging=None, datacenter_id=None, flowlogs=None, id=None, ips=None, lb_private_ips=None, listener_lan=None, logging_format=None, name=None, target_lan=None):
        if central_logging and not isinstance(central_logging, bool):
            raise TypeError("Expected argument 'central_logging' to be a bool")
        pulumi.set(__self__, "central_logging", central_logging)
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if flowlogs and not isinstance(flowlogs, list):
            raise TypeError("Expected argument 'flowlogs' to be a list")
        pulumi.set(__self__, "flowlogs", flowlogs)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ips and not isinstance(ips, list):
            raise TypeError("Expected argument 'ips' to be a list")
        pulumi.set(__self__, "ips", ips)
        if lb_private_ips and not isinstance(lb_private_ips, list):
            raise TypeError("Expected argument 'lb_private_ips' to be a list")
        pulumi.set(__self__, "lb_private_ips", lb_private_ips)
        if listener_lan and not isinstance(listener_lan, int):
            raise TypeError("Expected argument 'listener_lan' to be a int")
        pulumi.set(__self__, "listener_lan", listener_lan)
        if logging_format and not isinstance(logging_format, str):
            raise TypeError("Expected argument 'logging_format' to be a str")
        pulumi.set(__self__, "logging_format", logging_format)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if target_lan and not isinstance(target_lan, int):
            raise TypeError("Expected argument 'target_lan' to be a int")
        pulumi.set(__self__, "target_lan", target_lan)

    @property
    @pulumi.getter(name="centralLogging")
    def central_logging(self) -> bool:
        """
        Turn logging on and off for this product. Default value is 'false'.
        """
        return pulumi.get(self, "central_logging")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def flowlogs(self) -> Sequence['outputs.GetNetworkloadbalancerFlowlogResult']:
        """
        Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
        """
        return pulumi.get(self, "flowlogs")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of that Network Load Balancer
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ips(self) -> Sequence[str]:
        """
        Collection of IP addresses of the Network Load Balancer. (inbound and outbound) IP of the listenerLan must be a customer reserved IP for the public load balancer and private IP for the private load balancer.
        """
        return pulumi.get(self, "ips")

    @property
    @pulumi.getter(name="lbPrivateIps")
    def lb_private_ips(self) -> Sequence[str]:
        """
        Collection of private IP addresses with subnet mask of the Network Load Balancer. IPs must contain valid subnet mask. If user will not provide any IP then the system will generate one IP with /24 subnet.
        """
        return pulumi.get(self, "lb_private_ips")

    @property
    @pulumi.getter(name="listenerLan")
    def listener_lan(self) -> int:
        """
        Id of the listening LAN. (inbound)
        """
        return pulumi.get(self, "listener_lan")

    @property
    @pulumi.getter(name="loggingFormat")
    def logging_format(self) -> str:
        return pulumi.get(self, "logging_format")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Specifies the name of the flow log.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="targetLan")
    def target_lan(self) -> int:
        """
        Id of the balanced private target LAN. (outbound)
        """
        return pulumi.get(self, "target_lan")


class AwaitableGetNetworkloadbalancerResult(GetNetworkloadbalancerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkloadbalancerResult(
            central_logging=self.central_logging,
            datacenter_id=self.datacenter_id,
            flowlogs=self.flowlogs,
            id=self.id,
            ips=self.ips,
            lb_private_ips=self.lb_private_ips,
            listener_lan=self.listener_lan,
            logging_format=self.logging_format,
            name=self.name,
            target_lan=self.target_lan)


def get_networkloadbalancer(datacenter_id: Optional[str] = None,
                            id: Optional[str] = None,
                            name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkloadbalancerResult:
    """
    The **Network Load Balancer data source** can be used to search for and return existing network load balancers.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_networkloadbalancer(datacenter_id=ionoscloud_datacenter["example"]["id"],
        name="Network Load Balancer Name")
    ```


    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the network load balancer you want to search for.
           
           `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    :param str name: Name of an existing network load balancer that you want to search for.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getNetworkloadbalancer:getNetworkloadbalancer', __args__, opts=opts, typ=GetNetworkloadbalancerResult).value

    return AwaitableGetNetworkloadbalancerResult(
        central_logging=pulumi.get(__ret__, 'central_logging'),
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        flowlogs=pulumi.get(__ret__, 'flowlogs'),
        id=pulumi.get(__ret__, 'id'),
        ips=pulumi.get(__ret__, 'ips'),
        lb_private_ips=pulumi.get(__ret__, 'lb_private_ips'),
        listener_lan=pulumi.get(__ret__, 'listener_lan'),
        logging_format=pulumi.get(__ret__, 'logging_format'),
        name=pulumi.get(__ret__, 'name'),
        target_lan=pulumi.get(__ret__, 'target_lan'))
def get_networkloadbalancer_output(datacenter_id: Optional[pulumi.Input[str]] = None,
                                   id: Optional[pulumi.Input[Optional[str]]] = None,
                                   name: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetNetworkloadbalancerResult]:
    """
    The **Network Load Balancer data source** can be used to search for and return existing network load balancers.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By Name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_networkloadbalancer(datacenter_id=ionoscloud_datacenter["example"]["id"],
        name="Network Load Balancer Name")
    ```


    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the network load balancer you want to search for.
           
           `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    :param str name: Name of an existing network load balancer that you want to search for.
    """
    __args__ = dict()
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getNetworkloadbalancer:getNetworkloadbalancer', __args__, opts=opts, typ=GetNetworkloadbalancerResult)
    return __ret__.apply(lambda __response__: GetNetworkloadbalancerResult(
        central_logging=pulumi.get(__response__, 'central_logging'),
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        flowlogs=pulumi.get(__response__, 'flowlogs'),
        id=pulumi.get(__response__, 'id'),
        ips=pulumi.get(__response__, 'ips'),
        lb_private_ips=pulumi.get(__response__, 'lb_private_ips'),
        listener_lan=pulumi.get(__response__, 'listener_lan'),
        logging_format=pulumi.get(__response__, 'logging_format'),
        name=pulumi.get(__response__, 'name'),
        target_lan=pulumi.get(__response__, 'target_lan')))
