// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getDistribution(args?: GetDistributionArgs, opts?: pulumi.InvokeOptions): Promise<GetDistributionResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:cdn/getDistribution:getDistribution", {
        "domain": args.domain,
        "id": args.id,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getDistribution.
 */
export interface GetDistributionArgs {
    domain?: string;
    id?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getDistribution.
 */
export interface GetDistributionResult {
    readonly certificateId: string;
    readonly domain?: string;
    readonly id: string;
    readonly partialMatch?: boolean;
    readonly publicEndpointV4: string;
    readonly publicEndpointV6: string;
    readonly resourceUrn: string;
    readonly routingRules: outputs.cdn.GetDistributionRoutingRule[];
}
export function getDistributionOutput(args?: GetDistributionOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetDistributionResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:cdn/getDistribution:getDistribution", {
        "domain": args.domain,
        "id": args.id,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getDistribution.
 */
export interface GetDistributionOutputArgs {
    domain?: pulumi.Input<string>;
    id?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
