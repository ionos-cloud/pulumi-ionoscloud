// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getInmemorydbSnapshot(args: GetInmemorydbSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetInmemorydbSnapshotResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getInmemorydbSnapshot:getInmemorydbSnapshot", {
        "id": args.id,
        "location": args.location,
    }, opts);
}

/**
 * A collection of arguments for invoking getInmemorydbSnapshot.
 */
export interface GetInmemorydbSnapshotArgs {
    id: string;
    location: string;
}

/**
 * A collection of values returned by getInmemorydbSnapshot.
 */
export interface GetInmemorydbSnapshotResult {
    readonly id: string;
    readonly location: string;
    readonly metadatas: outputs.GetInmemorydbSnapshotMetadata[];
}
export function getInmemorydbSnapshotOutput(args: GetInmemorydbSnapshotOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetInmemorydbSnapshotResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getInmemorydbSnapshot:getInmemorydbSnapshot", {
        "id": args.id,
        "location": args.location,
    }, opts);
}

/**
 * A collection of arguments for invoking getInmemorydbSnapshot.
 */
export interface GetInmemorydbSnapshotOutputArgs {
    id: pulumi.Input<string>;
    location: pulumi.Input<string>;
}
