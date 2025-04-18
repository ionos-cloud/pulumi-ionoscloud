// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **PgSql User data source** can be used to search for and return an existing PgSql user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dbaas.getPSQLUser({
 *     clusterId: "cluster_id",
 *     username: "username",
 * });
 * ```
 */
export function getPSQLUser(args: GetPSQLUserArgs, opts?: pulumi.InvokeOptions): Promise<GetPSQLUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:dbaas/getPSQLUser:getPSQLUser", {
        "clusterId": args.clusterId,
        "username": args.username,
    }, opts);
}

/**
 * A collection of arguments for invoking getPSQLUser.
 */
export interface GetPSQLUserArgs {
    /**
     * [string] The ID of the cluster.
     */
    clusterId: string;
    /**
     * [string] Name of an existing user that you want to search for.
     */
    username: string;
}

/**
 * A collection of values returned by getPSQLUser.
 */
export interface GetPSQLUserResult {
    readonly clusterId: string;
    /**
     * [string] The id of the user.
     */
    readonly id: string;
    /**
     * [bool] Describes whether this user is a system user or not. A system user cannot be updated or deleted.
     */
    readonly isSystemUser: boolean;
    readonly username: string;
}
/**
 * The **PgSql User data source** can be used to search for and return an existing PgSql user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dbaas.getPSQLUser({
 *     clusterId: "cluster_id",
 *     username: "username",
 * });
 * ```
 */
export function getPSQLUserOutput(args: GetPSQLUserOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetPSQLUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:dbaas/getPSQLUser:getPSQLUser", {
        "clusterId": args.clusterId,
        "username": args.username,
    }, opts);
}

/**
 * A collection of arguments for invoking getPSQLUser.
 */
export interface GetPSQLUserOutputArgs {
    /**
     * [string] The ID of the cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * [string] Name of an existing user that you want to search for.
     */
    username: pulumi.Input<string>;
}
