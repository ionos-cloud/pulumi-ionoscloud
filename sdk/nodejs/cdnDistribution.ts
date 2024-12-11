// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Manages a **CDN Distribution** on IonosCloud.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as fs from "fs";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * //optionally you can add a certificate to the distribution
 * const cert = new ionoscloud.cert.Certificate("cert", {
 *     certificate: fs.readFileSync("path_to_cert", "utf8"),
 *     certificateChain: fs.readFileSync("path_to_cert_chain", "utf8"),
 *     privateKey: fs.readFileSync("path_to_private_key", "utf8"),
 * });
 * const example = new ionoscloud.CdnDistribution("example", {
 *     domain: "example.com",
 *     certificateId: cert.id,
 *     routingRules: [
 *         {
 *             scheme: "https",
 *             prefix: "/api",
 *             upstream: {
 *                 host: "server.example.com",
 *                 caching: true,
 *                 waf: true,
 *                 sniMode: "distribution",
 *                 rateLimitClass: "R500",
 *                 geoRestrictions: {
 *                     allowLists: [
 *                         "CN",
 *                         "RU",
 *                     ],
 *                 },
 *             },
 *         },
 *         {
 *             scheme: "http/https",
 *             prefix: "/api2",
 *             upstream: {
 *                 host: "server2.example.com",
 *                 caching: false,
 *                 waf: false,
 *                 sniMode: "origin",
 *                 rateLimitClass: "R10",
 *                 geoRestrictions: {
 *                     blockLists: [
 *                         "CN",
 *                         "RU",
 *                     ],
 *                 },
 *             },
 *         },
 *     ],
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * Resource Distribution can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:index/cdnDistribution:CdnDistribution myDistribution {distribution uuid}
 * ```
 */
export class CdnDistribution extends pulumi.CustomResource {
    /**
     * Get an existing CdnDistribution resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CdnDistributionState, opts?: pulumi.CustomResourceOptions): CdnDistribution {
        return new CdnDistribution(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/cdnDistribution:CdnDistribution';

    /**
     * Returns true if the given object is an instance of CdnDistribution.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is CdnDistribution {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === CdnDistribution.__pulumiType;
    }

    /**
     * [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     */
    public readonly certificateId!: pulumi.Output<string | undefined>;
    /**
     * [string] The domain of the distribution.
     */
    public readonly domain!: pulumi.Output<string>;
    /**
     * IP of the distribution, it has to be included on the domain DNS Zone as A record.
     */
    public /*out*/ readonly publicEndpointV4!: pulumi.Output<string>;
    /**
     * IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
     */
    public /*out*/ readonly publicEndpointV6!: pulumi.Output<string>;
    /**
     * Unique resource indentifier.
     */
    public /*out*/ readonly resourceUrn!: pulumi.Output<string>;
    /**
     * [list] The routing rules for the distribution.
     */
    public readonly routingRules!: pulumi.Output<outputs.CdnDistributionRoutingRule[]>;

    /**
     * Create a CdnDistribution resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CdnDistributionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CdnDistributionArgs | CdnDistributionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CdnDistributionState | undefined;
            resourceInputs["certificateId"] = state ? state.certificateId : undefined;
            resourceInputs["domain"] = state ? state.domain : undefined;
            resourceInputs["publicEndpointV4"] = state ? state.publicEndpointV4 : undefined;
            resourceInputs["publicEndpointV6"] = state ? state.publicEndpointV6 : undefined;
            resourceInputs["resourceUrn"] = state ? state.resourceUrn : undefined;
            resourceInputs["routingRules"] = state ? state.routingRules : undefined;
        } else {
            const args = argsOrState as CdnDistributionArgs | undefined;
            if ((!args || args.domain === undefined) && !opts.urn) {
                throw new Error("Missing required property 'domain'");
            }
            if ((!args || args.routingRules === undefined) && !opts.urn) {
                throw new Error("Missing required property 'routingRules'");
            }
            resourceInputs["certificateId"] = args ? args.certificateId : undefined;
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["routingRules"] = args ? args.routingRules : undefined;
            resourceInputs["publicEndpointV4"] = undefined /*out*/;
            resourceInputs["publicEndpointV6"] = undefined /*out*/;
            resourceInputs["resourceUrn"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(CdnDistribution.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering CdnDistribution resources.
 */
export interface CdnDistributionState {
    /**
     * [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     */
    certificateId?: pulumi.Input<string>;
    /**
     * [string] The domain of the distribution.
     */
    domain?: pulumi.Input<string>;
    /**
     * IP of the distribution, it has to be included on the domain DNS Zone as A record.
     */
    publicEndpointV4?: pulumi.Input<string>;
    /**
     * IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
     */
    publicEndpointV6?: pulumi.Input<string>;
    /**
     * Unique resource indentifier.
     */
    resourceUrn?: pulumi.Input<string>;
    /**
     * [list] The routing rules for the distribution.
     */
    routingRules?: pulumi.Input<pulumi.Input<inputs.CdnDistributionRoutingRule>[]>;
}

/**
 * The set of arguments for constructing a CdnDistribution resource.
 */
export interface CdnDistributionArgs {
    /**
     * [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     */
    certificateId?: pulumi.Input<string>;
    /**
     * [string] The domain of the distribution.
     */
    domain: pulumi.Input<string>;
    /**
     * [list] The routing rules for the distribution.
     */
    routingRules: pulumi.Input<pulumi.Input<inputs.CdnDistributionRoutingRule>[]>;
}
