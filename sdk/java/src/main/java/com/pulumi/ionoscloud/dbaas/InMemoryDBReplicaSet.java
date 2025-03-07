// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.dbaas;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import com.pulumi.ionoscloud.Utilities;
import com.pulumi.ionoscloud.dbaas.InMemoryDBReplicaSetArgs;
import com.pulumi.ionoscloud.dbaas.inputs.InMemoryDBReplicaSetState;
import com.pulumi.ionoscloud.dbaas.outputs.InMemoryDBReplicaSetConnections;
import com.pulumi.ionoscloud.dbaas.outputs.InMemoryDBReplicaSetCredentials;
import com.pulumi.ionoscloud.dbaas.outputs.InMemoryDBReplicaSetMaintenanceWindow;
import com.pulumi.ionoscloud.dbaas.outputs.InMemoryDBReplicaSetResources;
import java.lang.Integer;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manages a **DBaaS InMemoryDB Replica Set**.
 * 
 * ## Import
 * 
 * Resource DBaaS InMemoryDB Replica Set can be imported using the `replicaset_id` and the `location`, separated by `:`, e.g:
 * 
 * ```sh
 * $ pulumi import ionoscloud:dbaas/inMemoryDBReplicaSet:InMemoryDBReplicaSet example location:replicaSet uuid
 * ```
 * 
 */
@ResourceType(type="ionoscloud:dbaas/inMemoryDBReplicaSet:InMemoryDBReplicaSet")
public class InMemoryDBReplicaSet extends com.pulumi.resources.CustomResource {
    /**
     * [object] The network connection for your replica set. Only one connection is allowed. Updates to the value of the fields force the replica set to be re-created.
     * 
     */
    @Export(name="connections", refs={InMemoryDBReplicaSetConnections.class}, tree="[0]")
    private Output<InMemoryDBReplicaSetConnections> connections;

    /**
     * @return [object] The network connection for your replica set. Only one connection is allowed. Updates to the value of the fields force the replica set to be re-created.
     * 
     */
    public Output<InMemoryDBReplicaSetConnections> connections() {
        return this.connections;
    }
    /**
     * [object] Credentials for the InMemoryDB replicaset, only one type of password can be used since they are mutually exclusive. These values are used to create the initial InMemoryDB user, updating any of these will force recreation of the replica set resource.
     * 
     */
    @Export(name="credentials", refs={InMemoryDBReplicaSetCredentials.class}, tree="[0]")
    private Output<InMemoryDBReplicaSetCredentials> credentials;

    /**
     * @return [object] Credentials for the InMemoryDB replicaset, only one type of password can be used since they are mutually exclusive. These values are used to create the initial InMemoryDB user, updating any of these will force recreation of the replica set resource.
     * 
     */
    public Output<InMemoryDBReplicaSetCredentials> credentials() {
        return this.credentials;
    }
    /**
     * [string] The human-readable name of your replica set.
     * 
     */
    @Export(name="displayName", refs={String.class}, tree="[0]")
    private Output<String> displayName;

    /**
     * @return [string] The human-readable name of your replica set.
     * 
     */
    public Output<String> displayName() {
        return this.displayName;
    }
    /**
     * [string] The DNS name pointing to your replica set. Will be used to connect to the active/standalone instance.
     * 
     * &gt; **⚠ NOTE:** `IONOS_API_URL_INMEMORYDB` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
     * 
     */
    @Export(name="dnsName", refs={String.class}, tree="[0]")
    private Output<String> dnsName;

    /**
     * @return [string] The DNS name pointing to your replica set. Will be used to connect to the active/standalone instance.
     * 
     * &gt; **⚠ NOTE:** `IONOS_API_URL_INMEMORYDB` can be used to set a custom API URL for the resource. `location` field needs to be empty, otherwise it will override the custom API URL. Setting `endpoint` or `IONOS_API_URL` does not have any effect.
     * 
     */
    public Output<String> dnsName() {
        return this.dnsName;
    }
    /**
     * [string] The eviction policy for the replica set, possible values are:
     * 
     */
    @Export(name="evictionPolicy", refs={String.class}, tree="[0]")
    private Output<String> evictionPolicy;

