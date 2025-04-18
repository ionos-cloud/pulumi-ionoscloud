// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cdn.outputs;

import com.ionoscloud.pulumi.ionoscloud.cdn.outputs.DistributionRoutingRuleUpstream;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class DistributionRoutingRule {
    /**
     * @return [string] The prefix of the routing rule.
     * 
     */
    private String prefix;
    /**
     * @return [string] The scheme of the routing rule.
     * 
     */
    private String scheme;
    /**
     * @return [map] - A map of properties for the rule
     * 
     */
    private DistributionRoutingRuleUpstream upstream;

    private DistributionRoutingRule() {}
    /**
     * @return [string] The prefix of the routing rule.
     * 
     */
    public String prefix() {
        return this.prefix;
    }
    /**
     * @return [string] The scheme of the routing rule.
     * 
     */
    public String scheme() {
        return this.scheme;
    }
    /**
     * @return [map] - A map of properties for the rule
     * 
     */
    public DistributionRoutingRuleUpstream upstream() {
        return this.upstream;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(DistributionRoutingRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String prefix;
        private String scheme;
        private DistributionRoutingRuleUpstream upstream;
        public Builder() {}
        public Builder(DistributionRoutingRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.prefix = defaults.prefix;
    	      this.scheme = defaults.scheme;
    	      this.upstream = defaults.upstream;
        }

        @CustomType.Setter
        public Builder prefix(String prefix) {
            if (prefix == null) {
              throw new MissingRequiredPropertyException("DistributionRoutingRule", "prefix");
            }
            this.prefix = prefix;
            return this;
        }
        @CustomType.Setter
        public Builder scheme(String scheme) {
            if (scheme == null) {
              throw new MissingRequiredPropertyException("DistributionRoutingRule", "scheme");
            }
            this.scheme = scheme;
            return this;
        }
        @CustomType.Setter
        public Builder upstream(DistributionRoutingRuleUpstream upstream) {
            if (upstream == null) {
              throw new MissingRequiredPropertyException("DistributionRoutingRule", "upstream");
            }
            this.upstream = upstream;
            return this;
        }
        public DistributionRoutingRule build() {
            final var _resultValue = new DistributionRoutingRule();
            _resultValue.prefix = prefix;
            _resultValue.scheme = scheme;
            _resultValue.upstream = upstream;
            return _resultValue;
        }
    }
}
