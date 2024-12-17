// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * The Application Load Balancer Forwarding Rule data source can be used to search for and return an existing Application Load Balancer Forwarding Rules.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers Forwarding Rules.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getApplicationLoadbalancerForwardingrule({
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     applicationLoadbalancerId: ionoscloud_application_loadbalancer.example.id,
 *     name: "ALB FR Example",
 * });
 * ```
 *
 * ### By Name with Partial Match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getApplicationLoadbalancerForwardingrule({
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     applicationLoadbalancerId: ionoscloud_application_loadbalancer.example.id,
 *     name: "Example",
 *     partialMatch: true,
 * });
 * ```
 */
export function getApplicationLoadbalancerForwardingrule(args: GetApplicationLoadbalancerForwardingruleArgs, opts?: pulumi.InvokeOptions): Promise<GetApplicationLoadbalancerForwardingruleResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:index/getApplicationLoadbalancerForwardingrule:getApplicationLoadbalancerForwardingrule", {
        "applicationLoadbalancerId": args.applicationLoadbalancerId,
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getApplicationLoadbalancerForwardingrule.
 */
export interface GetApplicationLoadbalancerForwardingruleArgs {
    /**
     * Application Load Balancer's UUID.
     */
    applicationLoadbalancerId: string;
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
     * Both `datacenterId` and `applicationLoadbalancerId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getApplicationLoadbalancerForwardingrule.
 */
export interface GetApplicationLoadbalancerForwardingruleResult {
    readonly applicationLoadbalancerId: string;
    /**
     * The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
     * - `server certificates` - Array of items in that collection.
     */
    readonly clientTimeout: number;
    readonly datacenterId: string;
    /**
     * Array of items in that collection
     */
    readonly httpRules: outputs.GetApplicationLoadbalancerForwardingruleHttpRule[];
    /**
     * Id of Application Load Balancer Forwarding Rule
     */
    readonly id?: string;
    /**
     * Listening (inbound) IP.
     */
    readonly listenerIp: string;
    /**
     * Listening (inbound) port number; valid range is 1 to 65535.
     */
    readonly listenerPort: number;
    /**
     * The unique name of the Application Load Balancer HTTP rule.
     */
    readonly name?: string;
    readonly partialMatch?: boolean;
    /**
     * Balancing protocol.
     */
    readonly protocol: string;
    readonly serverCertificates: string[];
}
/**
 * The Application Load Balancer Forwarding Rule data source can be used to search for and return an existing Application Load Balancer Forwarding Rules.
 * You can provide a string for the name parameter which will be compared with provisioned Application Load Balancers Forwarding Rules.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search and make sure that your resources have unique names.
 *
 * ## Example Usage
 *
 * ### By Name
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getApplicationLoadbalancerForwardingrule({
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     applicationLoadbalancerId: ionoscloud_application_loadbalancer.example.id,
 *     name: "ALB FR Example",
 * });
 * ```
 *
 * ### By Name with Partial Match
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = ionoscloud.getApplicationLoadbalancerForwardingrule({
 *     datacenterId: ionoscloud_datacenter.example.id,
 *     applicationLoadbalancerId: ionoscloud_application_loadbalancer.example.id,
 *     name: "Example",
 *     partialMatch: true,
 * });
 * ```
 */
export function getApplicationLoadbalancerForwardingruleOutput(args: GetApplicationLoadbalancerForwardingruleOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetApplicationLoadbalancerForwardingruleResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:index/getApplicationLoadbalancerForwardingrule:getApplicationLoadbalancerForwardingrule", {
        "applicationLoadbalancerId": args.applicationLoadbalancerId,
        "datacenterId": args.datacenterId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getApplicationLoadbalancerForwardingrule.
 */
export interface GetApplicationLoadbalancerForwardingruleOutputArgs {
    /**
     * Application Load Balancer's UUID.
     */
    applicationLoadbalancerId: pulumi.Input<string>;
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
     * Both `datacenterId` and `applicationLoadbalancerId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     */
    partialMatch?: pulumi.Input<boolean>;
}
