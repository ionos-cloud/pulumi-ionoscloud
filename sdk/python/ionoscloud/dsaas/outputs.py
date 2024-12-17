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
    'ClusterLan',
    'ClusterLanRoute',
    'ClusterMaintenanceWindow',
    'NodePoolMaintenanceWindow',
    'GetClusterConfigResult',
    'GetClusterConfigClusterResult',
    'GetClusterConfigContextResult',
    'GetClusterConfigUserResult',
    'GetClusterLanResult',
    'GetClusterLanRouteResult',
    'GetClusterMaintenanceWindowResult',
    'GetNodePoolMaintenanceWindowResult',
    'GetNodePoolsNodePoolResult',
    'GetNodePoolsNodePoolMaintenanceWindowResult',
]

@pulumi.output_type
class ClusterLan(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lanId":
            suggest = "lan_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ClusterLan. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ClusterLan.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ClusterLan.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 lan_id: str,
                 dhcp: Optional[bool] = None,
                 routes: Optional[Sequence['outputs.ClusterLanRoute']] = None):
        """
        :param str lan_id: [string] The LAN ID of an existing LAN at the related data center.
        :param bool dhcp: [bool] Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is 'true'.
        :param Sequence['ClusterLanRouteArgs'] routes: [list] An array of additional LANs attached to worker nodes.
        """
        pulumi.set(__self__, "lan_id", lan_id)
        if dhcp is not None:
            pulumi.set(__self__, "dhcp", dhcp)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        [string] The LAN ID of an existing LAN at the related data center.
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter
    def dhcp(self) -> Optional[bool]:
        """
        [bool] Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is 'true'.
        """
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter
    def routes(self) -> Optional[Sequence['outputs.ClusterLanRoute']]:
        """
        [list] An array of additional LANs attached to worker nodes.
        """
        return pulumi.get(self, "routes")


@pulumi.output_type
class ClusterLanRoute(dict):
    def __init__(__self__, *,
                 gateway: str,
                 network: str):
        """
        :param str gateway: [string] IPv4 or IPv6 gateway IP for the route.
        :param str network: [string] IPv4 or IPv6 CIDR to be routed via the interface.
        """
        pulumi.set(__self__, "gateway", gateway)
        pulumi.set(__self__, "network", network)

    @property
    @pulumi.getter
    def gateway(self) -> str:
        """
        [string] IPv4 or IPv6 gateway IP for the route.
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        [string] IPv4 or IPv6 CIDR to be routed via the interface.
        """
        return pulumi.get(self, "network")


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
        :param str day_of_the_week: [string] Must be set with one the values `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` or `Sunday`.
        :param str time: [string] Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format. This pattern matches the "HH:MM:SS 24-hour format with leading 0" format. For more information take a look at [this link](https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format).
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] Must be set with one the values `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` or `Sunday`.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format. This pattern matches the "HH:MM:SS 24-hour format with leading 0" format. For more information take a look at [this link](https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format).
        """
        return pulumi.get(self, "time")


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
        :param str day_of_the_week: [string] Must be set with one the values `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` or `Sunday`.
        :param str time: [string] Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format. This pattern matches the "HH:MM:SS 24-hour format with leading 0" format. For more information take a look at [this link](https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format).
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        """
        [string] Must be set with one the values `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` or `Sunday`.
        """
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        [string] Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format. This pattern matches the "HH:MM:SS 24-hour format with leading 0" format. For more information take a look at [this link](https://stackoverflow.com/questions/7536755/regular-expression-for-matching-hhmm-time-format).
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
        :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
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
        Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetClusterConfigContextResult(dict):
    def __init__(__self__, *,
                 context: Mapping[str, str],
                 name: str):
        """
        :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
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
        Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetClusterConfigUserResult(dict):
    def __init__(__self__, *,
                 name: str,
                 user: Mapping[str, str]):
        """
        :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def user(self) -> Mapping[str, str]:
        return pulumi.get(self, "user")


@pulumi.output_type
class GetClusterLanResult(dict):
    def __init__(__self__, *,
                 dhcp: bool,
                 lan_id: str,
                 routes: Sequence['outputs.GetClusterLanRouteResult']):
        """
        :param bool dhcp: Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is 'true'.
        :param str lan_id: The LAN ID of an existing LAN at the related data center
        :param Sequence['GetClusterLanRouteArgs'] routes: An array of additional LANs attached to worker nodes
        """
        pulumi.set(__self__, "dhcp", dhcp)
        pulumi.set(__self__, "lan_id", lan_id)
        pulumi.set(__self__, "routes", routes)

    @property
    @pulumi.getter
    def dhcp(self) -> bool:
        """
        Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is 'true'.
        """
        return pulumi.get(self, "dhcp")

    @property
    @pulumi.getter(name="lanId")
    def lan_id(self) -> str:
        """
        The LAN ID of an existing LAN at the related data center
        """
        return pulumi.get(self, "lan_id")

    @property
    @pulumi.getter
    def routes(self) -> Sequence['outputs.GetClusterLanRouteResult']:
        """
        An array of additional LANs attached to worker nodes
        """
        return pulumi.get(self, "routes")


@pulumi.output_type
class GetClusterLanRouteResult(dict):
    def __init__(__self__, *,
                 gateway: str,
                 network: str):
        """
        :param str gateway: IPv4 or IPv6 gateway IP for the route
        :param str network: IPv4 or IPv6 CIDR to be routed via the interface
        """
        pulumi.set(__self__, "gateway", gateway)
        pulumi.set(__self__, "network", network)

    @property
    @pulumi.getter
    def gateway(self) -> str:
        """
        IPv4 or IPv6 gateway IP for the route
        """
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        IPv4 or IPv6 CIDR to be routed via the interface
        """
        return pulumi.get(self, "network")


