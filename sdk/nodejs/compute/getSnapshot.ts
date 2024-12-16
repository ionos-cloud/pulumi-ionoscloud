// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export function getSnapshot(args?: GetSnapshotArgs, opts?: pulumi.InvokeOptions): Promise<GetSnapshotResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getSnapshot:getSnapshot", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "size": args.size,
    }, opts);
}

/**
 * A collection of arguments for invoking getSnapshot.
 */
export interface GetSnapshotArgs {
    id?: string;
    location?: string;
    name?: string;
    size?: number;
}

/**
 * A collection of values returned by getSnapshot.
 */
export interface GetSnapshotResult {
    readonly cpuHotPlug: boolean;
    readonly cpuHotUnplug: boolean;
    readonly description: string;
    readonly discScsiHotPlug: boolean;
    readonly discScsiHotUnplug: boolean;
    readonly discVirtioHotPlug: boolean;
    readonly discVirtioHotUnplug: boolean;
    readonly id?: string;
    readonly licenceType: string;
    readonly location: string;
    readonly name: string;
    readonly nicHotPlug: boolean;
    readonly nicHotUnplug: boolean;
    readonly ramHotPlug: boolean;
    readonly ramHotUnplug: boolean;
    readonly secAuthProtection: boolean;
    readonly size: number;
}
export function getSnapshotOutput(args?: GetSnapshotOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetSnapshotResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getSnapshot:getSnapshot", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "size": args.size,
    }, opts);
}

/**
 * A collection of arguments for invoking getSnapshot.
 */
export interface GetSnapshotOutputArgs {
    id?: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    size?: pulumi.Input<number>;
}
