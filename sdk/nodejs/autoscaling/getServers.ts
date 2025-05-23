// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The autoscaling group servers data source can be used to search for and return existing servers that are part of a specific autoscaling group.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const autoscalingGroupServers = ionoscloud.autoscaling.getServers({
 *     groupId: "autoscaling_group_uuid",
 * });
 * ```
 */
export function getServers(args: GetServersArgs, opts?: pulumi.InvokeOptions): Promise<GetServersResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:autoscaling/getServers:getServers", {
        "groupId": args.groupId,
    }, opts);
}

/**
 * A collection of arguments for invoking getServers.
 */
export interface GetServersArgs {
    /**
     * The unique ID of the autoscaling group.
     *
     * `groupId` must be provided. If it is not provided, the datasource will return an error.
     */
    groupId: string;
}

/**
 * A collection of values returned by getServers.
 */
export interface GetServersResult {
    /**
     * Id of the autoscaling group.
     */
    readonly groupId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * List of servers.
     */
    readonly servers: outputs.autoscaling.GetServersServer[];
}
/**
 * The autoscaling group servers data source can be used to search for and return existing servers that are part of a specific autoscaling group.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const autoscalingGroupServers = ionoscloud.autoscaling.getServers({
 *     groupId: "autoscaling_group_uuid",
 * });
 * ```
 */
export function getServersOutput(args: GetServersOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetServersResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:autoscaling/getServers:getServers", {
        "groupId": args.groupId,
    }, opts);
}

/**
 * A collection of arguments for invoking getServers.
 */
export interface GetServersOutputArgs {
    /**
     * The unique ID of the autoscaling group.
     *
     * `groupId` must be provided. If it is not provided, the datasource will return an error.
     */
    groupId: pulumi.Input<string>;
}
