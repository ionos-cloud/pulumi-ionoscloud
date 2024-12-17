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
    'TargetGroupHealthCheckArgs',
    'TargetGroupHealthCheckArgsDict',
    'TargetGroupHttpHealthCheckArgs',
    'TargetGroupHttpHealthCheckArgsDict',
    'TargetGroupTargetArgs',
    'TargetGroupTargetArgsDict',
    'GetK8sClustersFilterArgs',
    'GetK8sClustersFilterArgsDict',
    'GetServersFilterArgs',
    'GetServersFilterArgsDict',
]

MYPY = False

if not MYPY:
    class TargetGroupHealthCheckArgsDict(TypedDict):
        check_interval: NotRequired[pulumi.Input[int]]
        """
        [int] The interval in milliseconds between consecutive health checks; default is 2000.
        """
        check_timeout: NotRequired[pulumi.Input[int]]
        """
        [int] The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with 'Check Interval' set, the lesser of the two  values is used once the TCP connection is established.
        """
        retries: NotRequired[pulumi.Input[int]]
        """
        [int] The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection.
        """
elif False:
    TargetGroupHealthCheckArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TargetGroupHealthCheckArgs:
    def __init__(__self__, *,
                 check_interval: Optional[pulumi.Input[int]] = None,
                 check_timeout: Optional[pulumi.Input[int]] = None,
                 retries: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] check_interval: [int] The interval in milliseconds between consecutive health checks; default is 2000.
        :param pulumi.Input[int] check_timeout: [int] The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with 'Check Interval' set, the lesser of the two  values is used once the TCP connection is established.
        :param pulumi.Input[int] retries: [int] The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection.
        """
        if check_interval is not None:
            pulumi.set(__self__, "check_interval", check_interval)
        if check_timeout is not None:
            pulumi.set(__self__, "check_timeout", check_timeout)
        if retries is not None:
            pulumi.set(__self__, "retries", retries)

    @property
    @pulumi.getter(name="checkInterval")
    def check_interval(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The interval in milliseconds between consecutive health checks; default is 2000.
        """
        return pulumi.get(self, "check_interval")

    @check_interval.setter
    def check_interval(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "check_interval", value)

    @property
    @pulumi.getter(name="checkTimeout")
    def check_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The maximum time in milliseconds to wait for a target to respond to a check. For target VMs with 'Check Interval' set, the lesser of the two  values is used once the TCP connection is established.
        """
        return pulumi.get(self, "check_timeout")

    @check_timeout.setter
    def check_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "check_timeout", value)

    @property
    @pulumi.getter
    def retries(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The maximum number of attempts to reconnect to a target after a connection failure. Valid range is 0 to 65535, and default is three reconnection.
        """
        return pulumi.get(self, "retries")

    @retries.setter
    def retries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retries", value)


if not MYPY:
    class TargetGroupHttpHealthCheckArgsDict(TypedDict):
        match_type: pulumi.Input[str]
        """
        [string]
        """
        response: pulumi.Input[str]
        """
        [string] The response returned by the request, depending on the match type.
        """
        method: NotRequired[pulumi.Input[str]]
        """
        [string] The method for the HTTP health check.
        """
        negate: NotRequired[pulumi.Input[bool]]
        """
        [bool]
        """
        path: NotRequired[pulumi.Input[str]]
        """
        [string] The path (destination URL) for the HTTP health check request; the default is /.
        """
        regex: NotRequired[pulumi.Input[bool]]
        """
        [bool]
        """
