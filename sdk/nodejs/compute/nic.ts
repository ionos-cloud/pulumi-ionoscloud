// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **NIC** on IonosCloud.
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleIPBlock = new ionoscloud.compute.IPBlock("example", {
 *     location: example.location,
 *     size: 2,
 *     name: "IP Block Example",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "Lan",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Server Example",
 *     datacenterId: example.id,
 *     cores: 1,
 *     ram: 1024,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_XEON",
 *     imageName: "Ubuntu-20.04",
 *     imagePassword: serverImagePassword.result,
 *     volume: {
 *         name: "system",
 *         size: 14,
 *         diskType: "SSD",
 *     },
 *     nic: {
 *         lan: 1,
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleNic = new ionoscloud.compute.Nic("example", {
 *     datacenterId: example.id,
 *     serverId: exampleServer.id,
 *     lan: exampleLan.id,
 *     name: "NIC",
 *     dhcp: true,
 *     firewallActive: true,
 *     firewallType: "INGRESS",
 *     ips: [
 *         exampleIPBlock.ips[0],
 *         exampleIPBlock.ips[1],
 *     ],
 * });
 * ```
 *
 * ### With IPv6
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "IPv6 Enabled LAN",
 *     ipv6CidrBlock: "ipv6_cidr_block_from_dc",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Server Example",
 *     datacenterId: example.id,
 *     cores: 1,
 *     ram: 1024,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_XEON",
 *     imageName: "Ubuntu-20.04",
 *     imagePassword: serverImagePassword.result,
 *     volume: {
 *         name: "system",
 *         size: 14,
 *         diskType: "SSD",
 *     },
 *     nic: {
 *         lan: 1,
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleNic = new ionoscloud.compute.Nic("example", {
 *     datacenterId: example.id,
 *     serverId: exampleServer.id,
 *     lan: exampleLan.id,
 *     name: "IPv6 Enabled NIC",
 *     dhcp: true,
 *     firewallActive: true,
 *     firewallType: "INGRESS",
 *     dhcpv6: false,
 *     ipv6CidrBlock: "ipv6_cidr_block_from_lan",
 *     ipv6Ips: [
 *         "ipv6_ip1",
 *         "ipv6_ip2",
 *         "ipv6_ip3",
 *     ],
 * });
 * ```
 * ## Example configuring Flowlog
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "IPv6 Enabled LAN",
 *     ipv6CidrBlock: "ipv6_cidr_block_from_dc",
 * });
 * const serverImagePassword = new random.index.Password("server_image_password", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("example", {
 *     name: "Server Example",
 *     datacenterId: example.id,
 *     cores: 1,
 *     ram: 1024,
 *     availabilityZone: "ZONE_1",
 *     cpuFamily: "INTEL_XEON",
 *     imageName: "Ubuntu-20.04",
 *     imagePassword: serverImagePassword.result,
 *     volume: {
 *         name: "system",
 *         size: 14,
 *         diskType: "SSD",
 *     },
 *     nic: {
 *         lan: 1,
 *         dhcp: true,
 *         firewallActive: true,
 *     },
 * });
 * const exampleNic = new ionoscloud.compute.Nic("example", {
 *     datacenterId: example.id,
 *     serverId: exampleServer.id,
 *     lan: exampleLan.id,
 *     name: "IPV6 and Flowlog Enabled NIC",
 *     dhcp: true,
 *     firewallActive: true,
 *     firewallType: "INGRESS",
 *     dhcpv6: false,
 *     ipv6CidrBlock: "ipv6_cidr_block_from_lan",
 *     ipv6Ips: [
 *         "ipv6_ip1",
 *         "ipv6_ip2",
 *         "ipv6_ip3",
 *     ],
 *     flowlog: {
 *         action: "ACCEPTED",
 *         bucket: "flowlog-bucket",
 *         direction: "INGRESS",
 *         name: "flowlog",
 *     },
 * });
 * ```
 *
 * This will configure flowlog for accepted ingress traffic and will log it into an existing IONOS Object Storage bucket named `flowlog-bucket`. Any s3 compatible client can be used to create it. Adding a flowlog does not force re-creation of the NIC, but changing any other field than
 * `name` will. Deleting a flowlog will also force NIC re-creation.
 *
 * ## Working with load balancers
 *
 * Please be aware that when using a NIC in a load balancer, the load balancer will
 * change the NIC's ID behind the scenes, therefore the plan will always report this change
 * trying to revert the state to the one specified by your file.
 * In order to prevent this, use the "lifecycle meta-argument" when declaring your NIC,
 * in order to ignore changes to the `lan` attribute:
 *
 * Here's an example:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * const example = new ionoscloud.compute.Nic("example", {
 *     datacenterId: foobar.id,
 *     serverId: exampleIonoscloudServer.id,
 *     lan: 2,
 *     dhcp: true,
 *     firewallActive: true,
 *     name: "updated",
 * });
 * ```
 *
 * ## Import
 *
 * Resource **Nic** can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/nic:Nic mynic datacenter uuid/server uuid/nic uuid
 * ```
 */
export class Nic extends pulumi.CustomResource {
    /**
     * Get an existing Nic resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NicState, opts?: pulumi.CustomResourceOptions): Nic {
        return new Nic(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/nic:Nic';

    /**
     * Returns true if the given object is an instance of Nic.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Nic {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Nic.__pulumiType;
    }

    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * The Logical Unit Number (LUN) of the storage volume. Null if this NIC was created from CloudAPI and no DCD changes were done on the Datacenter.
     */
    public /*out*/ readonly deviceNumber!: pulumi.Output<number>;
    /**
     * [Boolean] Indicates if the NIC should get an IP address using DHCP (true) or not (false).
     */
    public readonly dhcp!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] Indicates if the NIC should get an IPv6 address using DHCP (true) or not (false).
     */
    public readonly dhcpv6!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
     */
    public readonly firewallActive!: pulumi.Output<boolean | undefined>;
    /**
     * [String] The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
     */
    public readonly firewallType!: pulumi.Output<string>;
    /**
     * Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     */
    public readonly flowlog!: pulumi.Output<outputs.compute.NicFlowlog | undefined>;
    /**
     * [list] Collection of IP addresses assigned to a NIC. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     */
    public readonly ips!: pulumi.Output<string[]>;
    /**
     * Automatically assigned /80 IPv6 CIDR block if the NIC is connected to an IPv6 enabled LAN. You can also specify an /80 IPv6 CIDR block for the NIC on your own, which must be inside the /64 IPv6 CIDR block of the LAN and unique.
     */
    public readonly ipv6CidrBlock!: pulumi.Output<string>;
    /**
     * [list] Collection of IPv6 addresses assigned to a NIC. Explicitly assigned public IPs need to come from the NIC's Ipv6 CIDR block, Passing value null or empty array will assign an IPv6 address automatically from the NIC's CIDR block.
     */
    public readonly ipv6Ips!: pulumi.Output<string[]>;
    /**
     * [integer] The LAN ID the NIC will sit on.
     */
    public readonly lan!: pulumi.Output<number>;
    /**
     * The MAC address of the NIC. Can be set on creation only. If not set, one will be assigned automatically by the API. Immutable, update forces re-creation.
     */
    public readonly mac!: pulumi.Output<string>;
    /**
     * [string] The name of the LAN.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The PCI slot number of the Nic.
     */
    public /*out*/ readonly pciSlot!: pulumi.Output<number>;
    /**
     * The list of Security Group IDs for the resource. 
     *
     * ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the NIC resource.
     */
    public readonly securityGroupsIds!: pulumi.Output<string[] | undefined>;
    /**
     * [string] The ID of a server.
     */
    public readonly serverId!: pulumi.Output<string>;

    /**
     * Create a Nic resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NicArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NicArgs | NicState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as NicState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["deviceNumber"] = state ? state.deviceNumber : undefined;
            resourceInputs["dhcp"] = state ? state.dhcp : undefined;
            resourceInputs["dhcpv6"] = state ? state.dhcpv6 : undefined;
            resourceInputs["firewallActive"] = state ? state.firewallActive : undefined;
            resourceInputs["firewallType"] = state ? state.firewallType : undefined;
            resourceInputs["flowlog"] = state ? state.flowlog : undefined;
            resourceInputs["ips"] = state ? state.ips : undefined;
            resourceInputs["ipv6CidrBlock"] = state ? state.ipv6CidrBlock : undefined;
            resourceInputs["ipv6Ips"] = state ? state.ipv6Ips : undefined;
            resourceInputs["lan"] = state ? state.lan : undefined;
            resourceInputs["mac"] = state ? state.mac : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["pciSlot"] = state ? state.pciSlot : undefined;
            resourceInputs["securityGroupsIds"] = state ? state.securityGroupsIds : undefined;
            resourceInputs["serverId"] = state ? state.serverId : undefined;
        } else {
            const args = argsOrState as NicArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.lan === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lan'");
            }
            if ((!args || args.serverId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverId'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["dhcp"] = args ? args.dhcp : undefined;
            resourceInputs["dhcpv6"] = args ? args.dhcpv6 : undefined;
            resourceInputs["firewallActive"] = args ? args.firewallActive : undefined;
            resourceInputs["firewallType"] = args ? args.firewallType : undefined;
            resourceInputs["flowlog"] = args ? args.flowlog : undefined;
            resourceInputs["ips"] = args ? args.ips : undefined;
            resourceInputs["ipv6CidrBlock"] = args ? args.ipv6CidrBlock : undefined;
            resourceInputs["ipv6Ips"] = args ? args.ipv6Ips : undefined;
            resourceInputs["lan"] = args ? args.lan : undefined;
            resourceInputs["mac"] = args ? args.mac : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["securityGroupsIds"] = args ? args.securityGroupsIds : undefined;
            resourceInputs["serverId"] = args ? args.serverId : undefined;
            resourceInputs["deviceNumber"] = undefined /*out*/;
            resourceInputs["pciSlot"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Nic.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Nic resources.
 */
export interface NicState {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * The Logical Unit Number (LUN) of the storage volume. Null if this NIC was created from CloudAPI and no DCD changes were done on the Datacenter.
     */
    deviceNumber?: pulumi.Input<number>;
    /**
     * [Boolean] Indicates if the NIC should get an IP address using DHCP (true) or not (false).
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * [Boolean] Indicates if the NIC should get an IPv6 address using DHCP (true) or not (false).
     */
    dhcpv6?: pulumi.Input<boolean>;
    /**
     * [Boolean] If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
     */
    firewallActive?: pulumi.Input<boolean>;
    /**
     * [String] The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
     */
    firewallType?: pulumi.Input<string>;
    /**
     * Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     */
    flowlog?: pulumi.Input<inputs.compute.NicFlowlog>;
    /**
     * [list] Collection of IP addresses assigned to a NIC. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     */
    ips?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Automatically assigned /80 IPv6 CIDR block if the NIC is connected to an IPv6 enabled LAN. You can also specify an /80 IPv6 CIDR block for the NIC on your own, which must be inside the /64 IPv6 CIDR block of the LAN and unique.
     */
    ipv6CidrBlock?: pulumi.Input<string>;
    /**
     * [list] Collection of IPv6 addresses assigned to a NIC. Explicitly assigned public IPs need to come from the NIC's Ipv6 CIDR block, Passing value null or empty array will assign an IPv6 address automatically from the NIC's CIDR block.
     */
    ipv6Ips?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [integer] The LAN ID the NIC will sit on.
     */
    lan?: pulumi.Input<number>;
    /**
     * The MAC address of the NIC. Can be set on creation only. If not set, one will be assigned automatically by the API. Immutable, update forces re-creation.
     */
    mac?: pulumi.Input<string>;
    /**
     * [string] The name of the LAN.
     */
    name?: pulumi.Input<string>;
    /**
     * The PCI slot number of the Nic.
     */
    pciSlot?: pulumi.Input<number>;
    /**
     * The list of Security Group IDs for the resource. 
     *
     * ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the NIC resource.
     */
    securityGroupsIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The ID of a server.
     */
    serverId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Nic resource.
 */
export interface NicArgs {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if the NIC should get an IP address using DHCP (true) or not (false).
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * [Boolean] Indicates if the NIC should get an IPv6 address using DHCP (true) or not (false).
     */
    dhcpv6?: pulumi.Input<boolean>;
    /**
     * [Boolean] If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
     */
    firewallActive?: pulumi.Input<boolean>;
    /**
     * [String] The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
     */
    firewallType?: pulumi.Input<string>;
    /**
     * Only 1 flow log can be configured. Only the name field can change as part of an update. Flow logs holistically capture network information such as source and destination IP addresses, source and destination ports, number of packets, amount of bytes, the start and end time of the recording, and the type of protocol – and log the extent to which your instances are being accessed.
     */
    flowlog?: pulumi.Input<inputs.compute.NicFlowlog>;
    /**
     * [list] Collection of IP addresses assigned to a NIC. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     */
    ips?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Automatically assigned /80 IPv6 CIDR block if the NIC is connected to an IPv6 enabled LAN. You can also specify an /80 IPv6 CIDR block for the NIC on your own, which must be inside the /64 IPv6 CIDR block of the LAN and unique.
     */
    ipv6CidrBlock?: pulumi.Input<string>;
    /**
     * [list] Collection of IPv6 addresses assigned to a NIC. Explicitly assigned public IPs need to come from the NIC's Ipv6 CIDR block, Passing value null or empty array will assign an IPv6 address automatically from the NIC's CIDR block.
     */
    ipv6Ips?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [integer] The LAN ID the NIC will sit on.
     */
    lan: pulumi.Input<number>;
    /**
     * The MAC address of the NIC. Can be set on creation only. If not set, one will be assigned automatically by the API. Immutable, update forces re-creation.
     */
    mac?: pulumi.Input<string>;
    /**
     * [string] The name of the LAN.
     */
    name?: pulumi.Input<string>;
    /**
     * The list of Security Group IDs for the resource. 
     *
     * ⚠️ **Note:**: Removing the `flowlog` forces re-creation of the NIC resource.
     */
    securityGroupsIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] The ID of a server.
     */
    serverId: pulumi.Input<string>;
}
