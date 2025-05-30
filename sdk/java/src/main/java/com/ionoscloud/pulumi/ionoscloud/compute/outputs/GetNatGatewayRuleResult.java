// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.ionoscloud.pulumi.ionoscloud.compute.outputs.GetNatGatewayRuleTargetPortRange;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetNatGatewayRuleResult {
    private String datacenterId;
    /**
     * @return Id of the NAT gateway rule
     * 
     */
    private String id;
    /**
     * @return Name of the NAT gateway rule
     * 
     */
    private String name;
    private String natgatewayId;
    /**
     * @return Protocol of the NAT gateway rule. Defaults to ALL. If protocol is &#39;ICMP&#39; then targetPortRange start and end cannot be set.
     * 
     */
    private String protocol;
    /**
     * @return Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource
     * 
     */
    private String publicIp;
    /**
     * @return Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
     * 
     */
    private String sourceSubnet;
    /**
     * @return Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port
     * 
     */
    private List<GetNatGatewayRuleTargetPortRange> targetPortRanges;
    /**
     * @return Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
     * 
     */
    private String targetSubnet;
    /**
     * @return ype of the NAT gateway rule.
     * 
     */
    private String type;

    private GetNatGatewayRuleResult() {}
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return Id of the NAT gateway rule
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Name of the NAT gateway rule
     * 
     */
    public String name() {
        return this.name;
    }
    public String natgatewayId() {
        return this.natgatewayId;
    }
    /**
     * @return Protocol of the NAT gateway rule. Defaults to ALL. If protocol is &#39;ICMP&#39; then targetPortRange start and end cannot be set.
     * 
     */
    public String protocol() {
        return this.protocol;
    }
    /**
     * @return Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource
     * 
     */
    public String publicIp() {
        return this.publicIp;
    }
    /**
     * @return Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
     * 
     */
    public String sourceSubnet() {
        return this.sourceSubnet;
    }
    /**
     * @return Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port
     * 
     */
    public List<GetNatGatewayRuleTargetPortRange> targetPortRanges() {
        return this.targetPortRanges;
    }
    /**
     * @return Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
     * 
     */
    public String targetSubnet() {
        return this.targetSubnet;
    }
    /**
     * @return ype of the NAT gateway rule.
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetNatGatewayRuleResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String datacenterId;
        private String id;
        private String name;
        private String natgatewayId;
        private String protocol;
        private String publicIp;
        private String sourceSubnet;
        private List<GetNatGatewayRuleTargetPortRange> targetPortRanges;
        private String targetSubnet;
        private String type;
        public Builder() {}
        public Builder(GetNatGatewayRuleResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.datacenterId = defaults.datacenterId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.natgatewayId = defaults.natgatewayId;
    	      this.protocol = defaults.protocol;
    	      this.publicIp = defaults.publicIp;
    	      this.sourceSubnet = defaults.sourceSubnet;
    	      this.targetPortRanges = defaults.targetPortRanges;
    	      this.targetSubnet = defaults.targetSubnet;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder natgatewayId(String natgatewayId) {
            if (natgatewayId == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "natgatewayId");
            }
            this.natgatewayId = natgatewayId;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder publicIp(String publicIp) {
            if (publicIp == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "publicIp");
            }
            this.publicIp = publicIp;
            return this;
        }
        @CustomType.Setter
        public Builder sourceSubnet(String sourceSubnet) {
            if (sourceSubnet == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "sourceSubnet");
            }
            this.sourceSubnet = sourceSubnet;
            return this;
        }
        @CustomType.Setter
        public Builder targetPortRanges(List<GetNatGatewayRuleTargetPortRange> targetPortRanges) {
            if (targetPortRanges == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "targetPortRanges");
            }
            this.targetPortRanges = targetPortRanges;
            return this;
        }
        public Builder targetPortRanges(GetNatGatewayRuleTargetPortRange... targetPortRanges) {
            return targetPortRanges(List.of(targetPortRanges));
        }
        @CustomType.Setter
        public Builder targetSubnet(String targetSubnet) {
            if (targetSubnet == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "targetSubnet");
            }
            this.targetSubnet = targetSubnet;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetNatGatewayRuleResult", "type");
            }
            this.type = type;
            return this;
        }
        public GetNatGatewayRuleResult build() {
            final var _resultValue = new GetNatGatewayRuleResult();
            _resultValue.datacenterId = datacenterId;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.natgatewayId = natgatewayId;
            _resultValue.protocol = protocol;
            _resultValue.publicIp = publicIp;
            _resultValue.sourceSubnet = sourceSubnet;
            _resultValue.targetPortRanges = targetPortRanges;
            _resultValue.targetSubnet = targetSubnet;
            _resultValue.type = type;
            return _resultValue;
        }
    }
}
