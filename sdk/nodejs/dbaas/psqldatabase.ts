// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manages a **DbaaS PgSql Database**.
 *
 * ## Example Usage
 *
 * Create a `PgSQL` cluster as presented in the documentation for the cluster, then define a database resource
 * and link it with the previously created cluster:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ionoscloud from "@pulumi/ionoscloud";
 *
 * const examplePgDatabase = new ionoscloud.dbaas.PSQLDatabase("example_pg_database", {
 *     clusterId: example.id,
 *     name: "exampledatabase",
 *     owner: "exampleuser",
 * });
 * ```
 *
 * ## Import
 *
 * In order to import a PgSql database, you can define an empty database resource in the plan:
 *
 * hcl
 *
 * resource "ionoscloud_pg_database" "example" {
 *
 * }
 *
 * The resource can be imported using the `clusterId` and the `name`, for example:
 *
 * ```sh
 * $ pulumi import ionoscloud:dbaas/pSQLDatabase:PSQLDatabase example clusterid/name
 * ```
 */
export class PSQLDatabase extends pulumi.CustomResource {
    /**
     * Get an existing PSQLDatabase resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PSQLDatabaseState, opts?: pulumi.CustomResourceOptions): PSQLDatabase {
        return new PSQLDatabase(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ionoscloud:dbaas/pSQLDatabase:PSQLDatabase';

    /**
     * Returns true if the given object is an instance of PSQLDatabase.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is PSQLDatabase {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === PSQLDatabase.__pulumiType;
    }

    /**
     * [string] The unique ID of the cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * [string] The name of the database.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * [string] The owner of the database.
     */
    public readonly owner!: pulumi.Output<string>;

    /**
     * Create a PSQLDatabase resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PSQLDatabaseArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PSQLDatabaseArgs | PSQLDatabaseState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as PSQLDatabaseState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
        } else {
            const args = argsOrState as PSQLDatabaseArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.owner === undefined) && !opts.urn) {
                throw new Error("Missing required property 'owner'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(PSQLDatabase.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering PSQLDatabase resources.
 */
export interface PSQLDatabaseState {
    /**
     * [string] The unique ID of the cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * [string] The name of the database.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The owner of the database.
     */
    owner?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a PSQLDatabase resource.
 */
export interface PSQLDatabaseArgs {
    /**
     * [string] The unique ID of the cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * [string] The name of the database.
     */
    name?: pulumi.Input<string>;
    /**
     * [string] The owner of the database.
     */
    owner: pulumi.Input<string>;
}
