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
    'GetIpsecGatewayResult',
    'AwaitableGetIpsecGatewayResult',
    'get_ipsec_gateway',
    'get_ipsec_gateway_output',
]

@pulumi.output_type
class GetIpsecGatewayResult:
    """
    A collection of values returned by getIpsecGateway.
    """
    def __init__(__self__, connections=None, description=None, gateway_ip=None, id=None, location=None, maintenance_windows=None, name=None, tier=None, version=None):
        if connections and not isinstance(connections, list):
            raise TypeError("Expected argument 'connections' to be a list")
        pulumi.set(__self__, "connections", connections)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if gateway_ip and not isinstance(gateway_ip, str):
            raise TypeError("Expected argument 'gateway_ip' to be a str")
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def connections(self) -> Sequence['outputs.GetIpsecGatewayConnectionResult']:
        """
        The network connection for your gateway.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (Optional)[string] The human-readable description of the IPSec Gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> str:
        """
        Public IP address to be assigned to the gateway.
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique ID of the IPSec Gateway.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetIpsecGatewayMaintenanceWindowResult']:
        """
        A weekly 4 hour-long window, during which maintenance might occur.
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the IPSec Gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        Gateway performance options.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The IKE version that is permitted for the VPN tunnels.
        """
        return pulumi.get(self, "version")


class AwaitableGetIpsecGatewayResult(GetIpsecGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpsecGatewayResult(
            connections=self.connections,
            description=self.description,
            gateway_ip=self.gateway_ip,
            id=self.id,
            location=self.location,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            tier=self.tier,
            version=self.version)


def get_ipsec_gateway(id: Optional[str] = None,
                      location: Optional[str] = None,
                      name: Optional[str] = None,
                      version: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpsecGatewayResult:
    """
    The **VPN IPSec Gateway data source** can be used to search for and return an existing IPSec Gateway.
    You can provide a string for the name parameter which will be compared with provisioned IPSec Gateways.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By ID

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_ipsec_gateway(id="gateway_id",
        location="gateway_location")
    ```

    ### By Name

    Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
    this data source is called.

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_ipsec_gateway(name="ipsec-gateway",
        location="gateway_location")
    ```


    :param str id: ID of an existing IPSec Gateway that you want to search for.
    :param str location: The location of the IPSec Gateway.
    :param str name: Name of an existing IPSec Gateway that you want to search for.
    :param str version: The IKE version that is permitted for the VPN tunnels.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:vpn/getIpsecGateway:getIpsecGateway', __args__, opts=opts, typ=GetIpsecGatewayResult).value

    return AwaitableGetIpsecGatewayResult(
        connections=pulumi.get(__ret__, 'connections'),
        description=pulumi.get(__ret__, 'description'),
        gateway_ip=pulumi.get(__ret__, 'gateway_ip'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        tier=pulumi.get(__ret__, 'tier'),
        version=pulumi.get(__ret__, 'version'))
def get_ipsec_gateway_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                             location: Optional[pulumi.Input[Optional[str]]] = None,
                             name: Optional[pulumi.Input[Optional[str]]] = None,
                             version: Optional[pulumi.Input[Optional[str]]] = None,
                             opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetIpsecGatewayResult]:
    """
    The **VPN IPSec Gateway data source** can be used to search for and return an existing IPSec Gateway.
    You can provide a string for the name parameter which will be compared with provisioned IPSec Gateways.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search string so that it is specific enough to return only one result.

    ## Example Usage

    ### By ID

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_ipsec_gateway(id="gateway_id",
        location="gateway_location")
    ```

    ### By Name

    Needs to have the resource be previously created, or a depends_on clause to ensure that the resource is created before
    this data source is called.

    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.vpn.get_ipsec_gateway(name="ipsec-gateway",
        location="gateway_location")
    ```


    :param str id: ID of an existing IPSec Gateway that you want to search for.
    :param str location: The location of the IPSec Gateway.
    :param str name: Name of an existing IPSec Gateway that you want to search for.
    :param str version: The IKE version that is permitted for the VPN tunnels.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['location'] = location
    __args__['name'] = name
    __args__['version'] = version
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:vpn/getIpsecGateway:getIpsecGateway', __args__, opts=opts, typ=GetIpsecGatewayResult)
    return __ret__.apply(lambda __response__: GetIpsecGatewayResult(
        connections=pulumi.get(__response__, 'connections'),
        description=pulumi.get(__response__, 'description'),
        gateway_ip=pulumi.get(__response__, 'gateway_ip'),
        id=pulumi.get(__response__, 'id'),
        location=pulumi.get(__response__, 'location'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        tier=pulumi.get(__response__, 'tier'),
        version=pulumi.get(__response__, 'version')))
