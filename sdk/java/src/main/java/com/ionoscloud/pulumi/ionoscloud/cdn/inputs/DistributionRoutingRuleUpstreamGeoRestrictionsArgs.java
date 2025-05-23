// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cdn.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DistributionRoutingRuleUpstreamGeoRestrictionsArgs extends com.pulumi.resources.ResourceArgs {

    public static final DistributionRoutingRuleUpstreamGeoRestrictionsArgs Empty = new DistributionRoutingRuleUpstreamGeoRestrictionsArgs();

    /**
     * [string] List of allowed countries
     * 
     */
    @Import(name="allowLists")
    private @Nullable Output<List<String>> allowLists;

    /**
     * @return [string] List of allowed countries
     * 
     */
    public Optional<Output<List<String>>> allowLists() {
        return Optional.ofNullable(this.allowLists);
    }

    /**
     * [string] List of blocked countries
     * 
     */
    @Import(name="blockLists")
    private @Nullable Output<List<String>> blockLists;

    /**
     * @return [string] List of blocked countries
     * 
     */
    public Optional<Output<List<String>>> blockLists() {
        return Optional.ofNullable(this.blockLists);
    }

    private DistributionRoutingRuleUpstreamGeoRestrictionsArgs() {}

    private DistributionRoutingRuleUpstreamGeoRestrictionsArgs(DistributionRoutingRuleUpstreamGeoRestrictionsArgs $) {
        this.allowLists = $.allowLists;
        this.blockLists = $.blockLists;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DistributionRoutingRuleUpstreamGeoRestrictionsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DistributionRoutingRuleUpstreamGeoRestrictionsArgs $;

        public Builder() {
            $ = new DistributionRoutingRuleUpstreamGeoRestrictionsArgs();
        }

        public Builder(DistributionRoutingRuleUpstreamGeoRestrictionsArgs defaults) {
            $ = new DistributionRoutingRuleUpstreamGeoRestrictionsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param allowLists [string] List of allowed countries
         * 
         * @return builder
         * 
         */
        public Builder allowLists(@Nullable Output<List<String>> allowLists) {
            $.allowLists = allowLists;
            return this;
        }

        /**
         * @param allowLists [string] List of allowed countries
         * 
         * @return builder
         * 
         */
        public Builder allowLists(List<String> allowLists) {
            return allowLists(Output.of(allowLists));
        }

        /**
         * @param allowLists [string] List of allowed countries
         * 
         * @return builder
         * 
         */
        public Builder allowLists(String... allowLists) {
            return allowLists(List.of(allowLists));
        }

        /**
         * @param blockLists [string] List of blocked countries
         * 
         * @return builder
         * 
         */
        public Builder blockLists(@Nullable Output<List<String>> blockLists) {
            $.blockLists = blockLists;
            return this;
        }

        /**
         * @param blockLists [string] List of blocked countries
         * 
         * @return builder
         * 
         */
        public Builder blockLists(List<String> blockLists) {
            return blockLists(Output.of(blockLists));
        }

        /**
         * @param blockLists [string] List of blocked countries
         * 
         * @return builder
         * 
         */
        public Builder blockLists(String... blockLists) {
            return blockLists(List.of(blockLists));
        }

        public DistributionRoutingRuleUpstreamGeoRestrictionsArgs build() {
            return $;
        }
    }

}
