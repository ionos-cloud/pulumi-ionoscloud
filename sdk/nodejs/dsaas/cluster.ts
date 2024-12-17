// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Dataplatform Cluster**.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {
 *     location: "de/txl",
 *     description: "Datacenter for testing Dataplatform Cluster",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("exampleLan", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": false,
 * });
 * const exampleCluster = new ionoscloud.dsaas.Cluster("exampleCluster", {
 *     datacenterId: exampleDatacenter.id,
 *     maintenanceWindows: [{
 *         dayOfTheWeek: "Sunday",
 *         time: "09:00:00",
 *     }],
 *     version: "23.11",
 *     lans: [{
 *         lanId: exampleLan.id,
 *         dhcp: false,
 *         routes: [{
 *             network: "182.168.42.1/24",
 *             gateway: "192.168.42.1",
 *         }],
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * Resource Dataplatform Cluster can be imported using the `cluster_id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:dsaas/cluster:Cluster mycluser {cluster uuid}
 * ```
 */
export class Cluster extends pulumi.CustomResource {
    /**
     * Get an existing Cluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState, opts?: pulumi.CustomResourceOptions): Cluster {
        return new Cluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:dsaas/cluster:Cluster';

    /**
     * Returns true if the given object is an instance of Cluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Cluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Cluster.__pulumiType;
    }

    /**
     * [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [list] A list of LANs you want this node pool to be part of.
     */
    public readonly lans!: pulumi.Output<outputs.dsaas.ClusterLan[] | undefined>;
    /**
     * [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    public readonly maintenanceWindows!: pulumi.Output<outputs.dsaas.ClusterMaintenanceWindow[]>;
    /**
     * [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [int] The version of the Data Platform.
     */
    public readonly version!: pulumi.Output<string>;

    /**
     * Create a Cluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ClusterArgs | ClusterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ClusterState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["lans"] = state ? state.lans : undefined;
            resourceInputs["maintenanceWindows"] = state ? state.maintenanceWindows : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as ClusterArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["lans"] = args ? args.lans : undefined;
            resourceInputs["maintenanceWindows"] = args ? args.maintenanceWindows : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Cluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Cluster resources.
 */
export interface ClusterState {
    /**
     * [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [list] A list of LANs you want this node pool to be part of.
     */
    lans?: pulumi.Input<pulumi.Input<inputs.dsaas.ClusterLan>[]>;
    /**
     * [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    maintenanceWindows?: pulumi.Input<pulumi.Input<inputs.dsaas.ClusterMaintenanceWindow>[]>;
    /**
     * [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    name?: pulumi.Input<string>;
    /**
     * [int] The version of the Data Platform.
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    /**
     * [string] The UUID of the virtual data center (VDC) the cluster is provisioned.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [list] A list of LANs you want this node pool to be part of.
     */
    lans?: pulumi.Input<pulumi.Input<inputs.dsaas.ClusterLan>[]>;
    /**
     * [string] Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    maintenanceWindows?: pulumi.Input<pulumi.Input<inputs.dsaas.ClusterMaintenanceWindow>[]>;
    /**
     * [string] The name of your cluster. Must be 63 characters or less and must be empty or begin and end with an alphanumeric character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    name?: pulumi.Input<string>;
    /**
     * [int] The version of the Data Platform.
     */
    version?: pulumi.Input<string>;
}
