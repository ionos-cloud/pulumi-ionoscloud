// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Managed Kubernetes Node Pool**, part of a managed Kubernetes cluster on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {
 *     location: "us/las",
 *     description: "datacenter description",
 *     secAuthProtection: false,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("exampleLan", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": false,
 * });
 * const exampleIPBlock = new ionoscloud.compute.IPBlock("exampleIPBlock", {
 *     location: "us/las",
 *     size: 3,
 * });
 * const exampleCluster = new ionoscloud.k8s.Cluster("exampleCluster", {
 *     k8sVersion: "1.28.6",
 *     maintenanceWindow: {
 *         dayOfTheWeek: "Sunday",
 *         time: "09:00:00Z",
 *     },
 *     apiSubnetAllowLists: ["1.2.3.4/32"],
 *     s3Buckets: [{
 *         name: "globally_unique_s3_bucket_name",
 *     }],
 * });
 * const exampleNodePool = new ionoscloud.k8s.NodePool("exampleNodePool", {
 *     datacenterId: exampleDatacenter.id,
 *     k8sClusterId: exampleCluster.id,
 *     k8sVersion: exampleCluster.k8sVersion,
 *     maintenanceWindow: {
 *         dayOfTheWeek: "Monday",
 *         time: "09:00:00Z",
 *     },
 *     autoScaling: {
 *         minNodeCount: 1,
 *         maxNodeCount: 2,
 *     },
 *     cpuFamily: "INTEL_XEON",
 *     availabilityZone: "AUTO",
 *     storageType: "SSD",
 *     nodeCount: 1,
 *     coresCount: 2,
 *     ramSize: 2048,
 *     storageSize: 40,
 *     publicIps: [
 *         exampleIPBlock.ips[0],
 *         exampleIPBlock.ips[1],
 *         exampleIPBlock.ips[2],
 *     ],
 *     lans: [{
 *         id: exampleLan.id,
 *         dhcp: true,
 *         routes: [{
 *             network: "1.2.3.5/24",
 *             gatewayIp: "10.1.5.17",
 *         }],
 *     }],
 *     labels: {
 *         lab1: "value1",
 *         lab2: "value2",
 *     },
 *     annotations: {
 *         ann1: "value1",
 *         ann2: "value2",
 *     },
 * });
 * ```
 * **Note:** Set `createBeforeDestroy` on the lan resource if you want to remove it from the nodepool during an update. This is to ensure that the nodepool is updated before the lan is destroyed.
 *
 * ## Import
 *
 * A Kubernetes Node Pool resource can be imported using its Kubernetes cluster's uuid as well as its own UUID, both of which you can retrieve from the cloud API: `resource id`, e.g.:
 *
 * ```sh
 * $ pulumi import ionoscloud:k8s/nodePool:NodePool demo {k8s_cluster_uuid}/{k8s_nodepool_id}
 * ```
 *
 * This can be helpful when you want to import kubernetes node pools which you have already created manually or using other means, outside of terraform, towards the goal of managing them via Terraform
 *
 * ⚠️ **_Warning: **During a maintenance window, k8s can update your `k8s_version` if the old one reaches end of life. This upgrade will not be shown in the plan, as we prevent
 *
 * terraform from doing a downgrade, as downgrading `k8s_version` is not supported._**
 *
 * ⚠️ **_Warning: **If you are upgrading from v5.x.x to v6.x.x**: You have to modify you plan for lans to match the new structure, by putting the ids from the old slice in lans.id fields. This is not backwards compatible._**
 */
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
    public static readonly __pulumiType = 'ionoscloud:k8s/nodePool:NodePool';

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
     * When set to true, allows the update of immutable fields by destroying and re-creating the node pool
     */
    public readonly allowReplace!: pulumi.Output<boolean | undefined>;
    /**
     * [map] A key/value map of annotations
     */
    public readonly annotations!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
     */
    public readonly autoScaling!: pulumi.Output<outputs.k8s.NodePoolAutoScaling | undefined>;
    /**
     * [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
     */
    public readonly availabilityZone!: pulumi.Output<string>;
    /**
     * [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
     */
    public readonly coresCount!: pulumi.Output<number>;
    /**
     * [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
     */
    public readonly cpuFamily!: pulumi.Output<string>;
    /**
     * [string] A Datacenter's UUID
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [string] A k8s cluster's UUID
     */
    public readonly k8sClusterId!: pulumi.Output<string>;
    /**
     * [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
     */
    public readonly k8sVersion!: pulumi.Output<string>;
    /**
     * [map] A key/value map of labels
     */
    public readonly labels!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
     */
    public readonly lans!: pulumi.Output<outputs.k8s.NodePoolLan[] | undefined>;
    /**
     * See the **maintenance_window** section in the example above
     */
    public readonly maintenanceWindow!: pulumi.Output<outputs.k8s.NodePoolMaintenanceWindow>;
    /**
     * [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [int] - The desired number of nodes in the node pool
     */
    public readonly nodeCount!: pulumi.Output<number>;
    /**
     * [list] A list of public IPs associated with the node pool; must have at least `nodeCount + 1` elements
     */
    public readonly publicIps!: pulumi.Output<string[] | undefined>;
    /**
     * [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
     */
    public readonly ramSize!: pulumi.Output<number>;
    /**
     * [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
     */
    public readonly storageSize!: pulumi.Output<number>;
    /**
     * [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
     */
    public readonly storageType!: pulumi.Output<string>;

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
            resourceInputs["allowReplace"] = state ? state.allowReplace : undefined;
            resourceInputs["annotations"] = state ? state.annotations : undefined;
            resourceInputs["autoScaling"] = state ? state.autoScaling : undefined;
            resourceInputs["availabilityZone"] = state ? state.availabilityZone : undefined;
            resourceInputs["coresCount"] = state ? state.coresCount : undefined;
            resourceInputs["cpuFamily"] = state ? state.cpuFamily : undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["k8sClusterId"] = state ? state.k8sClusterId : undefined;
            resourceInputs["k8sVersion"] = state ? state.k8sVersion : undefined;
            resourceInputs["labels"] = state ? state.labels : undefined;
            resourceInputs["lans"] = state ? state.lans : undefined;
            resourceInputs["maintenanceWindow"] = state ? state.maintenanceWindow : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nodeCount"] = state ? state.nodeCount : undefined;
            resourceInputs["publicIps"] = state ? state.publicIps : undefined;
            resourceInputs["ramSize"] = state ? state.ramSize : undefined;
            resourceInputs["storageSize"] = state ? state.storageSize : undefined;
            resourceInputs["storageType"] = state ? state.storageType : undefined;
        } else {
            const args = argsOrState as NodePoolArgs | undefined;
            if ((!args || args.availabilityZone === undefined) && !opts.urn) {
                throw new Error("Missing required property 'availabilityZone'");
            }
            if ((!args || args.coresCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'coresCount'");
            }
            if ((!args || args.cpuFamily === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cpuFamily'");
            }
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.k8sClusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'k8sClusterId'");
            }
            if ((!args || args.k8sVersion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'k8sVersion'");
            }
            if ((!args || args.nodeCount === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nodeCount'");
            }
            if ((!args || args.ramSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ramSize'");
            }
            if ((!args || args.storageSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageSize'");
            }
            if ((!args || args.storageType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageType'");
            }
            resourceInputs["allowReplace"] = args ? args.allowReplace : undefined;
            resourceInputs["annotations"] = args ? args.annotations : undefined;
            resourceInputs["autoScaling"] = args ? args.autoScaling : undefined;
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["coresCount"] = args ? args.coresCount : undefined;
            resourceInputs["cpuFamily"] = args ? args.cpuFamily : undefined;
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["k8sClusterId"] = args ? args.k8sClusterId : undefined;
            resourceInputs["k8sVersion"] = args ? args.k8sVersion : undefined;
            resourceInputs["labels"] = args ? args.labels : undefined;
            resourceInputs["lans"] = args ? args.lans : undefined;
            resourceInputs["maintenanceWindow"] = args ? args.maintenanceWindow : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nodeCount"] = args ? args.nodeCount : undefined;
            resourceInputs["publicIps"] = args ? args.publicIps : undefined;
            resourceInputs["ramSize"] = args ? args.ramSize : undefined;
            resourceInputs["storageSize"] = args ? args.storageSize : undefined;
            resourceInputs["storageType"] = args ? args.storageType : undefined;
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
     * When set to true, allows the update of immutable fields by destroying and re-creating the node pool
     */
    allowReplace?: pulumi.Input<boolean>;
    /**
     * [map] A key/value map of annotations
     */
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
     */
    autoScaling?: pulumi.Input<inputs.k8s.NodePoolAutoScaling>;
    /**
     * [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
     */
    coresCount?: pulumi.Input<number>;
    /**
     * [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
     */
    cpuFamily?: pulumi.Input<string>;
    /**
     * [string] A Datacenter's UUID
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [string] A k8s cluster's UUID
     */
    k8sClusterId?: pulumi.Input<string>;
    /**
     * [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
     */
    k8sVersion?: pulumi.Input<string>;
    /**
     * [map] A key/value map of labels
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
     */
    lans?: pulumi.Input<pulumi.Input<inputs.k8s.NodePoolLan>[]>;
    /**
     * See the **maintenance_window** section in the example above
     */
    maintenanceWindow?: pulumi.Input<inputs.k8s.NodePoolMaintenanceWindow>;
    /**
     * [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
     */
    name?: pulumi.Input<string>;
    /**
     * [int] - The desired number of nodes in the node pool
     */
    nodeCount?: pulumi.Input<number>;
    /**
     * [list] A list of public IPs associated with the node pool; must have at least `nodeCount + 1` elements
     */
    publicIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
     */
    ramSize?: pulumi.Input<number>;
    /**
     * [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
     */
    storageSize?: pulumi.Input<number>;
    /**
     * [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
     */
    storageType?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NodePool resource.
 */
export interface NodePoolArgs {
    /**
     * When set to true, allows the update of immutable fields by destroying and re-creating the node pool
     */
    allowReplace?: pulumi.Input<boolean>;
    /**
     * [map] A key/value map of annotations
     */
    annotations?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * [string] Wether the Node Pool should autoscale. For more details, please check the API documentation
     */
    autoScaling?: pulumi.Input<inputs.k8s.NodePoolAutoScaling>;
    /**
     * [string] - The desired Compute availability zone - See the API documentation for more information. *This attribute is immutable*.
     */
    availabilityZone: pulumi.Input<string>;
    /**
     * [int] - The CPU cores count for each node of the node pool. *This attribute is immutable*.
     */
    coresCount: pulumi.Input<number>;
    /**
     * [string] The desired CPU Family - See the API documentation for more information. *This attribute is immutable*.
     */
    cpuFamily: pulumi.Input<string>;
    /**
     * [string] A Datacenter's UUID
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] A k8s cluster's UUID
     */
    k8sClusterId: pulumi.Input<string>;
    /**
     * [string] The desired Kubernetes Version. For supported values, please check the API documentation. Downgrades are not supported. The provider will ignore downgrades of patch level.
     */
    k8sVersion: pulumi.Input<string>;
    /**
     * [map] A key/value map of labels
     */
    labels?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * [list] A list of numeric LAN id's you want this node pool to be part of. For more details, please check the API documentation, as well as the example above
     */
    lans?: pulumi.Input<pulumi.Input<inputs.k8s.NodePoolLan>[]>;
    /**
     * See the **maintenance_window** section in the example above
     */
    maintenanceWindow?: pulumi.Input<inputs.k8s.NodePoolMaintenanceWindow>;
    /**
     * [string] The name of the Kubernetes Cluster. *This attribute is immutable*.
     */
    name?: pulumi.Input<string>;
    /**
     * [int] - The desired number of nodes in the node pool
     */
    nodeCount: pulumi.Input<number>;
    /**
     * [list] A list of public IPs associated with the node pool; must have at least `nodeCount + 1` elements
     */
    publicIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [int] - The desired amount of RAM, in MB. *This attribute is immutable*.
     */
    ramSize: pulumi.Input<number>;
    /**
     * [int] - The size of the volume in GB. The size should be greater than 10GB. *This attribute is immutable*.
     */
    storageSize: pulumi.Input<number>;
    /**
     * [string] - The desired storage type - SSD/HDD. *This attribute is immutable*.
     */
    storageType: pulumi.Input<string>;
}
