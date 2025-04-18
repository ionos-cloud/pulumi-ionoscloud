// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetResourceArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetResourceArgs Empty = new GetResourceArgs();

    /**
     * The ID of the specific resource to retrieve information about.
     * 
     */
    @Import(name="resourceId")
    private @Nullable Output<String> resourceId;

    /**
     * @return The ID of the specific resource to retrieve information about.
     * 
     */
    public Optional<Output<String>> resourceId() {
        return Optional.ofNullable(this.resourceId);
    }

    /**
     * The specific type of resources to retrieve information about.
     * 
     */
    @Import(name="resourceType")
    private @Nullable Output<String> resourceType;

    /**
     * @return The specific type of resources to retrieve information about.
     * 
     */
    public Optional<Output<String>> resourceType() {
        return Optional.ofNullable(this.resourceType);
    }

    private GetResourceArgs() {}

    private GetResourceArgs(GetResourceArgs $) {
        this.resourceId = $.resourceId;
        this.resourceType = $.resourceType;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetResourceArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetResourceArgs $;

        public Builder() {
            $ = new GetResourceArgs();
        }

        public Builder(GetResourceArgs defaults) {
            $ = new GetResourceArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param resourceId The ID of the specific resource to retrieve information about.
         * 
         * @return builder
         * 
         */
        public Builder resourceId(@Nullable Output<String> resourceId) {
            $.resourceId = resourceId;
            return this;
        }

        /**
         * @param resourceId The ID of the specific resource to retrieve information about.
         * 
         * @return builder
         * 
         */
        public Builder resourceId(String resourceId) {
            return resourceId(Output.of(resourceId));
        }

        /**
         * @param resourceType The specific type of resources to retrieve information about.
         * 
         * @return builder
         * 
         */
        public Builder resourceType(@Nullable Output<String> resourceType) {
            $.resourceType = resourceType;
            return this;
        }

        /**
         * @param resourceType The specific type of resources to retrieve information about.
         * 
         * @return builder
         * 
         */
        public Builder resourceType(String resourceType) {
            return resourceType(Output.of(resourceType));
        }

        public GetResourceArgs build() {
            return $;
        }
    }

}
