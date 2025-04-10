// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages **Users** and list users and groups associated with that user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@ionos-cloud/sdk-pulumi";
 * import * as random from "@pulumi/random";
 *
 * const group1 = new ionoscloud.compute.Group("group1", {
 *     name: "group1",
 *     createDatacenter: true,
 *     createSnapshot: true,
 *     reserveIp: true,
 *     accessActivityLog: false,
 *     createK8sCluster: true,
 * });
 * const group2 = new ionoscloud.compute.Group("group2", {
 *     name: "group2",
 *     createDatacenter: true,
 *     createSnapshot: true,
 *     reserveIp: true,
 *     accessActivityLog: false,
 *     createK8sCluster: true,
 * });
 * const group3 = new ionoscloud.compute.Group("group3", {
 *     name: "group3",
 *     createDatacenter: true,
 *     createSnapshot: true,
 *     reserveIp: true,
 *     accessActivityLog: false,
 * });
 * const userPassword = new random.index.Password("user_password", {
 *     length: 16,
 *     special: true,
 *     overrideSpecial: "!#$%&*()-_=+[]{}<>:?",
 * });
 * const example = new ionoscloud.compute.User("example", {
 *     firstName: "example",
 *     lastName: "example",
 *     email: "unique@email.com",
 *     password: userPassword.result,
 *     administrator: false,
 *     forceSecAuth: false,
 *     active: true,
 *     groupIds: [
 *         group1.id,
 *         group2.id,
 *         group3.id,
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * Resource User can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/user:User myuser user uuid
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * [Boolean] Indicates if the user is active
     */
    public readonly active!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
     */
    public readonly administrator!: pulumi.Output<boolean | undefined>;
    /**
     * [string] An e-mail address for the user.
     */
    public readonly email!: pulumi.Output<string>;
    /**
     * [string] A first name for the user.
     */
    public readonly firstName!: pulumi.Output<string>;
    /**
     * [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
     */
    public readonly forceSecAuth!: pulumi.Output<boolean | undefined>;
    /**
     * [Set] The groups that this user will be a member of
     *
     * **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     */
    public readonly groupIds!: pulumi.Output<string[] | undefined>;
    /**
     * [string] A last name for the user.
     */
    public readonly lastName!: pulumi.Output<string>;
    /**
     * [string] A password for the user.
     */
    public readonly password!: pulumi.Output<string>;
    /**
     * Canonical (IONOS Object Storage) id of the user for a given identity
     */
    public /*out*/ readonly s3CanonicalUserId!: pulumi.Output<string>;
    /**
     * [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
     */
    public /*out*/ readonly secAuthActive!: pulumi.Output<boolean>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as UserState | undefined;
            resourceInputs["active"] = state ? state.active : undefined;
            resourceInputs["administrator"] = state ? state.administrator : undefined;
            resourceInputs["email"] = state ? state.email : undefined;
            resourceInputs["firstName"] = state ? state.firstName : undefined;
            resourceInputs["forceSecAuth"] = state ? state.forceSecAuth : undefined;
            resourceInputs["groupIds"] = state ? state.groupIds : undefined;
            resourceInputs["lastName"] = state ? state.lastName : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["s3CanonicalUserId"] = state ? state.s3CanonicalUserId : undefined;
            resourceInputs["secAuthActive"] = state ? state.secAuthActive : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if ((!args || args.email === undefined) && !opts.urn) {
                throw new Error("Missing required property 'email'");
            }
            if ((!args || args.firstName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'firstName'");
            }
            if ((!args || args.lastName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'lastName'");
            }
            if ((!args || args.password === undefined) && !opts.urn) {
                throw new Error("Missing required property 'password'");
            }
            resourceInputs["active"] = args ? args.active : undefined;
            resourceInputs["administrator"] = args ? args.administrator : undefined;
            resourceInputs["email"] = args ? args.email : undefined;
            resourceInputs["firstName"] = args ? args.firstName : undefined;
            resourceInputs["forceSecAuth"] = args ? args.forceSecAuth : undefined;
            resourceInputs["groupIds"] = args ? args.groupIds : undefined;
            resourceInputs["lastName"] = args ? args.lastName : undefined;
            resourceInputs["password"] = args?.password ? pulumi.secret(args.password) : undefined;
            resourceInputs["s3CanonicalUserId"] = undefined /*out*/;
            resourceInputs["secAuthActive"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(User.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * [Boolean] Indicates if the user is active
     */
    active?: pulumi.Input<boolean>;
    /**
     * [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
     */
    administrator?: pulumi.Input<boolean>;
    /**
     * [string] An e-mail address for the user.
     */
    email?: pulumi.Input<string>;
    /**
     * [string] A first name for the user.
     */
    firstName?: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
     */
    forceSecAuth?: pulumi.Input<boolean>;
    /**
     * [Set] The groups that this user will be a member of
     *
     * **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     */
    groupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] A last name for the user.
     */
    lastName?: pulumi.Input<string>;
    /**
     * [string] A password for the user.
     */
    password?: pulumi.Input<string>;
    /**
     * Canonical (IONOS Object Storage) id of the user for a given identity
     */
    s3CanonicalUserId?: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if secure authentication is active for the user or not. *it can not be used in create requests - can be used in update*
     */
    secAuthActive?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * [Boolean] Indicates if the user is active
     */
    active?: pulumi.Input<boolean>;
    /**
     * [Boolean] Indicates if the user has administrative rights. Administrators do not need to be managed in groups, as they automatically have access to all resources associated with the contract.
     */
    administrator?: pulumi.Input<boolean>;
    /**
     * [string] An e-mail address for the user.
     */
    email: pulumi.Input<string>;
    /**
     * [string] A first name for the user.
     */
    firstName: pulumi.Input<string>;
    /**
     * [Boolean] Indicates if secure (two-factor) authentication should be forced for the user (true) or not (false).
     */
    forceSecAuth?: pulumi.Input<boolean>;
    /**
     * [Set] The groups that this user will be a member of
     *
     * **NOTE:** Group_ids field cannot be used at the same time with userIds field in group resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     */
    groupIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * [string] A last name for the user.
     */
    lastName: pulumi.Input<string>;
    /**
     * [string] A password for the user.
     */
    password: pulumi.Input<string>;
}
