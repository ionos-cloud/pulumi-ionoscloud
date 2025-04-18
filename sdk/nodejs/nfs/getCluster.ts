// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
 *
 * ## By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nfs.getCluster({
 *     location: "location",
 *     id: "cluster-id",
 * });
 * ```
 *
 * ## By Name
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nfs.getCluster({
 *     location: "location",
 *     name: "partial-name",
 *     partialMatch: true,
 * });
 * ```
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:nfs/getCluster:getCluster", {
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
     * ID of the Network File Storage cluster.
     */
    id?: string;
    /**
     * The location where the Network File Storage cluster is located.
     */
    location: string;
    /**
     * Name of the Network File Storage cluster.
     */
    name?: string;
    /**
     * Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     */
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getCluster.
 */
export interface GetClusterResult {
    /**
     * A list of connections for the Network File Storage cluster. You can specify only one connection. Each connection supports the following:
     */
    readonly connections: outputs.nfs.GetClusterConnection[];
    /**
     * The ID of the Network File Storage cluster.
     */
    readonly id: string;
    /**
     * The location where the Network File Storage cluster is located.
     */
    readonly location: string;
    /**
     * The name of the Network File Storage cluster.
     */
    readonly name: string;
    /**
     * The NFS configuration for the Network File Storage cluster. Each NFS configuration supports the following:
     */
    readonly nfs: outputs.nfs.GetClusterNf[];
    readonly partialMatch?: boolean;
    /**
     * The size of the Network File Storage cluster in TiB. Note that the cluster size cannot be reduced after provisioning. This value determines the billing fees. Default is `2`. The minimum value is `2` and the maximum value is `42`.
     */
    readonly size: number;
}
/**
 * Returns information about clusters of Network File Storage (NFS) on IonosCloud.
 *
 * ## By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nfs.getCluster({
 *     location: "location",
 *     id: "cluster-id",
 * });
 * ```
 *
 * ## By Name
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nfs.getCluster({
 *     location: "location",
 *     name: "partial-name",
 *     partialMatch: true,
 * });
 * ```
 */
export function getClusterOutput(args: GetClusterOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetClusterResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:nfs/getCluster:getCluster", {
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
     * ID of the Network File Storage cluster.
     */
    id?: pulumi.Input<string>;
    /**
     * The location where the Network File Storage cluster is located.
     */
    location: pulumi.Input<string>;
    /**
     * Name of the Network File Storage cluster.
     */
    name?: pulumi.Input<string>;
    /**
     * Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     */
    partialMatch?: pulumi.Input<boolean>;
}
