// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.kafka.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetTopicArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetTopicArgs Empty = new GetTopicArgs();

    /**
     * ID of the Kafka Cluster that the topic belongs to.
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return ID of the Kafka Cluster that the topic belongs to.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * ID of an existing Kafka Cluster Topic that you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of an existing Kafka Cluster Topic that you want to search for.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
     * Cluster. Possible values: `de/fra`, `de/txl`
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
     * Cluster. Possible values: `de/fra`, `de/txl`
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * Name of an existing Kafka Cluster Topic that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of an existing Kafka Cluster Topic that you want to search for.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetTopicArgs() {}

    private GetTopicArgs(GetTopicArgs $) {
        this.clusterId = $.clusterId;
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetTopicArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetTopicArgs $;

        public Builder() {
            $ = new GetTopicArgs();
        }

        public Builder(GetTopicArgs defaults) {
            $ = new GetTopicArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId ID of the Kafka Cluster that the topic belongs to.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId ID of the Kafka Cluster that the topic belongs to.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param id ID of an existing Kafka Cluster Topic that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of an existing Kafka Cluster Topic that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
         * Cluster. Possible values: `de/fra`, `de/txl`
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location of the Kafka Cluster Topic. Must be the same as the location of the Kafka
         * Cluster. Possible values: `de/fra`, `de/txl`
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name Name of an existing Kafka Cluster Topic that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of an existing Kafka Cluster Topic that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetTopicArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("GetTopicArgs", "clusterId");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetTopicArgs", "location");
            }
            return $;
        }
    }

}
