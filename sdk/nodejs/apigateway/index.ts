// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { ApigatewayArgs, ApigatewayState } from "./apigateway";
export type Apigateway = import("./apigateway").Apigateway;
export const Apigateway: typeof import("./apigateway").Apigateway = null as any;
utilities.lazyLoad(exports, ["Apigateway"], () => require("./apigateway"));

export { GetApigatewayArgs, GetApigatewayResult, GetApigatewayOutputArgs } from "./getApigateway";
export const getApigateway: typeof import("./getApigateway").getApigateway = null as any;
export const getApigatewayOutput: typeof import("./getApigateway").getApigatewayOutput = null as any;
utilities.lazyLoad(exports, ["getApigateway","getApigatewayOutput"], () => require("./getApigateway"));

export { GetRouteArgs, GetRouteResult, GetRouteOutputArgs } from "./getRoute";
export const getRoute: typeof import("./getRoute").getRoute = null as any;
export const getRouteOutput: typeof import("./getRoute").getRouteOutput = null as any;
utilities.lazyLoad(exports, ["getRoute","getRouteOutput"], () => require("./getRoute"));

export { RouteArgs, RouteState } from "./route";
export type Route = import("./route").Route;
export const Route: typeof import("./route").Route = null as any;
utilities.lazyLoad(exports, ["Route"], () => require("./route"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:apigateway/apigateway:Apigateway":
                return new Apigateway(name, <any>undefined, { urn })
            case "ionoscloud:apigateway/route:Route":
                return new Route(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "apigateway/apigateway", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "apigateway/route", _module)
