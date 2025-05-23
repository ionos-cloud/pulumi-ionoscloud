// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetTargetGroupArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetTargetGroupArgs Empty = new GetTargetGroupArgs();

    /**
     * ID of the target group you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of the target group you want to search for.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetTargetGroupArgs() {}

    private GetTargetGroupArgs(GetTargetGroupArgs $) {
        this.id = $.id;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetTargetGroupArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetTargetGroupArgs $;

        public Builder() {
            $ = new GetTargetGroupArgs();
        }

        public Builder(GetTargetGroupArgs defaults) {
            $ = new GetTargetGroupArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of the target group you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of the target group you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param name Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of an existing target group that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using name argument. Default value is false.
         * 
         * Either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
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
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetTargetGroupArgs build() {
            return $;
        }
    }

}