    /**
     * @return [string] The eviction policy for the replica set, possible values are:
     * 
     */
    public Output<String> evictionPolicy() {
        return this.evictionPolicy;
    }
    /**
     * [string] The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
     * 
     */
    @Export(name="initialSnapshotId", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> initialSnapshotId;

    /**
     * @return [string] The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
     * 
     */
    public Output<Optional<String>> initialSnapshotId() {
        return Codegen.optional(this.initialSnapshotId);
    }
    /**
     * [string] The location of your replica set. Updates to the value of the field force the replica set to be re-created. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * 
     */
    @Export(name="location", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> location;

    /**
     * @return [string] The location of your replica set. Updates to the value of the field force the replica set to be re-created. If this is not set and if no value is provided for the `IONOS_API_URL` env var, the default `location` will be: `de/fra`.
     * 
     */
    public Output<Optional<String>> location() {
        return Codegen.optional(this.location);
    }
    /**
     * (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    @Export(name="maintenanceWindow", refs={InMemoryDBReplicaSetMaintenanceWindow.class}, tree="[0]")
    private Output<InMemoryDBReplicaSetMaintenanceWindow> maintenanceWindow;

    /**
     * @return (Computed) A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    public Output<InMemoryDBReplicaSetMaintenanceWindow> maintenanceWindow() {
        return this.maintenanceWindow;
    }
    /**
     * [string] Specifies How and If data is persisted, possible values are:
     * * `None` - Data is inMemory only and will not be persisted. Useful for cache only applications.
     * * `AOF` - (Append Only File) AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the InMemoryDB protocol itself.
     * * `RDB` - RDB persistence performs snapshots of the current in memory state.
     * * `RDB_AOF` - Both RDB and AOF persistence are enabled.
     * 
     */
    @Export(name="persistenceMode", refs={String.class}, tree="[0]")
    private Output<String> persistenceMode;

    /**
     * @return [string] Specifies How and If data is persisted, possible values are:
     * * `None` - Data is inMemory only and will not be persisted. Useful for cache only applications.
     * * `AOF` - (Append Only File) AOF persistence logs every write operation received by the server. These operations can then be replayed again at server startup, reconstructing the original dataset. Commands are logged using the same format as the InMemoryDB protocol itself.
     * * `RDB` - RDB persistence performs snapshots of the current in memory state.
     * * `RDB_AOF` - Both RDB and AOF persistence are enabled.
     * 
     */
    public Output<String> persistenceMode() {
        return this.persistenceMode;
    }
    /**
     * [int] The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only standby for a failure of the active instance.
     * 
     */
    @Export(name="replicas", refs={Integer.class}, tree="[0]")
    private Output<Integer> replicas;

    /**
     * @return [int] The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only standby for a failure of the active instance.
     * 
     */
    public Output<Integer> replicas() {
        return this.replicas;
    }
    /**
     * [object] The resources of the individual replicas.
     * 
     */
    @Export(name="resources", refs={InMemoryDBReplicaSetResources.class}, tree="[0]")
    private Output<InMemoryDBReplicaSetResources> resources;

    /**
     * @return [object] The resources of the individual replicas.
     * 
     */
    public Output<InMemoryDBReplicaSetResources> resources() {
        return this.resources;
    }
    /**
     * [string] The InMemoryDB version of your replica set.
     * 
     */
    @Export(name="version", refs={String.class}, tree="[0]")
    private Output<String> version;

    /**
     * @return [string] The InMemoryDB version of your replica set.
     * 
     */
    public Output<String> version() {
        return this.version;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public InMemoryDBReplicaSet(java.lang.String name) {
        this(name, InMemoryDBReplicaSetArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public InMemoryDBReplicaSet(java.lang.String name, InMemoryDBReplicaSetArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public InMemoryDBReplicaSet(java.lang.String name, InMemoryDBReplicaSetArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:dbaas/inMemoryDBReplicaSet:InMemoryDBReplicaSet", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private InMemoryDBReplicaSet(java.lang.String name, Output<java.lang.String> id, @Nullable InMemoryDBReplicaSetState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ionoscloud:dbaas/inMemoryDBReplicaSet:InMemoryDBReplicaSet", name, state, makeResourceOptions(options, id), false);
    }

    private static InMemoryDBReplicaSetArgs makeArgs(InMemoryDBReplicaSetArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? InMemoryDBReplicaSetArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static InMemoryDBReplicaSet get(java.lang.String name, Output<java.lang.String> id, @Nullable InMemoryDBReplicaSetState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new InMemoryDBReplicaSet(name, id, state, options);
    }
}
