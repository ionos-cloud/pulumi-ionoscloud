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
    'ClusterMaintenanceWindow',
    'ClusterS3Bucket',
    'NodePoolAutoScaling',
    'NodePoolLan',
    'NodePoolLanRoute',
    'NodePoolMaintenanceWindow',
    'GetClusterConfigResult',
    'GetClusterConfigClusterResult',
    'GetClusterConfigContextResult',
    'GetClusterConfigUserResult',
    'GetClusterMaintenanceWindowResult',
    'GetClusterS3BucketResult',
    'GetNodePoolAutoScalingResult',
    'GetNodePoolLanResult',
    'GetNodePoolLanRouteResult',
    'GetNodePoolMaintenanceWindowResult',
]

@pulumi.output_type
class ClusterMaintenanceWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfTheWeek":
            suggest = "day_of_the_week"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterMaintenanceWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterMaintenanceWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterMaintenanceWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: [string] Day of the week when maintenance is allowed
        :param str time: [string] A clock time in the day when maintenance is allowed
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] Day of the week when maintenance is allowed
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] A clock time in the day when maintenance is allowed
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class ClusterS3Bucket(dict):
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        :param str name: [string] The name of the Kubernetes Cluster.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        [string] The name of the Kubernetes Cluster.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class NodePoolAutoScaling(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maxNodeCount":
            suggest = "max_node_count"
        elif key == "minNodeCount":
            suggest = "min_node_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodePoolAutoScaling. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodePoolAutoScaling.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodePoolAutoScaling.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 max_node_count: int,
                 min_node_count: int):
        """
        :param int max_node_count: [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
        :param int min_node_count: [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
        """
        pulumi.set(__self__, "max_node_count", max_node_count)
        pulumi.set(__self__, "min_node_count", min_node_count)

    @property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> int:
        """
        [int] The maximum number of worker nodes that the node pool can scale to. Should be greater than min_node_count
        """
        return pulumi.get(self, "max_node_count")

    @property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> int:
        """
        [int] The minimum number of worker nodes the node pool can scale down to. Should be less than max_node_count
        """
        return pulumi.get(self, "min_node_count")


@pulumi.output_type
class NodePoolLan(dict):
    def __init__(__self__, *,
                 id: int,
                 dhcp: Optional[bool] = None,
                 routes: Optional[Sequence['outputs.NodePoolLanRoute']] = None):
        """
        :param int id: [int] The LAN ID of an existing LAN at the related datacenter
        :param bool dhcp: [boolean] Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP. Default value is `true`
        :param Sequence['NodePoolLanRouteArgs'] routes: An array of additional LANs attached to worker nodes
        """
        pulumi.set(__self__, "id", id)
        if dhcp is not None:
            pulumi.set(__self__, "dhcp", dhcp)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        [int] The LAN ID of an existing LAN at the related datacenter
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def dhcp(self) -> Optional[bool]:
        """
        [boolean] Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP. Default value is `true`
        """
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter
    def routes(self) -> Optional[Sequence['outputs.NodePoolLanRoute']]:
        """
        An array of additional LANs attached to worker nodes
        """
        return pulumi.get(self, "routes")


@pulumi.output_type
class NodePoolLanRoute(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gatewayIp":
            suggest = "gateway_ip"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodePoolLanRoute. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodePoolLanRoute.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodePoolLanRoute.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gateway_ip: str,
                 network: str):
        """
        :param str gateway_ip: [string] IPv4 or IPv6 Gateway IP for the route
        :param str network: [string] IPv4 or IPv6 CIDR to be routed via the interface
        """
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        pulumi.set(__self__, "network", network)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> str:
        """
        [string] IPv4 or IPv6 Gateway IP for the route
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        [string] IPv4 or IPv6 CIDR to be routed via the interface
        """
        return pulumi.get(self, "network")


@pulumi.output_type
class NodePoolMaintenanceWindow(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfTheWeek":
            suggest = "day_of_the_week"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NodePoolMaintenanceWindow. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NodePoolMaintenanceWindow.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NodePoolMaintenanceWindow.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: [string] Day of the week when maintenance is allowed
        :param str time: [string] A clock time in the day when maintenance is allowed
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] Day of the week when maintenance is allowed
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] A clock time in the day when maintenance is allowed
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetClusterConfigResult(dict):
    def __init__(__self__, *,
                 api_version: str,
                 clusters: Sequence['outputs.GetClusterConfigClusterResult'],
                 contexts: Sequence['outputs.GetClusterConfigContextResult'],
                 current_context: str,
                 kind: str,
                 users: Sequence['outputs.GetClusterConfigUserResult']):
        pulumi.set(__self__, "api_version", api_version)
        pulumi.set(__self__, "clusters", clusters)
        pulumi.set(__self__, "contexts", contexts)
        pulumi.set(__self__, "current_context", current_context)
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> str:
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def clusters(self) -> Sequence['outputs.GetClusterConfigClusterResult']:
        return pulumi.get(self, "clusters")

    @property
    @pulumi.getter
    def contexts(self) -> Sequence['outputs.GetClusterConfigContextResult']:
        return pulumi.get(self, "contexts")

    @property
    @pulumi.getter(name="currentContext")
    def current_context(self) -> str:
        return pulumi.get(self, "current_context")

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def users(self) -> Sequence['outputs.GetClusterConfigUserResult']:
        return pulumi.get(self, "users")


