// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **Share data source** can be used to search for and return an existing share object.
 * You need to provide the groupId and resourceId to get the group resources for the shared resource.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getShare({
 *     groupId: "group_id",
 *     resourceId: "resource_id",
 * });
 * ```
 */
export function getShare(args: GetShareArgs, opts?: pulumi.InvokeOptions): Promise<GetShareResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getShare:getShare", {
        "groupId": args.groupId,
        "resourceId": args.resourceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getShare.
 */
export interface GetShareArgs {
    /**
     * The ID of the specific group containing the resource to update.
     */
    groupId: string;
    /**
     * The ID of the specific resource to update.
     *
     *
     * `resourceId` and `groupId` must be provided. If any of them are missing, the datasource will return an error.
     */
    resourceId: string;
}

/**
 * A collection of values returned by getShare.
 */
export interface GetShareResult {
    /**
     * The flag that specifies if the group has permission to edit privileges on this resource.
     */
    readonly editPrivilege: boolean;
    /**
     * The ID of the specific group containing the resource to update.
     */
    readonly groupId: string;
    /**
     * The id of the share resource.
     */
    readonly id: string;
    /**
     * The ID of the specific resource to update.
     */
    readonly resourceId: string;
    /**
     * The group has permission to share this resource.
     */
    readonly sharePrivilege: boolean;
}
/**
 * The **Share data source** can be used to search for and return an existing share object.
 * You need to provide the groupId and resourceId to get the group resources for the shared resource.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getShare({
 *     groupId: "group_id",
 *     resourceId: "resource_id",
 * });
 * ```
 */
export function getShareOutput(args: GetShareOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetShareResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getShare:getShare", {
        "groupId": args.groupId,
        "resourceId": args.resourceId,
    }, opts);
}

/**
 * A collection of arguments for invoking getShare.
 */
export interface GetShareOutputArgs {
    /**
     * The ID of the specific group containing the resource to update.
     */
    groupId: pulumi.Input<string>;
    /**
     * The ID of the specific resource to update.
     *
     *
     * `resourceId` and `groupId` must be provided. If any of them are missing, the datasource will return an error.
     */
    resourceId: pulumi.Input<string>;
}
