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
from ._inputs import *

__all__ = ['ClusterArgs', 'Cluster']

@pulumi.input_type
class ClusterArgs:
    def __init__(__self__, *,
                 connections: pulumi.Input['ClusterConnectionsArgs'],
                 size: pulumi.Input[int],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nfs: Optional[pulumi.Input['ClusterNfsArgs']] = None):
        """
        The set of arguments for constructing a Cluster resource.
        :param pulumi.Input['ClusterConnectionsArgs'] connections: The network connections for the Network File Storage Cluster.
        :param pulumi.Input[int] size: The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        :param pulumi.Input[str] location: The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
               - `de/fra` - Frankfurt
               - `de/txl` - Berlin
        :param pulumi.Input[str] name: The name of the Network File Storage cluster.
        """
        pulumi.set(__self__, "connections", connections)
        pulumi.set(__self__, "size", size)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nfs is not None:
            pulumi.set(__self__, "nfs", nfs)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Input['ClusterConnectionsArgs']:
        """
        The network connections for the Network File Storage Cluster.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: pulumi.Input['ClusterConnectionsArgs']):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
        - `de/fra` - Frankfurt
        - `de/txl` - Berlin
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Network File Storage cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input['ClusterNfsArgs']]:
        return pulumi.get(self, "nfs")

    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input['ClusterNfsArgs']]):
        pulumi.set(self, "nfs", value)


@pulumi.input_type
class _ClusterState:
    def __init__(__self__, *,
                 connections: Optional[pulumi.Input['ClusterConnectionsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nfs: Optional[pulumi.Input['ClusterNfsArgs']] = None,
                 size: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Cluster resources.
        :param pulumi.Input['ClusterConnectionsArgs'] connections: The network connections for the Network File Storage Cluster.
        :param pulumi.Input[str] location: The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
               - `de/fra` - Frankfurt
               - `de/txl` - Berlin
        :param pulumi.Input[str] name: The name of the Network File Storage cluster.
        :param pulumi.Input[int] size: The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if nfs is not None:
            pulumi.set(__self__, "nfs", nfs)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input['ClusterConnectionsArgs']]:
        """
        The network connections for the Network File Storage Cluster.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input['ClusterConnectionsArgs']]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
        - `de/fra` - Frankfurt
        - `de/txl` - Berlin
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Network File Storage cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input['ClusterNfsArgs']]:
        return pulumi.get(self, "nfs")

    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input['ClusterNfsArgs']]):
        pulumi.set(self, "nfs", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)


class Cluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Union['ClusterConnectionsArgs', 'ClusterConnectionsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nfs: Optional[pulumi.Input[Union['ClusterNfsArgs', 'ClusterNfsArgsDict']]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Create clusters of Network File Storage (NFS) on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        # Basic example
        nfs_dc = ionoscloud.compute.Datacenter("nfs_dc",
            name="NFS Datacenter",
            location="de/txl",
            description="Datacenter Description",
            sec_auth_protection=False)
        nfs_lan = ionoscloud.compute.Lan("nfs_lan",
            datacenter_id=nfs_dc.id,
            public=False,
            name="Lan for NFS")
        example = ionoscloud.nfs.Cluster("example",
            name="test",
            location="de/txl",
            size=2,
            nfs={
                "min_version": "4.2",
            },
            connections={
                "datacenter_id": nfs_dc.id,
                "ip_address": "192.168.100.10/24",
                "lan": nfs_lan.id,
            })
        ```

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud
        import pulumi_random as random

        # Complete example
        nfs_dc = ionoscloud.compute.Datacenter("nfs_dc",
            name="NFS Datacenter",
            location="de/txl",
            description="Datacenter Description",
            sec_auth_protection=False)
        nfs_lan = ionoscloud.compute.Lan("nfs_lan",
            datacenter_id=nfs_dc.id,
            public=False,
            name="Lan for NFS")
        h_dd_image = ionoscloud.compute.get_image(image_alias="ubuntu:20.04",
            type="HDD",
            cloud_init="V1",
            location="de/txl")
        password = random.index.Password("password",
            length=16,
            special=False)
        # needed for the NIC - which provides the IP address for the NFS cluster.
        nfs_server = ionoscloud.compute.Server("nfs_server",
            name="Server for NFS",
            datacenter_id=nfs_dc.id,
            cores=1,
            ram=2048,
            availability_zone="ZONE_1",
            cpu_family="INTEL_SKYLAKE",
            image_name=h_dd_image.id,
            image_password=password["result"],
            volume={
                "name": "system",
                "size": 14,
                "disk_type": "SSD",
            },
            nic={
                "name": "NIC A",
                "lan": nfs_lan.id,
                "dhcp": True,
                "firewall_active": True,
            })
        example = ionoscloud.nfs.Cluster("example",
            name="test",
            location="de/txl",
            size=2,
            nfs={
                "min_version": "4.2",
            },
            connections={
                "datacenter_id": nfs_dc.id,
                "ip_address": "nfs_cluster_cidr_from_nic",
                "lan": nfs_lan.id,
            })
        ```

        ## Import

        A Network File Storage Cluster resource can be imported using its `location` and `resource id`:

        ```sh
        $ pulumi import ionoscloud:nfs/cluster:Cluster name location:uuid
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ClusterConnectionsArgs', 'ClusterConnectionsArgsDict']] connections: The network connections for the Network File Storage Cluster.
        :param pulumi.Input[str] location: The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
               - `de/fra` - Frankfurt
               - `de/txl` - Berlin
        :param pulumi.Input[str] name: The name of the Network File Storage cluster.
        :param pulumi.Input[int] size: The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create clusters of Network File Storage (NFS) on IonosCloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud

        # Basic example
        nfs_dc = ionoscloud.compute.Datacenter("nfs_dc",
            name="NFS Datacenter",
            location="de/txl",
            description="Datacenter Description",
            sec_auth_protection=False)
        nfs_lan = ionoscloud.compute.Lan("nfs_lan",
            datacenter_id=nfs_dc.id,
            public=False,
            name="Lan for NFS")
        example = ionoscloud.nfs.Cluster("example",
            name="test",
            location="de/txl",
            size=2,
            nfs={
                "min_version": "4.2",
            },
            connections={
                "datacenter_id": nfs_dc.id,
                "ip_address": "192.168.100.10/24",
                "lan": nfs_lan.id,
            })
        ```

        ```python
        import pulumi
        import pulumi_ionoscloud as ionoscloud
        import pulumi_random as random

        # Complete example
        nfs_dc = ionoscloud.compute.Datacenter("nfs_dc",
            name="NFS Datacenter",
            location="de/txl",
            description="Datacenter Description",
            sec_auth_protection=False)
        nfs_lan = ionoscloud.compute.Lan("nfs_lan",
            datacenter_id=nfs_dc.id,
            public=False,
            name="Lan for NFS")
        h_dd_image = ionoscloud.compute.get_image(image_alias="ubuntu:20.04",
            type="HDD",
            cloud_init="V1",
            location="de/txl")
        password = random.index.Password("password",
            length=16,
            special=False)
        # needed for the NIC - which provides the IP address for the NFS cluster.
        nfs_server = ionoscloud.compute.Server("nfs_server",
            name="Server for NFS",
            datacenter_id=nfs_dc.id,
            cores=1,
            ram=2048,
            availability_zone="ZONE_1",
            cpu_family="INTEL_SKYLAKE",
            image_name=h_dd_image.id,
            image_password=password["result"],
            volume={
                "name": "system",
                "size": 14,
                "disk_type": "SSD",
            },
            nic={
                "name": "NIC A",
                "lan": nfs_lan.id,
                "dhcp": True,
                "firewall_active": True,
            })
        example = ionoscloud.nfs.Cluster("example",
            name="test",
            location="de/txl",
            size=2,
            nfs={
                "min_version": "4.2",
            },
            connections={
                "datacenter_id": nfs_dc.id,
                "ip_address": "nfs_cluster_cidr_from_nic",
                "lan": nfs_lan.id,
            })
        ```

        ## Import

        A Network File Storage Cluster resource can be imported using its `location` and `resource id`:

        ```sh
        $ pulumi import ionoscloud:nfs/cluster:Cluster name location:uuid
        ```

        :param str resource_name: The name of the resource.
        :param ClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Union['ClusterConnectionsArgs', 'ClusterConnectionsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 nfs: Optional[pulumi.Input[Union['ClusterNfsArgs', 'ClusterNfsArgsDict']]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterArgs.__new__(ClusterArgs)

            if connections is None and not opts.urn:
                raise TypeError("Missing required property 'connections'")
            __props__.__dict__["connections"] = connections
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["nfs"] = nfs
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
        super(Cluster, __self__).__init__(
            'ionoscloud:nfs/cluster:Cluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            connections: Optional[pulumi.Input[Union['ClusterConnectionsArgs', 'ClusterConnectionsArgsDict']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            nfs: Optional[pulumi.Input[Union['ClusterNfsArgs', 'ClusterNfsArgsDict']]] = None,
            size: Optional[pulumi.Input[int]] = None) -> 'Cluster':
        """
        Get an existing Cluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ClusterConnectionsArgs', 'ClusterConnectionsArgsDict']] connections: The network connections for the Network File Storage Cluster.
        :param pulumi.Input[str] location: The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
               - `de/fra` - Frankfurt
               - `de/txl` - Berlin
        :param pulumi.Input[str] name: The name of the Network File Storage cluster.
        :param pulumi.Input[int] size: The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ClusterState.__new__(_ClusterState)

        __props__.__dict__["connections"] = connections
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["nfs"] = nfs
        __props__.__dict__["size"] = size
        return Cluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output['outputs.ClusterConnections']:
        """
        The network connections for the Network File Storage Cluster.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
        - `de/fra` - Frankfurt
        - `de/txl` - Berlin
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Network File Storage cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nfs(self) -> pulumi.Output[Optional['outputs.ClusterNfs']]:
        return pulumi.get(self, "nfs")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
        """
        return pulumi.get(self, "size")

