// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getRegistry(args?: GetRegistryArgs, opts?: pulumi.InvokeOptions): Promise<GetRegistryResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:creg/getRegistry:getRegistry", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegistry.
 */
export interface GetRegistryArgs {
    id?: string;
    location?: string;
    name?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getRegistry.
 */
export interface GetRegistryResult {
    readonly apiSubnetAllowLists: string[];
    readonly features: outputs.creg.GetRegistryFeature[];
    readonly garbageCollectionSchedules: outputs.creg.GetRegistryGarbageCollectionSchedule[];
    readonly hostname: string;
    readonly id: string;
    readonly location?: string;
    readonly maintenanceWindows: outputs.creg.GetRegistryMaintenanceWindow[];
    readonly name: string;
    readonly partialMatch?: boolean;
    readonly storageUsages: outputs.creg.GetRegistryStorageUsage[];
}
export function getRegistryOutput(args?: GetRegistryOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetRegistryResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:creg/getRegistry:getRegistry", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getRegistry.
 */
export interface GetRegistryOutputArgs {
    id?: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
