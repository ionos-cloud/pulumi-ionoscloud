// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Overview
 *
 * The `ionoscloud.vpn.WireguardGateway` resource manages a WireGuard Gateway within the IONOS Cloud infrastructure.
 * This resource facilitates the creation, management, and deletion of WireGuard VPN Gateways, enabling secure connections between your network resources.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const datacenterExample = new ionoscloud.compute.Datacenter("datacenter_example", {
 *     name: "datacenter_example",
 *     location: "de/fra",
 * });
 * const ipblockExample = new ionoscloud.compute.IPBlock("ipblock_example", {
 *     location: "de/fra",
 *     size: 1,
 *     name: "ipblock_example",
 * });
 * const lanExample = new ionoscloud.compute.Lan("lan_example", {
 *     name: "lan_example",
 *     datacenterId: datacenterExample.id,
 * });
 * const gateway = new ionoscloud.vpn.WireguardGateway("gateway", {
 *     location: "de/fra",
 *     name: "gateway_example",
 *     description: "description",
 *     privateKey: "private",
 *     gatewayIp: ipblockExample.ips[0],
 *     interfaceIpv4Cidr: "192.168.1.100/24",
 *     connections: [{
 *         datacenterId: datacenterExample.id,
 *         lanId: lanExample.id,
 *         ipv4Cidr: "192.168.1.108/24",
 *     }],
 *     maintenanceWindow: {
 *         dayOfTheWeek: "Monday",
 *         time: "09:00:00",
 *     },
 *     tier: "STANDARD",
 * });
 * ```
 *
 * ## Import
 *
 * WireGuard Gateways can be imported using their ID:
 *
 * ```sh
 * $ pulumi import ionoscloud:vpn/wireguardGateway:WireguardGateway example_gateway location:id
 * ```
 */
export class WireguardGateway extends pulumi.CustomResource {
    /**
     * Get an existing WireguardGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WireguardGatewayState, opts?: pulumi.CustomResourceOptions): WireguardGateway {
        return new WireguardGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:vpn/wireguardGateway:WireguardGateway';

    /**
     * Returns true if the given object is an instance of WireguardGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WireguardGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WireguardGateway.__pulumiType;
    }

    /**
     * [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
     */
    public readonly connections!: pulumi.Output<outputs.vpn.WireguardGatewayConnection[]>;
    /**
     * [String] A description of the WireGuard Gateway.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * [String] The IP address of the WireGuard Gateway.
     */
    public readonly gatewayIp!: pulumi.Output<string>;
    /**
     * [String] The IPv4 CIDR for the WireGuard Gateway interface.
     */
    public readonly interfaceIpv4Cidr!: pulumi.Output<string | undefined>;
    /**
     * [String] The IPv6 CIDR for the WireGuard Gateway interface.
     */
    public readonly interfaceIpv6Cidr!: pulumi.Output<string | undefined>;
    public readonly listenPort!: pulumi.Output<number | undefined>;
    /**
     * [String] The location of the WireGuard Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    public readonly maintenanceWindow!: pulumi.Output<outputs.vpn.WireguardGatewayMaintenanceWindow>;
    /**
     * [String] The name of the WireGuard Gateway.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [String] The private key for the WireGuard Gateway. To be created with the wg utility.
     */
    public readonly privateKey!: pulumi.Output<string>;
    /**
     * (Computed)[String] The public key for the WireGuard Gateway.
     * -
     * > **⚠ NOTE:** `IONOS_API_URL_VPN` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
     */
    public /*out*/ readonly publicKey!: pulumi.Output<string>;
    /**
     * (Computed)[String] The current status of the WireGuard Gateway.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    public readonly tier!: pulumi.Output<string | undefined>;

    /**
     * Create a WireguardGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WireguardGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WireguardGatewayArgs | WireguardGatewayState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WireguardGatewayState | undefined;
            resourceInputs["connections"] = state ? state.connections : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["gatewayIp"] = state ? state.gatewayIp : undefined;
            resourceInputs["interfaceIpv4Cidr"] = state ? state.interfaceIpv4Cidr : undefined;
            resourceInputs["interfaceIpv6Cidr"] = state ? state.interfaceIpv6Cidr : undefined;
            resourceInputs["listenPort"] = state ? state.listenPort : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["maintenanceWindow"] = state ? state.maintenanceWindow : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["privateKey"] = state ? state.privateKey : undefined;
            resourceInputs["publicKey"] = state ? state.publicKey : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
            resourceInputs["tier"] = state ? state.tier : undefined;
        } else {
            const args = argsOrState as WireguardGatewayArgs | undefined;
            if ((!args || args.connections === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connections'");
            }
            if ((!args || args.gatewayIp === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gatewayIp'");
            }
            if ((!args || args.privateKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'privateKey'");
            }
            resourceInputs["connections"] = args ? args.connections : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["gatewayIp"] = args ? args.gatewayIp : undefined;
            resourceInputs["interfaceIpv4Cidr"] = args ? args.interfaceIpv4Cidr : undefined;
            resourceInputs["interfaceIpv6Cidr"] = args ? args.interfaceIpv6Cidr : undefined;
            resourceInputs["listenPort"] = args ? args.listenPort : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["maintenanceWindow"] = args ? args.maintenanceWindow : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["privateKey"] = args?.privateKey ? pulumi.secret(args.privateKey) : undefined;
            resourceInputs["tier"] = args ? args.tier : undefined;
            resourceInputs["publicKey"] = undefined /*out*/;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["privateKey"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(WireguardGateway.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WireguardGateway resources.
 */
export interface WireguardGatewayState {
    /**
     * [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
     */
    connections?: pulumi.Input<pulumi.Input<inputs.vpn.WireguardGatewayConnection>[]>;
    /**
     * [String] A description of the WireGuard Gateway.
     */
    description?: pulumi.Input<string>;
    /**
     * [String] The IP address of the WireGuard Gateway.
     */
    gatewayIp?: pulumi.Input<string>;
    /**
     * [String] The IPv4 CIDR for the WireGuard Gateway interface.
     */
    interfaceIpv4Cidr?: pulumi.Input<string>;
    /**
     * [String] The IPv6 CIDR for the WireGuard Gateway interface.
     */
    interfaceIpv6Cidr?: pulumi.Input<string>;
    listenPort?: pulumi.Input<number>;
    /**
     * [String] The location of the WireGuard Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    location?: pulumi.Input<string>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    maintenanceWindow?: pulumi.Input<inputs.vpn.WireguardGatewayMaintenanceWindow>;
    /**
     * [String] The name of the WireGuard Gateway.
     */
    name?: pulumi.Input<string>;
    /**
     * [String] The private key for the WireGuard Gateway. To be created with the wg utility.
     */
    privateKey?: pulumi.Input<string>;
    /**
     * (Computed)[String] The public key for the WireGuard Gateway.
     * -
     * > **⚠ NOTE:** `IONOS_API_URL_VPN` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
     */
    publicKey?: pulumi.Input<string>;
    /**
     * (Computed)[String] The current status of the WireGuard Gateway.
     */
    status?: pulumi.Input<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    tier?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WireguardGateway resource.
 */
export interface WireguardGatewayArgs {
    /**
     * [Block] The connection configuration for the WireGuard Gateway. This block supports fields documented below.
     */
    connections: pulumi.Input<pulumi.Input<inputs.vpn.WireguardGatewayConnection>[]>;
    /**
     * [String] A description of the WireGuard Gateway.
     */
    description?: pulumi.Input<string>;
    /**
     * [String] The IP address of the WireGuard Gateway.
     */
    gatewayIp: pulumi.Input<string>;
    /**
     * [String] The IPv4 CIDR for the WireGuard Gateway interface.
     */
    interfaceIpv4Cidr?: pulumi.Input<string>;
    /**
     * [String] The IPv6 CIDR for the WireGuard Gateway interface.
     */
    interfaceIpv6Cidr?: pulumi.Input<string>;
    listenPort?: pulumi.Input<number>;
    /**
     * [String] The location of the WireGuard Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    location?: pulumi.Input<string>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    maintenanceWindow?: pulumi.Input<inputs.vpn.WireguardGatewayMaintenanceWindow>;
    /**
     * [String] The name of the WireGuard Gateway.
     */
    name?: pulumi.Input<string>;
    /**
     * [String] The private key for the WireGuard Gateway. To be created with the wg utility.
     */
    privateKey: pulumi.Input<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    tier?: pulumi.Input<string>;
}
