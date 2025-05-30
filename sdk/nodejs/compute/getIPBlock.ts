// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **IP Block data source** can be used to search for and return an existing Ip Block.
 * You can provide a string for the id, the name or the location parameters which will be compared with the provisioned Ip Blocks.
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
 * const example = ionoscloud.compute.getIPBlock({
 *     id: "ipblock_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPBlock({
 *     name: "IP Block Name",
 * });
 * ```
 *
 * ### By Location
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPBlock({
 *     location: "us/las",
 * });
 * ```
 *
 * ### By Name & Location
 */
export function getIPBlock(args?: GetIPBlockArgs, opts?: pulumi.InvokeOptions): Promise<GetIPBlockResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getIPBlock:getIPBlock", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "size": args.size,
    }, opts);
}

/**
 * A collection of arguments for invoking getIPBlock.
 */
export interface GetIPBlockArgs {
    /**
     * ID of an existing Ip Block that you want to search for.
     */
    id?: string;
    /**
     * The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     */
    location?: string;
    /**
     * Name of an existing Ip Block that you want to search for.
     */
    name?: string;
    /**
     * The number of IP addresses to reserve for this block.
     */
    size?: number;
}

/**
 * A collection of values returned by getIPBlock.
 */
export interface GetIPBlockResult {
    /**
     * The id of Ip Block
     */
    readonly id: string;
    /**
     * Read-Only attribute. Lists consumption detail of an individual ip
     */
    readonly ipConsumers: outputs.compute.GetIPBlockIpConsumer[];
    /**
     * The list of IP addresses associated with this block.
     */
    readonly ips: string[];
    /**
     * The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     */
    readonly location: string;
    /**
     * The name of Ip Block
     */
    readonly name: string;
    /**
     * The number of IP addresses to reserve for this block.
     */
    readonly size: number;
}
/**
 * The **IP Block data source** can be used to search for and return an existing Ip Block.
 * You can provide a string for the id, the name or the location parameters which will be compared with the provisioned Ip Blocks.
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
 * const example = ionoscloud.compute.getIPBlock({
 *     id: "ipblock_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPBlock({
 *     name: "IP Block Name",
 * });
 * ```
 *
 * ### By Location
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPBlock({
 *     location: "us/las",
 * });
 * ```
 *
 * ### By Name & Location
 */
export function getIPBlockOutput(args?: GetIPBlockOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetIPBlockResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getIPBlock:getIPBlock", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "size": args.size,
    }, opts);
}

/**
 * A collection of arguments for invoking getIPBlock.
 */
export interface GetIPBlockOutputArgs {
    /**
     * ID of an existing Ip Block that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * The regional location for this IP Block: us/las, us/ewr, de/fra, de/fkb.
     */
    location?: pulumi.Input<string>;
    /**
     * Name of an existing Ip Block that you want to search for.
     */
    name?: pulumi.Input<string>;
    /**
     * The number of IP addresses to reserve for this block.
     */
    size?: pulumi.Input<number>;
}
