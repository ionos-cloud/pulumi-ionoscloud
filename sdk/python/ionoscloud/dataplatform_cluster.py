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
from . import outputs
from ._inputs import *

__all__ = ['DataplatformClusterArgs', 'DataplatformCluster']

@pulumi.input_type
class DataplatformClusterArgs:
    def __init__(__self__, *,
                 datacenter_id: pulumi.Input[str],
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DataplatformCluster resource.
        :param pulumi.Input[str] datacenter_id: [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]] lans: [list] A list of LANs you want this node pool to be part of.
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]] maintenance_windows: [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[str] version: [int] The version of the Data Platform.
        """
        pulumi.set(__self__, "datacenter_id", datacenter_id)
        if lans is not None:
            pulumi.set(__self__, "lans", lans)
        if maintenance_windows is not None:
            pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Input[str]:
        """
        [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def lans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]]:
        """
        [list] A list of LANs you want this node pool to be part of.
        """
        return pulumi.get(self, "lans")

    @lans.setter
    def lans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]]):
        pulumi.set(self, "lans", value)

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]]:
        """
        [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]]):
        pulumi.set(self, "maintenance_windows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [int] The version of the Data Platform.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


@pulumi.input_type
class _DataplatformClusterState:
    def __init__(__self__, *,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DataplatformCluster resources.
        :param pulumi.Input[str] datacenter_id: [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]] lans: [list] A list of LANs you want this node pool to be part of.
        :param pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]] maintenance_windows: [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[str] version: [int] The version of the Data Platform.
        """
        if datacenter_id is not None:
            pulumi.set(__self__, "datacenter_id", datacenter_id)
        if lans is not None:
            pulumi.set(__self__, "lans", lans)
        if maintenance_windows is not None:
            pulumi.set(__self__, "maintenance_windows", maintenance_windows)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        """
        return pulumi.get(self, "datacenter_id")

    @datacenter_id.setter
    def datacenter_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter_id", value)

    @property
    @pulumi.getter
    def lans(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]]:
        """
        [list] A list of LANs you want this node pool to be part of.
        """
        return pulumi.get(self, "lans")

    @lans.setter
    def lans(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterLanArgs']]]]):
        pulumi.set(self, "lans", value)

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]]:
        """
        [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @maintenance_windows.setter
    def maintenance_windows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataplatformClusterMaintenanceWindowArgs']]]]):
        pulumi.set(self, "maintenance_windows", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [int] The version of the Data Platform.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class DataplatformCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterLanArgs', 'DataplatformClusterLanArgsDict']]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterMaintenanceWindowArgs', 'DataplatformClusterMaintenanceWindowArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **Dataplatform Cluster**.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="de/txl",
            description="Datacenter for testing Dataplatform Cluster")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_dataplatform_cluster = ionoscloud.DataplatformCluster("exampleDataplatformCluster",
            datacenter_id=example_datacenter.id,
            maintenance_windows=[{
                "day_of_the_week": "Sunday",
                "time": "09:00:00",
            }],
            version="23.11",
            lans=[{
                "lan_id": example_lan.id,
                "dhcp": False,
                "routes": [{
                    "network": "182.168.42.1/24",
                    "gateway": "192.168.42.1",
                }],
            }])
        ```

        ## Import

        Resource Dataplatform Cluster can be imported using the `cluster_id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/dataplatformCluster:DataplatformCluster mycluser {cluster uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterLanArgs', 'DataplatformClusterLanArgsDict']]]] lans: [list] A list of LANs you want this node pool to be part of.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterMaintenanceWindowArgs', 'DataplatformClusterMaintenanceWindowArgsDict']]]] maintenance_windows: [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[str] version: [int] The version of the Data Platform.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataplatformClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Dataplatform Cluster**.

        ## Example Usage

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter",
            location="de/txl",
            description="Datacenter for testing Dataplatform Cluster")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_dataplatform_cluster = ionoscloud.DataplatformCluster("exampleDataplatformCluster",
            datacenter_id=example_datacenter.id,
            maintenance_windows=[{
                "day_of_the_week": "Sunday",
                "time": "09:00:00",
            }],
            version="23.11",
            lans=[{
                "lan_id": example_lan.id,
                "dhcp": False,
                "routes": [{
                    "network": "182.168.42.1/24",
                    "gateway": "192.168.42.1",
                }],
            }])
        ```

        ## Import

        Resource Dataplatform Cluster can be imported using the `cluster_id`, e.g.

        ```sh
        $ pulumi import ionoscloud:index/dataplatformCluster:DataplatformCluster mycluser {cluster uuid}
        ```

        :param str resource_name: The name of the resource.
        :param DataplatformClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataplatformClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter_id: Optional[pulumi.Input[str]] = None,
                 lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterLanArgs', 'DataplatformClusterLanArgsDict']]]]] = None,
                 maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterMaintenanceWindowArgs', 'DataplatformClusterMaintenanceWindowArgsDict']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataplatformClusterArgs.__new__(DataplatformClusterArgs)

            if datacenter_id is None and not opts.urn:
                raise TypeError("Missing required property 'datacenter_id'")
            __props__.__dict__["datacenter_id"] = datacenter_id
            __props__.__dict__["lans"] = lans
            __props__.__dict__["maintenance_windows"] = maintenance_windows
            __props__.__dict__["name"] = name
            __props__.__dict__["version"] = version
        super(DataplatformCluster, __self__).__init__(
            'ionoscloud:index/dataplatformCluster:DataplatformCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter_id: Optional[pulumi.Input[str]] = None,
            lans: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterLanArgs', 'DataplatformClusterLanArgsDict']]]]] = None,
            maintenance_windows: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterMaintenanceWindowArgs', 'DataplatformClusterMaintenanceWindowArgsDict']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'DataplatformCluster':
        """
        Get an existing DataplatformCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter_id: [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterLanArgs', 'DataplatformClusterLanArgsDict']]]] lans: [list] A list of LANs you want this node pool to be part of.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataplatformClusterMaintenanceWindowArgs', 'DataplatformClusterMaintenanceWindowArgsDict']]]] maintenance_windows: [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        :param pulumi.Input[str] name: [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        :param pulumi.Input[str] version: [int] The version of the Data Platform.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DataplatformClusterState.__new__(_DataplatformClusterState)

        __props__.__dict__["datacenter_id"] = datacenter_id
        __props__.__dict__["lans"] = lans
        __props__.__dict__["maintenance_windows"] = maintenance_windows
        __props__.__dict__["name"] = name
        __props__.__dict__["version"] = version
        return DataplatformCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datacenterId")
    def datacenter_id(self) -> pulumi.Output[str]:
        """
        [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
        """
        return pulumi.get(self, "datacenter_id")

    @property
    @pulumi.getter
    def lans(self) -> pulumi.Output[Optional[Sequence['outputs.DataplatformClusterLan']]]:
        """
        [list] A list of LANs you want this node pool to be part of.
        """
        return pulumi.get(self, "lans")

    @property
    @pulumi.getter(name="maintenanceWindows")
    def maintenance_windows(self) -> pulumi.Output[Sequence['outputs.DataplatformClusterMaintenanceWindow']]:
        """
        [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
        """
        return pulumi.get(self, "maintenance_windows")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        [int] The version of the Data Platform.
        """
        return pulumi.get(self, "version")

