// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export function getWireguardPeer(args: GetWireguardPeerArgs, opts?: pulumi.InvokeOptions): Promise<GetWireguardPeerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:vpn/getWireguardPeer:getWireguardPeer", {
        "gatewayId": args.gatewayId,
        "id": args.id,
        "location": args.location,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getWireguardPeer.
 */
export interface GetWireguardPeerArgs {
    gatewayId: string;
    id?: string;
    location?: string;
    name?: string;
}

/**
 * A collection of values returned by getWireguardPeer.
 */
export interface GetWireguardPeerResult {
    readonly allowedIps: string[];
    readonly description: string;
    readonly endpoints: outputs.vpn.GetWireguardPeerEndpoint[];
    readonly gatewayId: string;
    readonly id: string;
    readonly location?: string;
    readonly name: string;
    readonly publicKey: string;
    readonly status: string;
}
export function getWireguardPeerOutput(args: GetWireguardPeerOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetWireguardPeerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:vpn/getWireguardPeer:getWireguardPeer", {
        "gatewayId": args.gatewayId,
        "id": args.id,
        "location": args.location,
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getWireguardPeer.
 */
export interface GetWireguardPeerOutputArgs {
    gatewayId: pulumi.Input<string>;
    id?: pulumi.Input<string>;
    location?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
}
