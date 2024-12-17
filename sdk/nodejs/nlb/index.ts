// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { BalancerArgs, BalancerState } from "./balancer";
export type Balancer = import("./balancer").Balancer;
export const Balancer: typeof import("./balancer").Balancer = null as any;
utilities.lazyLoad(exports, ["Balancer"], () => require("./balancer"));

export { ForwardingRuleArgs, ForwardingRuleState } from "./forwardingRule";
export type ForwardingRule = import("./forwardingRule").ForwardingRule;
export const ForwardingRule: typeof import("./forwardingRule").ForwardingRule = null as any;
utilities.lazyLoad(exports, ["ForwardingRule"], () => require("./forwardingRule"));

export { GetBalancerArgs, GetBalancerResult, GetBalancerOutputArgs } from "./getBalancer";
export const getBalancer: typeof import("./getBalancer").getBalancer = null as any;
export const getBalancerOutput: typeof import("./getBalancer").getBalancerOutput = null as any;
utilities.lazyLoad(exports, ["getBalancer","getBalancerOutput"], () => require("./getBalancer"));

export { GetForwardingRuleArgs, GetForwardingRuleResult, GetForwardingRuleOutputArgs } from "./getForwardingRule";
export const getForwardingRule: typeof import("./getForwardingRule").getForwardingRule = null as any;
export const getForwardingRuleOutput: typeof import("./getForwardingRule").getForwardingRuleOutput = null as any;
utilities.lazyLoad(exports, ["getForwardingRule","getForwardingRuleOutput"], () => require("./getForwardingRule"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "ionoscloud:nlb/balancer:Balancer":
                return new Balancer(name, <any>undefined, { urn })
            case "ionoscloud:nlb/forwardingRule:ForwardingRule":
                return new ForwardingRule(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("ionoscloud", "nlb/balancer", _module)
pulumi.runtime.registerResourceModule("ionoscloud", "nlb/forwardingRule", _module)
