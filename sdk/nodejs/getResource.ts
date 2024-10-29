// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The **Resource data source** can be used to search for and return any existing IonosCloud resource and optionally their group associations.
 * You can provide a string for the resource type (datacenter,image,snapshot,ipblock) and/or resource id parameters which will be queries against available resources.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Type
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getResource({
 *     resourceType: "datacenter",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getResource(args?: GetResourceArgs, opts?: pulumi.InvokeOptions): Promise<GetResourceResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getResource:getResource", {
        "resourceId": args.resourceId,
        "resourceType": args.resourceType,
    }, opts);
}

/**
 * A collection of arguments for invoking getResource.
 */
export interface GetResourceArgs {
    /**
     * The ID of the specific resource to retrieve information about.
     */
    resourceId?: string;
    /**
     * The specific type of resources to retrieve information about.
     */
    resourceType?: string;
}

/**
 * A collection of values returned by getResource.
 */
export interface GetResourceResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly resourceId?: string;
    readonly resourceType?: string;
}
/**
 * The **Resource data source** can be used to search for and return any existing IonosCloud resource and optionally their group associations.
 * You can provide a string for the resource type (datacenter,image,snapshot,ipblock) and/or resource id parameters which will be queries against available resources.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By Type
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getResource({
 *     resourceType: "datacenter",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getResourceOutput(args?: GetResourceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetResourceResult> {
    return pulumi.output(args).apply((a: any) => getResource(a, opts))
}

/**
 * A collection of arguments for invoking getResource.
 */
export interface GetResourceOutputArgs {
    /**
     * The ID of the specific resource to retrieve information about.
     */
    resourceId?: pulumi.Input<string>;
    /**
     * The specific type of resources to retrieve information about.
     */
    resourceType?: pulumi.Input<string>;
}
