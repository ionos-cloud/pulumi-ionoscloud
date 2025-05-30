// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **Kafka topic data source** can be used to search for and return an existing Kafka Cluster Topic.
 * You can provide a string for the name parameter which will be compared with provisioned Kafka Cluster Topics.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.kafka.getTopic({
 *     id: "your_kafka_cluster_topic_id",
 *     clusterId: "your_kafka_cluster_id",
 *     location: "your_kafka_cluster_location",
 * });
 * ```
 *
 * ### By Name
 *
 * Needs to have the resource be previously created, or a dependsOn clause to ensure that the resource is created before
 * this data source is called.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.kafka.getTopic({
 *     name: "kafka-cluster-topic",
 *     clusterId: "your_kafka_cluster_id",
 *     location: "location_of_kafka_cluster",
 * });
 * ```
 */
export function getTopic(args: GetTopicArgs, opts?: pulumi.InvokeOptions): Promise<GetTopicResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:kafka/getTopic:getTopic", {
        "clusterId": args.clusterId,
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getTopic.
 */
export interface GetTopicArgs {
    /**
     * ID of the Kafka Cluster that the topic belongs to.
     */
    clusterId: string;
    /**
     * ID of an existing Kafka Cluster Topic that you want to search for.
     */
    id?: string;
    /**
     * The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
     * Cluster. Possible values: `de/fra`, `de/txl`
     */
    location: string;
    /**
     * Name of an existing Kafka Cluster Topic that you want to search for.
     */
    name?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getTopic.
 */
export interface GetTopicResult {
    /**
     * The id of the Kafka Cluster that the topic belongs to.
     */
    readonly clusterId: string;
    /**
     * UUID of the Kafka Cluster Topic.
     */
    readonly id: string;
    readonly location: string;
    /**
     * The name of the Kafka Cluster Topic.
     */
    readonly name: string;
    /**
     * The number of partitions of the topic. Partitions allow for parallel processing of messages.
     */
    readonly numberOfPartitions: number;
    readonly partialMatch?: boolean;
    /**
     * The number of replicas of the topic. The replication factor determines how many copies of the
     * topic are stored on different brokers.
     */
    readonly replicationFactor: number;
    /**
     * This configuration controls the maximum time we will retain a log before we will discard old log
     * segments to free up space. This represents an SLA on how soon consumers must read their data. If set to -1, no time
     * limit is applied.
     */
    readonly retentionTime: number;
    /**
     * This configuration controls the segment file size for the log. Retention and cleaning is always done a file at a time so a larger segment size means fewer files but less granular control over retention.
     */
    readonly segmentBytes: number;
}
/**
 * The **Kafka topic data source** can be used to search for and return an existing Kafka Cluster Topic.
 * You can provide a string for the name parameter which will be compared with provisioned Kafka Cluster Topics.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.kafka.getTopic({
 *     id: "your_kafka_cluster_topic_id",
 *     clusterId: "your_kafka_cluster_id",
 *     location: "your_kafka_cluster_location",
 * });
 * ```
 *
 * ### By Name
 *
 * Needs to have the resource be previously created, or a dependsOn clause to ensure that the resource is created before
 * this data source is called.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.kafka.getTopic({
 *     name: "kafka-cluster-topic",
 *     clusterId: "your_kafka_cluster_id",
 *     location: "location_of_kafka_cluster",
 * });
 * ```
 */
export function getTopicOutput(args: GetTopicOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetTopicResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:kafka/getTopic:getTopic", {
        "clusterId": args.clusterId,
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getTopic.
 */
export interface GetTopicOutputArgs {
    /**
     * ID of the Kafka Cluster that the topic belongs to.
     */
    clusterId: pulumi.Input<string>;
    /**
     * ID of an existing Kafka Cluster Topic that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
     * Cluster. Possible values: `de/fra`, `de/txl`
     */
    location: pulumi.Input<string>;
    /**
     * Name of an existing Kafka Cluster Topic that you want to search for.
     */
    name?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
