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
    'GetDnsRecordResult',
    'AwaitableGetDnsRecordResult',
    'get_dns_record',
    'get_dns_record_output',
]

@pulumi.output_type
class GetDnsRecordResult:
    """
    A collection of values returned by getDnsRecord.
    """
    def __init__(__self__, content=None, enabled=None, fqdn=None, id=None, name=None, partial_match=None, priority=None, ttl=None, type=None, zone_id=None):
        if content and not isinstance(content, str):
            raise TypeError("Expected argument 'content' to be a str")
        pulumi.set(__self__, "content", content)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def content(self) -> str:
        """
        The content of the DNS Record.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Indicates if the DNS Record is active or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The UUID of the DNS Record.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the DNS Record.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority for the DNS Record.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        The time to live of the DNS Record.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the DNS Record.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetDnsRecordResult(GetDnsRecordResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnsRecordResult(
            content=self.content,
            enabled=self.enabled,
            fqdn=self.fqdn,
            id=self.id,
            name=self.name,
            partial_match=self.partial_match,
            priority=self.priority,
            ttl=self.ttl,
            type=self.type,
            zone_id=self.zone_id)


def get_dns_record(id: Optional[str] = None,
                   name: Optional[str] = None,
                   partial_match: Optional[bool] = None,
                   zone_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnsRecordResult:
    """
    The **DNS Record** can be used to search for and return an existing DNS Record.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.

    ## Example Usage


    :param str id: [string] The ID of the DNS Record you want to search for.
    :param str name: [string] The name of the DNS Record you want to search for.
    :param bool partial_match: [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    :param str zone_id: [string] The ID of the DNS Zone in which the DNS Record can be found.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:index/getDnsRecord:getDnsRecord', __args__, opts=opts, typ=GetDnsRecordResult).value

    return AwaitableGetDnsRecordResult(
        content=pulumi.get(__ret__, 'content'),
        enabled=pulumi.get(__ret__, 'enabled'),
        fqdn=pulumi.get(__ret__, 'fqdn'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        priority=pulumi.get(__ret__, 'priority'),
        ttl=pulumi.get(__ret__, 'ttl'),
        type=pulumi.get(__ret__, 'type'),
        zone_id=pulumi.get(__ret__, 'zone_id'))
def get_dns_record_output(id: Optional[pulumi.Input[Optional[str]]] = None,
                          name: Optional[pulumi.Input[Optional[str]]] = None,
                          partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                          zone_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetDnsRecordResult]:
    """
    The **DNS Record** can be used to search for and return an existing DNS Record.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.

    ## Example Usage


    :param str id: [string] The ID of the DNS Record you want to search for.
    :param str name: [string] The name of the DNS Record you want to search for.
    :param bool partial_match: [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    :param str zone_id: [string] The ID of the DNS Zone in which the DNS Record can be found.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    __args__['zoneId'] = zone_id
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:index/getDnsRecord:getDnsRecord', __args__, opts=opts, typ=GetDnsRecordResult)
    return __ret__.apply(lambda __response__: GetDnsRecordResult(
        content=pulumi.get(__response__, 'content'),
        enabled=pulumi.get(__response__, 'enabled'),
        fqdn=pulumi.get(__response__, 'fqdn'),
        id=pulumi.get(__response__, 'id'),
        name=pulumi.get(__response__, 'name'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        priority=pulumi.get(__response__, 'priority'),
        ttl=pulumi.get(__response__, 'ttl'),
        type=pulumi.get(__response__, 'type'),
        zone_id=pulumi.get(__response__, 'zone_id')))
