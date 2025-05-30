// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **Cross Connect data source** can be used to search for and return existing cross connects.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getCrossconnect({
 *     id: "private_crossconnect_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getCrossconnect({
 *     name: "Cross Connect Example",
 * });
 * ```
 */
export function getCrossconnect(args?: GetCrossconnectArgs, opts?: pulumi.InvokeOptions): Promise<GetCrossconnectResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getCrossconnect:getCrossconnect", {
        "description": args.description,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getCrossconnect.
 */
export interface GetCrossconnectArgs {
    /**
     * Description of cross connect
     */
    description?: string;
    /**
     * ID of the cross connect you want to search for.
     *
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     */
    id?: string;
    /**
     * Name of an existing cross connect that you want to search for.
     */
    name?: string;
}

/**
 * A collection of values returned by getCrossconnect.
 */
export interface GetCrossconnectResult {
    /**
     * Lists datacenters that can be joined to this cross connect
     */
    readonly connectableDatacenters: outputs.compute.GetCrossconnectConnectableDatacenter[];
    /**
     * Description of cross connect
     */
    readonly description: string;
    /**
     * The UUID of the connectable datacenter
     */
    readonly id: string;
    /**
     * The name of the connectable datacenter
     */
    readonly name: string;
    /**
     * Lists LAN's joined to this cross connect
     */
    readonly peers: outputs.compute.GetCrossconnectPeer[];
}
/**
 * The **Cross Connect data source** can be used to search for and return existing cross connects.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getCrossconnect({
 *     id: "private_crossconnect_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getCrossconnect({
 *     name: "Cross Connect Example",
 * });
 * ```
 */
export function getCrossconnectOutput(args?: GetCrossconnectOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetCrossconnectResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getCrossconnect:getCrossconnect", {
        "description": args.description,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getCrossconnect.
 */
export interface GetCrossconnectOutputArgs {
    /**
     * Description of cross connect
     */
    description?: pulumi.Input<string>;
    /**
     * ID of the cross connect you want to search for.
     *
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing cross connect that you want to search for.
     */
    name?: pulumi.Input<string>;
}
