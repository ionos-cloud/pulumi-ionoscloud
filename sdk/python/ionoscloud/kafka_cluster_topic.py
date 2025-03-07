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

__all__ = ['KafkaClusterTopicArgs', 'KafkaClusterTopic']

@pulumi.input_type
class KafkaClusterTopicArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 location: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 number_of_partitions: Optional[pulumi.Input[int]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 retention_time: Optional[pulumi.Input[int]] = None,
                 segment_bytes: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a KafkaClusterTopic resource.
        :param pulumi.Input[str] cluster_id: [string] ID of the Kafka Cluster that the topic belongs to.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[int] number_of_partitions: [int] The number of partitions of the topic. Partitions allow for parallel
               processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
               Default value: 3.
        :param pulumi.Input[int] replication_factor: [int] The number of replicas of the topic. The replication factor determines how many
               copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
               of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        :param pulumi.Input[int] retention_time: [int] This configuration controls the maximum time we will retain a log before we will
               discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
               to -1, no time limit is applied. Default value: 604800000.
        :param pulumi.Input[int] segment_bytes: [int] This configuration controls the segment file size for the log. Retention and
               cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
               retention. Default value: 1073741824.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if number_of_partitions is not None:
            pulumi.set(__self__, "number_of_partitions", number_of_partitions)
        if replication_factor is not None:
            pulumi.set(__self__, "replication_factor", replication_factor)
        if retention_time is not None:
            pulumi.set(__self__, "retention_time", retention_time)
        if segment_bytes is not None:
            pulumi.set(__self__, "segment_bytes", segment_bytes)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        [string] ID of the Kafka Cluster that the topic belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
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
    @pulumi.getter(name="numberOfPartitions")
    def number_of_partitions(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The number of partitions of the topic. Partitions allow for parallel
        processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
        Default value: 3.
        """
        return pulumi.get(self, "number_of_partitions")

    @number_of_partitions.setter
    def number_of_partitions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number_of_partitions", value)

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The number of replicas of the topic. The replication factor determines how many
        copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
        of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        """
        return pulumi.get(self, "replication_factor")

    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replication_factor", value)

    @property
    @pulumi.getter(name="retentionTime")
    def retention_time(self) -> Optional[pulumi.Input[int]]:
        """
        [int] This configuration controls the maximum time we will retain a log before we will
        discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
        to -1, no time limit is applied. Default value: 604800000.
        """
        return pulumi.get(self, "retention_time")

    @retention_time.setter
    def retention_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_time", value)

    @property
    @pulumi.getter(name="segmentBytes")
    def segment_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        [int] This configuration controls the segment file size for the log. Retention and
        cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
        retention. Default value: 1073741824.
        """
        return pulumi.get(self, "segment_bytes")

    @segment_bytes.setter
    def segment_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "segment_bytes", value)


@pulumi.input_type
class _KafkaClusterTopicState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 number_of_partitions: Optional[pulumi.Input[int]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 retention_time: Optional[pulumi.Input[int]] = None,
                 segment_bytes: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering KafkaClusterTopic resources.
        :param pulumi.Input[str] cluster_id: [string] ID of the Kafka Cluster that the topic belongs to.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[int] number_of_partitions: [int] The number of partitions of the topic. Partitions allow for parallel
               processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
               Default value: 3.
        :param pulumi.Input[int] replication_factor: [int] The number of replicas of the topic. The replication factor determines how many
               copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
               of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        :param pulumi.Input[int] retention_time: [int] This configuration controls the maximum time we will retain a log before we will
               discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
               to -1, no time limit is applied. Default value: 604800000.
        :param pulumi.Input[int] segment_bytes: [int] This configuration controls the segment file size for the log. Retention and
               cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
               retention. Default value: 1073741824.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if number_of_partitions is not None:
            pulumi.set(__self__, "number_of_partitions", number_of_partitions)
        if replication_factor is not None:
            pulumi.set(__self__, "replication_factor", replication_factor)
        if retention_time is not None:
            pulumi.set(__self__, "retention_time", retention_time)
        if segment_bytes is not None:
            pulumi.set(__self__, "segment_bytes", segment_bytes)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        [string] ID of the Kafka Cluster that the topic belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
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
    @pulumi.getter(name="numberOfPartitions")
    def number_of_partitions(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The number of partitions of the topic. Partitions allow for parallel
        processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
        Default value: 3.
        """
        return pulumi.get(self, "number_of_partitions")

    @number_of_partitions.setter
    def number_of_partitions(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number_of_partitions", value)

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> Optional[pulumi.Input[int]]:
        """
        [int] The number of replicas of the topic. The replication factor determines how many
        copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
        of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        """
        return pulumi.get(self, "replication_factor")

    @replication_factor.setter
    def replication_factor(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "replication_factor", value)

    @property
    @pulumi.getter(name="retentionTime")
    def retention_time(self) -> Optional[pulumi.Input[int]]:
        """
        [int] This configuration controls the maximum time we will retain a log before we will
        discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
        to -1, no time limit is applied. Default value: 604800000.
        """
        return pulumi.get(self, "retention_time")

    @retention_time.setter
    def retention_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_time", value)

    @property
    @pulumi.getter(name="segmentBytes")
    def segment_bytes(self) -> Optional[pulumi.Input[int]]:
        """
        [int] This configuration controls the segment file size for the log. Retention and
        cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
        retention. Default value: 1073741824.
        """
        return pulumi.get(self, "segment_bytes")

    @segment_bytes.setter
    def segment_bytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "segment_bytes", value)


warnings.warn("""ionoscloud.index/kafkaclustertopic.KafkaClusterTopic has been deprecated in favor of ionoscloud.kafka/topic.Topic""", DeprecationWarning)


class KafkaClusterTopic(pulumi.CustomResource):
    warnings.warn("""ionoscloud.index/kafkaclustertopic.KafkaClusterTopic has been deprecated in favor of ionoscloud.kafka/topic.Topic""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 number_of_partitions: Optional[pulumi.Input[int]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 retention_time: Optional[pulumi.Input[int]] = None,
                 segment_bytes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Manages a **Kafka Cluster Topic** on IonosCloud.

        ## Example Usage

        This resource will create an operational Kafka Cluster Topic. After this section completes, the provisioner can be
        called.

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter", location="de/fra")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_cluster = ionoscloud.kafka.Cluster("exampleCluster",
            location=example_datacenter.location,
            version="3.7.0",
            size="S",
            connections=ionoscloud.kafka.ClusterConnectionsArgs(
                datacenter_id=example_datacenter.id,
                lan_id=example_lan.id,
                broker_addresses=[
                    "192.168.1.101/24",
                    "192.168.1.102/24",
                    "192.168.1.103/24",
                ],
            ))
        example_topic = ionoscloud.kafka.Topic("exampleTopic",
            cluster_id=example_cluster.id,
            location=example_cluster.location,
            replication_factor=1,
            number_of_partitions=1,
            retention_time=86400000,
            segment_bytes=1073741824)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Kafka Cluster Topic can be imported using the `location`, `kafka cluster id` and the `kafka cluster topic id`:

        ```sh
        $ pulumi import ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic my_topic {location}:{kafka cluster uuid}:{kafka cluster topic uuid}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: [string] ID of the Kafka Cluster that the topic belongs to.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[int] number_of_partitions: [int] The number of partitions of the topic. Partitions allow for parallel
               processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
               Default value: 3.
        :param pulumi.Input[int] replication_factor: [int] The number of replicas of the topic. The replication factor determines how many
               copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
               of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        :param pulumi.Input[int] retention_time: [int] This configuration controls the maximum time we will retain a log before we will
               discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
               to -1, no time limit is applied. Default value: 604800000.
        :param pulumi.Input[int] segment_bytes: [int] This configuration controls the segment file size for the log. Retention and
               cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
               retention. Default value: 1073741824.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KafkaClusterTopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a **Kafka Cluster Topic** on IonosCloud.

        ## Example Usage

        This resource will create an operational Kafka Cluster Topic. After this section completes, the provisioner can be
        called.

        <!--Start PulumiCodeChooser -->
        ```python
        import pulumi
        import ionoscloud as ionoscloud

        # Basic example
        example_datacenter = ionoscloud.compute.Datacenter("exampleDatacenter", location="de/fra")
        example_lan = ionoscloud.compute.Lan("exampleLan",
            datacenter_id=example_datacenter.id,
            public=False)
        example_cluster = ionoscloud.kafka.Cluster("exampleCluster",
            location=example_datacenter.location,
            version="3.7.0",
            size="S",
            connections=ionoscloud.kafka.ClusterConnectionsArgs(
                datacenter_id=example_datacenter.id,
                lan_id=example_lan.id,
                broker_addresses=[
                    "192.168.1.101/24",
                    "192.168.1.102/24",
                    "192.168.1.103/24",
                ],
            ))
        example_topic = ionoscloud.kafka.Topic("exampleTopic",
            cluster_id=example_cluster.id,
            location=example_cluster.location,
            replication_factor=1,
            number_of_partitions=1,
            retention_time=86400000,
            segment_bytes=1073741824)
        ```
        <!--End PulumiCodeChooser -->

        ## Import

        Kafka Cluster Topic can be imported using the `location`, `kafka cluster id` and the `kafka cluster topic id`:

        ```sh
        $ pulumi import ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic my_topic {location}:{kafka cluster uuid}:{kafka cluster topic uuid}
        ```

        :param str resource_name: The name of the resource.
        :param KafkaClusterTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KafkaClusterTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 number_of_partitions: Optional[pulumi.Input[int]] = None,
                 replication_factor: Optional[pulumi.Input[int]] = None,
                 retention_time: Optional[pulumi.Input[int]] = None,
                 segment_bytes: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        pulumi.log.warn("""KafkaClusterTopic is deprecated: ionoscloud.index/kafkaclustertopic.KafkaClusterTopic has been deprecated in favor of ionoscloud.kafka/topic.Topic""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KafkaClusterTopicArgs.__new__(KafkaClusterTopicArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["number_of_partitions"] = number_of_partitions
            __props__.__dict__["replication_factor"] = replication_factor
            __props__.__dict__["retention_time"] = retention_time
            __props__.__dict__["segment_bytes"] = segment_bytes
        super(KafkaClusterTopic, __self__).__init__(
            'ionoscloud:index/kafkaClusterTopic:KafkaClusterTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            number_of_partitions: Optional[pulumi.Input[int]] = None,
            replication_factor: Optional[pulumi.Input[int]] = None,
            retention_time: Optional[pulumi.Input[int]] = None,
            segment_bytes: Optional[pulumi.Input[int]] = None) -> 'KafkaClusterTopic':
        """
        Get an existing KafkaClusterTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: [string] ID of the Kafka Cluster that the topic belongs to.
        :param pulumi.Input[str] location: [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
        :param pulumi.Input[str] name: [string] Name of the Kafka Cluster.
        :param pulumi.Input[int] number_of_partitions: [int] The number of partitions of the topic. Partitions allow for parallel
               processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
               Default value: 3.
        :param pulumi.Input[int] replication_factor: [int] The number of replicas of the topic. The replication factor determines how many
               copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
               of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        :param pulumi.Input[int] retention_time: [int] This configuration controls the maximum time we will retain a log before we will
               discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
               to -1, no time limit is applied. Default value: 604800000.
        :param pulumi.Input[int] segment_bytes: [int] This configuration controls the segment file size for the log. Retention and
               cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
               retention. Default value: 1073741824.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KafkaClusterTopicState.__new__(_KafkaClusterTopicState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["number_of_partitions"] = number_of_partitions
        __props__.__dict__["replication_factor"] = replication_factor
        __props__.__dict__["retention_time"] = retention_time
        __props__.__dict__["segment_bytes"] = segment_bytes
        return KafkaClusterTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        [string] ID of the Kafka Cluster that the topic belongs to.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        [string] The location of the Kafka Cluster Topic. Possible values: `de/fra`, `de/txl`
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
    @pulumi.getter(name="numberOfPartitions")
    def number_of_partitions(self) -> pulumi.Output[Optional[int]]:
        """
        [int] The number of partitions of the topic. Partitions allow for parallel
        processing of messages. The partition count must be greater than or equal to the replication factor. Minimum value: 1.
        Default value: 3.
        """
        return pulumi.get(self, "number_of_partitions")

    @property
    @pulumi.getter(name="replicationFactor")
    def replication_factor(self) -> pulumi.Output[Optional[int]]:
        """
        [int] The number of replicas of the topic. The replication factor determines how many
        copies of the topic are stored on different brokers. The replication factor must be less than or equal to the number
        of brokers in the Kafka Cluster. Minimum value: 1. Default value: 3.
        """
        return pulumi.get(self, "replication_factor")

    @property
    @pulumi.getter(name="retentionTime")
    def retention_time(self) -> pulumi.Output[Optional[int]]:
        """
        [int] This configuration controls the maximum time we will retain a log before we will
        discard old log segments to free up space. This represents an SLA on how soon consumers must read their data. If set
        to -1, no time limit is applied. Default value: 604800000.
        """
        return pulumi.get(self, "retention_time")

    @property
    @pulumi.getter(name="segmentBytes")
    def segment_bytes(self) -> pulumi.Output[Optional[int]]:
        """
        [int] This configuration controls the segment file size for the log. Retention and
        cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over
        retention. Default value: 1073741824.
        """
        return pulumi.get(self, "segment_bytes")

