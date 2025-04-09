// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * An IPSec Gateway resource manages the creation, management, and deletion of VPN IPSec Gateways within the IONOS Cloud
 * infrastructure. This resource facilitates the creation of VPN IPSec Gateways, enabling secure connections between your
 * network resources.
 *
 * ## Usage example
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * // Basic example
 * const testDatacenter = new ionoscloud.compute.Datacenter("test_datacenter", {
 *     name: "test_vpn_gateway_basic",
 *     location: "de/fra",
 * });
 * const testLan = new ionoscloud.compute.Lan("test_lan", {
 *     name: "test_lan_basic",
 *     "public": false,
 *     datacenterId: testDatacenter.id,
 * });
 * const testIpblock = new ionoscloud.compute.IPBlock("test_ipblock", {
 *     name: "test_ipblock_basic",
 *     location: "de/fra",
 *     size: 1,
 * });
 * const example = new ionoscloud.vpn.IpsecGateway("example", {
 *     name: "ipsec_gateway_basic",
 *     location: "de/fra",
 *     gatewayIp: testIpblock.ips[0],
 *     version: "IKEv2",
 *     description: "This gateway connects site A to VDC X.",
 *     connections: [{
 *         datacenterId: testDatacenter.id,
 *         lanId: testLan.id,
 *         ipv4Cidr: "192.168.100.10/24",
 *     }],
 * });
 * ```
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * // Complete example
 * const testDatacenter = new ionoscloud.compute.Datacenter("test_datacenter", {
 *     name: "vpn_gateway_test",
 *     location: "de/fra",
 * });
 * const testLan = new ionoscloud.compute.Lan("test_lan", {
 *     name: "test_lan",
 *     "public": false,
 *     datacenterId: testDatacenter.id,
 *     ipv6CidrBlock: lanIpv6CidrBlock,
 * });
 * const testIpblock = new ionoscloud.compute.IPBlock("test_ipblock", {
 *     name: "test_ipblock",
 *     location: "de/fra",
 *     size: 1,
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const testServer = new ionoscloud.compute.Server("test_server", {
 *     name: "test_server",
 *     datacenterId: testDatacenter.id,
 *     cores: 1,
 *     ram: 2048,
 *     imageName: "ubuntu:latest",
 *     imagePassword: serverImagePassword.result,
 *     nic: {
 *         lan: testLan.id,
 *         name: "test_nic",
 *         dhcp: true,
 *         dhcpv6: false,
 *         ipv6CidrBlock: ipv6CidrBlock,
 *         firewallActive: false,
 *     },
 *     volume: {
 *         name: "test_volume",
 *         diskType: "HDD",
 *         size: 10,
 *         licenceType: "OTHER",
 *     },
 * });
 * const example = new ionoscloud.vpn.IpsecGateway("example", {
 *     name: "ipsec-gateway",
 *     location: "de/fra",
 *     gatewayIp: testIpblock.ips[0],
 *     version: "IKEv2",
 *     description: "This gateway connects site A to VDC X.",
 *     connections: [{
 *         datacenterId: testDatacenter.id,
 *         lanId: testLan.id,
 *         ipv4Cidr: "ipv4_cidr_block_from_nic",
 *         ipv6Cidr: "ipv6_cidr_block_from_dc",
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
 * The resource can be imported using the `location` and `gateway_id`, for example:
 *
 * ```sh
 * $ pulumi import ionoscloud:vpn/ipsecGateway:IpsecGateway example location:gateway_id
 * ```
 */
export class IpsecGateway extends pulumi.CustomResource {
    /**
     * Get an existing IpsecGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpsecGatewayState, opts?: pulumi.CustomResourceOptions): IpsecGateway {
        return new IpsecGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:vpn/ipsecGateway:IpsecGateway';

    /**
     * Returns true if the given object is an instance of IpsecGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IpsecGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IpsecGateway.__pulumiType;
    }

    /**
     * [list] The network connection for your gateway. **Note**: all connections must belong to the
     * same datacenter. Minimum items: 1. Maximum items: 10.
     */
    public readonly connections!: pulumi.Output<outputs.vpn.IpsecGatewayConnection[]>;
    /**
     * [string] The human-readable description of the IPSec Gateway.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
     * the same datacenter as the connections.
     */
    public readonly gatewayIp!: pulumi.Output<string>;
    /**
     * [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    public readonly maintenanceWindow!: pulumi.Output<outputs.vpn.IpsecGatewayMaintenanceWindow>;
    /**
     * [string] The name of the IPSec Gateway.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    public readonly tier!: pulumi.Output<string | undefined>;
    /**
     * [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
     * values: `IKEv2`.
     */
    public readonly version!: pulumi.Output<string | undefined>;

    /**
     * Create a IpsecGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpsecGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpsecGatewayArgs | IpsecGatewayState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IpsecGatewayState | undefined;
            resourceInputs["connections"] = state ? state.connections : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["gatewayIp"] = state ? state.gatewayIp : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["maintenanceWindow"] = state ? state.maintenanceWindow : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["tier"] = state ? state.tier : undefined;
            resourceInputs["version"] = state ? state.version : undefined;
        } else {
            const args = argsOrState as IpsecGatewayArgs | undefined;
            if ((!args || args.connections === undefined) && !opts.urn) {
                throw new Error("Missing required property 'connections'");
            }
            if ((!args || args.gatewayIp === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gatewayIp'");
            }
            resourceInputs["connections"] = args ? args.connections : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["gatewayIp"] = args ? args.gatewayIp : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["maintenanceWindow"] = args ? args.maintenanceWindow : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tier"] = args ? args.tier : undefined;
            resourceInputs["version"] = args ? args.version : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IpsecGateway.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IpsecGateway resources.
 */
export interface IpsecGatewayState {
    /**
     * [list] The network connection for your gateway. **Note**: all connections must belong to the
     * same datacenter. Minimum items: 1. Maximum items: 10.
     */
    connections?: pulumi.Input<pulumi.Input<inputs.vpn.IpsecGatewayConnection>[]>;
    /**
     * [string] The human-readable description of the IPSec Gateway.
     */
    description?: pulumi.Input<string>;
    /**
     * [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
     * the same datacenter as the connections.
     */
    gatewayIp?: pulumi.Input<string>;
    /**
     * [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    location?: pulumi.Input<string>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    maintenanceWindow?: pulumi.Input<inputs.vpn.IpsecGatewayMaintenanceWindow>;
    /**
     * [string] The name of the IPSec Gateway.
     */
    name?: pulumi.Input<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    tier?: pulumi.Input<string>;
    /**
     * [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
     * values: `IKEv2`.
     */
    version?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IpsecGateway resource.
 */
export interface IpsecGatewayArgs {
    /**
     * [list] The network connection for your gateway. **Note**: all connections must belong to the
     * same datacenter. Minimum items: 1. Maximum items: 10.
     */
    connections: pulumi.Input<pulumi.Input<inputs.vpn.IpsecGatewayConnection>[]>;
    /**
     * [string] The human-readable description of the IPSec Gateway.
     */
    description?: pulumi.Input<string>;
    /**
     * [string] Public IP address to be assigned to the gateway. Note: This must be an IP address in
     * the same datacenter as the connections.
     */
    gatewayIp: pulumi.Input<string>;
    /**
     * [string] The location of the IPSec Gateway. Supported locations: de/fra, de/txl, es/vit,
     * gb/bhx, gb/lhr, us/ewr, us/las, us/mci, fr/par.
     */
    location?: pulumi.Input<string>;
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     */
    maintenanceWindow?: pulumi.Input<inputs.vpn.IpsecGatewayMaintenanceWindow>;
    /**
     * [string] The name of the IPSec Gateway.
     */
    name?: pulumi.Input<string>;
    /**
     * (Computed)[string] Gateway performance options.  See product documentation for full details. Options: STANDARD, STANDARD_HA, ENHANCED, ENHANCED_HA, PREMIUM, PREMIUM_HA.
     */
    tier?: pulumi.Input<string>;
    /**
     * [string] The IKE version that is permitted for the VPN tunnels. Default: `IKEv2`. Possible
     * values: `IKEv2`.
     */
    version?: pulumi.Input<string>;
}
