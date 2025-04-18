// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The **IP Failover data source** can be used to search for and return an existing IP Failover object.
 * You need to provide the datacenterId and the id of the lan to get the ip failover object for the provided datacenter.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPFailover({
 *     datacenterId: "datacenter_id",
 *     lanId: "lan_id",
 * });
 * ```
 */
export function getIPFailover(args: GetIPFailoverArgs, opts?: pulumi.InvokeOptions): Promise<GetIPFailoverResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:compute/getIPFailover:getIPFailover", {
        "datacenterId": args.datacenterId,
        "ip": args.ip,
        "lanId": args.lanId,
    }, opts);
}

/**
 * A collection of arguments for invoking getIPFailover.
 */
export interface GetIPFailoverArgs {
    /**
     * The ID of the datacenter containing the ip failover datasource
     */
    datacenterId: string;
    /**
     * The reserved IP address to be used in the IP failover group.
     */
    ip: string;
    /**
     * The id of the lan of which the IP failover belongs
     */
    lanId: string;
}

/**
 * A collection of values returned by getIPFailover.
 */
export interface GetIPFailoverResult {
    /**
     * The ID of a Data Center.
     */
    readonly datacenterId: string;
    readonly id: string;
    /**
     * The reserved IP address to be used in the IP failover group.
     */
    readonly ip: string;
    /**
     * The ID of a LAN.
     */
    readonly lanId: string;
    /**
     * The ID of a NIC.
     */
    readonly nicuuid: string;
}
/**
 * The **IP Failover data source** can be used to search for and return an existing IP Failover object.
 * You need to provide the datacenterId and the id of the lan to get the ip failover object for the provided datacenter.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.compute.getIPFailover({
 *     datacenterId: "datacenter_id",
 *     lanId: "lan_id",
 * });
 * ```
 */
export function getIPFailoverOutput(args: GetIPFailoverOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetIPFailoverResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:compute/getIPFailover:getIPFailover", {
        "datacenterId": args.datacenterId,
        "ip": args.ip,
        "lanId": args.lanId,
    }, opts);
}

/**
 * A collection of arguments for invoking getIPFailover.
 */
export interface GetIPFailoverOutputArgs {
    /**
     * The ID of the datacenter containing the ip failover datasource
     */
    datacenterId: pulumi.Input<string>;
    /**
     * The reserved IP address to be used in the IP failover group.
     */
    ip: pulumi.Input<string>;
    /**
     * The id of the lan of which the IP failover belongs
     */
    lanId: pulumi.Input<string>;
}
