// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **DNS Zone** can be used to search for and return an existing DNS Zone.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 *
 * ### By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     id: "zone_id",
 * });
 * ```
 *
 * ### By name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     name: "example.com",
 * });
 * ```
 *
 * ### By name with partial match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     name: "example",
 *     partialMatch: true,
 * });
 * ```
 */
export function getZone(args?: GetZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetZoneResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:dns/getZone:getZone", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getZone.
 */
export interface GetZoneArgs {
    /**
     * [string] The ID of the DNS Zone you want to search for.
     */
    id?: string;
    /**
     * [string] The name of the DNS Zone you want to search for.
     */
    name?: string;
    /**
     * [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getZone.
 */
export interface GetZoneResult {
    /**
     * The description of the DNS Zone.
     */
    readonly description: string;
    /**
     * Indicates if the DNS Zone is activated or not.
     */
    readonly enabled: boolean;
    /**
     * The UUID of the DNS Zone.
     */
    readonly id: string;
    /**
     * The name of the DNS Zone.
     */
    readonly name: string;
    /**
     * A list of available name servers.
     */
    readonly nameservers: string[];
    readonly partialMatch?: boolean;
}
/**
 * The **DNS Zone** can be used to search for and return an existing DNS Zone.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_zone** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 *
 * ### By ID
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     id: "zone_id",
 * });
 * ```
 *
 * ### By name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     name: "example.com",
 * });
 * ```
 *
 * ### By name with partial match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.dns.getZone({
 *     name: "example",
 *     partialMatch: true,
 * });
 * ```
 */
export function getZoneOutput(args?: GetZoneOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetZoneResult> {
    args = args || {};
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:dns/getZone:getZone", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getZone.
 */
export interface GetZoneOutputArgs {
    /**
     * [string] The ID of the DNS Zone you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * [string] The name of the DNS Zone you want to search for.
     */
    name?: pulumi.Input<string>;
    /**
     * [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    partialMatch?: pulumi.Input<boolean>;
}
