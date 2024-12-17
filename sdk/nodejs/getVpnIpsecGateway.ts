// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The **VPN IPSec Gateway data source** can be used to search for and return an existing IPSec Gateway.
 * You can provide a string for the name parameter which will be compared with provisioned IPSec Gateways.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getVpnIpsecGateway(args: GetVpnIpsecGatewayArgs, opts?: pulumi.InvokeOptions): Promise<GetVpnIpsecGatewayResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getVpnIpsecGateway:getVpnIpsecGateway", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "version": args.version,
    }, opts);
}

/**
 * A collection of arguments for invoking getVpnIpsecGateway.
 */
export interface GetVpnIpsecGatewayArgs {
    /**
     * ID of an existing IPSec Gateway that you want to search for.
     */
    id?: string;
    /**
     * The location of the IPSec Gateway.
     */
    location: string;
    /**
     * Name of an existing IPSec Gateway that you want to search for.
     */
    name?: string;
    /**
     * The IKE version that is permitted for the VPN tunnels.
     */
    version?: string;
}

/**
 * A collection of values returned by getVpnIpsecGateway.
 */
export interface GetVpnIpsecGatewayResult {
    /**
     * The network connection for your gateway.
     */
    readonly connections: outputs.GetVpnIpsecGatewayConnection[];
    /**
     * (Optional)[string] The human-readable description of the IPSec Gateway.
     */
    readonly description: string;
    /**
     * Public IP address to be assigned to the gateway.
     */
    readonly gatewayIp: string;
    /**
     * The unique ID of the IPSec Gateway.
     */
    readonly id: string;
    readonly location: string;
    /**
     * The name of the IPSec Gateway.
     */
    readonly name: string;
    /**
     * The IKE version that is permitted for the VPN tunnels.
     */
    readonly version: string;
}
/**
 * The **VPN IPSec Gateway data source** can be used to search for and return an existing IPSec Gateway.
 * You can provide a string for the name parameter which will be compared with provisioned IPSec Gateways.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getVpnIpsecGatewayOutput(args: GetVpnIpsecGatewayOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetVpnIpsecGatewayResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getVpnIpsecGateway:getVpnIpsecGateway", {
        "id": args.id,
        "location": args.location,
        "name": args.name,
        "version": args.version,
    }, opts);
}

/**
 * A collection of arguments for invoking getVpnIpsecGateway.
 */
export interface GetVpnIpsecGatewayOutputArgs {
    /**
     * ID of an existing IPSec Gateway that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * The location of the IPSec Gateway.
     */
    location: pulumi.Input<string>;
    /**
     * Name of an existing IPSec Gateway that you want to search for.
     */
    name?: pulumi.Input<string>;
    /**
     * The IKE version that is permitted for the VPN tunnels.
     */
    version?: pulumi.Input<string>;
}
