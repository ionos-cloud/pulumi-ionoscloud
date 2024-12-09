// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages an **API Gateway Route** on IonosCloud.
 *
 * ## Example Usage
 *
 * This resource will create an operational API Gateway Route. After this section completes, the provisioner can be called.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const example = new ionoscloud.Apigateway("example", {
 *     metrics: true,
 *     customDomains: [
 *         {
 *             name: "example.com",
 *             certificateId: "00000000-0000-0000-0000-000000000000",
 *         },
 *         {
 *             name: "example.org",
 *             certificateId: "00000000-0000-0000-0000-000000000000",
 *         },
 *     ],
 * });
 * const apigatewayRoute = new ionoscloud.ApigatewayRoute("apigatewayRoute", {
 *     type: "http",
 *     paths: [
 *         "/foo/*",
 *         "/bar",
 *     ],
 *     methods: [
 *         "GET",
 *         "POST",
 *     ],
 *     websocket: false,
 *     upstreams: [{
 *         scheme: "http",
 *         loadbalancer: "roundrobin",
 *         host: "example.com",
 *         port: 80,
 *         weight: 100,
 *     }],
 *     gatewayId: example.id,
 * });
 * ```
 *
 * ## Import
 *
 * API Gateway route can be imported using the `apigateway route id`:
 *
 * ```sh
 * $ pulumi import ionoscloud:index/apigatewayRoute:ApigatewayRoute myroute {apigateway uuid}:{apigateway route uuid}
 * ```
 */
export class ApigatewayRoute extends pulumi.CustomResource {
    /**
     * Get an existing ApigatewayRoute resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApigatewayRouteState, opts?: pulumi.CustomResourceOptions): ApigatewayRoute {
        return new ApigatewayRoute(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/apigatewayRoute:ApigatewayRoute';

    /**
     * Returns true if the given object is an instance of ApigatewayRoute.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ApigatewayRoute {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ApigatewayRoute.__pulumiType;
    }

    /**
     * [string] The ID of the API Gateway that the route belongs to.
     */
    public readonly gatewayId!: pulumi.Output<string>;
    /**
     * [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
     * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
     */
    public readonly methods!: pulumi.Output<string[]>;
    /**
     * [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [list] The paths that the route should match. Minimum items: 1.
     */
    public readonly paths!: pulumi.Output<string[]>;
    /**
     * [string] This field specifies the protocol used by the ingress to route traffic to the backend
     * service. Default value: `http`.
     */
    public readonly type!: pulumi.Output<string | undefined>;
    /**
     * Upstreams information of the API Gateway Route. Minimum items: 1.
     */
    public readonly upstreams!: pulumi.Output<outputs.ApigatewayRouteUpstream[]>;
    /**
     * [bool] To enable websocket support. Default value: `false`.
     */
    public readonly websocket!: pulumi.Output<boolean | undefined>;

    /**
     * Create a ApigatewayRoute resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ApigatewayRouteArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApigatewayRouteArgs | ApigatewayRouteState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ApigatewayRouteState | undefined;
            resourceInputs["gatewayId"] = state ? state.gatewayId : undefined;
            resourceInputs["methods"] = state ? state.methods : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["paths"] = state ? state.paths : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["upstreams"] = state ? state.upstreams : undefined;
            resourceInputs["websocket"] = state ? state.websocket : undefined;
        } else {
            const args = argsOrState as ApigatewayRouteArgs | undefined;
            if ((!args || args.gatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gatewayId'");
            }
            if ((!args || args.methods === undefined) && !opts.urn) {
                throw new Error("Missing required property 'methods'");
            }
            if ((!args || args.paths === undefined) && !opts.urn) {
                throw new Error("Missing required property 'paths'");
            }
            if ((!args || args.upstreams === undefined) && !opts.urn) {
                throw new Error("Missing required property 'upstreams'");
            }
            resourceInputs["gatewayId"] = args ? args.gatewayId : undefined;
            resourceInputs["methods"] = args ? args.methods : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["paths"] = args ? args.paths : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["upstreams"] = args ? args.upstreams : undefined;
            resourceInputs["websocket"] = args ? args.websocket : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ApigatewayRoute.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ApigatewayRoute resources.
 */
export interface ApigatewayRouteState {
    /**
     * [string] The ID of the API Gateway that the route belongs to.
     */
    gatewayId?: pulumi.Input<string>;
    /**
     * [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
     * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
     */
    methods?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] The paths that the route should match. Minimum items: 1.
     */
    paths?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] This field specifies the protocol used by the ingress to route traffic to the backend
     * service. Default value: `http`.
     */
    type?: pulumi.Input<string>;
    /**
     * Upstreams information of the API Gateway Route. Minimum items: 1.
     */
    upstreams?: pulumi.Input<pulumi.Input<inputs.ApigatewayRouteUpstream>[]>;
    /**
     * [bool] To enable websocket support. Default value: `false`.
     */
    websocket?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a ApigatewayRoute resource.
 */
export interface ApigatewayRouteArgs {
    /**
     * [string] The ID of the API Gateway that the route belongs to.
     */
    gatewayId: pulumi.Input<string>;
    /**
     * [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
     * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
     */
    methods: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] The paths that the route should match. Minimum items: 1.
     */
    paths: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] This field specifies the protocol used by the ingress to route traffic to the backend
     * service. Default value: `http`.
     */
    type?: pulumi.Input<string>;
    /**
     * Upstreams information of the API Gateway Route. Minimum items: 1.
     */
    upstreams: pulumi.Input<pulumi.Input<inputs.ApigatewayRouteUpstream>[]>;
    /**
     * [bool] To enable websocket support. Default value: `false`.
     */
    websocket?: pulumi.Input<boolean>;
}
