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

__all__ = [
    'GetDnsZoneResult',
    'AwaitableGetDnsZoneResult',
    'get_dns_zone',
    'get_dns_zone_output',
]

@pulumi.output_type
class GetDnsZoneResult:
    """
    A collection of values returned by getDnsZone.
    """
    def __init__(__self__, description=None, enabled=None, id=None, name=None, nameservers=None, partial_match=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nameservers and not isinstance(nameservers, list):
            raise TypeError("Expected argument 'nameservers' to be a list")
        pulumi.set(__self__, "nameservers", nameservers)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the DNS Zone.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Indicates if the DNS Zone is activated or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The UUID of the DNS Zone.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the DNS Zone.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nameservers(self) -> Sequence[str]:
        """
        A list of available name servers.
        """
        return pulumi.get(self, "nameservers")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")


class AwaitableGetDnsZoneResult(GetDnsZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsZoneResult(
            description=self.description,
            enabled=self.enabled,
            id=self.id,
            name=self.name,
            nameservers=self.nameservers,
            partial_match=self.partial_match)


def get_dns_zone(id: Optional[str] = None,
                 name: Optional[str] = None,
                 partial_match: Optional[bool] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsZoneResult:
    """
    The **DNS Zone** can be used to search for and return an existing DNS Zone.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.

    ## Example Usage

    ### By name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dns_zone(name="example.com")
    ```

    ### By name with partial match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dns_zone(name="example",
        partial_match=True)
    ```


    :param str id: [string] The ID of the DNS Zone you want to search for.
    :param str name: [string] The name of the DNS Zone you want to search for.
    :param bool partial_match: [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getDnsZone:getDnsZone', __args__, opts=opts, typ=GetDnsZoneResult).value

    return AwaitableGetDnsZoneResult(
        description=pulumi.get(__ret__, 'description'),
        enabled=pulumi.get(__ret__, 'enabled'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        nameservers=pulumi.get(__ret__, 'nameservers'),
        partial_match=pulumi.get(__ret__, 'partial_match'))
def get_dns_zone_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                        name: Optional[pulumi.Input[Optional[str]]] = None,
                        partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDnsZoneResult]:
    """
    The **DNS Zone** can be used to search for and return an existing DNS Zone.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.

    ## Example Usage

    ### By name
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dns_zone(name="example.com")
    ```

    ### By name with partial match
    ```python
    import pulumi
    import pulumi_ionoscloud as ionoscloud

    example = ionoscloud.get_dns_zone(name="example",
        partial_match=True)
    ```


    :param str id: [string] The ID of the DNS Zone you want to search for.
    :param str name: [string] The name of the DNS Zone you want to search for.
    :param bool partial_match: [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getDnsZone:getDnsZone', __args__, opts=opts, typ=GetDnsZoneResult)
    return __ret__.apply(lambda __response__: GetDnsZoneResult(
        description=pulumi.get(__response__, 'description'),
        enabled=pulumi.get(__response__, 'enabled'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        nameservers=pulumi.get(__response__, 'nameservers'),
        partial_match=pulumi.get(__response__, 'partial_match')))
