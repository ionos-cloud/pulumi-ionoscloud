// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.KafkaClusterConnectionsArgs;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class KafkaClusterArgs extends com.pulumi.resources.ResourceArgs {

    public static final KafkaClusterArgs Empty = new KafkaClusterArgs();

    /**
     * Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     * 
     */
    @Import(name="connections", required=true)
    private Output<KafkaClusterConnectionsArgs> connections;

    /**
     * @return Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
     * 
     */
    public Output<KafkaClusterConnectionsArgs> connections() {
        return this.connections;
    }

    /**
     * [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * [string] Name of the Kafka Cluster.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] Name of the Kafka Cluster.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
     * 
     */
    @Import(name="size", required=true)
    private Output<String> size;

    /**
     * @return [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
     * 
     */
    public Output<String> size() {
        return this.size;
    }

    /**
     * [string] Version of the Kafka Cluster. Possible values: `3.7.0`
     * 
     */
    @Import(name="version", required=true)
    private Output<String> version;

    /**
     * @return [string] Version of the Kafka Cluster. Possible values: `3.7.0`
     * 
     */
    public Output<String> version() {
        return this.version;
    }

    private KafkaClusterArgs() {}

    private KafkaClusterArgs(KafkaClusterArgs $) {
        this.connections = $.connections;
        this.location = $.location;
        this.name = $.name;
        this.size = $.size;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KafkaClusterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KafkaClusterArgs $;

        public Builder() {
            $ = new KafkaClusterArgs();
        }

        public Builder(KafkaClusterArgs defaults) {
            $ = new KafkaClusterArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param connections Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder connections(Output<KafkaClusterConnectionsArgs> connections) {
            $.connections = connections;
            return this;
        }

        /**
         * @param connections Connection information of the Kafka Cluster. Minimum items: 1, maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder connections(KafkaClusterConnectionsArgs connections) {
            return connections(Output.of(connections));
        }

        /**
         * @param location [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location [string] The location of the Kafka Cluster. Possible values: `de/fra`, `de/txl`
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] Name of the Kafka Cluster.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] Name of the Kafka Cluster.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param size [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
         * 
         * @return builder
         * 
         */
        public Builder size(Output<String> size) {
            $.size = size;
            return this;
        }

        /**
         * @param size [string] Size of the Kafka Cluster. Possible values: `XS`, `S`
         * 
         * @return builder
         * 
         */
        public Builder size(String size) {
            return size(Output.of(size));
        }

        /**
         * @param version [string] Version of the Kafka Cluster. Possible values: `3.7.0`
         * 
         * @return builder
         * 
         */
        public Builder version(Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version [string] Version of the Kafka Cluster. Possible values: `3.7.0`
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public KafkaClusterArgs build() {
            if ($.connections == null) {
                throw new MissingRequiredPropertyException("KafkaClusterArgs", "connections");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("KafkaClusterArgs", "location");
            }
            if ($.size == null) {
                throw new MissingRequiredPropertyException("KafkaClusterArgs", "size");
            }
            if ($.version == null) {
                throw new MissingRequiredPropertyException("KafkaClusterArgs", "version");
            }
            return $;
        }
    }

}
