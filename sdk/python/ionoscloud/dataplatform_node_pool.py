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
from ._inputs import *

__all__ = ['DataplatformNodePoolArgs', 'DataplatformNodePool']

@pulumi.input_type
class DataplatformNodePoolArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 node_count: pulumi.Input[int],
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 cores_count: Optional[pulumi.Input[int]] = None,
                 cpu_family: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ram_size: Optional[pulumi.Input[int]] = None,
                 storage_size: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataplatformNodePool resource.
        :param pulumi.Input[str] cluster_id: The UUID of an existing Dataplatform cluster.
        :param pulumi.Input[int] node_count: The number of nodes that make up the node pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Key-value pairs attached to node pool resource as [Kubernetes
               annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        :param pulumi.Input[str] availability_zone: The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        :param pulumi.Input[int] cores_count: The number of CPU cores per node.
        :param pulumi.Input[str] cpu_family: A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
               be retrieved from the datacenter resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value pairs attached to the node pool resource as [Kubernetes
               labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]] maintenance_windows: Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
               character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[int] ram_size: The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        :param pulumi.Input[int] storage_size: The size of the volume in GB. The size must be greater than 10GB.
        :param pulumi.Input[str] storage_type: The type of hardware for the volume.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "node_count", node_count)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if cores_count is not None:
            pulumi.set(__self__, "cores_count", cores_count)
        if cpu_family is not None:
            pulumi.set(__self__, "cpu_family", cpu_family)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if maintenance_windows is not None:
            pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ram_size is not None:
            pulumi.set(__self__, "ram_size", ram_size)
        if storage_size is not None:
            pulumi.set(__self__, "storage_size", storage_size)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The UUID of an existing Dataplatform cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Input[int]:
        """
        The number of nodes that make up the node pool.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs attached to node pool resource as [Kubernetes
        annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="coresCount")
    def cores_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of CPU cores per node.
        """
        return pulumi.get(self, "cores_count")

    @cores_count.setter
    def cores_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cores_count", value)

    @property
    @pulumi.getter(name="cpuFamily")
    def cpu_family(self) -> Optional[pulumi.Input[str]]:
        """
        A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
        be retrieved from the datacenter resource.
        """
        return pulumi.get(self, "cpu_family")

    @cpu_family.setter
    def cpu_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cpu_family", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs attached to the node pool resource as [Kubernetes
        labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]]:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]]):
        pulumi.set(self, "maintenance_windows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
        character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> Optional[pulumi.Input[int]]:
        """
        The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        """
        return pulumi.get(self, "ram_size")

    @ram_size.setter
    def ram_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ram_size", value)

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the volume in GB. The size must be greater than 10GB.
        """
        return pulumi.get(self, "storage_size")

    @storage_size.setter
    def storage_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_size", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of hardware for the volume.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)


@pulumi.input_type
class _DataplatformNodePoolState:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cores_count: Optional[pulumi.Input[int]] = None,
                 cpu_family: Optional[pulumi.Input[str]] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 ram_size: Optional[pulumi.Input[int]] = None,
                 storage_size: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataplatformNodePool resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Key-value pairs attached to node pool resource as [Kubernetes
               annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        :param pulumi.Input[str] availability_zone: The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        :param pulumi.Input[str] cluster_id: The UUID of an existing Dataplatform cluster.
        :param pulumi.Input[int] cores_count: The number of CPU cores per node.
        :param pulumi.Input[str] cpu_family: A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
               be retrieved from the datacenter resource.
        :param pulumi.Input[str] datacenter_id: The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value pairs attached to the node pool resource as [Kubernetes
               labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]] maintenance_windows: Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
               character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[int] node_count: The number of nodes that make up the node pool.
        :param pulumi.Input[int] ram_size: The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        :param pulumi.Input[int] storage_size: The size of the volume in GB. The size must be greater than 10GB.
        :param pulumi.Input[str] storage_type: The type of hardware for the volume.
        :param pulumi.Input[str] version: The version of the Data Platform.
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if availability_zone is not None:
            pulumi.set(__self__, "availability_zone", availability_zone)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cores_count is not None:
            pulumi.set(__self__, "cores_count", cores_count)
        if cpu_family is not None:
            pulumi.set(__self__, "cpu_family", cpu_family)
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if maintenance_windows is not None:
            pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if ram_size is not None:
            pulumi.set(__self__, "ram_size", ram_size)
        if storage_size is not None:
            pulumi.set(__self__, "storage_size", storage_size)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs attached to node pool resource as [Kubernetes
        annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        """
        return pulumi.get(self, "availability_zone")

    @availability_zone.setter
    def availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "availability_zone", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of an existing Dataplatform cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="coresCount")
    def cores_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of CPU cores per node.
        """
        return pulumi.get(self, "cores_count")

    @cores_count.setter
    def cores_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cores_count", value)

    @property
    @pulumi.getter(name="cpuFamily")
    def cpu_family(self) -> Optional[pulumi.Input[str]]:
        """
        A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
        be retrieved from the datacenter resource.
        """
        return pulumi.get(self, "cpu_family")

    @cpu_family.setter
    def cpu_family(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cpu_family", value)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value pairs attached to the node pool resource as [Kubernetes
        labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]]:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformNodePoolMaintenanceWindowArgs']]]]):
        pulumi.set(self, "maintenance_windows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
        character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of nodes that make up the node pool.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> Optional[pulumi.Input[int]]:
        """
        The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        """
        return pulumi.get(self, "ram_size")

    @ram_size.setter
    def ram_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ram_size", value)

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the volume in GB. The size must be greater than 10GB.
        """
        return pulumi.get(self, "storage_size")

    @storage_size.setter
    def storage_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_size", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of hardware for the volume.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the Data Platform.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


