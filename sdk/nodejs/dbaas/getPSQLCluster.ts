// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getPSQLCluster(args?: GetPSQLClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetPSQLClusterResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", {
        "displayName": args.displayName,
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getPSQLCluster.
 */
export interface GetPSQLClusterArgs {
    displayName?: string;
    id?: string;
}

/**
 * A collection of values returned by getPSQLCluster.
 */
export interface GetPSQLClusterResult {
    readonly backupLocation: string;
    readonly connectionPoolers: outputs.dbaas.GetPSQLClusterConnectionPooler[];
    readonly connections: outputs.dbaas.GetPSQLClusterConnection[];
    readonly cores: number;
    readonly displayName?: string;
    readonly dnsName: string;
    readonly fromBackups: outputs.dbaas.GetPSQLClusterFromBackup[];
    readonly id?: string;
    readonly instances: number;
    readonly location: string;
    readonly maintenanceWindows: outputs.dbaas.GetPSQLClusterMaintenanceWindow[];
    readonly postgresVersion: string;
    readonly ram: number;
    readonly storageSize: number;
    readonly storageType: string;
    readonly synchronizationMode: string;
}
export function getPSQLClusterOutput(args?: GetPSQLClusterOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetPSQLClusterResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:dbaas/getPSQLCluster:getPSQLCluster", {
        "displayName": args.displayName,
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getPSQLCluster.
 */
export interface GetPSQLClusterOutputArgs {
    displayName?: pulumi.Input<string>;
    id?: pulumi.Input<string>;
}
