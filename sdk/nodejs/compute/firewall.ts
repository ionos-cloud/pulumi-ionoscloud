// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a set of **Firewall Rules** on IonosCloud.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const exampleDatacenter = new ionoscloud.compute.Datacenter("exampleDatacenter", {
 *     location: "us/las",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleIPBlock = new ionoscloud.compute.IPBlock("exampleIPBlock", {
 *     location: exampleDatacenter.location,
 *     size: 2,
 * });
 * const serverImagePassword = new random.RandomPassword("serverImagePassword", {
 *     length: 16,
 *     special: false,
 * });
 * const exampleServer = new ionoscloud.compute.Server("exampleServer", {
 *     datacenterId: exampleDatacenter.id,
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
 * const exampleNic = new ionoscloud.compute.Nic("exampleNic", {
 *     datacenterId: exampleDatacenter.id,
 *     serverId: exampleServer.id,
 *     lan: 2,
 *     dhcp: true,
 *     firewallActive: true,
 * });
 * const exampleFirewall = new ionoscloud.compute.Firewall("exampleFirewall", {
 *     datacenterId: exampleDatacenter.id,
 *     serverId: exampleServer.id,
 *     nicId: exampleNic.id,
 *     protocol: "ICMP",
 *     sourceMac: "00:0a:95:9d:68:16",
 *     sourceIp: exampleIPBlock.ips[0],
 *     targetIp: exampleIPBlock.ips[1],
 *     icmpType: "1",
 *     icmpCode: "8",
 *     type: "INGRESS",
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * Resource Firewall can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/firewall:Firewall myfwrule {datacenter uuid}/{server uuid}/{nic uuid}/{firewall uuid}
 * ```
 */
export class Firewall extends pulumi.CustomResource {
    /**
     * Get an existing Firewall resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FirewallState, opts?: pulumi.CustomResourceOptions): Firewall {
        return new Firewall(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/firewall:Firewall';

    /**
     * Returns true if the given object is an instance of Firewall.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Firewall {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Firewall.__pulumiType;
    }

    /**
     * [string] The Virtual Data Center ID.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
     */
    public readonly icmpCode!: pulumi.Output<string | undefined>;
    /**
     * [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
     */
    public readonly icmpType!: pulumi.Output<string | undefined>;
    /**
     * [string] The name of the firewall rule.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] The NIC ID.
     */
    public readonly nicId!: pulumi.Output<string>;
    /**
     * [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    public readonly portRangeEnd!: pulumi.Output<number | undefined>;
    /**
     * [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    public readonly portRangeStart!: pulumi.Output<number | undefined>;
    /**
     * [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
     */
    public readonly protocol!: pulumi.Output<string>;
    /**
     * [string] The Server ID.
     */
    public readonly serverId!: pulumi.Output<string>;
    /**
     * [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
     */
    public readonly sourceIp!: pulumi.Output<string>;
    /**
     * [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
     */
    public readonly sourceMac!: pulumi.Output<string | undefined>;
    /**
     * [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
     */
    public readonly targetIp!: pulumi.Output<string>;
    /**
     * [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
     */
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a Firewall resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FirewallArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FirewallArgs | FirewallState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FirewallState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["icmpCode"] = state ? state.icmpCode : undefined;
            resourceInputs["icmpType"] = state ? state.icmpType : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nicId"] = state ? state.nicId : undefined;
            resourceInputs["portRangeEnd"] = state ? state.portRangeEnd : undefined;
            resourceInputs["portRangeStart"] = state ? state.portRangeStart : undefined;
            resourceInputs["protocol"] = state ? state.protocol : undefined;
            resourceInputs["serverId"] = state ? state.serverId : undefined;
            resourceInputs["sourceIp"] = state ? state.sourceIp : undefined;
            resourceInputs["sourceMac"] = state ? state.sourceMac : undefined;
            resourceInputs["targetIp"] = state ? state.targetIp : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as FirewallArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.nicId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nicId'");
            }
            if ((!args || args.protocol === undefined) && !opts.urn) {
                throw new Error("Missing required property 'protocol'");
            }
            if ((!args || args.serverId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverId'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["icmpCode"] = args ? args.icmpCode : undefined;
            resourceInputs["icmpType"] = args ? args.icmpType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nicId"] = args ? args.nicId : undefined;
            resourceInputs["portRangeEnd"] = args ? args.portRangeEnd : undefined;
            resourceInputs["portRangeStart"] = args ? args.portRangeStart : undefined;
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["serverId"] = args ? args.serverId : undefined;
            resourceInputs["sourceIp"] = args ? args.sourceIp : undefined;
            resourceInputs["sourceMac"] = args ? args.sourceMac : undefined;
            resourceInputs["targetIp"] = args ? args.targetIp : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const aliasOpts = { aliases: [{ type: "ionoscloud:index/firewall:Firewall" }] };
        opts = pulumi.mergeOptions(opts, aliasOpts);
        super(Firewall.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Firewall resources.
 */
export interface FirewallState {
    /**
     * [string] The Virtual Data Center ID.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
     */
    icmpCode?: pulumi.Input<string>;
    /**
     * [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
     */
    icmpType?: pulumi.Input<string>;
    /**
     * [string] The name of the firewall rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The NIC ID.
     */
    nicId?: pulumi.Input<string>;
    /**
     * [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    portRangeEnd?: pulumi.Input<number>;
    /**
     * [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    portRangeStart?: pulumi.Input<number>;
    /**
     * [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
     */
    protocol?: pulumi.Input<string>;
    /**
     * [string] The Server ID.
     */
    serverId?: pulumi.Input<string>;
    /**
     * [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
     */
    sourceIp?: pulumi.Input<string>;
    /**
     * [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
     */
    sourceMac?: pulumi.Input<string>;
    /**
     * [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
     */
    targetIp?: pulumi.Input<string>;
    /**
     * [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Firewall resource.
 */
export interface FirewallArgs {
    /**
     * [string] The Virtual Data Center ID.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
     */
    icmpCode?: pulumi.Input<string>;
    /**
     * [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
     */
    icmpType?: pulumi.Input<string>;
    /**
     * [string] The name of the firewall rule.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The NIC ID.
     */
    nicId: pulumi.Input<string>;
    /**
     * [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    portRangeEnd?: pulumi.Input<number>;
    /**
     * [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     */
    portRangeStart?: pulumi.Input<number>;
    /**
     * [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
     */
    protocol: pulumi.Input<string>;
    /**
     * [string] The Server ID.
     */
    serverId: pulumi.Input<string>;
    /**
     * [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
     */
    sourceIp?: pulumi.Input<string>;
    /**
     * [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
     */
    sourceMac?: pulumi.Input<string>;
    /**
     * [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
     */
    targetIp?: pulumi.Input<string>;
    /**
     * [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
     */
    type?: pulumi.Input<string>;
}
