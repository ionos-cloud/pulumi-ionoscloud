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
    'GetNodePoolResult',
    'AwaitableGetNodePoolResult',
    'get_node_pool',
    'get_node_pool_output',
]

@pulumi.output_type
class GetNodePoolResult:
    """
    A collection of values returned by getNodePool.
    """
    def __init__(__self__, annotations=None, availability_zone=None, cluster_id=None, cores_count=None, cpu_family=None, datacenter_id=None, id=None, labels=None, maintenance_windows=None, name=None, node_count=None, partial_match=None, ram_size=None, storage_size=None, storage_type=None, version=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if cores_count and not isinstance(cores_count, int):
            raise TypeError("Expected argument 'cores_count' to be a int")
        pulumi.set(__self__, "cores_count", cores_count)
        if cpu_family and not isinstance(cpu_family, str):
            raise TypeError("Expected argument 'cpu_family' to be a str")
        pulumi.set(__self__, "cpu_family", cpu_family)
        if datacenter_id and not isinstance(datacenter_id, str):
            raise TypeError("Expected argument 'datacenter_id' to be a str")
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if maintenance_windows and not isinstance(maintenance_windows, list):
            raise TypeError("Expected argument 'maintenance_windows' to be a list")
        pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if partial_match and not isinstance(partial_match, bool):
            raise TypeError("Expected argument 'partial_match' to be a bool")
        pulumi.set(__self__, "partial_match", partial_match)
        if ram_size and not isinstance(ram_size, int):
            raise TypeError("Expected argument 'ram_size' to be a int")
        pulumi.set(__self__, "ram_size", ram_size)
        if storage_size and not isinstance(storage_size, int):
            raise TypeError("Expected argument 'storage_size' to be a int")
        pulumi.set(__self__, "storage_size", storage_size)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, str]:
        """
        Key-value pairs attached to node pool resource as [Kubernetes annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).
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
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        """
        ID of the cluster the searched node pool is part of.
        """
        return pulumi.get(self, "cluster_id")

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
        A CPU family.
        """
        return pulumi.get(self, "cpu_family")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> str:
        """
        The UUID of the virtual data center (VDC) the cluster is provisioned.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID of your node pool.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Key-value pairs attached to the node pool resource as [Kubernetes labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Sequence['outputs.GetNodePoolMaintenanceWindowResult']:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of your node pool
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
    @pulumi.getter(name="partialMatch")
    def partial_match(self) -> Optional[bool]:
        return pulumi.get(self, "partial_match")

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> int:
        """
        The RAM size for one node in MB.
        """
        return pulumi.get(self, "ram_size")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> int:
        """
        The size of the volume in GB.
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


class AwaitableGetNodePoolResult(GetNodePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodePoolResult(
            annotations=self.annotations,
            availability_zone=self.availability_zone,
            cluster_id=self.cluster_id,
            cores_count=self.cores_count,
            cpu_family=self.cpu_family,
            datacenter_id=self.datacenter_id,
            id=self.id,
            labels=self.labels,
            maintenance_windows=self.maintenance_windows,
            name=self.name,
            node_count=self.node_count,
            partial_match=self.partial_match,
            ram_size=self.ram_size,
            storage_size=self.storage_size,
            storage_type=self.storage_type,
            version=self.version)


def get_node_pool(cluster_id: Optional[str] = None,
                  id: Optional[str] = None,
                  name: Optional[str] = None,
                  partial_match: Optional[bool] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodePoolResult:
    """
    The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage


    :param str cluster_id: ID of the cluster the searched node pool is part of.
    :param str id: ID of the node pool you want to search for.
    :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ionoscloud:dsaas/getNodePool:getNodePool', __args__, opts=opts, typ=GetNodePoolResult).value

    return AwaitableGetNodePoolResult(
        annotations=pulumi.get(__ret__, 'annotations'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        cluster_id=pulumi.get(__ret__, 'cluster_id'),
        cores_count=pulumi.get(__ret__, 'cores_count'),
        cpu_family=pulumi.get(__ret__, 'cpu_family'),
        datacenter_id=pulumi.get(__ret__, 'datacenter_id'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        maintenance_windows=pulumi.get(__ret__, 'maintenance_windows'),
        name=pulumi.get(__ret__, 'name'),
        node_count=pulumi.get(__ret__, 'node_count'),
        partial_match=pulumi.get(__ret__, 'partial_match'),
        ram_size=pulumi.get(__ret__, 'ram_size'),
        storage_size=pulumi.get(__ret__, 'storage_size'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        version=pulumi.get(__ret__, 'version'))
def get_node_pool_output(cluster_id: Optional[pulumi.Input[str]] = None,
                         id: Optional[pulumi.Input[Optional[str]]] = None,
                         name: Optional[pulumi.Input[Optional[str]]] = None,
                         partial_match: Optional[pulumi.Input[Optional[bool]]] = None,
                         opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetNodePoolResult]:
    """
    The **Dataplatform Node Pool Data Source** can be used to search for and return an existing Dataplatform Node Pool under a Dataplatform Cluster.
    If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
    When this happens, please refine your search and make sure that your resources have unique names.

    ## Example Usage


    :param str cluster_id: ID of the cluster the searched node pool is part of.
    :param str id: ID of the node pool you want to search for.
    :param str name: Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
    :param bool partial_match: Whether partial matching is allowed or not when using name argument. Default value is false.
           
           Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['id'] = id
    __args__['name'] = name
    __args__['partialMatch'] = partial_match
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ionoscloud:dsaas/getNodePool:getNodePool', __args__, opts=opts, typ=GetNodePoolResult)
    return __ret__.apply(lambda __response__: GetNodePoolResult(
        annotations=pulumi.get(__response__, 'annotations'),
        availability_zone=pulumi.get(__response__, 'availability_zone'),
        cluster_id=pulumi.get(__response__, 'cluster_id'),
        cores_count=pulumi.get(__response__, 'cores_count'),
        cpu_family=pulumi.get(__response__, 'cpu_family'),
        datacenter_id=pulumi.get(__response__, 'datacenter_id'),
        id=pulumi.get(__response__, 'id'),
        labels=pulumi.get(__response__, 'labels'),
        maintenance_windows=pulumi.get(__response__, 'maintenance_windows'),
        name=pulumi.get(__response__, 'name'),
        node_count=pulumi.get(__response__, 'node_count'),
        partial_match=pulumi.get(__response__, 'partial_match'),
        ram_size=pulumi.get(__response__, 'ram_size'),
        storage_size=pulumi.get(__response__, 'storage_size'),
        storage_type=pulumi.get(__response__, 'storage_type'),
        version=pulumi.get(__response__, 'version')))
