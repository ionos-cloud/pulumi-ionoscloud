// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class AutoCertificateProvider extends pulumi.CustomResource {
    /**
     * Get an existing AutoCertificateProvider resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AutoCertificateProviderState, opts?: pulumi.CustomResourceOptions): AutoCertificateProvider {
        return new AutoCertificateProvider(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:index/autoCertificateProvider:AutoCertificateProvider';

    /**
     * Returns true if the given object is an instance of AutoCertificateProvider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AutoCertificateProvider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AutoCertificateProvider.__pulumiType;
    }

    /**
     * The email address of the certificate requester
     */
    public readonly email!: pulumi.Output<string>;
    public readonly externalAccountBinding!: pulumi.Output<outputs.AutoCertificateProviderExternalAccountBinding | undefined>;
    /**
     * The location of the certificate provider
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * The name of the certificate provider
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The URL of the certificate provider
     */
    public readonly server!: pulumi.Output<string>;

    /**
     * Create a AutoCertificateProvider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AutoCertificateProviderArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AutoCertificateProviderArgs | AutoCertificateProviderState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AutoCertificateProviderState | undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["externalAccountBinding"] = state ? state.externalAccountBinding : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["server"] = state ? state.server : undefined;
        } else {
            const args = argsOrState as AutoCertificateProviderArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            if ((!args || args.server === undefined) && !opts.urn) {
                throw new Error("Missing required property 'server'");
            }
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["externalAccountBinding"] = args ? args.externalAccountBinding : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["server"] = args ? args.server : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AutoCertificateProvider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AutoCertificateProvider resources.
 */
export interface AutoCertificateProviderState {
    /**
     * The email address of the certificate requester
     */
    email?: pulumi.Input<string>;
    externalAccountBinding?: pulumi.Input<inputs.AutoCertificateProviderExternalAccountBinding>;
    /**
     * The location of the certificate provider
     */
    location?: pulumi.Input<string>;
    /**
     * The name of the certificate provider
     */
    name?: pulumi.Input<string>;
    /**
     * The URL of the certificate provider
     */
    server?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AutoCertificateProvider resource.
 */
export interface AutoCertificateProviderArgs {
    /**
     * The email address of the certificate requester
     */
    email: pulumi.Input<string>;
    externalAccountBinding?: pulumi.Input<inputs.AutoCertificateProviderExternalAccountBinding>;
    /**
     * The location of the certificate provider
     */
    location: pulumi.Input<string>;
    /**
     * The name of the certificate provider
     */
    name?: pulumi.Input<string>;
    /**
     * The URL of the certificate provider
     */
    server: pulumi.Input<string>;
}
