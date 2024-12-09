// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getK8sClusters(args?: GetK8sClustersArgs, opts?: pulumi.InvokeOptions): Promise<GetK8sClustersResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getK8sClusters:getK8sClusters", {
        "filters": args.filters,
    }, opts);
}

/**
 * A collection of arguments for invoking getK8sClusters.
 */
export interface GetK8sClustersArgs {
    filters?: inputs.GetK8sClustersFilter[];
}

/**
 * A collection of values returned by getK8sClusters.
 */
export interface GetK8sClustersResult {
    readonly clusters: outputs.GetK8sClustersCluster[];
    readonly entries: number;
    readonly filters?: outputs.GetK8sClustersFilter[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
export function getK8sClustersOutput(args?: GetK8sClustersOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetK8sClustersResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getK8sClusters:getK8sClusters", {
        "filters": args.filters,
    }, opts);
}

/**
 * A collection of arguments for invoking getK8sClusters.
 */
export interface GetK8sClustersOutputArgs {
    filters?: pulumi.Input<pulumi.Input<inputs.GetK8sClustersFilterArgs>[]>;
}
