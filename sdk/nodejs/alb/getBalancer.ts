// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **Application Load Balancer data source** can be used to search for and return an existing Application Load Balancer.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Id
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     id: "alb_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "ALB name",
 * });
 * ```
 *
 * ### By Name with Partial Match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "name",
 *     partialMatch: true,
 * });
 * ```
 */
export function getBalancer(args: GetBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetBalancerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:alb/getBalancer:getBalancer", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getBalancer.
 */
export interface GetBalancerArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: string;
    /**
     * ID of the application load balancer you want to search for.
     */
    id?: string;
    /**
     * Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
     */
    name?: string;
    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getBalancer.
 */
export interface GetBalancerResult {
    /**
     * Turn logging on and off for this product. Default value is 'false'.
     */
    readonly centralLogging: boolean;
    readonly datacenterId: string;
    /**
     * Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     */
    readonly flowlogs: outputs.alb.GetBalancerFlowlog[];
    /**
     * Id of the application load balancer.
     */
    readonly id: string;
    /**
     * Collection of the Application Load Balancer IP addresses. (Inbound and outbound) IPs of the listenerLan are customer-reserved public IPs for the public Load Balancers, and private IPs for the private Load Balancers.
     */
    readonly ips: string[];
    /**
     * Collection of private IP addresses with the subnet mask of the Application Load Balancer. IPs must contain valid a subnet mask. If no IP is provided, the system will generate an IP with /24 subnet.
     */
    readonly lbPrivateIps: string[];
    /**
     * ID of the listening (inbound) LAN.
     */
    readonly listenerLan: number;
    readonly loggingFormat: string;
    /**
     * Specifies the name of the flow log.
     */
    readonly name: string;
    readonly partialMatch?: boolean;
    /**
     * ID of the balanced private target LAN (outbound).
     */
    readonly targetLan: number;
}
/**
 * The **Application Load Balancer data source** can be used to search for and return an existing Application Load Balancer.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Id
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     id: "alb_id",
 * });
 * ```
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "ALB name",
 * });
 * ```
 *
 * ### By Name with Partial Match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.alb.getBalancer({
 *     datacenterId: exampleIonoscloudDatacenter.id,
 *     name: "name",
 *     partialMatch: true,
 * });
 * ```
 */
export function getBalancerOutput(args: GetBalancerOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetBalancerResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:alb/getBalancer:getBalancer", {
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getBalancer.
 */
export interface GetBalancerOutputArgs {
    /**
     * Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * ID of the application load balancer you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing application load balancer that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partialMatch` parameter is not set to true.
     */
    name?: pulumi.Input<string>;
    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     *
     * `datacenterId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: pulumi.Input<boolean>;
}
