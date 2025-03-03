// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class PgDatabaseState extends com.pulumi.resources.ResourceArgs {

    public static final PgDatabaseState Empty = new PgDatabaseState();

    @Import(name="clusterId")
    private @Nullable Output<String> clusterId;

    public Optional<Output<String>> clusterId() {
        return Optional.ofNullable(this.clusterId);
    }

    /**
     * The databasename of a given database.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The databasename of a given database.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The name of the role owning a given database.
     * 
     */
    @Import(name="owner")
    private @Nullable Output<String> owner;

    /**
     * @return The name of the role owning a given database.
     * 
     */
    public Optional<Output<String>> owner() {
        return Optional.ofNullable(this.owner);
    }

    private PgDatabaseState() {}

    private PgDatabaseState(PgDatabaseState $) {
        this.clusterId = $.clusterId;
        this.name = $.name;
        this.owner = $.owner;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(PgDatabaseState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private PgDatabaseState $;

        public Builder() {
            $ = new PgDatabaseState();
        }

        public Builder(PgDatabaseState defaults) {
            $ = new PgDatabaseState(Objects.requireNonNull(defaults));
        }

        public Builder clusterId(@Nullable Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param name The databasename of a given database.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The databasename of a given database.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param owner The name of the role owning a given database.
         * 
         * @return builder
         * 
         */
        public Builder owner(@Nullable Output<String> owner) {
            $.owner = owner;
            return this;
        }

        /**
         * @param owner The name of the role owning a given database.
         * 
         * @return builder
         * 
         */
        public Builder owner(String owner) {
            return owner(Output.of(owner));
        }

        public PgDatabaseState build() {
            return $;
        }
    }

}
