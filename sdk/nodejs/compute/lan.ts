// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages a **LAN** on IonosCloud.
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
 * const exampleCrossconnect = new ionoscloud.compute.Crossconnect("example", {
 *     name: "Cross Connect Example",
 *     description: "Cross Connect Description",
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": false,
 *     name: "Lan Example",
 *     pcc: exampleCrossconnect.id,
 * });
 * ```
 *
 * ### With IPv6 Enabled
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * const example = new ionoscloud.compute.Datacenter("example", {
 *     name: "Datacenter Example",
 *     location: "de/txl",
 *     description: "Datacenter Description",
 *     secAuthProtection: false,
 * });
 * const exampleLan = new ionoscloud.compute.Lan("example", {
 *     datacenterId: example.id,
 *     "public": true,
 *     name: "Lan IPv6 Example",
 *     ipv6CidrBlock: "AUTO",
 * });
 * ```
 *
 * ## Important Notes
 *
 * - Please note that only LANs datacenters found in the same physical location can be connected through a Cross-connect
 * - A LAN cannot be a part of two Cross-connects
 *
 * ## Import
 *
 * Resource Lan can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/lan:Lan mylandatacenter uuid/lan id
 * ```
 */
export class Lan extends pulumi.CustomResource {
    /**
     * Get an existing Lan resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LanState, opts?: pulumi.CustomResourceOptions): Lan {
        return new Lan(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/lan:Lan';

    /**
     * Returns true if the given object is an instance of Lan.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Lan {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Lan.__pulumiType;
    }

    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * IP failover configurations for lan
     */
    public readonly ipFailovers!: pulumi.Output<outputs.compute.LanIpFailover[]>;
    /**
     * [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
     */
    public /*out*/ readonly ipv4CidrBlock!: pulumi.Output<string>;
    /**
     * Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
     */
    public readonly ipv6CidrBlock!: pulumi.Output<string>;
    /**
     * [string] The name of the LAN.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [String] The unique id of a `ionoscloud.compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
     */
    public readonly pcc!: pulumi.Output<string | undefined>;
    /**
     * [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
     */
    public readonly public!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Lan resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LanArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LanArgs | LanState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LanState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["ipFailovers"] = state ? state.ipFailovers : undefined;
            resourceInputs["ipv4CidrBlock"] = state ? state.ipv4CidrBlock : undefined;
            resourceInputs["ipv6CidrBlock"] = state ? state.ipv6CidrBlock : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["pcc"] = state ? state.pcc : undefined;
            resourceInputs["public"] = state ? state.public : undefined;
        } else {
            const args = argsOrState as LanArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["ipFailovers"] = args ? args.ipFailovers : undefined;
            resourceInputs["ipv6CidrBlock"] = args ? args.ipv6CidrBlock : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["pcc"] = args ? args.pcc : undefined;
            resourceInputs["public"] = args ? args.public : undefined;
            resourceInputs["ipv4CidrBlock"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Lan.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Lan resources.
 */
export interface LanState {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * IP failover configurations for lan
     */
    ipFailovers?: pulumi.Input<pulumi.Input<inputs.compute.LanIpFailover>[]>;
    /**
     * [String] For public LANs this property is null, for private LANs it contains the private IPv4 CIDR range. This property is a read only property.
     */
    ipv4CidrBlock?: pulumi.Input<string>;
    /**
     * Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
     */
    ipv6CidrBlock?: pulumi.Input<string>;
    /**
     * [string] The name of the LAN.
     */
    name?: pulumi.Input<string>;
    /**
     * [String] The unique id of a `ionoscloud.compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
     */
    pcc?: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
     */
    public?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a Lan resource.
 */
export interface LanArgs {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * IP failover configurations for lan
     */
    ipFailovers?: pulumi.Input<pulumi.Input<inputs.compute.LanIpFailover>[]>;
    /**
     * Contains the LAN's /64 IPv6 CIDR block if this LAN is IPv6 enabled. 'AUTO' will result in enabling this LAN for IPv6 and automatically assign a /64 IPv6 CIDR block to this LAN. If you specify your own IPv6 CIDR block then you must provide a unique /64 block, which is inside the IPv6 CIDR block of the virtual datacenter and unique inside all LANs from this virtual datacenter.
     */
    ipv6CidrBlock?: pulumi.Input<string>;
    /**
     * [string] The name of the LAN.
     */
    name?: pulumi.Input<string>;
    /**
     * [String] The unique id of a `ionoscloud.compute.Crossconnect` resource, in order. It needs to be ensured that IP addresses of the NICs of all LANs connected to a given Cross Connect is not duplicated and belongs to the same subnet range
     */
    pcc?: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if the LAN faces the public Internet (true) or not (false).
     */
    public?: pulumi.Input<boolean>;
}
