// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cdn;

import com.ionoscloud.pulumi.ionoscloud.cdn.inputs.DistributionRoutingRuleArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class DistributionArgs extends com.pulumi.resources.ResourceArgs {

    public static final DistributionArgs Empty = new DistributionArgs();

    /**
     * [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     * 
     */
    @Import(name="certificateId")
    private @Nullable Output<String> certificateId;

    /**
     * @return [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
     * 
     */
    public Optional<Output<String>> certificateId() {
        return Optional.ofNullable(this.certificateId);
    }

    /**
     * [string] The domain of the distribution.
     * 
     */
    @Import(name="domain", required=true)
    private Output<String> domain;

    /**
     * @return [string] The domain of the distribution.
     * 
     */
    public Output<String> domain() {
        return this.domain;
    }

    /**
     * [list] The routing rules for the distribution.
     * 
     */
    @Import(name="routingRules", required=true)
    private Output<List<DistributionRoutingRuleArgs>> routingRules;

    /**
     * @return [list] The routing rules for the distribution.
     * 
     */
    public Output<List<DistributionRoutingRuleArgs>> routingRules() {
        return this.routingRules;
    }

    private DistributionArgs() {}

    private DistributionArgs(DistributionArgs $) {
        this.certificateId = $.certificateId;
        this.domain = $.domain;
        this.routingRules = $.routingRules;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DistributionArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DistributionArgs $;

        public Builder() {
            $ = new DistributionArgs();
        }

        public Builder(DistributionArgs defaults) {
            $ = new DistributionArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param certificateId [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
         * 
         * @return builder
         * 
         */
        public Builder certificateId(@Nullable Output<String> certificateId) {
            $.certificateId = certificateId;
            return this;
        }

        /**
         * @param certificateId [string] The ID of the certificate to use for the distribution. You can create certificates with the certificate resource.
         * 
         * @return builder
         * 
         */
        public Builder certificateId(String certificateId) {
            return certificateId(Output.of(certificateId));
        }

        /**
         * @param domain [string] The domain of the distribution.
         * 
         * @return builder
         * 
         */
        public Builder domain(Output<String> domain) {
            $.domain = domain;
            return this;
        }

        /**
         * @param domain [string] The domain of the distribution.
         * 
         * @return builder
         * 
         */
        public Builder domain(String domain) {
            return domain(Output.of(domain));
        }

        /**
         * @param routingRules [list] The routing rules for the distribution.
         * 
         * @return builder
         * 
         */
        public Builder routingRules(Output<List<DistributionRoutingRuleArgs>> routingRules) {
            $.routingRules = routingRules;
            return this;
        }

        /**
         * @param routingRules [list] The routing rules for the distribution.
         * 
         * @return builder
         * 
         */
        public Builder routingRules(List<DistributionRoutingRuleArgs> routingRules) {
            return routingRules(Output.of(routingRules));
        }

        /**
         * @param routingRules [list] The routing rules for the distribution.
         * 
         * @return builder
         * 
         */
        public Builder routingRules(DistributionRoutingRuleArgs... routingRules) {
            return routingRules(List.of(routingRules));
        }

        public DistributionArgs build() {
            if ($.domain == null) {
                throw new MissingRequiredPropertyException("DistributionArgs", "domain");
            }
            if ($.routingRules == null) {
                throw new MissingRequiredPropertyException("DistributionArgs", "routingRules");
            }
            return $;
        }
    }

}