@pulumi.output_type
class GetClusterMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str time: Time at which the maintenance should start.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        Time at which the maintenance should start.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetNodePoolMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str time: Time at which the maintenance should start.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        Time at which the maintenance should start.
        """
        return pulumi.get(self, "time")


@pulumi.output_type
class GetNodePoolsNodePoolResult(dict):
    def __init__(__self__, *,
                 annotations: Mapping[str, str],
                 availability_zone: str,
                 cores_count: int,
                 cpu_family: str,
                 datacenter_id: str,
                 id: str,
                 labels: Mapping[str, str],
                 maintenance_windows: Sequence['outputs.GetNodePoolsNodePoolMaintenanceWindowResult'],
                 name: str,
                 node_count: int,
                 ram_size: int,
                 storage_size: int,
                 storage_type: str,
                 version: str):
        """
        :param Mapping[str, str] annotations: Key-value pairs attached to node pool resource as kubernetes annotations
        :param str availability_zone: The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        :param int cores_count: The number of CPU cores per node.
        :param str cpu_family: A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the datacenter resource.
        :param str datacenter_id: The UUID of the virtual data center (VDC) in which the node pool is provisioned
        :param Mapping[str, str] labels: Key-value pairs attached to the node pool resource as kubernetes labels
        :param Sequence['GetNodePoolsNodePoolMaintenanceWindowArgs'] maintenance_windows: Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        :param int node_count: The number of nodes that make up the node pool.
        :param int ram_size: The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        :param int storage_size: The size of the volume in GB. The size must be greater than 10GB.
        :param str storage_type: The type of hardware for the volume.
        :param str version: The version of the Data Platform.
        """
        pulumi.set(__self__, "annotations", annotations)
        pulumi.set(__self__, "availability_zone", availability_zone)
        pulumi.set(__self__, "cores_count", cores_count)
        pulumi.set(__self__, "cpu_family", cpu_family)
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "labels", labels)
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "node_count", node_count)
        pulumi.set(__self__, "ram_size", ram_size)
        pulumi.set(__self__, "storage_size", storage_size)
        pulumi.set(__self__, "storage_type", storage_type)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, str]:
        """
        Key-value pairs attached to node pool resource as kubernetes annotations
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> str:
        """
        The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="coresCount")
    def cores_count(self) -> int:
        """
        The number of CPU cores per node.
        """
        return pulumi.get(self, "cores_count")

    @property
    @pulumi.getter(name="cpuFamily")
    def cpu_family(self) -> str:
        """
        A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can be retrieved from the datacenter resource.
        """
        return pulumi.get(self, "cpu_family")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The UUID of the virtual data center (VDC) in which the node pool is provisioned
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Key-value pairs attached to the node pool resource as kubernetes labels
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetNodePoolsNodePoolMaintenanceWindowResult']:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> int:
        """
        The number of nodes that make up the node pool.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> int:
        """
        The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        """
        return pulumi.get(self, "ram_size")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        """
        The size of the volume in GB. The size must be greater than 10GB.
        """
        return pulumi.get(self, "storage_size")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        The type of hardware for the volume.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        The version of the Data Platform.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class GetNodePoolsNodePoolMaintenanceWindowResult(dict):
    def __init__(__self__, *,
                 day_of_the_week: str,
                 time: str):
        """
        :param str time: Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format.
        """
        pulumi.set(__self__, "day_of_the_week", day_of_the_week)
        pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter(name="dayOfTheWeek")
    def day_of_the_week(self) -> str:
        return pulumi.get(self, "day_of_the_week")

    @property
    @pulumi.getter
    def time(self) -> str:
        """
        Time at which the maintenance should start. Must conform to the 'HH:MM:SS' 24-hour format.
        """
        return pulumi.get(self, "time")


