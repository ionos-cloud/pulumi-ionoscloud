// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.autoscaling.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetGroupReplicaConfigurationNicFirewallRule {
    /**
     * @return Sets the allowed code (from 0 to 254) when ICMP protocol is selected. The value &#39;null&#39; allows all codes.
     * 
     */
    private Integer icmpCode;
    /**
     * @return Sets the allowed type (from 0 to 254) if the protocol ICMP is selected. The value &#39;null&#39; allows all types.
     * 
     */
    private Integer icmpType;
    /**
     * @return Name of an existing Autoscaling Group that you want to search for.
     * 
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     * 
     */
    private String name;
    /**
     * @return Sets the end range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;port_range_start&#39; and &#39;port_range_end&#39; allows all ports.
     * 
     */
    private Integer portRangeEnd;
    /**
     * @return Sets the initial range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;port_range_start&#39; and &#39;port_range_end&#39; allows all ports.
     * 
     */
    private Integer portRangeStart;
    /**
     * @return The protocol for the rule. The property cannot be modified after its creation (not allowed in update requests).
     * 
     */
    private String protocol;
    /**
     * @return Only traffic originating from the respective IPv4 address is permitted. The value &#39;null&#39; allows traffic from any IP address.
     * 
     */
    private String sourceIp;
    /**
     * @return Only traffic originating from the respective MAC address is permitted. Valid format: &#39;aa:bb:cc:dd:ee:ff&#39;. The value &#39;null&#39; allows traffic from any MAC address.
     * 
     */
    private String sourceMac;
    /**
     * @return If the target NIC has multiple IP addresses, only the traffic directed to the respective IP address of the NIC is allowed. The value &#39;null&#39; allows traffic to any target IP address.
     * 
     */
    private String targetIp;
    /**
     * @return Type of resource
     * 
     */
    private String type;

    private GetGroupReplicaConfigurationNicFirewallRule() {}
    /**
     * @return Sets the allowed code (from 0 to 254) when ICMP protocol is selected. The value &#39;null&#39; allows all codes.
     * 
     */
    public Integer icmpCode() {
        return this.icmpCode;
    }
    /**
     * @return Sets the allowed type (from 0 to 254) if the protocol ICMP is selected. The value &#39;null&#39; allows all types.
     * 
     */
    public Integer icmpType() {
        return this.icmpType;
    }
    /**
     * @return Name of an existing Autoscaling Group that you want to search for.
     * 
     * Either `name` or `id` must be provided. If none or both are provided, the datasource will return an error.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Sets the end range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;port_range_start&#39; and &#39;port_range_end&#39; allows all ports.
     * 
     */
    public Integer portRangeEnd() {
        return this.portRangeEnd;
    }
    /**
     * @return Sets the initial range of the allowed port (from 1 to 65535) if the protocol TCP or UDP is selected. The value &#39;null&#39; for &#39;port_range_start&#39; and &#39;port_range_end&#39; allows all ports.
     * 
     */
    public Integer portRangeStart() {
        return this.portRangeStart;
    }
    /**
     * @return The protocol for the rule. The property cannot be modified after its creation (not allowed in update requests).
     * 
     */
    public String protocol() {
        return this.protocol;
    }
    /**
     * @return Only traffic originating from the respective IPv4 address is permitted. The value &#39;null&#39; allows traffic from any IP address.
     * 
     */
    public String sourceIp() {
        return this.sourceIp;
    }
    /**
     * @return Only traffic originating from the respective MAC address is permitted. Valid format: &#39;aa:bb:cc:dd:ee:ff&#39;. The value &#39;null&#39; allows traffic from any MAC address.
     * 
     */
    public String sourceMac() {
        return this.sourceMac;
    }
    /**
     * @return If the target NIC has multiple IP addresses, only the traffic directed to the respective IP address of the NIC is allowed. The value &#39;null&#39; allows traffic to any target IP address.
     * 
     */
    public String targetIp() {
        return this.targetIp;
    }
    /**
     * @return Type of resource
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetGroupReplicaConfigurationNicFirewallRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer icmpCode;
        private Integer icmpType;
        private String name;
        private Integer portRangeEnd;
        private Integer portRangeStart;
        private String protocol;
        private String sourceIp;
        private String sourceMac;
        private String targetIp;
        private String type;
        public Builder() {}
        public Builder(GetGroupReplicaConfigurationNicFirewallRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.icmpCode = defaults.icmpCode;
    	      this.icmpType = defaults.icmpType;
    	      this.name = defaults.name;
    	      this.portRangeEnd = defaults.portRangeEnd;
    	      this.portRangeStart = defaults.portRangeStart;
    	      this.protocol = defaults.protocol;
    	      this.sourceIp = defaults.sourceIp;
    	      this.sourceMac = defaults.sourceMac;
    	      this.targetIp = defaults.targetIp;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder icmpCode(Integer icmpCode) {
            if (icmpCode == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "icmpCode");
            }
            this.icmpCode = icmpCode;
            return this;
        }
        @CustomType.Setter
        public Builder icmpType(Integer icmpType) {
            if (icmpType == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "icmpType");
            }
            this.icmpType = icmpType;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeEnd(Integer portRangeEnd) {
            if (portRangeEnd == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "portRangeEnd");
            }
            this.portRangeEnd = portRangeEnd;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeStart(Integer portRangeStart) {
            if (portRangeStart == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "portRangeStart");
            }
            this.portRangeStart = portRangeStart;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder sourceIp(String sourceIp) {
            if (sourceIp == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "sourceIp");
            }
            this.sourceIp = sourceIp;
            return this;
        }
        @CustomType.Setter
        public Builder sourceMac(String sourceMac) {
            if (sourceMac == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "sourceMac");
            }
            this.sourceMac = sourceMac;
            return this;
        }
        @CustomType.Setter
        public Builder targetIp(String targetIp) {
            if (targetIp == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "targetIp");
            }
            this.targetIp = targetIp;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetGroupReplicaConfigurationNicFirewallRule", "type");
            }
            this.type = type;
            return this;
        }
        public GetGroupReplicaConfigurationNicFirewallRule build() {
            final var _resultValue = new GetGroupReplicaConfigurationNicFirewallRule();
            _resultValue.icmpCode = icmpCode;
            _resultValue.icmpType = icmpType;
            _resultValue.name = name;
            _resultValue.portRangeEnd = portRangeEnd;
            _resultValue.portRangeStart = portRangeStart;
            _resultValue.protocol = protocol;
            _resultValue.sourceIp = sourceIp;
            _resultValue.sourceMac = sourceMac;
            _resultValue.targetIp = targetIp;
            _resultValue.type = type;
            return _resultValue;
        }
    }
}
