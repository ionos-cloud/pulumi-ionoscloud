// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetNetworkloadbalancerForwardingruleHealthCheck;
import com.pulumi.ionoscloud.outputs.GetNetworkloadbalancerForwardingruleTarget;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetNetworkloadbalancerForwardingruleResult {
    /**
     * @return Algorithm for the balancing.
     * 
     */
    private String algorithm;
    private String datacenterId;
    /**
     * @return Health check attributes for Network Load Balancer forwarding rule target.
     * 
     */
    private List<GetNetworkloadbalancerForwardingruleHealthCheck> healthChecks;
    /**
     * @return The id of that Network Load Balancer forwarding rule.
     * 
     */
    private @Nullable String id;
    /**
     * @return Listening IP. (inbound)
     * 
     */
    private String listenerIp;
    /**
     * @return Listening port number. (inbound) (range: 1 to 65535)
     * 
     */
    private Integer listenerPort;
    /**
     * @return The name of that Network Load Balancer forwarding rule.
     * 
     */
    private @Nullable String name;
    private String networkloadbalancerId;
    /**
     * @return Protocol of the balancing.
     * 
     */
    private String protocol;
    /**
     * @return Array of items in that collection.
     * 
     */
    private List<GetNetworkloadbalancerForwardingruleTarget> targets;

    private GetNetworkloadbalancerForwardingruleResult() {}
    /**
     * @return Algorithm for the balancing.
     * 
     */
    public String algorithm() {
        return this.algorithm;
    }
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return Health check attributes for Network Load Balancer forwarding rule target.
     * 
     */
    public List<GetNetworkloadbalancerForwardingruleHealthCheck> healthChecks() {
        return this.healthChecks;
    }
    /**
     * @return The id of that Network Load Balancer forwarding rule.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return Listening IP. (inbound)
     * 
     */
    public String listenerIp() {
        return this.listenerIp;
    }
    /**
     * @return Listening port number. (inbound) (range: 1 to 65535)
     * 
     */
    public Integer listenerPort() {
        return this.listenerPort;
    }
    /**
     * @return The name of that Network Load Balancer forwarding rule.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    public String networkloadbalancerId() {
        return this.networkloadbalancerId;
    }
    /**
     * @return Protocol of the balancing.
     * 
     */
    public String protocol() {
        return this.protocol;
    }
    /**
     * @return Array of items in that collection.
     * 
     */
    public List<GetNetworkloadbalancerForwardingruleTarget> targets() {
        return this.targets;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetNetworkloadbalancerForwardingruleResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String algorithm;
        private String datacenterId;
        private List<GetNetworkloadbalancerForwardingruleHealthCheck> healthChecks;
        private @Nullable String id;
        private String listenerIp;
        private Integer listenerPort;
        private @Nullable String name;
        private String networkloadbalancerId;
        private String protocol;
        private List<GetNetworkloadbalancerForwardingruleTarget> targets;
        public Builder() {}
        public Builder(GetNetworkloadbalancerForwardingruleResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.algorithm = defaults.algorithm;
    	      this.datacenterId = defaults.datacenterId;
    	      this.healthChecks = defaults.healthChecks;
    	      this.id = defaults.id;
    	      this.listenerIp = defaults.listenerIp;
    	      this.listenerPort = defaults.listenerPort;
    	      this.name = defaults.name;
    	      this.networkloadbalancerId = defaults.networkloadbalancerId;
    	      this.protocol = defaults.protocol;
    	      this.targets = defaults.targets;
        }

        @CustomType.Setter
        public Builder algorithm(String algorithm) {
            if (algorithm == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "algorithm");
            }
            this.algorithm = algorithm;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder healthChecks(List<GetNetworkloadbalancerForwardingruleHealthCheck> healthChecks) {
            if (healthChecks == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "healthChecks");
            }
            this.healthChecks = healthChecks;
            return this;
        }
        public Builder healthChecks(GetNetworkloadbalancerForwardingruleHealthCheck... healthChecks) {
            return healthChecks(List.of(healthChecks));
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder listenerIp(String listenerIp) {
            if (listenerIp == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "listenerIp");
            }
            this.listenerIp = listenerIp;
            return this;
        }
        @CustomType.Setter
        public Builder listenerPort(Integer listenerPort) {
            if (listenerPort == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "listenerPort");
            }
            this.listenerPort = listenerPort;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder networkloadbalancerId(String networkloadbalancerId) {
            if (networkloadbalancerId == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "networkloadbalancerId");
            }
            this.networkloadbalancerId = networkloadbalancerId;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder targets(List<GetNetworkloadbalancerForwardingruleTarget> targets) {
            if (targets == null) {
              throw new MissingRequiredPropertyException("GetNetworkloadbalancerForwardingruleResult", "targets");
            }
            this.targets = targets;
            return this;
        }
        public Builder targets(GetNetworkloadbalancerForwardingruleTarget... targets) {
            return targets(List.of(targets));
        }
        public GetNetworkloadbalancerForwardingruleResult build() {
            final var _resultValue = new GetNetworkloadbalancerForwardingruleResult();
            _resultValue.algorithm = algorithm;
            _resultValue.datacenterId = datacenterId;
            _resultValue.healthChecks = healthChecks;
            _resultValue.id = id;
            _resultValue.listenerIp = listenerIp;
            _resultValue.listenerPort = listenerPort;
            _resultValue.name = name;
            _resultValue.networkloadbalancerId = networkloadbalancerId;
            _resultValue.protocol = protocol;
            _resultValue.targets = targets;
            return _resultValue;
        }
    }
}
