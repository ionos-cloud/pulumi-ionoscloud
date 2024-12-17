// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
 * You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getRoute(args: GetRouteArgs, opts?: pulumi.InvokeOptions): Promise<GetRouteResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ionoscloud:apigateway/getRoute:getRoute", {
        "gatewayId": args.gatewayId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getRoute.
 */
export interface GetRouteArgs {
    /**
     * The ID of the API Gateway that the route belongs to.
     */
    gatewayId: string;
    /**
     * ID of an existing API Gateway Route that you want to search for.
     */
    id?: string;
    /**
     * Name of an existing API Gateway Route that you want to search for.
     */
    name?: string;
    partialMatch?: boolean;
}

/**
 * A collection of values returned by getRoute.
 */
export interface GetRouteResult {
    readonly gatewayId: string;
    /**
     * ID of the API Gateway Route.
     */
    readonly id: string;
    /**
     * The HTTP methods that the route should match.
     */
    readonly methods: string[];
    /**
     * The name of the API Gateway Route.
     */
    readonly name: string;
    readonly partialMatch?: boolean;
    /**
     * The paths that the route should match.
     */
    readonly paths: string[];
    /**
     * This field specifies the protocol used by the ingress to route traffic to the backend service.
     */
    readonly type: string;
    readonly upstreams: outputs.apigateway.GetRouteUpstream[];
    /**
     * Shows whether websocket support is enabled or disabled.
     */
    readonly websocket: boolean;
}
/**
 * The **API Gateway Route data source** can be used to search for and return an existing API Gateway route.
 * You can provide a string for the name parameter which will be compared with provisioned API Gateway routes.
 * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
 * When this happens, please refine your search string so that it is specific enough to return only one result.
 *
 * ## Example Usage
 */
export function getRouteOutput(args: GetRouteOutputArgs, opts?: pulumi.InvokeOutputOptions): pulumi.Output<GetRouteResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ionoscloud:apigateway/getRoute:getRoute", {
        "gatewayId": args.gatewayId,
        "id": args.id,
        "name": args.name,
        "partialMatch": args.partialMatch,
    }, opts);
}

/**
 * A collection of arguments for invoking getRoute.
 */
export interface GetRouteOutputArgs {
    /**
     * The ID of the API Gateway that the route belongs to.
     */
    gatewayId: pulumi.Input<string>;
    /**
     * ID of an existing API Gateway Route that you want to search for.
     */
    id?: pulumi.Input<string>;
    /**
     * Name of an existing API Gateway Route that you want to search for.
     */
    name?: pulumi.Input<string>;
    partialMatch?: pulumi.Input<boolean>;
}
