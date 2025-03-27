// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **NSG Data source** can be used to search for and return an existing security group.
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
 * const example = ionoscloud.nsg.getNsg({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     id: nsgId,
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nsg.getNsg({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "NSG Example",
 * });
 * ```
 */
export function getNsg(args: GetNsgArgs, opts?: pulumi.InvokeOptions): Promise<GetNsgResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:nsg/getNsg:getNsg", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getNsg.
 */
export interface GetNsgArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: string;
    /**
     * Id of an existing Network Security Group that you want to search for.
     */
    id?: string;
    /**
     * Name of an existing Network Security Group that you want to search for.
     *
     * Either `name`, or `id` must be provided. If none, the datasource will return an error.
     */
    name?: string;
}

/**
 * A collection of values returned by getNsg.
 */
export interface GetNsgResult {
    /**
     * UUID of the Virtual Data Center
     */
    readonly datacenterId: string;
    /**
     * Description for the Network Security Group
     */
    readonly description: string;
    /**
     * UUID of the Network Security Group
     */
    readonly id: string;
    /**
     * The name of the Network Security Group
     */
    readonly name: string;
    /**
     * List of IDs for the Firewall Rules attached to this group
     */
    readonly ruleIds: string[];
    /**
     * List of Firewall Rule objects attached to this group
     */
    readonly rules: outputs.nsg.GetNsgRule[];
}
/**
 * The **NSG Data source** can be used to search for and return an existing security group.
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
 * const example = ionoscloud.nsg.getNsg({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     id: nsgId,
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.nsg.getNsg({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "NSG Example",
 * });
 * ```
 */
export function getNsgOutput(args: GetNsgOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetNsgResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:nsg/getNsg:getNsg", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getNsg.
 */
export interface GetNsgOutputArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * Id of an existing Network Security Group that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing Network Security Group that you want to search for.
     *
     * Either `name`, or `id` must be provided. If none, the datasource will return an error.
     */
    name?: pulumi.Input<string>;
}
