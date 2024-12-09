// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **Datacenter data source** can be used to search for and return an existing Virtual Data Center.
 * You can provide a string for the name and location parameters which will be compared with provisioned Virtual Data Centers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Name & Location
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getDatacenter({
 *     location: "us/las",
 *     name: "Datacenter Example",
 * });
 * ```
 */
export function getDatacenter(args?: GetDatacenterArgs, opts?: pulumi.InvokeOptions): Promise<GetDatacenterResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getDatacenter:getDatacenter", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatacenter.
 */
export interface GetDatacenterArgs {
    /**
     * Id of an existing Virtual Data Center that you want to search for.
     */
    id?: string;
    /**
     * Id of the existing Virtual Data Center's location.
     *
     * Either `name`, `location` or `id` must be provided. If none, the datasource will return an error.
     */
    location?: string;
    /**
     * Name of an existing Virtual Data Center that you want to search for.
     */
    name?: string;
}

/**
 * A collection of values returned by getDatacenter.
 */
export interface GetDatacenterResult {
    /**
     * Array of features and CPU families available in a location
     */
    readonly cpuArchitectures: outputs.GetDatacenterCpuArchitecture[];
    /**
     * Description for the Virtual Data Center
     */
    readonly description: string;
    /**
     * List of features supported by the location this data center is part of
     */
    readonly features: string[];
    /**
     * UUID of the Virtual Data Center
     */
    readonly id?: string;
    readonly ipv6CidrBlock: string;
    /**
     * The regional location where the Virtual Data Center will be created
     */
    readonly location?: string;
    /**
     * The name of the Virtual Data Center
     */
    readonly name?: string;
    /**
     * Boolean value representing if the data center requires extra protection e.g. two factor protection
     */
    readonly secAuthProtection: boolean;
    /**
     * The version of that Data Center. Gets incremented with every change
     */
    readonly version: number;
}
/**
 * The **Datacenter data source** can be used to search for and return an existing Virtual Data Center.
 * You can provide a string for the name and location parameters which will be compared with provisioned Virtual Data Centers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Name & Location
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getDatacenter({
 *     location: "us/las",
 *     name: "Datacenter Example",
 * });
 * ```
 */
export function getDatacenterOutput(args?: GetDatacenterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDatacenterResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getDatacenter:getDatacenter", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getDatacenter.
 */
export interface GetDatacenterOutputArgs {
    /**
     * Id of an existing Virtual Data Center that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Id of the existing Virtual Data Center's location.
     *
     * Either `name`, `location` or `id` must be provided. If none, the datasource will return an error.
     */
    location?: pulumi.Input<string>;
    /**
     * Name of an existing Virtual Data Center that you want to search for.
     */
    name?: pulumi.Input<string>;
}
