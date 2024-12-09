# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetApplicationLoadbalancerForwardingruleResult',
    'AwaitableGetApplicationLoadbalancerForwardingruleResult',
    'get_application_loadbalancer_forwardingrule',
    'get_application_loadbalancer_forwardingrule_output',
]

@pulumi.output_type
class GetApplicationLoadbalancerForwardingruleResult:
    """
    A collection of values returned by getApplicationLoadbalancerForwardingrule.
    """
    def __init__(__self__, application_loadbalancer_id=None, client_timeout=None, datacenter_id=None, http_rules=None, id=None, listener_ip=None, listener_port=None, name=None, partial_match=None, protocol=None, server_certificates=None):
        if application_loadbalancer_id and not isinstance(application_loadbalancer_id, str):
            raise TypeError("Expected argument 'application_loadbalancer_id' to be a str")
        pulumi.set(__self__, "application_loadbalancer_id", application_loadbalancer_id)
        if client_timeout and not isinstance(client_timeout, int):
            raise TypeError("Expected argument 'client_timeout' to be a int")
        pulumi.set(__self__, "client_timeout", client_timeout)
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if http_rules and not isinstance(http_rules, list):
            raise TypeError("Expected argument 'http_rules' to be a list")
        pulumi.set(__self__, "http_rules", http_rules)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if listener_ip and not isinstance(listener_ip, str):
            raise TypeError("Expected argument 'listener_ip' to be a str")
        pulumi.set(__self__, "listener_ip", listener_ip)
        if listener_port and not isinstance(listener_port, int):
            raise TypeError("Expected argument 'listener_port' to be a int")
        pulumi.set(__self__, "listener_port", listener_port)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if server_certificates and not isinstance(server_certificates, list):
            raise TypeError("Expected argument 'server_certificates' to be a list")
        pulumi.set(__self__, "server_certificates", server_certificates)

    @property
    @pulumi.getter(name="applicationLoadbalancerId")
    def application_loadbalancer_id(self) -> str:
        return pulumi.get(self, "application_loadbalancer_id")

    @property
    @pulumi.getter(name="clientTimeout")
    def client_timeout(self) -> int:
        """
        The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
        - `server certificates` - Array of items in that collection.
        """
        return pulumi.get(self, "client_timeout")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter(name="httpRules")
    def http_rules(self) -> Sequence['outputs.GetApplicationLoadbalancerForwardingruleHttpRuleResult']:
        """
        Array of items in that collection
        """
        return pulumi.get(self, "http_rules")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Id of Application Load Balancer Forwarding Rule
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="listenerIp")
    def listener_ip(self) -> str:
        """
        Listening (inbound) IP.
        """
        return pulumi.get(self, "listener_ip")

    @property
    @pulumi.getter(name="listenerPort")
    def listener_port(self) -> int:
        """
        Listening (inbound) port number; valid range is 1 to 65535.
        """
        return pulumi.get(self, "listener_port")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The unique name of the Application Load Balancer HTTP rule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Balancing protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="serverCertificates")
    def server_certificates(self) -> Sequence[str]:
        return pulumi.get(self, "server_certificates")


class AwaitableGetApplicationLoadbalancerForwardingruleResult(GetApplicationLoadbalancerForwardingruleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationLoadbalancerForwardingruleResult(
            application_loadbalancer_id=self.application_loadbalancer_id,
            client_timeout=self.client_timeout,
            datacenter_id=self.datacenter_id,
            http_rules=self.http_rules,
            id=self.id,
            listener_ip=self.listener_ip,
            listener_port=self.listener_port,
            name=self.name,
            partial_match=self.partial_match,
            protocol=self.protocol,
            server_certificates=self.server_certificates)


def get_application_loadbalancer_forwardingrule(application_loadbalancer_id: Optional[str] = None,
                                                datacenter_id: Optional[str] = None,
                                                id: Optional[str] = None,
                                                name: Optional[str] = None,
                                                partial_match: Optional[bool] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationLoadbalancerForwardingruleResult:
    """
    The Application Load Balancer Forwarding Rule data source can be used to search for and return an existing Application Load Balancer Forwarding Rules.
    You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers Forwarding Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_application_loadbalancer_forwardingrule(datacenter_id=ionoscloud_datacenter["example"]["id"],
        application_loadbalancer_id=ionoscloud_application_loadbalancer["example"]["id"],
        name="ALB FR Example")
    ```
    <!--End PulumiCodeChooser -->

    ### By Name with Partial Match
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_application_loadbalancer_forwardingrule(datacenter_id=ionoscloud_datacenter["example"]["id"],
        application_loadbalancer_id=ionoscloud_application_loadbalancer["example"]["id"],
        name="Example",
        partial_match=True)
    ```
    <!--End PulumiCodeChooser -->


    :param str application_loadbalancer_id: Application Load Balancer's UUID.
    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the application load balancer you want to search for.
    :param str name: Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['applicationLoadbalancerId'] = application_loadbalancer_id
    __args__['datacenterId'] = datacenter_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getApplicationLoadbalancerForwardingrule:getApplicationLoadbalancerForwardingrule', __args__, opts=opts, typ=GetApplicationLoadbalancerForwardingruleResult).value

    return AwaitableGetApplicationLoadbalancerForwardingruleResult(
        application_loadbalancer_id=pulumi.get(__ret__, 'application_loadbalancer_id'),
        client_timeout=pulumi.get(__ret__, 'client_timeout'),
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        http_rules=pulumi.get(__ret__, 'http_rules'),
        id=pulumi.get(__ret__, 'id'),
        listener_ip=pulumi.get(__ret__, 'listener_ip'),
        listener_port=pulumi.get(__ret__, 'listener_port'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        protocol=pulumi.get(__ret__, 'protocol'),
        server_certificates=pulumi.get(__ret__, 'server_certificates'))


@_utilities.lift_output_func(get_application_loadbalancer_forwardingrule)
def get_application_loadbalancer_forwardingrule_output(application_loadbalancer_id: Optional[pulumi.Input[str]] = None,
                                                       datacenter_id: Optional[pulumi.Input[str]] = None,
                                                       id: Optional[pulumi.Input[Optional[str]]] = None,
                                                       name: Optional[pulumi.Input[Optional[str]]] = None,
                                                       partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationLoadbalancerForwardingruleResult]:
    """
    The Application Load Balancer Forwarding Rule data source can be used to search for and return an existing Application Load Balancer Forwarding Rules.
    You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers Forwarding Rules.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage

    ### By Name
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_application_loadbalancer_forwardingrule(datacenter_id=ionoscloud_datacenter["example"]["id"],
        application_loadbalancer_id=ionoscloud_application_loadbalancer["example"]["id"],
        name="ALB FR Example")
    ```
    <!--End PulumiCodeChooser -->

    ### By Name with Partial Match
    <!--Start PulumiCodeChooser -->
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_application_loadbalancer_forwardingrule(datacenter_id=ionoscloud_datacenter["example"]["id"],
        application_loadbalancer_id=ionoscloud_application_loadbalancer["example"]["id"],
        name="Example",
        partial_match=True)
    ```
    <!--End PulumiCodeChooser -->


    :param str application_loadbalancer_id: Application Load Balancer's UUID.
    :param str datacenter_id: Datacenter's UUID.
    :param str id: ID of the application load balancer you want to search for.
    :param str name: Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Both `datacenter_id` and `application_loadbalancer_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
    """
    ...