@pulumi.output_type
class GetClusterConfigClusterResult(dict):
    def __init__(__self__, *,
                 cluster: Mapping[str, str],
                 name: str):
        """
        :param str name: Name of an existing cluster that you want to search for.
        """
        pulumi.set(__self__, "cluster", cluster)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def cluster(self) -> Mapping[str, str]:
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetClusterConfigContextResult(dict):
    def __init__(__self__, *,
                 context: Mapping[str, str],
                 name: str):
        """
        :param str name: Name of an existing cluster that you want to search for.
        """
        pulumi.set(__self__, "context", context)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def context(self) -> Mapping[str, str]:
        return pulumi.get(self, "context")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetClusterConfigUserResult(dict):
    def __init__(__self__, *,
                 name: str,
                 user: Mapping[str, str]):
        """
        :param str name: Name of an existing cluster that you want to search for.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def user(self) -> Mapping[str, str]:
        return pulumi.get(self, "user")


@pulumi.output_type
class GetClusterMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: Day of the week when maintenance is allowed
        :param str time: A clock time in the day when maintenance is allowed
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        Day of the week when maintenance is allowed
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        A clock time in the day when maintenance is allowed
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetClusterS3BucketResult(dict):
    def __init__(__self__, *,
                 name: str):
        """
        :param str name: Name of an existing cluster that you want to search for.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetNodePoolAutoScalingResult(dict):
    def __init__(__self__, *,
                 max_node_count: int,
                 min_node_count: int):
        """
        :param int max_node_count: The maximum number of worker nodes that the node pool can scale to
        :param int min_node_count: The minimum number of worker nodes the node pool can scale down to
        """
        pulumi.set(__self__, "max_node_count", max_node_count)
        pulumi.set(__self__, "min_node_count", min_node_count)

    @property
    @pulumi.getter(name="maxNodeCount")
    def max_node_count(self) -> int:
        """
        The maximum number of worker nodes that the node pool can scale to
        """
        return pulumi.get(self, "max_node_count")

    @property
    @pulumi.getter(name="minNodeCount")
    def min_node_count(self) -> int:
        """
        The minimum number of worker nodes the node pool can scale down to
        """
        return pulumi.get(self, "min_node_count")


@pulumi.output_type
class GetNodePoolLanResult(dict):
    def __init__(__self__, *,
                 dhcp: bool,
                 id: int,
                 routes: Optional[Sequence['outputs.GetNodePoolLanRouteResult']] = None):
        """
        :param bool dhcp: Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP
        :param int id: ID of the node pool you want to search for.
               
               `k8s_cluster_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        :param Sequence['GetNodePoolLanRouteArgs'] routes: An array of additional LANs attached to worker nodes
        """
        pulumi.set(__self__, "dhcp", dhcp)
        pulumi.set(__self__, "id", id)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)

    @property
    @pulumi.getter
    def dhcp(self) -> bool:
        """
        Indicates if the Kubernetes Node Pool LAN will reserve an IP using DHCP
        """
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        ID of the node pool you want to search for.

        `k8s_cluster_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def routes(self) -> Optional[Sequence['outputs.GetNodePoolLanRouteResult']]:
        """
        An array of additional LANs attached to worker nodes
        """
        return pulumi.get(self, "routes")


@pulumi.output_type
class GetNodePoolLanRouteResult(dict):
    def __init__(__self__, *,
                 gateway_ip: str,
                 network: str):
        """
        :param str gateway_ip: IPv4 or IPv6 Gateway IP for the route
        :param str network: IPv4 or IPv6 CIDR to be routed via the interface
        """
        pulumi.set(__self__, "gateway_ip", gateway_ip)
        pulumi.set(__self__, "network", network)

    @property
    @pulumi.getter(name="gatewayIp")
    def gateway_ip(self) -> str:
        """
        IPv4 or IPv6 Gateway IP for the route
        """
        return pulumi.get(self, "gateway_ip")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        IPv4 or IPv6 CIDR to be routed via the interface
        """
        return pulumi.get(self, "network")


@pulumi.output_type
class GetNodePoolMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str day_of_the_week: Day of the week when maintenance is allowed
        :param str time: A clock time in the day when maintenance is allowed
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        Day of the week when maintenance is allowed
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        A clock time in the day when maintenance is allowed
        """
        return pulumi.get(self, "time")


