// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetDataplatformNodePoolsArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetDataplatformNodePoolsArgs Empty = new GetDataplatformNodePoolsArgs();

    /**
     * ID of the cluster the searched node pool is part of.
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return ID of the cluster the searched node pool is part of.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using name argument. Default value is false.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    private GetDataplatformNodePoolsArgs() {}

    private GetDataplatformNodePoolsArgs(GetDataplatformNodePoolsArgs $) {
        this.clusterId = $.clusterId;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetDataplatformNodePoolsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetDataplatformNodePoolsArgs $;

        public Builder() {
            $ = new GetDataplatformNodePoolsArgs();
        }

        public Builder(GetDataplatformNodePoolsArgs defaults) {
            $ = new GetDataplatformNodePoolsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId ID of the cluster the searched node pool is part of.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId ID of the cluster the searched node pool is part of.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param name Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of an existing cluster that you want to search for. Search by name is case-insensitive. The whole resource name is required if `partial_match` parameter is not set to true.
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
         * @return builder
         * 
         */
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        public GetDataplatformNodePoolsArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("GetDataplatformNodePoolsArgs", "clusterId");
            }
            return $;
        }
    }

}
