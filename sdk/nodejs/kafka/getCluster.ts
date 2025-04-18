// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
 * You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
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
 * const example = ionoscloud.kafka.getCluster({
 *     id: "your_kafka_cluster_id",
 *     location: "location_of_kafka_cluster",
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
 * const example = ionoscloud.kafka.getCluster({
 *     name: "kafka-cluster",
 *     location: "location_of_kafka_cluster",
 * });
 * ```
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:kafka/getCluster:getCluster", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterArgs {
    /**
     * ID of an existing Kafka Cluster that you want to search for.
     */
    id?: string;
    /**
     * The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     */
    location: string;
    /**
     * Name of an existing Kafka Cluster that you want to search for.
     */
    name?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    /**
     * IP address and port of cluster brokers.
     */
    readonly brokerAddresses: string[];
    /**
     * Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     */
    readonly connections: outputs.kafka.GetClusterConnection[];
    /**
     * UUID of the Kafka Cluster.
     */
    readonly id: string;
    readonly location: string;
    /**
     * The name of the Kafka Cluster.
     */
    readonly name: string;
    readonly partialMatch?: boolean;
    /**
     * The size of the Kafka Cluster.
     */
    readonly size: string;
    /**
     * The version of the Kafka Cluster.
     */
    readonly version: string;
}
/**
 * The **Kafka Cluster data source** can be used to search for and return an existing Kafka Cluster.
 * You can provide a string for the name parameter which will be compared with provisioned Kafka Clusters.
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
 * const example = ionoscloud.kafka.getCluster({
 *     id: "your_kafka_cluster_id",
 *     location: "location_of_kafka_cluster",
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
 * const example = ionoscloud.kafka.getCluster({
 *     name: "kafka-cluster",
 *     location: "location_of_kafka_cluster",
 * });
 * ```
 */
export function getClusterOutput(args: GetClusterOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetClusterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:kafka/getCluster:getCluster", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getCluster.
 */
export interface GetClusterOutputArgs {
    /**
     * ID of an existing Kafka Cluster that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     */
    location: pulumi.Input<string>;
    /**
     * Name of an existing Kafka Cluster that you want to search for.
     */
    name?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