warnings.warn("""ionoscloud.index/dataplatformnodepool.DataplatformNodePool has been deprecated in favor of ionoscloud.dsaas/nodepool.NodePool""", DeprecationWarning)


class DataplatformNodePool(pulumi.CustomResource):
    warnings.warn("""ionoscloud.index/dataplatformnodepool.DataplatformNodePool has been deprecated in favor of ionoscloud.dsaas/nodepool.NodePool""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cores_count: Optional[pulumi.Input[int]] = None,
                 cpu_family: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataplatformNodePoolMaintenanceWindowArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 ram_size: Optional[pulumi.Input[int]] = None,
                 storage_size: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a DataplatformNodePool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Key-value pairs attached to node pool resource as [Kubernetes
               annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        :param pulumi.Input[str] availability_zone: The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        :param pulumi.Input[str] cluster_id: The UUID of an existing Dataplatform cluster.
        :param pulumi.Input[int] cores_count: The number of CPU cores per node.
        :param pulumi.Input[str] cpu_family: A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
               be retrieved from the datacenter resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value pairs attached to the node pool resource as [Kubernetes
               labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataplatformNodePoolMaintenanceWindowArgs']]]] maintenance_windows: Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
               character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[int] node_count: The number of nodes that make up the node pool.
        :param pulumi.Input[int] ram_size: The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        :param pulumi.Input[int] storage_size: The size of the volume in GB. The size must be greater than 10GB.
        :param pulumi.Input[str] storage_type: The type of hardware for the volume.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataplatformNodePoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a DataplatformNodePool resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param DataplatformNodePoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataplatformNodePoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 availability_zone: Optional[pulumi.Input[str]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cores_count: Optional[pulumi.Input[int]] = None,
                 cpu_family: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataplatformNodePoolMaintenanceWindowArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 ram_size: Optional[pulumi.Input[int]] = None,
                 storage_size: Optional[pulumi.Input[int]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""DataplatformNodePool is deprecated: ionoscloud.index/dataplatformnodepool.DataplatformNodePool has been deprecated in favor of ionoscloud.dsaas/nodepool.NodePool""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataplatformNodePoolArgs.__new__(DataplatformNodePoolArgs)

            __props__.__dict__["annotations"] = annotations
            __props__.__dict__["availability_zone"] = availability_zone
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["cores_count"] = cores_count
            __props__.__dict__["cpu_family"] = cpu_family
            __props__.__dict__["labels"] = labels
            __props__.__dict__["maintenance_windows"] = maintenance_windows
            __props__.__dict__["name"] = name
            if node_count is None and not opts.urn:
                raise TypeError("Missing required property 'node_count'")
            __props__.__dict__["node_count"] = node_count
            __props__.__dict__["ram_size"] = ram_size
            __props__.__dict__["storage_size"] = storage_size
            __props__.__dict__["storage_type"] = storage_type
            __props__.__dict__["datacenter_id"] = None
            __props__.__dict__["version"] = None
        super(DataplatformNodePool, __self__).__init__(
            'ionoscloud:index/dataplatformNodePool:DataplatformNodePool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            availability_zone: Optional[pulumi.Input[str]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cores_count: Optional[pulumi.Input[int]] = None,
            cpu_family: Optional[pulumi.Input[str]] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataplatformNodePoolMaintenanceWindowArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            node_count: Optional[pulumi.Input[int]] = None,
            ram_size: Optional[pulumi.Input[int]] = None,
            storage_size: Optional[pulumi.Input[int]] = None,
            storage_type: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'DataplatformNodePool':
        """
        Get an existing DataplatformNodePool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] annotations: Key-value pairs attached to node pool resource as [Kubernetes
               annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        :param pulumi.Input[str] availability_zone: The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        :param pulumi.Input[str] cluster_id: The UUID of an existing Dataplatform cluster.
        :param pulumi.Input[int] cores_count: The number of CPU cores per node.
        :param pulumi.Input[str] cpu_family: A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
               be retrieved from the datacenter resource.
        :param pulumi.Input[str] datacenter_id: The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Key-value pairs attached to the node pool resource as [Kubernetes
               labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DataplatformNodePoolMaintenanceWindowArgs']]]] maintenance_windows: Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
               character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[int] node_count: The number of nodes that make up the node pool.
        :param pulumi.Input[int] ram_size: The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        :param pulumi.Input[int] storage_size: The size of the volume in GB. The size must be greater than 10GB.
        :param pulumi.Input[str] storage_type: The type of hardware for the volume.
        :param pulumi.Input[str] version: The version of the Data Platform.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataplatformNodePoolState.__new__(_DataplatformNodePoolState)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["availability_zone"] = availability_zone
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cores_count"] = cores_count
        __props__.__dict__["cpu_family"] = cpu_family
        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["labels"] = labels
        __props__.__dict__["maintenance_windows"] = maintenance_windows
        __props__.__dict__["name"] = name
        __props__.__dict__["node_count"] = node_count
        __props__.__dict__["ram_size"] = ram_size
        __props__.__dict__["storage_size"] = storage_size
        __props__.__dict__["storage_type"] = storage_type
        __props__.__dict__["version"] = version
        return DataplatformNodePool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value pairs attached to node pool resource as [Kubernetes
        annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> pulumi.Output[str]:
        """
        The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The UUID of an existing Dataplatform cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="coresCount")
    def cores_count(self) -> pulumi.Output[int]:
        """
        The number of CPU cores per node.
        """
        return pulumi.get(self, "cores_count")

    @property
    @pulumi.getter(name="cpuFamily")
    def cpu_family(self) -> pulumi.Output[str]:
        """
        A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
        be retrieved from the datacenter resource.
        """
        return pulumi.get(self, "cpu_family")

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        The UUID of the virtual data center (VDC) in which the nodepool is provisioned
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value pairs attached to the node pool resource as [Kubernetes
        labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> pulumi.Output[Sequence['outputs.DataplatformNodePoolMaintenanceWindow']]:
        """
        Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
        character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> pulumi.Output[int]:
        """
        The number of nodes that make up the node pool.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="ramSize")
    def ram_size(self) -> pulumi.Output[int]:
        """
        The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
        """
        return pulumi.get(self, "ram_size")

    @property
    @pulumi.getter(name="storageSize")
    def storage_size(self) -> pulumi.Output[int]:
        """
        The size of the volume in GB. The size must be greater than 10GB.
        """
        return pulumi.get(self, "storage_size")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[str]:
        """
        The type of hardware for the volume.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        The version of the Data Platform.
        """
        return pulumi.get(self, "version")

