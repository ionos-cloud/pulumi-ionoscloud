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

__all__ = [
    'GetNsgRuleResult',
]

@pulumi.output_type
class GetNsgRuleResult(dict):
    def __init__(__self__, *,
                 icmp_code: str,
                 icmp_type: str,
                 id: str,
                 name: str,
                 port_range_end: int,
                 port_range_start: int,
                 protocol: str,
                 source_ip: str,
                 source_mac: str,
                 target_ip: str,
                 type: str):
        """
        :param str id: Id of an existing Network Security Group that you want to search for.
        :param str name: Name of an existing Network Security Group that you want to search for.
               
               Either `name`, or `id` must be provided. If none, the datasource will return an error.
        """
        pulumi.set(__self__, "icmp_code", icmp_code)
        pulumi.set(__self__, "icmp_type", icmp_type)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "port_range_end", port_range_end)
        pulumi.set(__self__, "port_range_start", port_range_start)
        pulumi.set(__self__, "protocol", protocol)
        pulumi.set(__self__, "source_ip", source_ip)
        pulumi.set(__self__, "source_mac", source_mac)
        pulumi.set(__self__, "target_ip", target_ip)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="icmpCode")
    def icmp_code(self) -> str:
        return pulumi.get(self, "icmp_code")

    @property
    @pulumi.getter(name="icmpType")
    def icmp_type(self) -> str:
        return pulumi.get(self, "icmp_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Id of an existing Network Security Group that you want to search for.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing Network Security Group that you want to search for.

        Either `name`, or `id` must be provided. If none, the datasource will return an error.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portRangeEnd")
    def port_range_end(self) -> int:
        return pulumi.get(self, "port_range_end")

    @property
    @pulumi.getter(name="portRangeStart")
    def port_range_start(self) -> int:
        return pulumi.get(self, "port_range_start")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> str:
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter(name="sourceMac")
    def source_mac(self) -> str:
        return pulumi.get(self, "source_mac")

    @property
    @pulumi.getter(name="targetIp")
    def target_ip(self) -> str:
        return pulumi.get(self, "target_ip")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


