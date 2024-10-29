// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetCdnDistributionRoutingRule;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetCdnDistributionResult {
    /**
     * @return The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     * 
     */
    private String certificateId;
    /**
     * @return The domain of the distribution.
     * 
     */
    private @Nullable String domain;
    private @Nullable String id;
    private @Nullable Boolean partialMatch;
    /**
     * @return IP of the distribution, it has to be included on the domain DNS Zone as A record.
     * 
     */
    private String publicEndpointV4;
    /**
     * @return IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
     * 
     */
    private String publicEndpointV6;
    /**
     * @return Unique resource identifier.
     * 
     */
    private String resourceUrn;
    /**
     * @return The routing rules for the distribution.
     * 
     */
    private List<GetCdnDistributionRoutingRule> routingRules;

    private GetCdnDistributionResult() {}
    /**
     * @return The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     * 
     */
    public String certificateId() {
        return this.certificateId;
    }
    /**
     * @return The domain of the distribution.
     * 
     */
    public Optional<String> domain() {
        return Optional.ofNullable(this.domain);
    }
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public Optional<Boolean> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }
    /**
     * @return IP of the distribution, it has to be included on the domain DNS Zone as A record.
     * 
     */
    public String publicEndpointV4() {
        return this.publicEndpointV4;
    }
    /**
     * @return IP of the distribution, it has to be included on the domain DNS Zone as AAAA record.
     * 
     */
    public String publicEndpointV6() {
        return this.publicEndpointV6;
    }
    /**
     * @return Unique resource identifier.
     * 
     */
    public String resourceUrn() {
        return this.resourceUrn;
    }
    /**
     * @return The routing rules for the distribution.
     * 
     */
    public List<GetCdnDistributionRoutingRule> routingRules() {
        return this.routingRules;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCdnDistributionResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String certificateId;
        private @Nullable String domain;
        private @Nullable String id;
        private @Nullable Boolean partialMatch;
        private String publicEndpointV4;
        private String publicEndpointV6;
        private String resourceUrn;
        private List<GetCdnDistributionRoutingRule> routingRules;
        public Builder() {}
        public Builder(GetCdnDistributionResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.certificateId = defaults.certificateId;
    	      this.domain = defaults.domain;
    	      this.id = defaults.id;
    	      this.partialMatch = defaults.partialMatch;
    	      this.publicEndpointV4 = defaults.publicEndpointV4;
    	      this.publicEndpointV6 = defaults.publicEndpointV6;
    	      this.resourceUrn = defaults.resourceUrn;
    	      this.routingRules = defaults.routingRules;
        }

        @CustomType.Setter
        public Builder certificateId(String certificateId) {
            if (certificateId == null) {
              throw new MissingRequiredPropertyException("GetCdnDistributionResult", "certificateId");
            }
            this.certificateId = certificateId;
            return this;
        }
        @CustomType.Setter
        public Builder domain(@Nullable String domain) {

            this.domain = domain;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder partialMatch(@Nullable Boolean partialMatch) {

            this.partialMatch = partialMatch;
            return this;
        }
        @CustomType.Setter
        public Builder publicEndpointV4(String publicEndpointV4) {
            if (publicEndpointV4 == null) {
              throw new MissingRequiredPropertyException("GetCdnDistributionResult", "publicEndpointV4");
            }
            this.publicEndpointV4 = publicEndpointV4;
            return this;
        }
        @CustomType.Setter
        public Builder publicEndpointV6(String publicEndpointV6) {
            if (publicEndpointV6 == null) {
              throw new MissingRequiredPropertyException("GetCdnDistributionResult", "publicEndpointV6");
            }
            this.publicEndpointV6 = publicEndpointV6;
            return this;
        }
        @CustomType.Setter
        public Builder resourceUrn(String resourceUrn) {
            if (resourceUrn == null) {
              throw new MissingRequiredPropertyException("GetCdnDistributionResult", "resourceUrn");
            }
            this.resourceUrn = resourceUrn;
            return this;
        }
        @CustomType.Setter
        public Builder routingRules(List<GetCdnDistributionRoutingRule> routingRules) {
            if (routingRules == null) {
              throw new MissingRequiredPropertyException("GetCdnDistributionResult", "routingRules");
            }
            this.routingRules = routingRules;
            return this;
        }
        public Builder routingRules(GetCdnDistributionRoutingRule... routingRules) {
            return routingRules(List.of(routingRules));
        }
        public GetCdnDistributionResult build() {
            final var _resultValue = new GetCdnDistributionResult();
            _resultValue.certificateId = certificateId;
            _resultValue.domain = domain;
            _resultValue.id = id;
            _resultValue.partialMatch = partialMatch;
            _resultValue.publicEndpointV4 = publicEndpointV4;
            _resultValue.publicEndpointV6 = publicEndpointV6;
            _resultValue.resourceUrn = resourceUrn;
            _resultValue.routingRules = routingRules;
            return _resultValue;
        }
    }
}
