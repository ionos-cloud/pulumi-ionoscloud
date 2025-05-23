// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dns.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetZoneArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetZoneArgs Empty = new GetZoneArgs();

    /**
     * [string] The ID of the DNS Zone you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return [string] The ID of the DNS Zone you want to search for.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * [string] The name of the DNS Zone you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the DNS Zone you want to search for.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetZoneArgs() {}

    private GetZoneArgs(GetZoneArgs $) {
        this.id = $.id;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetZoneArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetZoneArgs $;

        public Builder() {
            $ = new GetZoneArgs();
        }

        public Builder(GetZoneArgs defaults) {
            $ = new GetZoneArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id [string] The ID of the DNS Zone you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id [string] The ID of the DNS Zone you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param name [string] The name of the DNS Zone you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the DNS Zone you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param partialMatch [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        /**
         * @param partialMatch [bool] Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Either `id` or `name` must be provided. If none, or both are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetZoneArgs build() {
            return $;
        }
    }

}
