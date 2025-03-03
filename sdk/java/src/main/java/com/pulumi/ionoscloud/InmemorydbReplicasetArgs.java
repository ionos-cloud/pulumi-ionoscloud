// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.InmemorydbReplicasetConnectionsArgs;
import com.pulumi.ionoscloud.inputs.InmemorydbReplicasetCredentialsArgs;
import com.pulumi.ionoscloud.inputs.InmemorydbReplicasetMaintenanceWindowArgs;
import com.pulumi.ionoscloud.inputs.InmemorydbReplicasetResourcesArgs;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class InmemorydbReplicasetArgs extends com.pulumi.resources.ResourceArgs {

    public static final InmemorydbReplicasetArgs Empty = new InmemorydbReplicasetArgs();

    /**
     * The network connection for your replica set. Only one connection is allowed.
     * 
     */
    @Import(name="connections", required=true)
    private Output<InmemorydbReplicasetConnectionsArgs> connections;

    /**
     * @return The network connection for your replica set. Only one connection is allowed.
     * 
     */
    public Output<InmemorydbReplicasetConnectionsArgs> connections() {
        return this.connections;
    }

    /**
     * Credentials for the InMemoryDB replicaset.
     * 
     */
    @Import(name="credentials", required=true)
    private Output<InmemorydbReplicasetCredentialsArgs> credentials;

    /**
     * @return Credentials for the InMemoryDB replicaset.
     * 
     */
    public Output<InmemorydbReplicasetCredentialsArgs> credentials() {
        return this.credentials;
    }

    /**
     * The human readable name of your replica set.
     * 
     */
    @Import(name="displayName", required=true)
    private Output<String> displayName;

    /**
     * @return The human readable name of your replica set.
     * 
     */
    public Output<String> displayName() {
        return this.displayName;
    }

    /**
     * The eviction policy for the replica set.
     * 
     */
    @Import(name="evictionPolicy", required=true)
    private Output<String> evictionPolicy;

    /**
     * @return The eviction policy for the replica set.
     * 
     */
    public Output<String> evictionPolicy() {
        return this.evictionPolicy;
    }

    /**
     * The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
     * 
     */
    @Import(name="initialSnapshotId")
    private @Nullable Output<String> initialSnapshotId;

    /**
     * @return The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
     * 
     */
    public Optional<Output<String>> initialSnapshotId() {
        return Optional.ofNullable(this.initialSnapshotId);
    }

    /**
     * The replica set location
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return The replica set location
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    @Import(name="maintenanceWindow")
    private @Nullable Output<InmemorydbReplicasetMaintenanceWindowArgs> maintenanceWindow;

    /**
     * @return A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    public Optional<Output<InmemorydbReplicasetMaintenanceWindowArgs>> maintenanceWindow() {
        return Optional.ofNullable(this.maintenanceWindow);
    }

    /**
     * Specifies How and If data is persisted.
     * 
     */
    @Import(name="persistenceMode", required=true)
    private Output<String> persistenceMode;

    /**
     * @return Specifies How and If data is persisted.
     * 
     */
    public Output<String> persistenceMode() {
        return this.persistenceMode;
    }

    /**
     * The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the
     * value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only
     * standby for a failure of the active instance.
     * 
     */
    @Import(name="replicas", required=true)
    private Output<Integer> replicas;

    /**
     * @return The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the
     * value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only
     * standby for a failure of the active instance.
     * 
     */
    public Output<Integer> replicas() {
        return this.replicas;
    }

    /**
     * The resources of the individual replicas.
     * 
     */
    @Import(name="resources", required=true)
    private Output<InmemorydbReplicasetResourcesArgs> resources;

    /**
     * @return The resources of the individual replicas.
     * 
     */
    public Output<InmemorydbReplicasetResourcesArgs> resources() {
        return this.resources;
    }

    /**
     * The InMemoryDB version of your replica set.
     * 
     */
    @Import(name="version", required=true)
    private Output<String> version;

    /**
     * @return The InMemoryDB version of your replica set.
     * 
     */
    public Output<String> version() {
        return this.version;
    }

    private InmemorydbReplicasetArgs() {}

    private InmemorydbReplicasetArgs(InmemorydbReplicasetArgs $) {
        this.connections = $.connections;
        this.credentials = $.credentials;
        this.displayName = $.displayName;
        this.evictionPolicy = $.evictionPolicy;
        this.initialSnapshotId = $.initialSnapshotId;
        this.location = $.location;
        this.maintenanceWindow = $.maintenanceWindow;
        this.persistenceMode = $.persistenceMode;
        this.replicas = $.replicas;
        this.resources = $.resources;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InmemorydbReplicasetArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InmemorydbReplicasetArgs $;

        public Builder() {
            $ = new InmemorydbReplicasetArgs();
        }

        public Builder(InmemorydbReplicasetArgs defaults) {
            $ = new InmemorydbReplicasetArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param connections The network connection for your replica set. Only one connection is allowed.
         * 
         * @return builder
         * 
         */
        public Builder connections(Output<InmemorydbReplicasetConnectionsArgs> connections) {
            $.connections = connections;
            return this;
        }

        /**
         * @param connections The network connection for your replica set. Only one connection is allowed.
         * 
         * @return builder
         * 
         */
        public Builder connections(InmemorydbReplicasetConnectionsArgs connections) {
            return connections(Output.of(connections));
        }

        /**
         * @param credentials Credentials for the InMemoryDB replicaset.
         * 
         * @return builder
         * 
         */
        public Builder credentials(Output<InmemorydbReplicasetCredentialsArgs> credentials) {
            $.credentials = credentials;
            return this;
        }

        /**
         * @param credentials Credentials for the InMemoryDB replicaset.
         * 
         * @return builder
         * 
         */
        public Builder credentials(InmemorydbReplicasetCredentialsArgs credentials) {
            return credentials(Output.of(credentials));
        }

        /**
         * @param displayName The human readable name of your replica set.
         * 
         * @return builder
         * 
         */
        public Builder displayName(Output<String> displayName) {
            $.displayName = displayName;
            return this;
        }

        /**
         * @param displayName The human readable name of your replica set.
         * 
         * @return builder
         * 
         */
        public Builder displayName(String displayName) {
            return displayName(Output.of(displayName));
        }

        /**
         * @param evictionPolicy The eviction policy for the replica set.
         * 
         * @return builder
         * 
         */
        public Builder evictionPolicy(Output<String> evictionPolicy) {
            $.evictionPolicy = evictionPolicy;
            return this;
        }

        /**
         * @param evictionPolicy The eviction policy for the replica set.
         * 
         * @return builder
         * 
         */
        public Builder evictionPolicy(String evictionPolicy) {
            return evictionPolicy(Output.of(evictionPolicy));
        }

        /**
         * @param initialSnapshotId The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
         * 
         * @return builder
         * 
         */
        public Builder initialSnapshotId(@Nullable Output<String> initialSnapshotId) {
            $.initialSnapshotId = initialSnapshotId;
            return this;
        }

        /**
         * @param initialSnapshotId The ID of a snapshot to restore the replica set from. If set, the replica set will be created from the snapshot.
         * 
         * @return builder
         * 
         */
        public Builder initialSnapshotId(String initialSnapshotId) {
            return initialSnapshotId(Output.of(initialSnapshotId));
        }

        /**
         * @param location The replica set location
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The replica set location
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param maintenanceWindow A weekly 4 hour-long window, during which maintenance might occur.
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindow(@Nullable Output<InmemorydbReplicasetMaintenanceWindowArgs> maintenanceWindow) {
            $.maintenanceWindow = maintenanceWindow;
            return this;
        }

        /**
         * @param maintenanceWindow A weekly 4 hour-long window, during which maintenance might occur.
         * 
         * @return builder
         * 
         */
        public Builder maintenanceWindow(InmemorydbReplicasetMaintenanceWindowArgs maintenanceWindow) {
            return maintenanceWindow(Output.of(maintenanceWindow));
        }

        /**
         * @param persistenceMode Specifies How and If data is persisted.
         * 
         * @return builder
         * 
         */
        public Builder persistenceMode(Output<String> persistenceMode) {
            $.persistenceMode = persistenceMode;
            return this;
        }

        /**
         * @param persistenceMode Specifies How and If data is persisted.
         * 
         * @return builder
         * 
         */
        public Builder persistenceMode(String persistenceMode) {
            return persistenceMode(Output.of(persistenceMode));
        }

        /**
         * @param replicas The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the
         * value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only
         * standby for a failure of the active instance.
         * 
         * @return builder
         * 
         */
        public Builder replicas(Output<Integer> replicas) {
            $.replicas = replicas;
            return this;
        }

        /**
         * @param replicas The total number of replicas in the replica set (one active and n-1 passive). In case of a standalone instance, the
         * value is 1. In all other cases, the value is &gt; 1. The replicas will not be available as read replicas, they are only
         * standby for a failure of the active instance.
         * 
         * @return builder
         * 
         */
        public Builder replicas(Integer replicas) {
            return replicas(Output.of(replicas));
        }

        /**
         * @param resources The resources of the individual replicas.
         * 
         * @return builder
         * 
         */
        public Builder resources(Output<InmemorydbReplicasetResourcesArgs> resources) {
            $.resources = resources;
            return this;
        }

        /**
         * @param resources The resources of the individual replicas.
         * 
         * @return builder
         * 
         */
        public Builder resources(InmemorydbReplicasetResourcesArgs resources) {
            return resources(Output.of(resources));
        }

        /**
         * @param version The InMemoryDB version of your replica set.
         * 
         * @return builder
         * 
         */
        public Builder version(Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version The InMemoryDB version of your replica set.
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public InmemorydbReplicasetArgs build() {
            if ($.connections == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "connections");
            }
            if ($.credentials == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "credentials");
            }
            if ($.displayName == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "displayName");
            }
            if ($.evictionPolicy == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "evictionPolicy");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "location");
            }
            if ($.persistenceMode == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "persistenceMode");
            }
            if ($.replicas == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "replicas");
            }
            if ($.resources == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "resources");
            }
            if ($.version == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetArgs", "version");
            }
            return $;
        }
    }

}
