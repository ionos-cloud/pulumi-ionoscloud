// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Create clusters of Network File Storage (NFS) on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * // Basic example
 * const nfsDc = new ionoscloud.compute.Datacenter("nfs_dc", {
 *     name: "NFS Datacenter",
 *     location: "de/txl",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const nfsLan = new ionoscloud.compute.Lan("nfs_lan", {
 *     datacenterId: nfsDc.id,
 *     "public": false,
 *     name: "Lan for NFS",
 * });
 * const example = new ionoscloud.nfs.Cluster("example", {
 *     name: "test",
 *     location: "de/txl",
 *     size: 2,
 *     nfs: {
 *         minVersion: "4.2",
 *     },
 *     connections: {
 *         datacenterId: nfsDc.id,
 *         ipAddress: "192.168.100.10/24",
 *         lan: nfsLan.id,
 *     },
 * });
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * // Complete example
 * const nfsDc = new ionoscloud.compute.Datacenter("nfs_dc", {
 *     name: "NFS Datacenter",
 *     location: "de/txl",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const nfsLan = new ionoscloud.compute.Lan("nfs_lan", {
 *     datacenterId: nfsDc.id,
 *     "public": false,
 *     name: "Lan for NFS",
 * });
 * const hDDImage = ionoscloud.compute.getImage({
 *     imageAlias: "ubuntu:20.04",
 *     type: "HDD",
 *     cloudInit: "V1",
 *     location: "de/txl",
 * });
 * const password = new random.index.Password("password", {
 *     length: 16,
 *     special: false,
 * });
 * // needed for the NIC - which provides the IP address for the NFS cluster.
 * const nfsServer = new ionoscloud.compute.Server("nfs_server", {
 *     name: "Server for NFS",
 *     datacenterId: nfsDc.id,
 *     cores: 1,
 *     ram: 2048,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_SKYLAKE",
 *     imageName: hDDImage.then(hDDImage => hDDImage.id),
 *     imagePassword: password.result,
 *     volume: {
 *         name: "system",
 *         size: 14,
 *         diskType: "SSD",
 *     },
 *     nic: {
 *         name: "NIC A",
 *         lan: nfsLan.id,
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const example = new ionoscloud.nfs.Cluster("example", {
 *     name: "test",
 *     location: "de/txl",
 *     size: 2,
 *     nfs: {
 *         minVersion: "4.2",
 *     },
 *     connections: {
 *         datacenterId: nfsDc.id,
 *         ipAddress: "nfs_cluster_cidr_from_nic",
 *         lan: nfsLan.id,
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * A Network File Storage Cluster resource can be imported using its `location` and `resource id`:
 *
 * ```sh
 * $ pulumi import ionoscloud:nfs/cluster:Cluster name location:uuid
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
    public static readonly __pulumiType = 'ionoscloud:nfs/cluster:Cluster';

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
     * The network connections for the Network File Storage Cluster.
     */
    public readonly connections!: pulumi.Output<outputs.nfs.ClusterConnections>;
    /**
     * The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * - `de/fra` - Frankfurt
     * - `de/txl` - Berlin
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * The name of the Network File Storage cluster.
     */
    public readonly name!: pulumi.Output<string>;
    public readonly nfs!: pulumi.Output<outputs.nfs.ClusterNfs | undefined>;
    /**
     * The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
     */
    public readonly size!: pulumi.Output<number>;

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
            resourceInputs["connections"] = state ? state.connections : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nfs"] = state ? state.nfs : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
        } else {
            const args = argsOrState as ClusterArgs | undefined;
            if ((!args || args.connections === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connections'");
            }
            if ((!args || args.size === undefined) && !opts.urn) {
                throw new Error("Missing required property 'size'");
            }
            resourceInputs["connections"] = args ? args.connections : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nfs"] = args ? args.nfs : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
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
     * The network connections for the Network File Storage Cluster.
     */
    connections?: pulumi.Input<inputs.nfs.ClusterConnections>;
    /**
     * The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * - `de/fra` - Frankfurt
     * - `de/txl` - Berlin
     */
    location?: pulumi.Input<string>;
    /**
     * The name of the Network File Storage cluster.
     */
    name?: pulumi.Input<string>;
    nfs?: pulumi.Input<inputs.nfs.ClusterNfs>;
    /**
     * The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
     */
    size?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Cluster resource.
 */
export interface ClusterArgs {
    /**
     * The network connections for the Network File Storage Cluster.
     */
    connections: pulumi.Input<inputs.nfs.ClusterConnections>;
    /**
     * The location where the Network File Storage cluster is located. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * - `de/fra` - Frankfurt
     * - `de/txl` - Berlin
     */
    location?: pulumi.Input<string>;
    /**
     * The name of the Network File Storage cluster.
     */
    name?: pulumi.Input<string>;
    nfs?: pulumi.Input<inputs.nfs.ClusterNfs>;
    /**
     * The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
     */
    size: pulumi.Input<number>;
}
