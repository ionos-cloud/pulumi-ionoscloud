// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

export class WireguardPeer extends pulumi.CustomResource {
    /**
     * Get an existing WireguardPeer resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WireguardPeerState, opts?: pulumi.CustomResourceOptions): WireguardPeer {
        return new WireguardPeer(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:vpn/wireguardPeer:WireguardPeer';

    /**
     * Returns true if the given object is an instance of WireguardPeer.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WireguardPeer {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WireguardPeer.__pulumiType;
    }

    /**
     * The subnet CIDRs that are allowed to connect to the WireGuard Gateway.
     */
    public readonly allowedIps!: pulumi.Output<string[]>;
    /**
     * Human readable description of the WireGuard Gateway Peer.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Endpoint configuration for the WireGuard Peer.
     */
    public readonly endpoint!: pulumi.Output<outputs.vpn.WireguardPeerEndpoint | undefined>;
    /**
     * The ID of the WireGuard Peer that the peer will connect to.
     */
    public readonly gatewayId!: pulumi.Output<string>;
    /**
     * The location of the WireGuard Peer. Supported locations: de/fra, de/txl, es/vit, gb/bhx, gb/lhr, us/ewr, us/las, us/mci,
     * fr/par
     */
    public readonly location!: pulumi.Output<string | undefined>;
    /**
     * The human readable name of your WireGuard Gateway Peer.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * WireGuard public key of the connecting peer
     */
    public readonly publicKey!: pulumi.Output<string>;
    /**
     * The status of the WireGuard Gateway
     */
    public /*out*/ readonly status!: pulumi.Output<string>;

    /**
     * Create a WireguardPeer resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WireguardPeerArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WireguardPeerArgs | WireguardPeerState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WireguardPeerState | undefined;
            resourceInputs["allowedIps"] = state ? state.allowedIps : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["endpoint"] = state ? state.endpoint : undefined;
            resourceInputs["gatewayId"] = state ? state.gatewayId : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["publicKey"] = state ? state.publicKey : undefined;
            resourceInputs["status"] = state ? state.status : undefined;
        } else {
            const args = argsOrState as WireguardPeerArgs | undefined;
            if ((!args || args.allowedIps === undefined) && !opts.urn) {
                throw new Error("Missing required property 'allowedIps'");
            }
            if ((!args || args.gatewayId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'gatewayId'");
            }
            if ((!args || args.publicKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'publicKey'");
            }
            resourceInputs["allowedIps"] = args ? args.allowedIps : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["gatewayId"] = args ? args.gatewayId : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["publicKey"] = args ? args.publicKey : undefined;
            resourceInputs["status"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(WireguardPeer.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WireguardPeer resources.
 */
export interface WireguardPeerState {
    /**
     * The subnet CIDRs that are allowed to connect to the WireGuard Gateway.
     */
    allowedIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Human readable description of the WireGuard Gateway Peer.
     */
    description?: pulumi.Input<string>;
    /**
     * Endpoint configuration for the WireGuard Peer.
     */
    endpoint?: pulumi.Input<inputs.vpn.WireguardPeerEndpoint>;
    /**
     * The ID of the WireGuard Peer that the peer will connect to.
     */
    gatewayId?: pulumi.Input<string>;
    /**
     * The location of the WireGuard Peer. Supported locations: de/fra, de/txl, es/vit, gb/bhx, gb/lhr, us/ewr, us/las, us/mci,
     * fr/par
     */
    location?: pulumi.Input<string>;
    /**
     * The human readable name of your WireGuard Gateway Peer.
     */
    name?: pulumi.Input<string>;
    /**
     * WireGuard public key of the connecting peer
     */
    publicKey?: pulumi.Input<string>;
    /**
     * The status of the WireGuard Gateway
     */
    status?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WireguardPeer resource.
 */
export interface WireguardPeerArgs {
    /**
     * The subnet CIDRs that are allowed to connect to the WireGuard Gateway.
     */
    allowedIps: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Human readable description of the WireGuard Gateway Peer.
     */
    description?: pulumi.Input<string>;
    /**
     * Endpoint configuration for the WireGuard Peer.
     */
    endpoint?: pulumi.Input<inputs.vpn.WireguardPeerEndpoint>;
    /**
     * The ID of the WireGuard Peer that the peer will connect to.
     */
    gatewayId: pulumi.Input<string>;
    /**
     * The location of the WireGuard Peer. Supported locations: de/fra, de/txl, es/vit, gb/bhx, gb/lhr, us/ewr, us/las, us/mci,
     * fr/par
     */
    location?: pulumi.Input<string>;
    /**
     * The human readable name of your WireGuard Gateway Peer.
     */
    name?: pulumi.Input<string>;
    /**
     * WireGuard public key of the connecting peer
     */
    publicKey: pulumi.Input<string>;
}
