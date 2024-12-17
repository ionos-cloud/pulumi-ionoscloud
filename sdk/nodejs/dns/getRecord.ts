// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **DNS Record** can be used to search for and return an existing DNS Record.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 */
export function getRecord(args: GetRecordArgs, opts?: pulumi.InvokeOptions): Promise<GetRecordResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:dns/getRecord:getRecord", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
        "zoneId": args.zoneId,
    }, opts);
}

/**
 * A collection of arguments for invoking getRecord.
 */
export interface GetRecordArgs {
    /**
     * [string] The ID of the DNS Record you want to search for.
     */
    id?: string;
    /**
     * [string] The name of the DNS Record you want to search for.
     */
    name?: string;
    /**
     * [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    partialMatch?: boolean;
    /**
     * [string] The ID of the DNS Zone in which the DNS Record can be found.
     */
    zoneId: string;
}

/**
 * A collection of values returned by getRecord.
 */
export interface GetRecordResult {
    /**
     * The content of the DNS Record.
     */
    readonly content: string;
    /**
     * Indicates if the DNS Record is active or not.
     */
    readonly enabled: boolean;
    readonly fqdn: string;
    /**
     * The UUID of the DNS Record.
     */
    readonly id?: string;
    /**
     * The name of the DNS Record.
     */
    readonly name?: string;
    readonly partialMatch?: boolean;
    /**
     * The priority for the DNS Record.
     */
    readonly priority: number;
    /**
     * The time to live of the DNS Record.
     */
    readonly ttl: number;
    /**
     * The type of the DNS Record.
     */
    readonly type: string;
    readonly zoneId: string;
}
/**
 * The **DNS Record** can be used to search for and return an existing DNS Record.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * > ⚠️  Only tokens are accepted for authorization in the **ionoscloud_dns_record** data source. Please ensure you are using tokens as other methods will not be valid.
 *
 * ## Example Usage
 */
export function getRecordOutput(args: GetRecordOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetRecordResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:dns/getRecord:getRecord", {
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
        "zoneId": args.zoneId,
    }, opts);
}

/**
 * A collection of arguments for invoking getRecord.
 */
export interface GetRecordOutputArgs {
    /**
     * [string] The ID of the DNS Record you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * [string] The name of the DNS Record you want to search for.
     */
    name?: pulumi.Input<string>;
    /**
     * [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     */
    partialMatch?: pulumi.Input<boolean>;
    /**
     * [string] The ID of the DNS Zone in which the DNS Record can be found.
     */
    zoneId: pulumi.Input<string>;
}
