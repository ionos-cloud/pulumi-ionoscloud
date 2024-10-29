// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetVcpuServerNicFirewallRule {
    /**
     * @return Defines the allowed code (from 0 to 254) if protocol ICMP is chosen
     * 
     */
    private Integer icmpCode;
    /**
     * @return Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen
     * 
     */
    private Integer icmpType;
    /**
     * @return ID of the server you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    private String id;
    /**
     * @return Name of an existing server that you want to search for.
     * 
     */
    private String name;
    /**
     * @return Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen
     * 
     */
    private Integer portRangeEnd;
    /**
     * @return Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen
     * 
     */
    private Integer portRangeStart;
    /**
     * @return he protocol for the rule
     * 
     */
    private String protocol;
    /**
     * @return Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs
     * 
     */
    private String sourceIp;
    /**
     * @return Only traffic originating from the respective MAC address is allowed
     * 
     */
    private String sourceMac;
    /**
     * @return In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed
     * 
     */
    private String targetIp;
    /**
     * @return The type of firewall rule
     * 
     */
    private String type;

    private GetVcpuServerNicFirewallRule() {}
    /**
     * @return Defines the allowed code (from 0 to 254) if protocol ICMP is chosen
     * 
     */
    public Integer icmpCode() {
        return this.icmpCode;
    }
    /**
     * @return Defines the allowed type (from 0 to 254) if the protocol ICMP is chosen
     * 
     */
    public Integer icmpType() {
        return this.icmpType;
    }
    /**
     * @return ID of the server you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Name of an existing server that you want to search for.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen
     * 
     */
    public Integer portRangeEnd() {
        return this.portRangeEnd;
    }
    /**
     * @return Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen
     * 
     */
    public Integer portRangeStart() {
        return this.portRangeStart;
    }
    /**
     * @return he protocol for the rule
     * 
     */
    public String protocol() {
        return this.protocol;
    }
    /**
     * @return Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs
     * 
     */
    public String sourceIp() {
        return this.sourceIp;
    }
    /**
     * @return Only traffic originating from the respective MAC address is allowed
     * 
     */
    public String sourceMac() {
        return this.sourceMac;
    }
    /**
     * @return In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed
     * 
     */
    public String targetIp() {
        return this.targetIp;
    }
    /**
     * @return The type of firewall rule
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVcpuServerNicFirewallRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer icmpCode;
        private Integer icmpType;
        private String id;
        private String name;
        private Integer portRangeEnd;
        private Integer portRangeStart;
        private String protocol;
        private String sourceIp;
        private String sourceMac;
        private String targetIp;
        private String type;
        public Builder() {}
        public Builder(GetVcpuServerNicFirewallRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.icmpCode = defaults.icmpCode;
    	      this.icmpType = defaults.icmpType;
    	      this.id = defaults.id;
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
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "icmpCode");
            }
            this.icmpCode = icmpCode;
            return this;
        }
        @CustomType.Setter
        public Builder icmpType(Integer icmpType) {
            if (icmpType == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "icmpType");
            }
            this.icmpType = icmpType;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeEnd(Integer portRangeEnd) {
            if (portRangeEnd == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "portRangeEnd");
            }
            this.portRangeEnd = portRangeEnd;
            return this;
        }
        @CustomType.Setter
        public Builder portRangeStart(Integer portRangeStart) {
            if (portRangeStart == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "portRangeStart");
            }
            this.portRangeStart = portRangeStart;
            return this;
        }
        @CustomType.Setter
        public Builder protocol(String protocol) {
            if (protocol == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "protocol");
            }
            this.protocol = protocol;
            return this;
        }
        @CustomType.Setter
        public Builder sourceIp(String sourceIp) {
            if (sourceIp == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "sourceIp");
            }
            this.sourceIp = sourceIp;
            return this;
        }
        @CustomType.Setter
        public Builder sourceMac(String sourceMac) {
            if (sourceMac == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "sourceMac");
            }
            this.sourceMac = sourceMac;
            return this;
        }
        @CustomType.Setter
        public Builder targetIp(String targetIp) {
            if (targetIp == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "targetIp");
            }
            this.targetIp = targetIp;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerNicFirewallRule", "type");
            }
            this.type = type;
            return this;
        }
        public GetVcpuServerNicFirewallRule build() {
            final var _resultValue = new GetVcpuServerNicFirewallRule();
            _resultValue.icmpCode = icmpCode;
            _resultValue.icmpType = icmpType;
            _resultValue.id = id;
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
