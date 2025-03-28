// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages Object Lock Configuration for Buckets on IonosCloud.
 *
 * ## Import
 *
 * IONOS Object Storage Bucket object lock configuration can be imported using the `bucket` name.
 *
 * ```sh
 * $ pulumi import ionoscloud:objectstorage/objectLockConfiguration:ObjectLockConfiguration example example
 * ```
 */
export class ObjectLockConfiguration extends pulumi.CustomResource {
    /**
     * Get an existing ObjectLockConfiguration resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ObjectLockConfigurationState, opts?: pulumi.CustomResourceOptions): ObjectLockConfiguration {
        return new ObjectLockConfiguration(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:objectstorage/objectLockConfiguration:ObjectLockConfiguration';

    /**
     * Returns true if the given object is an instance of ObjectLockConfiguration.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ObjectLockConfiguration {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ObjectLockConfiguration.__pulumiType;
    }

    /**
     * [string] The name of the bucket where the object will be stored.
     */
    public readonly bucket!: pulumi.Output<string>;
    /**
     * [Optional] The object lock configuration status of the bucket. Must be `Enabled`.
     */
    public readonly objectLockEnabled!: pulumi.Output<string>;
    /**
     * [block] A block of rule as defined below.
     */
    public readonly rule!: pulumi.Output<outputs.objectstorage.ObjectLockConfigurationRule | undefined>;

    /**
     * Create a ObjectLockConfiguration resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ObjectLockConfigurationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ObjectLockConfigurationArgs | ObjectLockConfigurationState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ObjectLockConfigurationState | undefined;
            resourceInputs["bucket"] = state ? state.bucket : undefined;
            resourceInputs["objectLockEnabled"] = state ? state.objectLockEnabled : undefined;
            resourceInputs["rule"] = state ? state.rule : undefined;
        } else {
            const args = argsOrState as ObjectLockConfigurationArgs | undefined;
            if ((!args || args.bucket === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bucket'");
            }
            resourceInputs["bucket"] = args ? args.bucket : undefined;
            resourceInputs["objectLockEnabled"] = args ? args.objectLockEnabled : undefined;
            resourceInputs["rule"] = args ? args.rule : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ObjectLockConfiguration.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ObjectLockConfiguration resources.
 */
export interface ObjectLockConfigurationState {
    /**
     * [string] The name of the bucket where the object will be stored.
     */
    bucket?: pulumi.Input<string>;
    /**
     * [Optional] The object lock configuration status of the bucket. Must be `Enabled`.
     */
    objectLockEnabled?: pulumi.Input<string>;
    /**
     * [block] A block of rule as defined below.
     */
    rule?: pulumi.Input<inputs.objectstorage.ObjectLockConfigurationRule>;
}

/**
 * The set of arguments for constructing a ObjectLockConfiguration resource.
 */
export interface ObjectLockConfigurationArgs {
    /**
     * [string] The name of the bucket where the object will be stored.
     */
    bucket: pulumi.Input<string>;
    /**
     * [Optional] The object lock configuration status of the bucket. Must be `Enabled`.
     */
    objectLockEnabled?: pulumi.Input<string>;
    /**
     * [block] A block of rule as defined below.
     */
    rule?: pulumi.Input<inputs.objectstorage.ObjectLockConfigurationRule>;
}
