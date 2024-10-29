// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class VpnWireguardGatewayConnection {
    /**
     * @return [String] The ID of the datacenter where the WireGuard Gateway is located.
     * 
     */
    private String datacenterId;
    /**
     * @return [String] The IPv4 CIDR for the WireGuard Gateway connection.
     * 
     */
    private @Nullable String ipv4Cidr;
    /**
     * @return [String] The IPv6 CIDR for the WireGuard Gateway connection.
     * 
     */
    private @Nullable String ipv6Cidr;
    /**
     * @return [String] The ID of the LAN where the WireGuard Gateway is connected.
     * 
     */
    private String lanId;

    private VpnWireguardGatewayConnection() {}
    /**
     * @return [String] The ID of the datacenter where the WireGuard Gateway is located.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return [String] The IPv4 CIDR for the WireGuard Gateway connection.
     * 
     */
    public Optional<String> ipv4Cidr() {
        return Optional.ofNullable(this.ipv4Cidr);
    }
    /**
     * @return [String] The IPv6 CIDR for the WireGuard Gateway connection.
     * 
     */
    public Optional<String> ipv6Cidr() {
        return Optional.ofNullable(this.ipv6Cidr);
    }
    /**
     * @return [String] The ID of the LAN where the WireGuard Gateway is connected.
     * 
     */
    public String lanId() {
        return this.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(VpnWireguardGatewayConnection defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String datacenterId;
        private @Nullable String ipv4Cidr;
        private @Nullable String ipv6Cidr;
        private String lanId;
        public Builder() {}
        public Builder(VpnWireguardGatewayConnection defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.datacenterId = defaults.datacenterId;
    	      this.ipv4Cidr = defaults.ipv4Cidr;
    	      this.ipv6Cidr = defaults.ipv6Cidr;
    	      this.lanId = defaults.lanId;
        }

        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("VpnWireguardGatewayConnection", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder ipv4Cidr(@Nullable String ipv4Cidr) {

            this.ipv4Cidr = ipv4Cidr;
            return this;
        }
        @CustomType.Setter
        public Builder ipv6Cidr(@Nullable String ipv6Cidr) {

            this.ipv6Cidr = ipv6Cidr;
            return this;
        }
        @CustomType.Setter
        public Builder lanId(String lanId) {
            if (lanId == null) {
              throw new MissingRequiredPropertyException("VpnWireguardGatewayConnection", "lanId");
            }
            this.lanId = lanId;
            return this;
        }
        public VpnWireguardGatewayConnection build() {
            final var _resultValue = new VpnWireguardGatewayConnection();
            _resultValue.datacenterId = datacenterId;
            _resultValue.ipv4Cidr = ipv4Cidr;
            _resultValue.ipv6Cidr = ipv6Cidr;
            _resultValue.lanId = lanId;
            return _resultValue;
        }
    }
}
