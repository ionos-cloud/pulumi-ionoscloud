// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **Nat Gateway Rule** on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleIPBlock = new ionoscloud.compute.IPBlock("example", {
 *     location: "us/las",
 *     size: 2,
 *     name: "IP Block Example",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "Lan Example",
 * });
 * const exampleNatGateway = new ionoscloud.compute.NatGateway("example", {
 *     datacenterId: example.id,
 *     name: "example",
 *     publicIps: [
 *         exampleIPBlock.ips[0],
 *         exampleIPBlock.ips[1],
 *     ],
 *     lans: [{
 *         id: exampleLan.id,
 *         gatewayIps: ["10.11.2.5"],
 *     }],
 * });
 * const exampleNatGatewayRule = new ionoscloud.compute.NatGatewayRule("example", {
 *     datacenterId: example.id,
 *     natgatewayId: exampleNatGateway.id,
 *     name: "example",
 *     type: "SNAT",
 *     protocol: "TCP",
 *     sourceSubnet: "10.0.1.0/24",
 *     publicIp: exampleIPBlock.ips[0],
 *     targetSubnet: "10.0.1.0/24",
 *     targetPortRange: {
 *         start: 500,
 *         end: 1000,
 *     },
 * });
 * ```
 *
 * ## Import
 *
 * A Nat Gateway Rule resource can be imported using its `resource id`, the `datacenter id` and the `natgateway id , e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/natGatewayRule:NatGatewayRule my_natgateway_rule datacenter uuid/nat gateway uuid/nat gateway rule uuid
 * ```
 */
export class NatGatewayRule extends pulumi.CustomResource {
    /**
     * Get an existing NatGatewayRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NatGatewayRuleState, opts?: pulumi.CustomResourceOptions): NatGatewayRule {
        return new NatGatewayRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/natGatewayRule:NatGatewayRule';

    /**
     * Returns true if the given object is an instance of NatGatewayRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NatGatewayRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NatGatewayRule.__pulumiType;
    }

    /**
     * [string] A Datacenter's UUID.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [string] Name of the NAT gateway rule.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] Nat Gateway's UUID.
     */
    public readonly natgatewayId!: pulumi.Output<string>;
    /**
     * [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
     */
    public readonly publicIp!: pulumi.Output<string>;
    /**
     * [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
     */
    public readonly sourceSubnet!: pulumi.Output<string>;
    /**
     * Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
     */
    public readonly targetPortRange!: pulumi.Output<outputs.compute.NatGatewayRuleTargetPortRange>;
    /**
     * [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
     */
    public readonly targetSubnet!: pulumi.Output<string>;
    /**
     * [string] Type of the NAT gateway rule.
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a NatGatewayRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NatGatewayRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NatGatewayRuleArgs | NatGatewayRuleState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NatGatewayRuleState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["natgatewayId"] = state ? state.natgatewayId : undefined;
            resourceInputs["protocol"] = state ? state.protocol : undefined;
            resourceInputs["publicIp"] = state ? state.publicIp : undefined;
            resourceInputs["sourceSubnet"] = state ? state.sourceSubnet : undefined;
            resourceInputs["targetPortRange"] = state ? state.targetPortRange : undefined;
            resourceInputs["targetSubnet"] = state ? state.targetSubnet : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as NatGatewayRuleArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.natgatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'natgatewayId'");
            }
            if ((!args || args.publicIp === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicIp'");
            }
            if ((!args || args.sourceSubnet === undefined) && !opts.urn) {
                throw new Error("Missing required property 'sourceSubnet'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["natgatewayId"] = args ? args.natgatewayId : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["publicIp"] = args ? args.publicIp : undefined;
            resourceInputs["sourceSubnet"] = args ? args.sourceSubnet : undefined;
            resourceInputs["targetPortRange"] = args ? args.targetPortRange : undefined;
            resourceInputs["targetSubnet"] = args ? args.targetSubnet : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(NatGatewayRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NatGatewayRule resources.
 */
export interface NatGatewayRuleState {
    /**
     * [string] A Datacenter's UUID.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [string] Name of the NAT gateway rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Nat Gateway's UUID.
     */
    natgatewayId?: pulumi.Input<string>;
    /**
     * [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
     */
    protocol?: pulumi.Input<string>;
    /**
     * [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
     */
    publicIp?: pulumi.Input<string>;
    /**
     * [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
     */
    sourceSubnet?: pulumi.Input<string>;
    /**
     * Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
     */
    targetPortRange?: pulumi.Input<inputs.compute.NatGatewayRuleTargetPortRange>;
    /**
     * [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
     */
    targetSubnet?: pulumi.Input<string>;
    /**
     * [string] Type of the NAT gateway rule.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NatGatewayRule resource.
 */
export interface NatGatewayRuleArgs {
    /**
     * [string] A Datacenter's UUID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] Name of the NAT gateway rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] Nat Gateway's UUID.
     */
    natgatewayId: pulumi.Input<string>;
    /**
     * [string] Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
     */
    protocol?: pulumi.Input<string>;
    /**
     * [string] Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource.
     */
    publicIp: pulumi.Input<string>;
    /**
     * [string] Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
     */
    sourceSubnet: pulumi.Input<string>;
    /**
     * Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port.
     */
    targetPortRange?: pulumi.Input<inputs.compute.NatGatewayRuleTargetPortRange>;
    /**
     * [string] Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
     */
    targetSubnet?: pulumi.Input<string>;
    /**
     * [string] Type of the NAT gateway rule.
     */
    type?: pulumi.Input<string>;
}
