// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class VpnWireguardPeerEndpoint {
    /**
     * @return [string] The hostname or IPV4 address that the WireGuard Server will connect to.
     * 
     */
    private String host;
    /**
     * @return [int] The port that the WireGuard Server will connect to. Defaults to `51820`.
     * 
     */
    private @Nullable Integer port;

    private VpnWireguardPeerEndpoint() {}
    /**
     * @return [string] The hostname or IPV4 address that the WireGuard Server will connect to.
     * 
     */
    public String host() {
        return this.host;
    }
    /**
     * @return [int] The port that the WireGuard Server will connect to. Defaults to `51820`.
     * 
     */
    public Optional<Integer> port() {
        return Optional.ofNullable(this.port);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(VpnWireguardPeerEndpoint defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String host;
        private @Nullable Integer port;
        public Builder() {}
        public Builder(VpnWireguardPeerEndpoint defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.host = defaults.host;
    	      this.port = defaults.port;
        }

        @CustomType.Setter
        public Builder host(String host) {
            if (host == null) {
              throw new MissingRequiredPropertyException("VpnWireguardPeerEndpoint", "host");
            }
            this.host = host;
            return this;
        }
        @CustomType.Setter
        public Builder port(@Nullable Integer port) {

            this.port = port;
            return this;
        }
        public VpnWireguardPeerEndpoint build() {
            final var _resultValue = new VpnWireguardPeerEndpoint();
            _resultValue.host = host;
            _resultValue.port = port;
            return _resultValue;
        }
    }
}
