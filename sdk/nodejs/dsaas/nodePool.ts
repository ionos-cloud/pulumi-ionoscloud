// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class NodePool extends pulumi.CustomResource {
    /**
     * Get an existing NodePool resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NodePoolState, opts?: pulumi.CustomResourceOptions): NodePool {
        return new NodePool(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:dsaas/nodePool:NodePool';

    /**
     * Returns true if the given object is an instance of NodePool.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NodePool {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NodePool.__pulumiType;
    }

    /**
     * Key-value pairs attached to node pool resource as [Kubernetes
     * annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
     */
    public readonly annotations!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * The UUID of an existing Dataplatform cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The number of CPU cores per node.
     */
    public readonly coresCount!: pulumi.Output<number>;
    /**
     * A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
     * be retrieved from the datacenter resource.
     */
    public readonly cpuFamily!: pulumi.Output<string>;
    /**
     * The UUID of the virtual data center (VDC) in which the nodepool is provisioned
     */
    public /*out*/ readonly datacenterId!: pulumi.Output<string>;
    /**
     * Key-value pairs attached to the node pool resource as [Kubernetes
     * labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    public readonly maintenanceWindows!: pulumi.Output<outputs.dsaas.NodePoolMaintenanceWindow[]>;
    /**
     * The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
     * character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The number of nodes that make up the node pool.
     */
    public readonly nodeCount!: pulumi.Output<number>;
    /**
     * The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
     */
    public readonly ramSize!: pulumi.Output<number>;
    /**
     * The size of the volume in GB. The size must be greater than 10GB.
     */
    public readonly storageSize!: pulumi.Output<number>;
    /**
     * The type of hardware for the volume.
     */
    public readonly storageType!: pulumi.Output<string>;
    /**
     * The version of the Data Platform.
     */
    public /*out*/ readonly version!: pulumi.Output<string>;

    /**
     * Create a NodePool resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NodePoolArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NodePoolArgs | NodePoolState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NodePoolState | undefined;
            resourceInputs["annotations"] = state ? state.annotations : undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["coresCount"] = state ? state.coresCount : undefined;
            resourceInputs["cpuFamily"] = state ? state.cpuFamily : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["maintenanceWindows"] = state ? state.maintenanceWindows : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nodeCount"] = state ? state.nodeCount : undefined;
            resourceInputs["ramSize"] = state ? state.ramSize : undefined;
            resourceInputs["storageSize"] = state ? state.storageSize : undefined;
            resourceInputs["storageType"] = state ? state.storageType : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as NodePoolArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.nodeCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nodeCount'");
            }
            resourceInputs["annotations"] = args ? args.annotations : undefined;
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["coresCount"] = args ? args.coresCount : undefined;
            resourceInputs["cpuFamily"] = args ? args.cpuFamily : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["maintenanceWindows"] = args ? args.maintenanceWindows : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nodeCount"] = args ? args.nodeCount : undefined;
            resourceInputs["ramSize"] = args ? args.ramSize : undefined;
            resourceInputs["storageSize"] = args ? args.storageSize : undefined;
            resourceInputs["storageType"] = args ? args.storageType : undefined;
            resourceInputs["datacenterId"] = undefined /*out*/;
            resourceInputs["version"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NodePool.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NodePool resources.
 */
export interface NodePoolState {
    /**
     * Key-value pairs attached to node pool resource as [Kubernetes
     * annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
     */
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * The UUID of an existing Dataplatform cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The number of CPU cores per node.
     */
    coresCount?: pulumi.Input<number>;
    /**
     * A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
     * be retrieved from the datacenter resource.
     */
    cpuFamily?: pulumi.Input<string>;
    /**
     * The UUID of the virtual data center (VDC) in which the nodepool is provisioned
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * Key-value pairs attached to the node pool resource as [Kubernetes
     * labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    maintenanceWindows?: pulumi.Input<pulumi.Input<inputs.dsaas.NodePoolMaintenanceWindow>[]>;
    /**
     * The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
     * character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    name?: pulumi.Input<string>;
    /**
     * The number of nodes that make up the node pool.
     */
    nodeCount?: pulumi.Input<number>;
    /**
     * The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
     */
    ramSize?: pulumi.Input<number>;
    /**
     * The size of the volume in GB. The size must be greater than 10GB.
     */
    storageSize?: pulumi.Input<number>;
    /**
     * The type of hardware for the volume.
     */
    storageType?: pulumi.Input<string>;
    /**
     * The version of the Data Platform.
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NodePool resource.
 */
export interface NodePoolArgs {
    /**
     * Key-value pairs attached to node pool resource as [Kubernetes
     * annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
     */
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The availability zone of the virtual datacenter region where the node pool resources should be provisioned.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * The UUID of an existing Dataplatform cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * The number of CPU cores per node.
     */
    coresCount?: pulumi.Input<number>;
    /**
     * A valid CPU family name or `AUTO` if the platform shall choose the best fitting option. Available CPU architectures can
     * be retrieved from the datacenter resource.
     */
    cpuFamily?: pulumi.Input<string>;
    /**
     * Key-value pairs attached to the node pool resource as [Kubernetes
     * labels](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * Starting time of a weekly 4 hour-long window, during which maintenance might occur in hh:mm:ss format
     */
    maintenanceWindows?: pulumi.Input<pulumi.Input<inputs.dsaas.NodePoolMaintenanceWindow>[]>;
    /**
     * The name of your node pool. Must be 63 characters or less and must be empty or begin and end with an alphanumeric
     * character ([a-z0-9A-Z]). It can contain dashes (-), underscores (_), dots (.), and alphanumerics in-between.
     */
    name?: pulumi.Input<string>;
    /**
     * The number of nodes that make up the node pool.
     */
    nodeCount: pulumi.Input<number>;
    /**
     * The RAM size for one node in MB. Must be set in multiples of 1024 MB, with a minimum size is of 2048 MB.
     */
    ramSize?: pulumi.Input<number>;
    /**
     * The size of the volume in GB. The size must be greater than 10GB.
     */
    storageSize?: pulumi.Input<number>;
    /**
     * The type of hardware for the volume.
     */
    storageType?: pulumi.Input<string>;
}
