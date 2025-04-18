// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetLocationPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetLocationPlainArgs Empty = new GetLocationPlainArgs();

    /**
     * A desired feature that the location must be able to provide.
     * 
     */
    @Import(name="feature")
    private @Nullable String feature;

    /**
     * @return A desired feature that the location must be able to provide.
     * 
     */
    public Optional<String> feature() {
        return Optional.ofNullable(this.feature);
    }

    /**
     * Name of the location to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of the location to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetLocationPlainArgs() {}

    private GetLocationPlainArgs(GetLocationPlainArgs $) {
        this.feature = $.feature;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetLocationPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetLocationPlainArgs $;

        public Builder() {
            $ = new GetLocationPlainArgs();
        }

        public Builder(GetLocationPlainArgs defaults) {
            $ = new GetLocationPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param feature A desired feature that the location must be able to provide.
         * 
         * @return builder
         * 
         */
        public Builder feature(@Nullable String feature) {
            $.feature = feature;
            return this;
        }

        /**
         * @param name Name of the location to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetLocationPlainArgs build() {
            return $;
        }
    }

}
