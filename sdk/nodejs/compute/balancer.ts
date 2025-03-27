// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a Load Balancer on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
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
 *     name: "Lan Example",
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
 * const exampleBalancer = new ionoscloud.compute.Balancer("example", {
 *     datacenterId: example.id,
 *     nicIds: [exampleServer.primaryNic],
 *     name: "Load Balancer Example",
 *     dhcp: true,
 * });
 * ```
 *
 * ## A note on nics
 *
 * When declaring NIC resources to be used with the load balancer, please make sure
 * you use the "lifecycle meta-argument" to make sure changes to the lan attribute
 * of the nic are ignored.
 *
 * Please see the Nic resource's documentation for an example on how to do that.
 *
 * ## Import
 *
 * Resource Load Balancer can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/balancer:Balancer myloadbalancer datacenter uuid/loadbalancer uuid
 * ```
 */
export class Balancer extends pulumi.CustomResource {
    /**
     * Get an existing Balancer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BalancerState, opts?: pulumi.CustomResourceOptions): Balancer {
        return new Balancer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/balancer:Balancer';

    /**
     * Returns true if the given object is an instance of Balancer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Balancer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Balancer.__pulumiType;
    }

    /**
     * [string] The ID of a Virtual Data Center.
     */
    public readonly datacenterId!: pulumi.Output<string>;
    /**
     * [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
     */
    public readonly dhcp!: pulumi.Output<boolean | undefined>;
    /**
     * [string] IPv4 address of the load balancer.
     */
    public readonly ip!: pulumi.Output<string>;
    /**
     * [string] The name of the load balancer.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [list] A list of NIC IDs that are part of the load balancer.
     */
    public readonly nicIds!: pulumi.Output<string[]>;

    /**
     * Create a Balancer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BalancerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BalancerArgs | BalancerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BalancerState | undefined;
            resourceInputs["datacenterId"] = state ? state.datacenterId : undefined;
            resourceInputs["dhcp"] = state ? state.dhcp : undefined;
            resourceInputs["ip"] = state ? state.ip : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["nicIds"] = state ? state.nicIds : undefined;
        } else {
            const args = argsOrState as BalancerArgs | undefined;
            if ((!args || args.datacenterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'datacenterId'");
            }
            if ((!args || args.nicIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'nicIds'");
            }
            resourceInputs["datacenterId"] = args ? args.datacenterId : undefined;
            resourceInputs["dhcp"] = args ? args.dhcp : undefined;
            resourceInputs["ip"] = args ? args.ip : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["nicIds"] = args ? args.nicIds : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Balancer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Balancer resources.
 */
export interface BalancerState {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId?: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * [string] IPv4 address of the load balancer.
     */
    ip?: pulumi.Input<string>;
    /**
     * [string] The name of the load balancer.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] A list of NIC IDs that are part of the load balancer.
     */
    nicIds?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Balancer resource.
 */
export interface BalancerArgs {
    /**
     * [string] The ID of a Virtual Data Center.
     */
    datacenterId: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if the load balancer will reserve an IP using DHCP.
     */
    dhcp?: pulumi.Input<boolean>;
    /**
     * [string] IPv4 address of the load balancer.
     */
    ip?: pulumi.Input<string>;
    /**
     * [string] The name of the load balancer.
     */
    name?: pulumi.Input<string>;
    /**
     * [list] A list of NIC IDs that are part of the load balancer.
     */
    nicIds: pulumi.Input<pulumi.Input<string>[]>;
}
