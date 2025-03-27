// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Manages **Groups** and **Group Privileges** on IonosCloud.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 * import * as random from "@pulumi/random";
 *
 * const user1Password = new random.index.Password("user1_password", {
 *     length: 16,
 *     special: true,
 *     overrideSpecial: "!#$%&*()-_=+[]{}<>:?",
 * });
 * const example1 = new ionoscloud.compute.User("example1", {
 *     firstName: "user1",
 *     lastName: "user1",
 *     email: "unique_email.com",
 *     password: user1Password.result,
 *     administrator: false,
 *     forceSecAuth: false,
 * });
 * const user2Password = new random.index.Password("user2_password", {
 *     length: 16,
 *     special: true,
 *     overrideSpecial: "!#$%&*()-_=+[]{}<>:?",
 * });
 * const example2 = new ionoscloud.compute.User("example2", {
 *     firstName: "user2",
 *     lastName: "user2",
 *     email: "unique_email.com",
 *     password: user2Password.result,
 *     administrator: false,
 *     forceSecAuth: false,
 * });
 * const example = new ionoscloud.compute.Group("example", {
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
 *     createFlowLog: true,
 *     accessAndManageMonitoring: true,
 *     accessAndManageCertificates: true,
 *     manageDbaas: true,
 *     userIds: [
 *         example1.id,
 *         example2.id,
 *     ],
 * });
 * ```
 *
 * ## Import
 *
 * Resource Group can be imported using the `resource id`, e.g.
 *
 * ```sh
 * $ pulumi import ionoscloud:compute/group:Group mygroup group uuid
 * ```
 *
 * > :warning: **If you are upgrading to v6.2.0**: You have to modify you plan for user_ids to match the new structure, by renaming the field old field, **user_id**, to user_ids and put the old value into an array. This is not backwards compatible.
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:compute/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * [Boolean] The group will be allowed to access the activity log.
     */
    public readonly accessActivityLog!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean]  The group will be allowed to access and manage certificates.
     */
    public readonly accessAndManageCertificates!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean]  The group will be allowed to access and manage monitoring.
     */
    public readonly accessAndManageMonitoring!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will be allowed to create backup unit privilege.
     */
    public readonly createBackupUnit!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will be allowed to create virtual data centers.
     */
    public readonly createDatacenter!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean]  The group will be allowed to create flow log.
     */
    public readonly createFlowLog!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will be allowed to create internet access privilege.
     */
    public readonly createInternetAccess!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean]  The group will be allowed to create kubernetes cluster privilege.
     */
    public readonly createK8sCluster!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will be allowed to create Cross Connects privilege.
     */
    public readonly createPcc!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will be allowed to create snapshots.
     */
    public readonly createSnapshot!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean]  Privilege for a group to manage DBaaS related functionality.
     */
    public readonly manageDbaas!: pulumi.Output<boolean | undefined>;
    /**
     * [string] A name for the group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [Boolean] The group will be allowed to reserve IP addresses.
     */
    public readonly reserveIp!: pulumi.Output<boolean | undefined>;
    /**
     * [Boolean] The group will have S3 privilege.
     */
    public readonly s3Privilege!: pulumi.Output<boolean | undefined>;
    /**
     * [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
     *
     * @deprecated Please use userIds for adding users to the group, since userId will be removed in the future
     */
    public readonly userId!: pulumi.Output<string | undefined>;
    /**
     * [list] A list of users to add to the group.
     */
    public readonly userIds!: pulumi.Output<string[] | undefined>;
    /**
     * List of users - See the User section
     *
     * **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     */
    public /*out*/ readonly users!: pulumi.Output<outputs.compute.GroupUser[]>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["accessActivityLog"] = state ? state.accessActivityLog : undefined;
            resourceInputs["accessAndManageCertificates"] = state ? state.accessAndManageCertificates : undefined;
            resourceInputs["accessAndManageMonitoring"] = state ? state.accessAndManageMonitoring : undefined;
            resourceInputs["createBackupUnit"] = state ? state.createBackupUnit : undefined;
            resourceInputs["createDatacenter"] = state ? state.createDatacenter : undefined;
            resourceInputs["createFlowLog"] = state ? state.createFlowLog : undefined;
            resourceInputs["createInternetAccess"] = state ? state.createInternetAccess : undefined;
            resourceInputs["createK8sCluster"] = state ? state.createK8sCluster : undefined;
            resourceInputs["createPcc"] = state ? state.createPcc : undefined;
            resourceInputs["createSnapshot"] = state ? state.createSnapshot : undefined;
            resourceInputs["manageDbaas"] = state ? state.manageDbaas : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["reserveIp"] = state ? state.reserveIp : undefined;
            resourceInputs["s3Privilege"] = state ? state.s3Privilege : undefined;
            resourceInputs["userId"] = state ? state.userId : undefined;
            resourceInputs["userIds"] = state ? state.userIds : undefined;
            resourceInputs["users"] = state ? state.users : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            resourceInputs["accessActivityLog"] = args ? args.accessActivityLog : undefined;
            resourceInputs["accessAndManageCertificates"] = args ? args.accessAndManageCertificates : undefined;
            resourceInputs["accessAndManageMonitoring"] = args ? args.accessAndManageMonitoring : undefined;
            resourceInputs["createBackupUnit"] = args ? args.createBackupUnit : undefined;
            resourceInputs["createDatacenter"] = args ? args.createDatacenter : undefined;
            resourceInputs["createFlowLog"] = args ? args.createFlowLog : undefined;
            resourceInputs["createInternetAccess"] = args ? args.createInternetAccess : undefined;
            resourceInputs["createK8sCluster"] = args ? args.createK8sCluster : undefined;
            resourceInputs["createPcc"] = args ? args.createPcc : undefined;
            resourceInputs["createSnapshot"] = args ? args.createSnapshot : undefined;
            resourceInputs["manageDbaas"] = args ? args.manageDbaas : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["reserveIp"] = args ? args.reserveIp : undefined;
            resourceInputs["s3Privilege"] = args ? args.s3Privilege : undefined;
            resourceInputs["userId"] = args ? args.userId : undefined;
            resourceInputs["userIds"] = args ? args.userIds : undefined;
            resourceInputs["users"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * [Boolean] The group will be allowed to access the activity log.
     */
    accessActivityLog?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to access and manage certificates.
     */
    accessAndManageCertificates?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to access and manage monitoring.
     */
    accessAndManageMonitoring?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create backup unit privilege.
     */
    createBackupUnit?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create virtual data centers.
     */
    createDatacenter?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to create flow log.
     */
    createFlowLog?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create internet access privilege.
     */
    createInternetAccess?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to create kubernetes cluster privilege.
     */
    createK8sCluster?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create Cross Connects privilege.
     */
    createPcc?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create snapshots.
     */
    createSnapshot?: pulumi.Input<boolean>;
    /**
     * [Boolean]  Privilege for a group to manage DBaaS related functionality.
     */
    manageDbaas?: pulumi.Input<boolean>;
    /**
     * [string] A name for the group.
     */
    name?: pulumi.Input<string>;
    /**
     * [Boolean] The group will be allowed to reserve IP addresses.
     */
    reserveIp?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will have S3 privilege.
     */
    s3Privilege?: pulumi.Input<boolean>;
    /**
     * [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
     *
     * @deprecated Please use userIds for adding users to the group, since userId will be removed in the future
     */
    userId?: pulumi.Input<string>;
    /**
     * [list] A list of users to add to the group.
     */
    userIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * List of users - See the User section
     *
     * **NOTE:** user_id/user_ids field cannot be used at the same time with groupIds field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     */
    users?: pulumi.Input<pulumi.Input<inputs.compute.GroupUser>[]>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * [Boolean] The group will be allowed to access the activity log.
     */
    accessActivityLog?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to access and manage certificates.
     */
    accessAndManageCertificates?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to access and manage monitoring.
     */
    accessAndManageMonitoring?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create backup unit privilege.
     */
    createBackupUnit?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create virtual data centers.
     */
    createDatacenter?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to create flow log.
     */
    createFlowLog?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create internet access privilege.
     */
    createInternetAccess?: pulumi.Input<boolean>;
    /**
     * [Boolean]  The group will be allowed to create kubernetes cluster privilege.
     */
    createK8sCluster?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create Cross Connects privilege.
     */
    createPcc?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will be allowed to create snapshots.
     */
    createSnapshot?: pulumi.Input<boolean>;
    /**
     * [Boolean]  Privilege for a group to manage DBaaS related functionality.
     */
    manageDbaas?: pulumi.Input<boolean>;
    /**
     * [string] A name for the group.
     */
    name?: pulumi.Input<string>;
    /**
     * [Boolean] The group will be allowed to reserve IP addresses.
     */
    reserveIp?: pulumi.Input<boolean>;
    /**
     * [Boolean] The group will have S3 privilege.
     */
    s3Privilege?: pulumi.Input<boolean>;
    /**
     * [string] The ID of the specific user to add to the group. Please use userIds argument since this is **DEPRECATED**
     *
     * @deprecated Please use userIds for adding users to the group, since userId will be removed in the future
     */
    userId?: pulumi.Input<string>;
    /**
     * [list] A list of users to add to the group.
     */
    userIds?: pulumi.Input<pulumi.Input<string>[]>;
}
