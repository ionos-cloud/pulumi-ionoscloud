// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.vpn.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class WireguardGatewayConnectionArgs extends com.pulumi.resources.ResourceArgs {

    public static final WireguardGatewayConnectionArgs Empty = new WireguardGatewayConnectionArgs();

    /**
     * [String] The ID of the datacenter where the WireGuard Gateway is located.
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return [String] The ID of the datacenter where the WireGuard Gateway is located.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * [String] The IPv4 CIDR for the WireGuard Gateway connection.
     * 
     */
    @Import(name="ipv4Cidr")
    private @Nullable Output<String> ipv4Cidr;

    /**
     * @return [String] The IPv4 CIDR for the WireGuard Gateway connection.
     * 
     */
    public Optional<Output<String>> ipv4Cidr() {
        return Optional.ofNullable(this.ipv4Cidr);
    }

    /**
     * [String] The IPv6 CIDR for the WireGuard Gateway connection.
     * 
     */
    @Import(name="ipv6Cidr")
    private @Nullable Output<String> ipv6Cidr;

    /**
     * @return [String] The IPv6 CIDR for the WireGuard Gateway connection.
     * 
     */
    public Optional<Output<String>> ipv6Cidr() {
        return Optional.ofNullable(this.ipv6Cidr);
    }

    /**
     * [String] The ID of the LAN where the WireGuard Gateway is connected.
     * 
     */
    @Import(name="lanId", required=true)
    private Output<String> lanId;

    /**
     * @return [String] The ID of the LAN where the WireGuard Gateway is connected.
     * 
     */
    public Output<String> lanId() {
        return this.lanId;
    }

    private WireguardGatewayConnectionArgs() {}

    private WireguardGatewayConnectionArgs(WireguardGatewayConnectionArgs $) {
        this.datacenterId = $.datacenterId;
        this.ipv4Cidr = $.ipv4Cidr;
        this.ipv6Cidr = $.ipv6Cidr;
        this.lanId = $.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(WireguardGatewayConnectionArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private WireguardGatewayConnectionArgs $;

        public Builder() {
            $ = new WireguardGatewayConnectionArgs();
        }

        public Builder(WireguardGatewayConnectionArgs defaults) {
            $ = new WireguardGatewayConnectionArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [String] The ID of the datacenter where the WireGuard Gateway is located.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [String] The ID of the datacenter where the WireGuard Gateway is located.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param ipv4Cidr [String] The IPv4 CIDR for the WireGuard Gateway connection.
         * 
         * @return builder
         * 
         */
        public Builder ipv4Cidr(@Nullable Output<String> ipv4Cidr) {
            $.ipv4Cidr = ipv4Cidr;
            return this;
        }

        /**
         * @param ipv4Cidr [String] The IPv4 CIDR for the WireGuard Gateway connection.
         * 
         * @return builder
         * 
         */
        public Builder ipv4Cidr(String ipv4Cidr) {
            return ipv4Cidr(Output.of(ipv4Cidr));
        }

        /**
         * @param ipv6Cidr [String] The IPv6 CIDR for the WireGuard Gateway connection.
         * 
         * @return builder
         * 
         */
        public Builder ipv6Cidr(@Nullable Output<String> ipv6Cidr) {
            $.ipv6Cidr = ipv6Cidr;
            return this;
        }

        /**
         * @param ipv6Cidr [String] The IPv6 CIDR for the WireGuard Gateway connection.
         * 
         * @return builder
         * 
         */
        public Builder ipv6Cidr(String ipv6Cidr) {
            return ipv6Cidr(Output.of(ipv6Cidr));
        }

        /**
         * @param lanId [String] The ID of the LAN where the WireGuard Gateway is connected.
         * 
         * @return builder
         * 
         */
        public Builder lanId(Output<String> lanId) {
            $.lanId = lanId;
            return this;
        }

        /**
         * @param lanId [String] The ID of the LAN where the WireGuard Gateway is connected.
         * 
         * @return builder
         * 
         */
        public Builder lanId(String lanId) {
            return lanId(Output.of(lanId));
        }

        public WireguardGatewayConnectionArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("WireguardGatewayConnectionArgs", "datacenterId");
            }
            if ($.lanId == null) {
                throw new MissingRequiredPropertyException("WireguardGatewayConnectionArgs", "lanId");
            }
            return $;
        }
    }

}
