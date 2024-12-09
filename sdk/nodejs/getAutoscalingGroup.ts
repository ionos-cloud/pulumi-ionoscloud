// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The autoscaling group data source can be used to search for and return an existing Autoscaling Group. You can provide a string for the name or id parameters which will be compared with provisioned Autoscaling Groups. If a single match is found, it will be returned.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const autoscalingGroup = ionoscloud.getAutoscalingGroup({
 *     name: "test_ds",
 * });
 * ```
 */
export function getAutoscalingGroup(args?: GetAutoscalingGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetAutoscalingGroupResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getAutoscalingGroup:getAutoscalingGroup", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getAutoscalingGroup.
 */
export interface GetAutoscalingGroupArgs {
    /**
     * Id of an existing Autoscaling Group that you want to search for.
     */
    id?: string;
    /**
     * Name of an existing Autoscaling Group that you want to search for.
     *
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     */
    name?: string;
}

/**
 * A collection of values returned by getAutoscalingGroup.
 */
export interface GetAutoscalingGroupResult {
    readonly datacenterId: string;
    /**
     * Unique identifier for the resource
     */
    readonly id?: string;
    /**
     * Location of the datacenter. This location is the same as the one from the selected template.
     */
    readonly location: string;
    /**
     * Maximum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     */
    readonly maxReplicaCount: number;
    /**
     * Minimum replica count value for `targetReplicaCount`. Will be enforced for both automatic and manual changes.
     */
    readonly minReplicaCount: number;
    /**
     * The name of the Autoscaling Group.
     */
    readonly name?: string;
    /**
     * Specifies the behavior of this Autoscaling Group. A policy consists of Triggers and Actions, whereby an Action is some kind of automated behavior, and a Trigger is defined by the circumstances under which the Action is triggered. Currently, two separate Actions, namely Scaling In and Out are supported, triggered through Thresholds defined on a given Metric.
     */
    readonly policies: outputs.GetAutoscalingGroupPolicy[];
    readonly replicaConfigurations: outputs.GetAutoscalingGroupReplicaConfiguration[];
    readonly targetReplicaCount: number;
}
/**
 * The autoscaling group data source can be used to search for and return an existing Autoscaling Group. You can provide a string for the name or id parameters which will be compared with provisioned Autoscaling Groups. If a single match is found, it will be returned.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const autoscalingGroup = ionoscloud.getAutoscalingGroup({
 *     name: "test_ds",
 * });
 * ```
 */
export function getAutoscalingGroupOutput(args?: GetAutoscalingGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAutoscalingGroupResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getAutoscalingGroup:getAutoscalingGroup", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getAutoscalingGroup.
 */
export interface GetAutoscalingGroupOutputArgs {
    /**
     * Id of an existing Autoscaling Group that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing Autoscaling Group that you want to search for.
     *
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     */
    name?: pulumi.Input<string>;
}
