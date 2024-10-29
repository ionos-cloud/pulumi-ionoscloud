// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **Target Group** data source can be used to search for and return an existing Application Load Balancer Target Group.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancer Target Groups.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Name
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTargetGroup({
 *     name: "Target Group Example",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ### By Name with Partial Match
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTargetGroup({
 *     name: "Example",
 *     partialMatch: true,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getTargetGroup(args?: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getTargetGroup:getTargetGroup", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupArgs {
    /**
     * ID of the target group you want to search for.
     */
    id?: string;
    /**
     * Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
     */
    name?: string;
    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getTargetGroup.
 */
export interface GetTargetGroupResult {
    /**
     * Balancing algorithm.
     */
    readonly algorithm: string;
    /**
     * Health check attributes for Target Group.
     */
    readonly healthChecks: outputs.GetTargetGroupHealthCheck[];
    /**
     * Http health check attributes for Target Group
     */
    readonly httpHealthChecks: outputs.GetTargetGroupHttpHealthCheck[];
    /**
     * The Id of that Target group
     */
    readonly id?: string;
    /**
     * The name of that Target Group.
     */
    readonly name?: string;
    readonly partialMatch?: boolean;
    /**
     * Balancing protocol.
     */
    readonly protocol: string;
    /**
     * The forwarding protocol version. Value is ignored when protocol is not 'HTTP'.
     */
    readonly protocolVersion: string;
    /**
     * Array of items in the collection
     */
    readonly targets: outputs.GetTargetGroupTarget[];
}
/**
 * The **Target Group** data source can be used to search for and return an existing Application Load Balancer Target Group.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancer Target Groups.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Name
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTargetGroup({
 *     name: "Target Group Example",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ### By Name with Partial Match
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getTargetGroup({
 *     name: "Example",
 *     partialMatch: true,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getTargetGroupOutput(args?: GetTargetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTargetGroupResult> {
    return pulumi.output(args).apply((a: any) => getTargetGroup(a, opts))
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupOutputArgs {
    /**
     * ID of the target group you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
     */
    name?: pulumi.Input<string>;
    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: pulumi.Input<boolean>;
}
