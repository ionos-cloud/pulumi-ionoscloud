// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class CrossconnectConnectableDatacenterArgs extends com.pulumi.resources.ResourceArgs {

    public static final CrossconnectConnectableDatacenterArgs Empty = new CrossconnectConnectableDatacenterArgs();

    /**
     * The UUID of the connectable datacenter
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return The UUID of the connectable datacenter
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The physical location of the connectable datacenter
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return The physical location of the connectable datacenter
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * [string] The name of the cross-connection.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the cross-connection.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    private CrossconnectConnectableDatacenterArgs() {}

    private CrossconnectConnectableDatacenterArgs(CrossconnectConnectableDatacenterArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(CrossconnectConnectableDatacenterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private CrossconnectConnectableDatacenterArgs $;

        public Builder() {
            $ = new CrossconnectConnectableDatacenterArgs();
        }

        public Builder(CrossconnectConnectableDatacenterArgs defaults) {
            $ = new CrossconnectConnectableDatacenterArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id The UUID of the connectable datacenter
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id The UUID of the connectable datacenter
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location The physical location of the connectable datacenter
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The physical location of the connectable datacenter
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] The name of the cross-connection.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the cross-connection.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public CrossconnectConnectableDatacenterArgs build() {
            return $;
        }
    }

}
