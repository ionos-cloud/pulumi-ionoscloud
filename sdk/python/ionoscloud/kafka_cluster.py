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

__all__ = ['KafkaClusterArgs', 'KafkaCluster']

@pulumi.input_type
class KafkaClusterArgs:
    def __init__(__self__, *,
                 connections: pulumi.Input['KafkaClusterConnectionsArgs'],
                 location: pulumi.Input[str],
                 size: pulumi.Input[str],
                 version: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KafkaCluster resource.
        :param pulumi.Input['KafkaClusterConnectionsArgs'] connections: Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] size: [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        :param pulumi.Input[str] version: [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        """
        pulumi.set(__self__, "connections", connections)
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "version", version)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Input['KafkaClusterConnectionsArgs']:
        """
        Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: pulumi.Input['KafkaClusterConnectionsArgs']):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[str]:
        """
        [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[str]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the Kafka Cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _KafkaClusterState:
    def __init__(__self__, *,
                 broker_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 connections: Optional[pulumi.Input['KafkaClusterConnectionsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KafkaCluster resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] broker_addresses: [list] IP address and port of cluster brokers.
        :param pulumi.Input['KafkaClusterConnectionsArgs'] connections: Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[str] size: [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        :param pulumi.Input[str] version: [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        if broker_addresses is not None:
            pulumi.set(__self__, "broker_addresses", broker_addresses)
        if connections is not None:
            pulumi.set(__self__, "connections", connections)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="brokerAddresses")
    def broker_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [list] IP address and port of cluster brokers.
        """
        return pulumi.get(self, "broker_addresses")

    @broker_addresses.setter
    def broker_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "broker_addresses", value)

    @property
    @pulumi.getter
    def connections(self) -> Optional[pulumi.Input['KafkaClusterConnectionsArgs']]:
        """
        Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        """
        return pulumi.get(self, "connections")

    @connections.setter
    def connections(self, value: Optional[pulumi.Input['KafkaClusterConnectionsArgs']]):
        pulumi.set(self, "connections", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Name of the Kafka Cluster.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class KafkaCluster(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Union['KafkaClusterConnectionsArgs', 'KafkaClusterConnectionsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manages a **Kafka Cluster** on IonosCloud.

        ## Example Usage

        This resource will create an operational Kafka Cluster. After this section completes, the provisioner can be called.

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter", location="de/fra")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_kafka_cluster = ionoscloud.KafkaCluster("exampleKafkaCluster",
            location="de/fra",
            version="3.7.0",
            size="S",
            connections={
                "datacenter_id": example_datacenter.id,
                "lan_id": example_lan.id,
                "broker_addresses": [
                    "192.168.1.101/24",
                    "192.168.1.102/24",
                    "192.168.1.103/24",
                ],
            })
        ```

        ## Import

        Kafka Cluster can be imported using the `location` and `kafka cluster id`:

        ```sh
        $ pulumi import ionoscloud:index/kafkaCluster:KafkaCluster mycluster {location}:{kafka cluster uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['KafkaClusterConnectionsArgs', 'KafkaClusterConnectionsArgsDict']] connections: Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[str] size: [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        :param pulumi.Input[str] version: [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KafkaClusterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Kafka Cluster** on IonosCloud.

        ## Example Usage

        This resource will create an operational Kafka Cluster. After this section completes, the provisioner can be called.

        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter", location="de/fra")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_kafka_cluster = ionoscloud.KafkaCluster("exampleKafkaCluster",
            location="de/fra",
            version="3.7.0",
            size="S",
            connections={
                "datacenter_id": example_datacenter.id,
                "lan_id": example_lan.id,
                "broker_addresses": [
                    "192.168.1.101/24",
                    "192.168.1.102/24",
                    "192.168.1.103/24",
                ],
            })
        ```

        ## Import

        Kafka Cluster can be imported using the `location` and `kafka cluster id`:

        ```sh
        $ pulumi import ionoscloud:index/kafkaCluster:KafkaCluster mycluster {location}:{kafka cluster uuid}
        ```

        :param str resource_name: The name of the resource.
        :param KafkaClusterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KafkaClusterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connections: Optional[pulumi.Input[Union['KafkaClusterConnectionsArgs', 'KafkaClusterConnectionsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KafkaClusterArgs.__new__(KafkaClusterArgs)

            if connections is None and not opts.urn:
                raise TypeError("Missing required property 'connections'")
            __props__.__dict__["connections"] = connections
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
            __props__.__dict__["broker_addresses"] = None
        super(KafkaCluster, __self__).__init__(
            'ionoscloud:index/kafkaCluster:KafkaCluster',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            broker_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            connections: Optional[pulumi.Input[Union['KafkaClusterConnectionsArgs', 'KafkaClusterConnectionsArgsDict']]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[str]] = None) -> 'KafkaCluster':
        """
        Get an existing KafkaCluster resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] broker_addresses: [list] IP address and port of cluster brokers.
        :param pulumi.Input[Union['KafkaClusterConnectionsArgs', 'KafkaClusterConnectionsArgsDict']] connections: Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[str] size: [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        :param pulumi.Input[str] version: [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KafkaClusterState.__new__(_KafkaClusterState)

        __props__.__dict__["broker_addresses"] = broker_addresses
        __props__.__dict__["connections"] = connections
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["size"] = size
        __props__.__dict__["version"] = version
        return KafkaCluster(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="brokerAddresses")
    def broker_addresses(self) -> pulumi.Output[Sequence[str]]:
        """
        [list] IP address and port of cluster brokers.
        """
        return pulumi.get(self, "broker_addresses")

    @property
    @pulumi.getter
    def connections(self) -> pulumi.Output['outputs.KafkaClusterConnections']:
        """
        Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
        """
        return pulumi.get(self, "connections")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        [string] Name of the Kafka Cluster.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[str]:
        """
        [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        [string] Version of the Kafka Cluster. Possible values: `3.7.0`
        """
        return pulumi.get(self, "version")

