// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a **Certificate** on IonosCloud.
 *
 * ## Import
 *
 * Resource certificate can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:cert/certificate:Certificate mycert certificate uuid
 * ```
 */
export class Certificate extends pulumi.CustomResource {
    /**
     * Get an existing Certificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertificateState, opts?: pulumi.CustomResourceOptions): Certificate {
        return new Certificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:cert/certificate:Certificate';

    /**
     * Returns true if the given object is an instance of Certificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Certificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Certificate.__pulumiType;
    }

    /**
     * [string] The certificate body. Pem encoded. Immutable.
     */
    public readonly certificate!: pulumi.Output<string>;
    /**
     * [string] The certificate chain. Pem encoded. Immutable.
     */
    public readonly certificateChain!: pulumi.Output<string | undefined>;
    /**
     * [string] The certificate name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] The certificate private key. Immutable. Sensitive.
     */
    public readonly privateKey!: pulumi.Output<string>;

    /**
     * Create a Certificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CertificateArgs | CertificateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CertificateState | undefined;
            resourceInputs["certificate"] = state ? state.certificate : undefined;
            resourceInputs["certificateChain"] = state ? state.certificateChain : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["privateKey"] = state ? state.privateKey : undefined;
        } else {
            const args = argsOrState as CertificateArgs | undefined;
            if ((!args || args.certificate === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificate'");
            }
            if ((!args || args.privateKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'privateKey'");
            }
            resourceInputs["certificate"] = args ? args.certificate : undefined;
            resourceInputs["certificateChain"] = args ? args.certificateChain : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["privateKey"] = args?.privateKey ? pulumi.secret(args.privateKey) : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["privateKey"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Certificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Certificate resources.
 */
export interface CertificateState {
    /**
     * [string] The certificate body. Pem encoded. Immutable.
     */
    certificate?: pulumi.Input<string>;
    /**
     * [string] The certificate chain. Pem encoded. Immutable.
     */
    certificateChain?: pulumi.Input<string>;
    /**
     * [string] The certificate name
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The certificate private key. Immutable. Sensitive.
     */
    privateKey?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Certificate resource.
 */
export interface CertificateArgs {
    /**
     * [string] The certificate body. Pem encoded. Immutable.
     */
    certificate: pulumi.Input<string>;
    /**
     * [string] The certificate chain. Pem encoded. Immutable.
     */
    certificateChain?: pulumi.Input<string>;
    /**
     * [string] The certificate name
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The certificate private key. Immutable. Sensitive.
     */
    privateKey: pulumi.Input<string>;
}