elif False:
    TargetGroupHttpHealthCheckArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TargetGroupHttpHealthCheckArgs:
    def __init__(__self__, *,
                 match_type: pulumi.Input[str],
                 response: pulumi.Input[str],
                 method: Optional[pulumi.Input[str]] = None,
                 negate: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 regex: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[str] match_type: [string]
        :param pulumi.Input[str] response: [string] The response returned by the request, depending on the match type.
        :param pulumi.Input[str] method: [string] The method for the HTTP health check.
        :param pulumi.Input[bool] negate: [bool]
        :param pulumi.Input[str] path: [string] The path (destination URL) for the HTTP health check request; the default is /.
        :param pulumi.Input[bool] regex: [bool]
        """
        pulumi.set(__self__, "match_type", match_type)
        pulumi.set(__self__, "response", response)
        if method is not None:
            pulumi.set(__self__, "method", method)
        if negate is not None:
            pulumi.set(__self__, "negate", negate)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if regex is not None:
            pulumi.set(__self__, "regex", regex)

    @property
    @pulumi.getter(name="matchType")
    def match_type(self) -> pulumi.Input[str]:
        """
        [string]
        """
        return pulumi.get(self, "match_type")

    @match_type.setter
    def match_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "match_type", value)

    @property
    @pulumi.getter
    def response(self) -> pulumi.Input[str]:
        """
        [string] The response returned by the request, depending on the match type.
        """
        return pulumi.get(self, "response")

    @response.setter
    def response(self, value: pulumi.Input[str]):
        pulumi.set(self, "response", value)

    @property
    @pulumi.getter
    def method(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The method for the HTTP health check.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter
    def negate(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool]
        """
        return pulumi.get(self, "negate")

    @negate.setter
    def negate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "negate", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The path (destination URL) for the HTTP health check request; the default is /.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def regex(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool]
        """
        return pulumi.get(self, "regex")

    @regex.setter
    def regex(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "regex", value)


if not MYPY:
    class TargetGroupTargetArgsDict(TypedDict):
        ip: pulumi.Input[str]
        """
        [string] The IP of the balanced target VM.
        """
        port: pulumi.Input[int]
        """
        [int] The port of the balanced target service; valid range is 1 to 65535.
        """
        weight: pulumi.Input[int]
        """
        [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
        """
        health_check_enabled: NotRequired[pulumi.Input[bool]]
        """
        [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
        """
        maintenance_enabled: NotRequired[pulumi.Input[bool]]
        """
        [bool] Maintenance mode prevents the target from receiving balanced traffic.
        """
        proxy_protocol: NotRequired[pulumi.Input[str]]
        """
        [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
        """
elif False:
    TargetGroupTargetArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TargetGroupTargetArgs:
    def __init__(__self__, *,
                 ip: pulumi.Input[str],
                 port: pulumi.Input[int],
                 weight: pulumi.Input[int],
                 health_check_enabled: Optional[pulumi.Input[bool]] = None,
                 maintenance_enabled: Optional[pulumi.Input[bool]] = None,
                 proxy_protocol: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] ip: [string] The IP of the balanced target VM.
        :param pulumi.Input[int] port: [int] The port of the balanced target service; valid range is 1 to 65535.
        :param pulumi.Input[int] weight: [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
        :param pulumi.Input[bool] health_check_enabled: [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
        :param pulumi.Input[bool] maintenance_enabled: [bool] Maintenance mode prevents the target from receiving balanced traffic.
        :param pulumi.Input[str] proxy_protocol: [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
        """
        pulumi.set(__self__, "ip", ip)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "weight", weight)
        if health_check_enabled is not None:
            pulumi.set(__self__, "health_check_enabled", health_check_enabled)
        if maintenance_enabled is not None:
            pulumi.set(__self__, "maintenance_enabled", maintenance_enabled)
        if proxy_protocol is not None:
            pulumi.set(__self__, "proxy_protocol", proxy_protocol)

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Input[str]:
        """
        [string] The IP of the balanced target VM.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        [int] The port of the balanced target service; valid range is 1 to 65535.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[int]:
        """
        [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[int]):
        pulumi.set(self, "weight", value)

    @property
    @pulumi.getter(name="healthCheckEnabled")
    def health_check_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
        """
        return pulumi.get(self, "health_check_enabled")

    @health_check_enabled.setter
    def health_check_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "health_check_enabled", value)

    @property
    @pulumi.getter(name="maintenanceEnabled")
    def maintenance_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        [bool] Maintenance mode prevents the target from receiving balanced traffic.
        """
        return pulumi.get(self, "maintenance_enabled")

    @maintenance_enabled.setter
    def maintenance_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "maintenance_enabled", value)

    @property
    @pulumi.getter(name="proxyProtocol")
    def proxy_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
        """
        return pulumi.get(self, "proxy_protocol")

    @proxy_protocol.setter
    def proxy_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_protocol", value)


if not MYPY:
    class GetK8sClustersFilterArgsDict(TypedDict):
        name: str
        value: str
elif False:
    GetK8sClustersFilterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetK8sClustersFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: str):
        pulumi.set(self, "value", value)


if not MYPY:
    class GetServersFilterArgsDict(TypedDict):
        name: str
        value: str
elif False:
    GetServersFilterArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GetServersFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 value: str):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: str):
        pulumi.set(self, "value", value)


