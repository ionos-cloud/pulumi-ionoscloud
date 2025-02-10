// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getTargetGroup(args?: GetTargetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetTargetGroupResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getTargetGroup:getTargetGroup", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupArgs {
    id?: string;
    name?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getTargetGroup.
 */
export interface GetTargetGroupResult {
    readonly algorithm: string;
    readonly healthChecks: outputs.compute.GetTargetGroupHealthCheck[];
    readonly httpHealthChecks: outputs.compute.GetTargetGroupHttpHealthCheck[];
    readonly id: string;
    readonly name: string;
    readonly partialMatch?: boolean;
    readonly protocol: string;
    readonly protocolVersion: string;
    readonly targets: outputs.compute.GetTargetGroupTarget[];
}
export function getTargetGroupOutput(args?: GetTargetGroupOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetTargetGroupResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getTargetGroup:getTargetGroup", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getTargetGroup.
 */
export interface GetTargetGroupOutputArgs {
    id?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
