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
    'ApigatewayCustomDomain',
    'RouteUpstream',
    'GetApigatewayCustomDomainResult',
    'GetRouteUpstreamResult',
]

@pulumi.output_type
class ApigatewayCustomDomain(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "certificateId":
            suggest = "certificate_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApigatewayCustomDomain. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApigatewayCustomDomain.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApigatewayCustomDomain.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 certificate_id: Optional[str] = None):
        """
        :param str name: [string] The domain name. Externally reachable.
        :param str certificate_id: [string] The certificate ID for the domain. Must be a valid certificate in UUID form.
        """
        pulumi.set(__self__, "name", name)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        [string] The domain name. Externally reachable.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[str]:
        """
        [string] The certificate ID for the domain. Must be a valid certificate in UUID form.
        """
        return pulumi.get(self, "certificate_id")


@pulumi.output_type
class RouteUpstream(dict):
    def __init__(__self__, *,
                 host: str,
                 loadbalancer: Optional[str] = None,
                 port: Optional[int] = None,
                 scheme: Optional[str] = None,
                 weight: Optional[int] = None):
        """
        :param str host: [string] The host of the upstream.
        :param str loadbalancer: [string] The load balancer algorithm. Default value: `roundrobin`.
        :param int port: [int] The port of the upstream. Default value: `80`.
        :param str scheme: [string] The target URL of the upstream. Default value: `http`.
        :param int weight: [int] Weight with which to split traffic to the upstream. Default value: `100`.
        """
        pulumi.set(__self__, "host", host)
        if loadbalancer is not None:
            pulumi.set(__self__, "loadbalancer", loadbalancer)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if scheme is not None:
            pulumi.set(__self__, "scheme", scheme)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        [string] The host of the upstream.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def loadbalancer(self) -> Optional[str]:
        """
        [string] The load balancer algorithm. Default value: `roundrobin`.
        """
        return pulumi.get(self, "loadbalancer")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        [int] The port of the upstream. Default value: `80`.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def scheme(self) -> Optional[str]:
        """
        [string] The target URL of the upstream. Default value: `http`.
        """
        return pulumi.get(self, "scheme")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        """
        [int] Weight with which to split traffic to the upstream. Default value: `100`.
        """
        return pulumi.get(self, "weight")


@pulumi.output_type
class GetApigatewayCustomDomainResult(dict):
    def __init__(__self__, *,
                 certificate_id: str,
                 name: str):
        """
        :param str certificate_id: The ID of the certificate to use for the distribution.
        :param str name: Name of an existing API Gateway that you want to search for.
        """
        pulumi.set(__self__, "certificate_id", certificate_id)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> str:
        """
        The ID of the certificate to use for the distribution.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing API Gateway that you want to search for.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetRouteUpstreamResult(dict):
    def __init__(__self__, *,
                 host: str,
                 loadbalancer: str,
                 port: int,
                 scheme: str,
                 weight: int):
        """
        :param str host: The host of the upstream.
        :param str loadbalancer: The load balancer algorithm.
        :param int port: The port of the upstream.
        :param str scheme: The target URL of the upstream.
        :param int weight: Weight with which to split traffic to the upstream.
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "loadbalancer", loadbalancer)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "scheme", scheme)
        pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def host(self) -> str:
        """
        The host of the upstream.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def loadbalancer(self) -> str:
        """
        The load balancer algorithm.
        """
        return pulumi.get(self, "loadbalancer")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        The port of the upstream.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def scheme(self) -> str:
        """
        The target URL of the upstream.
        """
        return pulumi.get(self, "scheme")

    @property
    @pulumi.getter
    def weight(self) -> int:
        """
        Weight with which to split traffic to the upstream.
        """
        return pulumi.get(self, "weight")


