// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getMongoUser(args: GetMongoUserArgs, opts?: pulumi.InvokeOptions): Promise<GetMongoUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:dbaas/getMongoUser:getMongoUser", {
        "clusterId": args.clusterId,
        "database": args.database,
        "id": args.id,
        "roles": args.roles,
        "username": args.username,
    }, opts);
}

/**
 * A collection of arguments for invoking getMongoUser.
 */
export interface GetMongoUserArgs {
    /**
     * [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
     */
    clusterId: string;
    /**
     * [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
     */
    database?: string;
    id?: string;
    /**
     * [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
     */
    roles?: inputs.dbaas.GetMongoUserRole[];
    /**
     * [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
     */
    username: string;
}

/**
 * A collection of values returned by getMongoUser.
 */
export interface GetMongoUserResult {
    readonly clusterId: string;
    readonly database: string;
    readonly id: string;
    readonly roles: outputs.dbaas.GetMongoUserRole[];
    readonly username: string;
}
/**
 * The **DbaaS Mongo User data source** can be used to search for and return an existing DbaaS MongoDB User.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getMongoUserOutput(args: GetMongoUserOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetMongoUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:dbaas/getMongoUser:getMongoUser", {
        "clusterId": args.clusterId,
        "database": args.database,
        "id": args.id,
        "roles": args.roles,
        "username": args.username,
    }, opts);
}

/**
 * A collection of arguments for invoking getMongoUser.
 */
export interface GetMongoUserOutputArgs {
    /**
     * [string] The unique ID of the cluster. Updates to the value of the field force the cluster to be re-created.
     */
    clusterId: pulumi.Input<string>;
    /**
     * [string] The user database to use for authentication. Updates to the value of the field force the cluster to be re-created.
     */
    database?: pulumi.Input<string>;
    id?: pulumi.Input<string>;
    /**
     * [string] a list of mongodb user roles. Updates to the value of the field force the cluster to be re-created.
     */
    roles?: pulumi.Input<pulumi.Input<inputs.dbaas.GetMongoUserRoleArgs>[]>;
    /**
     * [string] Used for authentication. Updates to the value of the field force the cluster to be re-created.
     */
    username: pulumi.Input<string>;
}
