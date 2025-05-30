// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * An IPSec Gateway Tunnel resource manages the creation, management, and deletion of VPN IPSec Gateway Tunnels within the
 * IONOS Cloud infrastructure. This resource facilitates the creation of VPN IPSec Gateway Tunnels, enabling secure
 * connections between your network resources.
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
 * const exampleIpsecTunnel = new ionoscloud.vpn.IpsecTunnel("example", {
 *     location: "de/fra",
 *     gatewayId: example.id,
 *     name: "example-tunnel",
 *     remoteHost: "vpn.mycompany.com",
 *     description: "Allows local subnet X to connect to virtual network Y.",
 *     auth: {
 *         method: "PSK",
 *         pskKey: "X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
 *     },
 *     ike: {
 *         diffieHellmanGroup: "16-MODP4096",
 *         encryptionAlgorithm: "AES256",
 *         integrityAlgorithm: "SHA256",
 *         lifetime: 86400,
 *     },
 *     esps: [{
 *         diffieHellmanGroup: "16-MODP4096",
 *         encryptionAlgorithm: "AES256",
 *         integrityAlgorithm: "SHA256",
 *         lifetime: 3600,
 *     }],
 *     cloudNetworkCidrs: ["0.0.0.0/0"],
 *     peerNetworkCidrs: ["1.2.3.4/32"],
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
 * });
 * const exampleIpsecTunnel = new ionoscloud.vpn.IpsecTunnel("example", {
 *     location: "de/fra",
 *     gatewayId: example.id,
 *     name: "example-tunnel",
 *     remoteHost: "vpn.mycompany.com",
 *     description: "Allows local subnet X to connect to virtual network Y.",
 *     auth: {
 *         method: "PSK",
 *         pskKey: "X2wosbaw74M8hQGbK3jCCaEusR6CCFRa",
 *     },
 *     ike: {
 *         diffieHellmanGroup: "16-MODP4096",
 *         encryptionAlgorithm: "AES256",
 *         integrityAlgorithm: "SHA256",
 *         lifetime: 86400,
 *     },
 *     esps: [{
 *         diffieHellmanGroup: "16-MODP4096",
 *         encryptionAlgorithm: "AES256",
 *         integrityAlgorithm: "SHA256",
 *         lifetime: 3600,
 *     }],
 *     cloudNetworkCidrs: ["0.0.0.0/0"],
 *     peerNetworkCidrs: ["1.2.3.4/32"],
 * });
 * ```
 *
 * ## Import
 *
 * The resource can be imported using the `location`, `gateway_id` and `tunnel_id`, for example:
 *
 * ```sh
 * $ pulumi import ionoscloud:vpn/ipsecTunnel:IpsecTunnel example location:gateway_id:tunnel_id
 * ```
 */
export class IpsecTunnel extends pulumi.CustomResource {
    /**
     * Get an existing IpsecTunnel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpsecTunnelState, opts?: pulumi.CustomResourceOptions): IpsecTunnel {
        return new IpsecTunnel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:vpn/ipsecTunnel:IpsecTunnel';

    /**
     * Returns true if the given object is an instance of IpsecTunnel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IpsecTunnel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IpsecTunnel.__pulumiType;
    }

    /**
     * [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
     * items: 1.
     */
    public readonly auth!: pulumi.Output<outputs.vpn.IpsecTunnelAuth>;
    /**
     * [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
     * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
     * Maximum items: 20.
     */
    public readonly cloudNetworkCidrs!: pulumi.Output<string[]>;
    /**
     * [string] The human-readable description of your IPSec Gateway Tunnel.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
     */
    public readonly esps!: pulumi.Output<outputs.vpn.IpsecTunnelEsp[]>;
    /**
     * [string] The ID of the IPSec Gateway that the tunnel belongs to.
     */
    public readonly gatewayId!: pulumi.Output<string>;
    /**
     * [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
     */
    public readonly ike!: pulumi.Output<outputs.vpn.IpsecTunnelIke>;
    /**
     * [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
     * gb/lhr, us/ewr, us/las, us/mci, fr/par
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * [string] The name of the IPSec Gateway Tunnel.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
     * tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
     */
    public readonly peerNetworkCidrs!: pulumi.Output<string[]>;
    /**
     * [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
     */
    public readonly remoteHost!: pulumi.Output<string>;

    /**
     * Create a IpsecTunnel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpsecTunnelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpsecTunnelArgs | IpsecTunnelState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IpsecTunnelState | undefined;
            resourceInputs["auth"] = state ? state.auth : undefined;
            resourceInputs["cloudNetworkCidrs"] = state ? state.cloudNetworkCidrs : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["esps"] = state ? state.esps : undefined;
            resourceInputs["gatewayId"] = state ? state.gatewayId : undefined;
            resourceInputs["ike"] = state ? state.ike : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["peerNetworkCidrs"] = state ? state.peerNetworkCidrs : undefined;
            resourceInputs["remoteHost"] = state ? state.remoteHost : undefined;
        } else {
            const args = argsOrState as IpsecTunnelArgs | undefined;
            if ((!args || args.auth === undefined) && !opts.urn) {
                throw new Error("Missing required property 'auth'");
            }
            if ((!args || args.cloudNetworkCidrs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cloudNetworkCidrs'");
            }
            if ((!args || args.esps === undefined) && !opts.urn) {
                throw new Error("Missing required property 'esps'");
            }
            if ((!args || args.gatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gatewayId'");
            }
            if ((!args || args.ike === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ike'");
            }
            if ((!args || args.peerNetworkCidrs === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerNetworkCidrs'");
            }
            if ((!args || args.remoteHost === undefined) && !opts.urn) {
                throw new Error("Missing required property 'remoteHost'");
            }
            resourceInputs["auth"] = args ? args.auth : undefined;
            resourceInputs["cloudNetworkCidrs"] = args ? args.cloudNetworkCidrs : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["esps"] = args ? args.esps : undefined;
            resourceInputs["gatewayId"] = args ? args.gatewayId : undefined;
            resourceInputs["ike"] = args ? args.ike : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["peerNetworkCidrs"] = args ? args.peerNetworkCidrs : undefined;
            resourceInputs["remoteHost"] = args ? args.remoteHost : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IpsecTunnel.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IpsecTunnel resources.
 */
export interface IpsecTunnelState {
    /**
     * [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
     * items: 1.
     */
    auth?: pulumi.Input<inputs.vpn.IpsecTunnelAuth>;
    /**
     * [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
     * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
     * Maximum items: 20.
     */
    cloudNetworkCidrs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The human-readable description of your IPSec Gateway Tunnel.
     */
    description?: pulumi.Input<string>;
    /**
     * [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
     */
    esps?: pulumi.Input<pulumi.Input<inputs.vpn.IpsecTunnelEsp>[]>;
    /**
     * [string] The ID of the IPSec Gateway that the tunnel belongs to.
     */
    gatewayId?: pulumi.Input<string>;
    /**
     * [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
     */
    ike?: pulumi.Input<inputs.vpn.IpsecTunnelIke>;
    /**
     * [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
     * gb/lhr, us/ewr, us/las, us/mci, fr/par
     */
    location?: pulumi.Input<string>;
    /**
     * [string] The name of the IPSec Gateway Tunnel.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
     * tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
     */
    peerNetworkCidrs?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
     */
    remoteHost?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a IpsecTunnel resource.
 */
export interface IpsecTunnelArgs {
    /**
     * [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
     * items: 1.
     */
    auth: pulumi.Input<inputs.vpn.IpsecTunnelAuth>;
    /**
     * [list] The network CIDRs on the "Left" side that are allowed to connect to the IPSec
     * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1.
     * Maximum items: 20.
     */
    cloudNetworkCidrs: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The human-readable description of your IPSec Gateway Tunnel.
     */
    description?: pulumi.Input<string>;
    /**
     * [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
     */
    esps: pulumi.Input<pulumi.Input<inputs.vpn.IpsecTunnelEsp>[]>;
    /**
     * [string] The ID of the IPSec Gateway that the tunnel belongs to.
     */
    gatewayId: pulumi.Input<string>;
    /**
     * [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
     */
    ike: pulumi.Input<inputs.vpn.IpsecTunnelIke>;
    /**
     * [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
     * gb/lhr, us/ewr, us/las, us/mci, fr/par
     */
    location?: pulumi.Input<string>;
    /**
     * [string] The name of the IPSec Gateway Tunnel.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] The network CIDRs on the "Right" side that are allowed to connect to the IPSec
     * tunnel. Specify "0.0.0.0/0" or "::/0" for all addresses. Minimum items: 1. Maximum items: 20.
     */
    peerNetworkCidrs: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
     */
    remoteHost: pulumi.Input<string>;
}
