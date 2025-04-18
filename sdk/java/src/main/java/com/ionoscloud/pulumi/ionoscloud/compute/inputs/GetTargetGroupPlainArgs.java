// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetTargetGroupPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetTargetGroupPlainArgs Empty = new GetTargetGroupPlainArgs();

    /**
     * ID of the target group you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of the target group you want to search for.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Boolean partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public Optional<Boolean> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetTargetGroupPlainArgs() {}

    private GetTargetGroupPlainArgs(GetTargetGroupPlainArgs $) {
        this.id = $.id;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetTargetGroupPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetTargetGroupPlainArgs $;

        public Builder() {
            $ = new GetTargetGroupPlainArgs();
        }

        public Builder(GetTargetGroupPlainArgs defaults) {
            $ = new GetTargetGroupPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of the target group you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param name Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Boolean partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        public GetTargetGroupPlainArgs build() {
            return $;
        }
    }

}
