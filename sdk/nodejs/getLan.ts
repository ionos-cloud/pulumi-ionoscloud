// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **LAN data source** can be used to search for and return existing lans.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getLan(args: GetLanArgs, opts?: pulumi.InvokeOptions): Promise<GetLanResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getLan:getLan", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getLan.
 */
export interface GetLanArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: string;
    /**
     * ID of the lan you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: string;
    /**
     * Name of an existing lan that you want to search for.
     */
    name?: string;
}

/**
 * A collection of values returned by getLan.
 */
export interface GetLanResult {
    /**
     * The ID of lan's Virtual Data Center.
     */
    readonly datacenterId: string;
    /**
     * The id of the LAN.
     */
    readonly id?: string;
    /**
     * list of
     */
    readonly ipFailovers: outputs.GetLanIpFailover[];
    readonly ipv6CidrBlock: string;
    /**
     * The name of the LAN.
     */
    readonly name?: string;
    /**
     * The unique id of a `ionoscloud.PrivateCrossconnect` resource, in order.
     */
    readonly pcc: string;
    /**
     * Indicates if the LAN faces the public Internet (true) or not (false).
     */
    readonly public: boolean;
}
/**
 * The **LAN data source** can be used to search for and return existing lans.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getLanOutput(args: GetLanOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLanResult> {
    return pulumi.output(args).apply((a: any) => getLan(a, opts))
}

/**
 * A collection of arguments for invoking getLan.
 */
export interface GetLanOutputArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * ID of the lan you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing lan that you want to search for.
     */
    name?: pulumi.Input<string>;
}
