// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **Object storage region data source** can be used to search for and return an existing S3 Regions.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.objectstorage.getRegion({
 *     id: "region_id",
 * });
 * ```
 */
export function getRegion(args: GetRegionArgs, opts?: pulumi.InvokeOptions): Promise<GetRegionResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:objectstorage/getRegion:getRegion", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegion.
 */
export interface GetRegionArgs {
    /**
     * Id of an existing object storage Region that you want to search for.
     */
    id: string;
}

/**
 * A collection of values returned by getRegion.
 */
export interface GetRegionResult {
    /**
     * The capabilities of the region
     */
    readonly capability: outputs.objectstorage.GetRegionCapability;
    /**
     * The endpoint URL for the region
     */
    readonly endpoint: string;
    /**
     * The id of the region
     */
    readonly id: string;
    /**
     * The data center location of the region as per [Get Location](https://www.terraform.io/docs/cloud/v6/#tag/Locations/operation/locationsGet). *Can't be used as `LocationConstraint` on bucket creation.*
     */
    readonly location: string;
    /**
     * The available classes in the region
     */
    readonly storageClasses: string[];
    /**
     * The version of the region properties
     */
    readonly version: number;
    /**
     * The website URL for the region
     */
    readonly website: string;
}
/**
 * The **Object storage region data source** can be used to search for and return an existing S3 Regions.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.objectstorage.getRegion({
 *     id: "region_id",
 * });
 * ```
 */
export function getRegionOutput(args: GetRegionOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetRegionResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:objectstorage/getRegion:getRegion", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegion.
 */
export interface GetRegionOutputArgs {
    /**
     * Id of an existing object storage Region that you want to search for.
     */
    id: pulumi.Input<string>;
}
