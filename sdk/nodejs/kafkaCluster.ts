// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages a **Kafka Cluster** on IonosCloud.
 *
 * ## Example Usage
 *
 * This resource will create an operational Kafka Cluster. After this section completes, the provisioner can be called.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * // Basic example
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {location: "de/fra"});
 * const exampleLan = new ionoscloud.compute.Lan("exampleLan", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": false,
 * });
 * const exampleKafkaCluster = new ionoscloud.KafkaCluster("exampleKafkaCluster", {
 *     location: "de/fra",
 *     version: "3.7.0",
 *     size: "S",
 *     connections: {
 *         datacenterId: exampleDatacenter.id,
 *         lanId: exampleLan.id,
 *         brokerAddresses: [
 *             "192.168.1.101/24",
 *             "192.168.1.102/24",
 *             "192.168.1.103/24",
 *         ],
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * Kafka Cluster can be imported using the `location` and `kafka cluster id`:
 *
 * ```sh
 * $ pulumi import ionoscloud:index/kafkaCluster:KafkaCluster mycluster {location}:{kafka cluster uuid}
 * ```
 */
export class KafkaCluster extends pulumi.CustomResource {
    /**
     * Get an existing KafkaCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KafkaClusterState, opts?: pulumi.CustomResourceOptions): KafkaCluster {
        return new KafkaCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/kafkaCluster:KafkaCluster';

    /**
     * Returns true if the given object is an instance of KafkaCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KafkaCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KafkaCluster.__pulumiType;
    }

    /**
     * [list] IP address and port of cluster brokers.
     */
    public /*out*/ readonly brokerAddresses!: pulumi.Output<string[]>;
    /**
     * Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     */
    public readonly connections!: pulumi.Output<outputs.KafkaClusterConnections>;
    /**
     * [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * [string] Name of the Kafka Cluster.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
     */
    public readonly size!: pulumi.Output<string>;
    /**
     * [string] Version of the Kafka Cluster. Possible values: `3.7.0`
     */
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a KafkaCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KafkaClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KafkaClusterArgs | KafkaClusterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KafkaClusterState | undefined;
            resourceInputs["brokerAddresses"] = state ? state.brokerAddresses : undefined;
            resourceInputs["connections"] = state ? state.connections : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as KafkaClusterArgs | undefined;
            if ((!args || args.connections === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connections'");
            }
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            if ((!args || args.size === undefined) && !opts.urn) {
                throw new Error("Missing required property 'size'");
            }
            if ((!args || args.version === undefined) && !opts.urn) {
                throw new Error("Missing required property 'version'");
            }
            resourceInputs["connections"] = args ? args.connections : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
            resourceInputs["brokerAddresses"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(KafkaCluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KafkaCluster resources.
 */
export interface KafkaClusterState {
    /**
     * [list] IP address and port of cluster brokers.
     */
    brokerAddresses?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     */
    connections?: pulumi.Input<inputs.KafkaClusterConnections>;
    /**
     * [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     */
    location?: pulumi.Input<string>;
    /**
     * [string] Name of the Kafka Cluster.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
     */
    size?: pulumi.Input<string>;
    /**
     * [string] Version of the Kafka Cluster. Possible values: `3.7.0`
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a KafkaCluster resource.
 */
export interface KafkaClusterArgs {
    /**
     * Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     */
    connections: pulumi.Input<inputs.KafkaClusterConnections>;
    /**
     * [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     */
    location: pulumi.Input<string>;
    /**
     * [string] Name of the Kafka Cluster.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
     */
    size: pulumi.Input<string>;
    /**
     * [string] Version of the Kafka Cluster. Possible values: `3.7.0`
     */
    version: pulumi.Input<string>;
}
