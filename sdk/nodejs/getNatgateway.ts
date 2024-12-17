// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **NAT gateway data source** can be used to search for and return existing NAT Gateways.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getNatgateway(args: GetNatgatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetNatgatewayResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getNatgateway:getNatgateway", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getNatgateway.
 */
export interface GetNatgatewayArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: string;
    /**
     * ID of the network load balancer forwarding rule you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: string;
    /**
     * Name of an existing network load balancer forwarding rule that you want to search for.
     */
    name?: string;
}

/**
 * A collection of values returned by getNatgateway.
 */
export interface GetNatgatewayResult {
    readonly datacenterId: string;
    /**
     * Id for the LAN connected to the NAT gateway
     */
    readonly id?: string;
    /**
     * Collection of LANs connected to the NAT gateway. IPs must contain valid subnet mask. If user will not provide any IP then system will generate an IP with /24 subnet.
     */
    readonly lans: outputs.GetNatgatewayLan[];
    /**
     * Name of that natgateway
     */
    readonly name?: string;
    /**
     * Collection of public IP addresses of the NAT gateway. Should be customer reserved IP addresses in that location
     */
    readonly publicIps: string[];
}
/**
 * The **NAT gateway data source** can be used to search for and return existing NAT Gateways.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getNatgatewayOutput(args: GetNatgatewayOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetNatgatewayResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getNatgateway:getNatgateway", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getNatgateway.
 */
export interface GetNatgatewayOutputArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * ID of the network load balancer forwarding rule you want to search for.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing network load balancer forwarding rule that you want to search for.
     */
    name?: pulumi.Input<string>;
}
