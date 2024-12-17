// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Creates and manages Network File Storage (NFS) Share objects on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * // Basic example
 * const nfsDc = new ionoscloud.compute.Datacenter("nfsDc", {
 *     location: "de/txl",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const nfsLan = new ionoscloud.compute.Lan("nfsLan", {
 *     datacenterId: nfsDc.id,
 *     "public": false,
 * });
 * const exampleCluster = new ionoscloud.nfs.Cluster("exampleCluster", {
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
 * const exampleShare = new ionoscloud.nfs.Share("exampleShare", {
 *     location: "de/txl",
 *     clusterId: exampleCluster.id,
 *     quota: 512,
 *     gid: 512,
 *     uid: 512,
 *     clientGroups: [{
 *         description: "Client Group 1",
 *         ipNetworks: ["10.234.50.0/24"],
 *         hosts: ["10.234.62.123"],
 *         nfs: {
 *             squash: "all-anonymous",
 *         },
 *     }],
 * });
 * ```
 *
 * ## Import
 *
 * A Network File Storage Share resource can be imported using its `location`, `cluster_id` and `resource id`:
 *
 * ```sh
 * $ pulumi import ionoscloud:nfs/share:Share name location:cluster_id:resource_id
 * ```
 */
export class Share extends pulumi.CustomResource {
    /**
     * Get an existing Share resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState, opts?: pulumi.CustomResourceOptions): Share {
        return new Share(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:nfs/share:Share';

    /**
     * Returns true if the given object is an instance of Share.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Share {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Share.__pulumiType;
    }

    /**
     * The groups of clients are the systems connecting to the Network File Storage cluster. Each group includes:
     */
    public readonly clientGroups!: pulumi.Output<outputs.nfs.ShareClientGroup[]>;
    /**
     * The ID of the Network File Storage Cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    public readonly gid!: pulumi.Output<number | undefined>;
    /**
     * The location of the Network File Storage Cluster.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * The directory being exported.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Path to the NFS export. The NFS path is the path to the directory being exported.
     */
    public /*out*/ readonly nfsPath!: pulumi.Output<string>;
    /**
     * The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`. Default is `0`.
     */
    public readonly quota!: pulumi.Output<number | undefined>;
    /**
     * The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    public readonly uid!: pulumi.Output<number | undefined>;

    /**
     * Create a Share resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareArgs | ShareState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ShareState | undefined;
            resourceInputs["clientGroups"] = state ? state.clientGroups : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["gid"] = state ? state.gid : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nfsPath"] = state ? state.nfsPath : undefined;
            resourceInputs["quota"] = state ? state.quota : undefined;
            resourceInputs["uid"] = state ? state.uid : undefined;
        } else {
            const args = argsOrState as ShareArgs | undefined;
            if ((!args || args.clientGroups === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clientGroups'");
            }
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            resourceInputs["clientGroups"] = args ? args.clientGroups : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["gid"] = args ? args.gid : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["quota"] = args ? args.quota : undefined;
            resourceInputs["uid"] = args ? args.uid : undefined;
            resourceInputs["nfsPath"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Share.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Share resources.
 */
export interface ShareState {
    /**
     * The groups of clients are the systems connecting to the Network File Storage cluster. Each group includes:
     */
    clientGroups?: pulumi.Input<pulumi.Input<inputs.nfs.ShareClientGroup>[]>;
    /**
     * The ID of the Network File Storage Cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    gid?: pulumi.Input<number>;
    /**
     * The location of the Network File Storage Cluster.
     */
    location?: pulumi.Input<string>;
    /**
     * The directory being exported.
     */
    name?: pulumi.Input<string>;
    /**
     * Path to the NFS export. The NFS path is the path to the directory being exported.
     */
    nfsPath?: pulumi.Input<string>;
    /**
     * The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`. Default is `0`.
     */
    quota?: pulumi.Input<number>;
    /**
     * The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    uid?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Share resource.
 */
export interface ShareArgs {
    /**
     * The groups of clients are the systems connecting to the Network File Storage cluster. Each group includes:
     */
    clientGroups: pulumi.Input<pulumi.Input<inputs.nfs.ShareClientGroup>[]>;
    /**
     * The ID of the Network File Storage Cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    gid?: pulumi.Input<number>;
    /**
     * The location of the Network File Storage Cluster.
     */
    location: pulumi.Input<string>;
    /**
     * The directory being exported.
     */
    name?: pulumi.Input<string>;
    /**
     * The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`. Default is `0`.
     */
    quota?: pulumi.Input<number>;
    /**
     * The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     */
    uid?: pulumi.Input<number>;
}
