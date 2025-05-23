// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages **Shares** and list shares permissions granted to the group members for each shared resource.
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
 * const exampleGroup = new ionoscloud.compute.Group("example", {
 *     name: "Group Example",
 *     createDatacenter: true,
 *     createSnapshot: true,
 *     reserveIp: true,
 *     accessActivityLog: true,
 *     createPcc: true,
 *     s3Privilege: true,
 *     createBackupUnit: true,
 *     createInternetAccess: true,
 *     createK8sCluster: true,
 * });
 * const exampleShare = new ionoscloud.compute.Share("example", {
 *     groupId: exampleGroup.id,
 *     resourceId: example.id,
 *     editPrivilege: true,
 *     sharePrivilege: false,
 * });
 * ```
 *
 * ## Import
 *
 * Resource Share can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/share:Share myshare group uuid/resource uuid
 * ```
 */
export class Share extends pulumi.CustomResource {
    /**
     * Get an existing Share resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ShareState, opts?: pulumi.CustomResourceOptions): Share {
        return new Share(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/share:Share';

    /**
     * Returns true if the given object is an instance of Share.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Share {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Share.__pulumiType;
    }

    /**
     * [Boolean] The group has permission to edit privileges on this resource.
     */
    public readonly editPrivilege!: pulumi.Output<boolean | undefined>;
    /**
     * [string] The ID of the specific group containing the resource to update.
     */
    public readonly groupId!: pulumi.Output<string>;
    /**
     * [string] The ID of the specific resource to update.
     */
    public readonly resourceId!: pulumi.Output<string>;
    /**
     * [Boolean] The group has permission to share this resource.
     *
     * ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
     * to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
     * to create the resources in a sequential manner. Another solution involves the usage of `dependsOn`
     * attributes inside the `ionoscloud.compute.Share` resource to enforce the sequential creation of the shares.
     */
    public readonly sharePrivilege!: pulumi.Output<boolean | undefined>;

    /**
     * Create a Share resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ShareArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ShareArgs | ShareState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ShareState | undefined;
            resourceInputs["editPrivilege"] = state ? state.editPrivilege : undefined;
            resourceInputs["groupId"] = state ? state.groupId : undefined;
            resourceInputs["resourceId"] = state ? state.resourceId : undefined;
            resourceInputs["sharePrivilege"] = state ? state.sharePrivilege : undefined;
        } else {
            const args = argsOrState as ShareArgs | undefined;
            if ((!args || args.groupId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupId'");
            }
            if ((!args || args.resourceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'resourceId'");
            }
            resourceInputs["editPrivilege"] = args ? args.editPrivilege : undefined;
            resourceInputs["groupId"] = args ? args.groupId : undefined;
            resourceInputs["resourceId"] = args ? args.resourceId : undefined;
            resourceInputs["sharePrivilege"] = args ? args.sharePrivilege : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Share.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Share resources.
 */
export interface ShareState {
    /**
     * [Boolean] The group has permission to edit privileges on this resource.
     */
    editPrivilege?: pulumi.Input<boolean>;
    /**
     * [string] The ID of the specific group containing the resource to update.
     */
    groupId?: pulumi.Input<string>;
    /**
     * [string] The ID of the specific resource to update.
     */
    resourceId?: pulumi.Input<string>;
    /**
     * [Boolean] The group has permission to share this resource.
     *
     * ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
     * to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
     * to create the resources in a sequential manner. Another solution involves the usage of `dependsOn`
     * attributes inside the `ionoscloud.compute.Share` resource to enforce the sequential creation of the shares.
     */
    sharePrivilege?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a Share resource.
 */
export interface ShareArgs {
    /**
     * [Boolean] The group has permission to edit privileges on this resource.
     */
    editPrivilege?: pulumi.Input<boolean>;
    /**
     * [string] The ID of the specific group containing the resource to update.
     */
    groupId: pulumi.Input<string>;
    /**
     * [string] The ID of the specific resource to update.
     */
    resourceId: pulumi.Input<string>;
    /**
     * [Boolean] The group has permission to share this resource.
     *
     * ⚠️ **Note:** There is a limitation due to which the creation of several shares at the same time leads
     * to an error. To avoid this, `parallelism=1` can be used when running `pulumi up` command in order
     * to create the resources in a sequential manner. Another solution involves the usage of `dependsOn`
     * attributes inside the `ionoscloud.compute.Share` resource to enforce the sequential creation of the shares.
     */
    sharePrivilege?: pulumi.Input<boolean>;
}
