// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cdn.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetDistributionRoutingRuleUpstreamGeoRestriction {
    /**
     * @return List of allowed countries
     * 
     */
    private List<String> allowLists;
    /**
     * @return List of blocked countries
     * 
     */
    private List<String> blockLists;

    private GetDistributionRoutingRuleUpstreamGeoRestriction() {}
    /**
     * @return List of allowed countries
     * 
     */
    public List<String> allowLists() {
        return this.allowLists;
    }
    /**
     * @return List of blocked countries
     * 
     */
    public List<String> blockLists() {
        return this.blockLists;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDistributionRoutingRuleUpstreamGeoRestriction defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> allowLists;
        private List<String> blockLists;
        public Builder() {}
        public Builder(GetDistributionRoutingRuleUpstreamGeoRestriction defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.allowLists = defaults.allowLists;
    	      this.blockLists = defaults.blockLists;
        }

        @CustomType.Setter
        public Builder allowLists(List<String> allowLists) {
            if (allowLists == null) {
              throw new MissingRequiredPropertyException("GetDistributionRoutingRuleUpstreamGeoRestriction", "allowLists");
            }
            this.allowLists = allowLists;
            return this;
        }
        public Builder allowLists(String... allowLists) {
            return allowLists(List.of(allowLists));
        }
        @CustomType.Setter
        public Builder blockLists(List<String> blockLists) {
            if (blockLists == null) {
              throw new MissingRequiredPropertyException("GetDistributionRoutingRuleUpstreamGeoRestriction", "blockLists");
            }
            this.blockLists = blockLists;
            return this;
        }
        public Builder blockLists(String... blockLists) {
            return blockLists(List.of(blockLists));
        }
        public GetDistributionRoutingRuleUpstreamGeoRestriction build() {
            final var _resultValue = new GetDistributionRoutingRuleUpstreamGeoRestriction();
            _resultValue.allowLists = allowLists;
            _resultValue.blockLists = blockLists;
            return _resultValue;
        }
    }
}
