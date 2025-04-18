// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a **Backup Unit** on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const backupUnitPassword = new random.index.Password("backup_unit_password", {
 *     length: 16,
 *     special: true,
 *     overrideSpecial: "!#$%&*()-_=+[]{}:?",
 * });
 * const example = new ionoscloud.compute.BackupUnit("example", {
 *     name: "Backup Unit Example",
 *     password: backupUnitPassword.result,
 *     email: "example@example-domain.com",
 * });
 * ```
 *
 * ## Important Notes
 *
 * - Please note that at the moment, Backup Units cannot be renamed
 * - Please note that the password attribute is write-only, and it cannot be retrieved from the API when importing a ionoscloud_backup_unit. The only way to keep track of it is to specify it on the resource to be imported, thus, making it a required attribute.
 *
 * ## Import
 *
 * A Backup Unit resource can be imported using its `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/backupUnit:BackupUnit demo backup_unit_uuid
 * ```
 *
 * This can be helpful when you want to import backup units which you have already created manually or using other means, outside of pulumi. Please note that you need to manually specify the password when first declaring the resource in pulumi, as there is no way to retrieve the password from the Cloud API.
 */
export class BackupUnit extends pulumi.CustomResource {
    /**
     * Get an existing BackupUnit resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BackupUnitState, opts?: pulumi.CustomResourceOptions): BackupUnit {
        return new BackupUnit(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/backupUnit:BackupUnit';

    /**
     * Returns true if the given object is an instance of BackupUnit.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BackupUnit {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BackupUnit.__pulumiType;
    }

    /**
     * [string] The email address assigned to the backup unit
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * The login associated with the backup unit. Derived from the contract number
     */
    public /*out*/ readonly login!: pulumi.Output<string>;
    /**
     * [string] The name of the Backup Unit. This argument is immutable.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] The desired password for the Backup Unit
     */
    public readonly password!: pulumi.Output<string>;

    /**
     * Create a BackupUnit resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BackupUnitArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BackupUnitArgs | BackupUnitState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as BackupUnitState | undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["login"] = state ? state.login : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
        } else {
            const args = argsOrState as BackupUnitArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["login"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(BackupUnit.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BackupUnit resources.
 */
export interface BackupUnitState {
    /**
     * [string] The email address assigned to the backup unit
     */
    email?: pulumi.Input<string>;
    /**
     * The login associated with the backup unit. Derived from the contract number
     */
    login?: pulumi.Input<string>;
    /**
     * [string] The name of the Backup Unit. This argument is immutable.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The desired password for the Backup Unit
     */
    password?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BackupUnit resource.
 */
export interface BackupUnitArgs {
    /**
     * [string] The email address assigned to the backup unit
     */
    email: pulumi.Input<string>;
    /**
     * [string] The name of the Backup Unit. This argument is immutable.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The desired password for the Backup Unit
     */
    password: pulumi.Input<string>;
}
