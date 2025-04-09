// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a **CM AutoCertificate**.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 *
 * const example = new ionoscloud.cert.AutoCertificateProvider("example", {
 *     name: "Let's Encrypt",
 *     email: "user@example.com",
 *     location: "de/fra",
 *     server: "https://acme-v02.api.letsencrypt.org/directory",
 *     externalAccountBinding: {
 *         keyId: "some-key-id",
 *         keySecret: "secret",
 *     },
 * });
 * const exampleAutoCertificate = new ionoscloud.cert.AutoCertificate("example", {
 *     providerId: example.id,
 *     commonName: "www.example.com",
 *     location: example.location,
 *     keyAlgorithm: "rsa4096",
 *     name: "My Auto renewed certificate",
 *     subjectAlternativeNames: ["app.example.com"],
 * });
 * ```
 *
 * ## Import
 *
 * The resource can be imported using the `auto_certificate_id` and the `location`, separated by `:`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:cert/autoCertificate:AutoCertificate example location:auto_certificate_id
 * ```
 */
export class AutoCertificate extends pulumi.CustomResource {
    /**
     * Get an existing AutoCertificate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AutoCertificateState, opts?: pulumi.CustomResourceOptions): AutoCertificate {
        return new AutoCertificate(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:cert/autoCertificate:AutoCertificate';

    /**
     * Returns true if the given object is an instance of AutoCertificate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AutoCertificate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AutoCertificate.__pulumiType;
    }

    /**
     * [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
     */
    public readonly commonName!: pulumi.Output<string>;
    /**
     * [string] The key algorithm used to generate the certificate.
     */
    public readonly keyAlgorithm!: pulumi.Output<string>;
    /**
     * [string] The ID of the last certificate that was issued.
     */
    public /*out*/ readonly lastIssuedCertificateId!: pulumi.Output<string>;
    /**
     * [string] The location of the auto-certificate.
     */
    public readonly location!: pulumi.Output<string>;
    /**
     * [string] A certificate name used for management purposes.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] The certificate provider used to issue the certificates.
     */
    public readonly providerId!: pulumi.Output<string>;
    /**
     * [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
     */
    public readonly subjectAlternativeNames!: pulumi.Output<string[] | undefined>;

    /**
     * Create a AutoCertificate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AutoCertificateArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AutoCertificateArgs | AutoCertificateState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AutoCertificateState | undefined;
            resourceInputs["commonName"] = state ? state.commonName : undefined;
            resourceInputs["keyAlgorithm"] = state ? state.keyAlgorithm : undefined;
            resourceInputs["lastIssuedCertificateId"] = state ? state.lastIssuedCertificateId : undefined;
            resourceInputs["location"] = state ? state.location : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["providerId"] = state ? state.providerId : undefined;
            resourceInputs["subjectAlternativeNames"] = state ? state.subjectAlternativeNames : undefined;
        } else {
            const args = argsOrState as AutoCertificateArgs | undefined;
            if ((!args || args.commonName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'commonName'");
            }
            if ((!args || args.keyAlgorithm === undefined) && !opts.urn) {
                throw new Error("Missing required property 'keyAlgorithm'");
            }
            if ((!args || args.location === undefined) && !opts.urn) {
                throw new Error("Missing required property 'location'");
            }
            if ((!args || args.providerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'providerId'");
            }
            resourceInputs["commonName"] = args ? args.commonName : undefined;
            resourceInputs["keyAlgorithm"] = args ? args.keyAlgorithm : undefined;
            resourceInputs["location"] = args ? args.location : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["providerId"] = args ? args.providerId : undefined;
            resourceInputs["subjectAlternativeNames"] = args ? args.subjectAlternativeNames : undefined;
            resourceInputs["lastIssuedCertificateId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AutoCertificate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AutoCertificate resources.
 */
export interface AutoCertificateState {
    /**
     * [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
     */
    commonName?: pulumi.Input<string>;
    /**
     * [string] The key algorithm used to generate the certificate.
     */
    keyAlgorithm?: pulumi.Input<string>;
    /**
     * [string] The ID of the last certificate that was issued.
     */
    lastIssuedCertificateId?: pulumi.Input<string>;
    /**
     * [string] The location of the auto-certificate.
     */
    location?: pulumi.Input<string>;
    /**
     * [string] A certificate name used for management purposes.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The certificate provider used to issue the certificates.
     */
    providerId?: pulumi.Input<string>;
    /**
     * [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
     */
    subjectAlternativeNames?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a AutoCertificate resource.
 */
export interface AutoCertificateArgs {
    /**
     * [string] The common name (DNS) of the certificate to issue. The common name needs to be part of a zone in IONOS Cloud DNS.
     */
    commonName: pulumi.Input<string>;
    /**
     * [string] The key algorithm used to generate the certificate.
     */
    keyAlgorithm: pulumi.Input<string>;
    /**
     * [string] The location of the auto-certificate.
     */
    location: pulumi.Input<string>;
    /**
     * [string] A certificate name used for management purposes.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The certificate provider used to issue the certificates.
     */
    providerId: pulumi.Input<string>;
    /**
     * [list][string] Optional additional names to be added to the issued certificate. The additional names needs to be part of a zone in IONOS Cloud DNS.
     */
    subjectAlternativeNames?: pulumi.Input<pulumi.Input<string>[]>;
}
