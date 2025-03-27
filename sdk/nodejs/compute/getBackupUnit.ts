// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **Backup Unit data source** can be used to search for and return an existing Backup Unit.
 * You can provide a string for either id or name parameters which will be compared with provisioned Backup Units.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getBackupUnit({
 *     id: "backup_unit_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getBackupUnit({
 *     name: "Backup Unit Example",
 * });
 * ```
 */
export function getBackupUnit(args?: GetBackupUnitArgs, opts?: pulumi.InvokeOptions): Promise<GetBackupUnitResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getBackupUnit:getBackupUnit", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getBackupUnit.
 */
export interface GetBackupUnitArgs {
    /**
     * ID of the backup unit you want to search for.
     *
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     */
    id?: string;
    /**
     * Name of an existing backup unit that you want to search for.
     */
    name?: string;
}

/**
 * A collection of values returned by getBackupUnit.
 */
export interface GetBackupUnitResult {
    /**
     * The e-mail address you want assigned to the backup unit.
     */
    readonly email: string;
    /**
     * The id of the Backup Unit.
     */
    readonly id: string;
    /**
     * The login associated with the backup unit. Derived from the contract number.
     */
    readonly login: string;
    /**
     * The name of the Backup Unit.
     */
    readonly name: string;
}
/**
 * The **Backup Unit data source** can be used to search for and return an existing Backup Unit.
 * You can provide a string for either id or name parameters which will be compared with provisioned Backup Units.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 *
 * ### By ID
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getBackupUnit({
 *     id: "backup_unit_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getBackupUnit({
 *     name: "Backup Unit Example",
 * });
 * ```
 */
export function getBackupUnitOutput(args?: GetBackupUnitOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetBackupUnitResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getBackupUnit:getBackupUnit", {
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getBackupUnit.
 */
export interface GetBackupUnitOutputArgs {
    /**
     * ID of the backup unit you want to search for.
     *
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing backup unit that you want to search for.
     */
    name?: pulumi.Input<string>;
}
