// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Manages **IP Failover** groups on IonosCloud.
 *
 * ## Example Usage
 *
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
 *     location: "us/las",
 *     size: 1,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("exampleLan", {
 *     datacenterId: exampleDatacenter.id,
 *     "public": true,
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
 *         ips: [exampleIPBlock.ips[0]],
 *     },
 * });
 * const exampleIpfailover = new ionoscloud.Ipfailover("exampleIpfailover", {
 *     datacenterId: exampleDatacenter.id,
 *     lanId: exampleLan.id,
 *     ip: exampleIPBlock.ips[0],
 *     nicuuid: exampleServer.primaryNic,
 * }, {
 *     dependsOn: [exampleLan],
 * });
 * ```
 *
 * ## A note on multiple NICs on an IP Failover
 *
 * If you want to add a secondary NIC to an IP Failover, follow these steps:
 * 1) Creating NIC A with failover IP on LAN 1
 * 2) Create NIC B unde the same LAN but with a different IP
 * 3) Create the IP Failover on LAN 1 with NIC A and failover IP of NIC A (A becomes now "master", no slaves)
 * 4) Update NIC B IP to be the failover IP ( B becomes now a slave, A remains master)
 *
 * After this you can create a new NIC C, NIC D and so on, in LAN 1, directly with the failover IP.
 *
 * Please check examples for a full example with the above steps.
 *
 * ## Import
 *
 * Resource IpFailover can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:index/ipfailover:Ipfailover myipfailover {datacenter uuid}/{lan uuid}
 * ```
 */
export class Ipfailover extends pulumi.CustomResource {
    /**
     * Get an existing Ipfailover resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpfailoverState, opts?: pulumi.CustomResourceOptions): Ipfailover {
        return new Ipfailover(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/ipfailover:Ipfailover';

    /**
     * Returns true if the given object is an instance of Ipfailover.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ipfailover {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ipfailover.__pulumiType;
    }

    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [string] The reserved IP address to be used in the IP failover group.
     */
    public readonly ip!: pulumi.Output<string>;
    /**
     * [string] The ID of a LAN.
     */
    public readonly lanId!: pulumi.Output<string>;
    /**
     * The UUID of the master NIC
     */
    public readonly nicuuid!: pulumi.Output<string>;

    /**
     * Create a Ipfailover resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpfailoverArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpfailoverArgs | IpfailoverState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as IpfailoverState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["ip"] = state ? state.ip : undefined;
            resourceInputs["lanId"] = state ? state.lanId : undefined;
            resourceInputs["nicuuid"] = state ? state.nicuuid : undefined;
        } else {
            const args = argsOrState as IpfailoverArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.ip === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ip'");
            }
            if ((!args || args.lanId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lanId'");
            }
            if ((!args || args.nicuuid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nicuuid'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["ip"] = args ? args.ip : undefined;
            resourceInputs["lanId"] = args ? args.lanId : undefined;
            resourceInputs["nicuuid"] = args ? args.nicuuid : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Ipfailover.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Ipfailover resources.
 */
export interface IpfailoverState {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [string] The reserved IP address to be used in the IP failover group.
     */
    ip?: pulumi.Input<string>;
    /**
     * [string] The ID of a LAN.
     */
    lanId?: pulumi.Input<string>;
    /**
     * The UUID of the master NIC
     */
    nicuuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Ipfailover resource.
 */
export interface IpfailoverArgs {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [string] The reserved IP address to be used in the IP failover group.
     */
    ip: pulumi.Input<string>;
    /**
     * [string] The ID of a LAN.
     */
    lanId: pulumi.Input<string>;
    /**
     * The UUID of the master NIC
     */
    nicuuid: pulumi.Input<string>;
}
