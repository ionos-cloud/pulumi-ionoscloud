// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **Bucket data source** can be used to search for and return existing buckets.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.objectstorage.getBucket({
 *     name: "example",
 * });
 * ```
 */
export function getBucket(args: GetBucketArgs, opts?: pulumi.InvokeOptions): Promise<GetBucketResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:objectstorage/getBucket:getBucket", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getBucket.
 */
export interface GetBucketArgs {
    /**
     * [string] The bucket name. [ 3 .. 63 ] characters
     */
    name: string;
}

/**
 * A collection of values returned by getBucket.
 */
export interface GetBucketResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly name: string;
    /**
     * The region where the bucket is located.
     */
    readonly region: string;
}
/**
 * The **Bucket data source** can be used to search for and return existing buckets.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.objectstorage.getBucket({
 *     name: "example",
 * });
 * ```
 */
export function getBucketOutput(args: GetBucketOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetBucketResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:objectstorage/getBucket:getBucket", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getBucket.
 */
export interface GetBucketOutputArgs {
    /**
     * [string] The bucket name. [ 3 .. 63 ] characters
     */
    name: pulumi.Input<string>;
}
