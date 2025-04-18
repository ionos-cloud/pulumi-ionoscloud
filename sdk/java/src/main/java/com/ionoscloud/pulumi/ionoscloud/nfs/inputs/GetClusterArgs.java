// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.nfs.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetClusterArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetClusterArgs Empty = new GetClusterArgs();

    /**
     * ID of the Network File Storage cluster.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of the Network File Storage cluster.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The location where the Network File Storage cluster is located.
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return The location where the Network File Storage cluster is located.
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * Name of the Network File Storage cluster.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the Network File Storage cluster.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetClusterArgs() {}

    private GetClusterArgs(GetClusterArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetClusterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetClusterArgs $;

        public Builder() {
            $ = new GetClusterArgs();
        }

        public Builder(GetClusterArgs defaults) {
            $ = new GetClusterArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location The location where the Network File Storage cluster is located.
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location where the Network File Storage cluster is located.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name Name of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetClusterArgs build() {
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetClusterArgs", "location");
            }
            return $;
        }
    }

}
