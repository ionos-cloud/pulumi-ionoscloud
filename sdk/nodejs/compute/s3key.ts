// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages an **IONOS Object Storage Key** on IonosCloud.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const exampleUser = new ionoscloud.compute.User("exampleUser", {
 *     firstName: "example",
 *     lastName: "example",
 *     email: "unique@email.com",
 *     password: "abc123-321CBA",
 *     administrator: false,
 *     forceSecAuth: false,
 * });
 * const exampleS3Key = new ionoscloud.compute.S3Key("exampleS3Key", {
 *     userId: exampleUser.id,
 *     active: true,
 * });
 * ```
 * <!--End PulumiCodeChooser -->
 *
 * ## Import
 *
 * An IONOS Object Storage Unit resource can be imported using its user id as well as its `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/s3Key:S3Key demo {userId}/{s3KeyId}
 * ```
 *
 * This can be helpful when you want to import IONOS Object Storage Keys which you have already created manually or using other means, outside of terraform.
 */
export class S3Key extends pulumi.CustomResource {
    /**
     * Get an existing S3Key resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: S3KeyState, opts?: pulumi.CustomResourceOptions): S3Key {
        return new S3Key(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/s3Key:S3Key';

    /**
     * Returns true if the given object is an instance of S3Key.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is S3Key {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === S3Key.__pulumiType;
    }

    /**
     * [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
     */
    public readonly active!: pulumi.Output<boolean | undefined>;
    /**
     * The IONOS Object Storage Secret key.
     */
    public /*out*/ readonly secretKey!: pulumi.Output<string>;
    /**
     * [string] The UUID of the user owning the IONOS Object Storage Key.
     */
    public readonly userId!: pulumi.Output<string>;

    /**
     * Create a S3Key resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: S3KeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: S3KeyArgs | S3KeyState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as S3KeyState | undefined;
            resourceInputs["active"] = state ? state.active : undefined;
            resourceInputs["secretKey"] = state ? state.secretKey : undefined;
            resourceInputs["userId"] = state ? state.userId : undefined;
        } else {
            const args = argsOrState as S3KeyArgs | undefined;
            if ((!args || args.userId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userId'");
            }
            resourceInputs["active"] = args ? args.active : undefined;
            resourceInputs["userId"] = args ? args.userId : undefined;
            resourceInputs["secretKey"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(S3Key.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering S3Key resources.
 */
export interface S3KeyState {
    /**
     * [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
     */
    active?: pulumi.Input<boolean>;
    /**
     * The IONOS Object Storage Secret key.
     */
    secretKey?: pulumi.Input<string>;
    /**
     * [string] The UUID of the user owning the IONOS Object Storage Key.
     */
    userId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a S3Key resource.
 */
export interface S3KeyArgs {
    /**
     * [boolean] Whether the IONOS Object Storage is active / enabled or not - Please keep in mind this is only required on create. Default value in true
     */
    active?: pulumi.Input<boolean>;
    /**
     * [string] The UUID of the user owning the IONOS Object Storage Key.
     */
    userId: pulumi.Input<string>;
}
