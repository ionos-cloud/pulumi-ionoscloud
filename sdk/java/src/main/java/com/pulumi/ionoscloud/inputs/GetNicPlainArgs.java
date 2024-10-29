// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetNicPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetNicPlainArgs Empty = new GetNicPlainArgs();

    /**
     * [string] The ID of a Virtual Data Center.
     * 
     */
    @Import(name="datacenterId", required=true)
    private String datacenterId;

    /**
     * @return [string] The ID of a Virtual Data Center.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }

    /**
     * Indicates if the NIC should get an IP address using DHCP (true) or not (false).
     * 
     */
    @Import(name="dhcp")
    private @Nullable Boolean dhcp;

    /**
     * @return Indicates if the NIC should get an IP address using DHCP (true) or not (false).
     * 
     */
    public Optional<Boolean> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }

    @Import(name="dhcpv6")
    private @Nullable Boolean dhcpv6;

    public Optional<Boolean> dhcpv6() {
        return Optional.ofNullable(this.dhcpv6);
    }

    /**
     * If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
     * 
     */
    @Import(name="firewallActive")
    private @Nullable Boolean firewallActive;

    /**
     * @return If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
     * 
     */
    public Optional<Boolean> firewallActive() {
        return Optional.ofNullable(this.firewallActive);
    }

    /**
     * The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
     * 
     */
    @Import(name="firewallType")
    private @Nullable String firewallType;

    /**
     * @return The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
     * 
     */
    public Optional<String> firewallType() {
        return Optional.ofNullable(this.firewallType);
    }

    /**
     * ID of the nic you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided.
     * If none, are provided, the datasource will return an error.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of the nic you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided.
     * If none, are provided, the datasource will return an error.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     * 
     */
    @Import(name="ips")
    private @Nullable List<String> ips;

    /**
     * @return Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     * 
     */
    public Optional<List<String>> ips() {
        return Optional.ofNullable(this.ips);
    }

    @Import(name="ipv6CidrBlock")
    private @Nullable String ipv6CidrBlock;

    public Optional<String> ipv6CidrBlock() {
        return Optional.ofNullable(this.ipv6CidrBlock);
    }

    @Import(name="ipv6Ips")
    private @Nullable List<String> ipv6Ips;

    public Optional<List<String>> ipv6Ips() {
        return Optional.ofNullable(this.ipv6Ips);
    }

    /**
     * The LAN ID the NIC will sit on.
     * 
     */
    @Import(name="lan")
    private @Nullable Integer lan;

    /**
     * @return The LAN ID the NIC will sit on.
     * 
     */
    public Optional<Integer> lan() {
        return Optional.ofNullable(this.lan);
    }

    /**
     * [string] The name of the LAN.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return [string] The name of the LAN.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] The ID of a server.
     * 
     */
    @Import(name="serverId", required=true)
    private String serverId;

    /**
     * @return [string] The ID of a server.
     * 
     */
    public String serverId() {
        return this.serverId;
    }

    private GetNicPlainArgs() {}

    private GetNicPlainArgs(GetNicPlainArgs $) {
        this.datacenterId = $.datacenterId;
        this.dhcp = $.dhcp;
        this.dhcpv6 = $.dhcpv6;
        this.firewallActive = $.firewallActive;
        this.firewallType = $.firewallType;
        this.id = $.id;
        this.ips = $.ips;
        this.ipv6CidrBlock = $.ipv6CidrBlock;
        this.ipv6Ips = $.ipv6Ips;
        this.lan = $.lan;
        this.name = $.name;
        this.serverId = $.serverId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetNicPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetNicPlainArgs $;

        public Builder() {
            $ = new GetNicPlainArgs();
        }

        public Builder(GetNicPlainArgs defaults) {
            $ = new GetNicPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [string] The ID of a Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param dhcp Indicates if the NIC should get an IP address using DHCP (true) or not (false).
         * 
         * @return builder
         * 
         */
        public Builder dhcp(@Nullable Boolean dhcp) {
            $.dhcp = dhcp;
            return this;
        }

        public Builder dhcpv6(@Nullable Boolean dhcpv6) {
            $.dhcpv6 = dhcpv6;
            return this;
        }

        /**
         * @param firewallActive If this resource is set to true and is nested under a server resource firewall, with open SSH port, resource must be nested under the NIC.
         * 
         * @return builder
         * 
         */
        public Builder firewallActive(@Nullable Boolean firewallActive) {
            $.firewallActive = firewallActive;
            return this;
        }

        /**
         * @param firewallType The type of firewall rules that will be allowed on the NIC. If it is not specified it will take the default value INGRESS
         * 
         * @return builder
         * 
         */
        public Builder firewallType(@Nullable String firewallType) {
            $.firewallType = firewallType;
            return this;
        }

        /**
         * @param id ID of the nic you want to search for.
         * 
         * `datacenter_id` and either `name` or `id` must be provided.
         * If none, are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param ips Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
         * 
         * @return builder
         * 
         */
        public Builder ips(@Nullable List<String> ips) {
            $.ips = ips;
            return this;
        }

        /**
         * @param ips Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
         * 
         * @return builder
         * 
         */
        public Builder ips(String... ips) {
            return ips(List.of(ips));
        }

        public Builder ipv6CidrBlock(@Nullable String ipv6CidrBlock) {
            $.ipv6CidrBlock = ipv6CidrBlock;
            return this;
        }

        public Builder ipv6Ips(@Nullable List<String> ipv6Ips) {
            $.ipv6Ips = ipv6Ips;
            return this;
        }

        public Builder ipv6Ips(String... ipv6Ips) {
            return ipv6Ips(List.of(ipv6Ips));
        }

        /**
         * @param lan The LAN ID the NIC will sit on.
         * 
         * @return builder
         * 
         */
        public Builder lan(@Nullable Integer lan) {
            $.lan = lan;
            return this;
        }

        /**
         * @param name [string] The name of the LAN.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param serverId [string] The ID of a server.
         * 
         * @return builder
         * 
         */
        public Builder serverId(String serverId) {
            $.serverId = serverId;
            return this;
        }

        public GetNicPlainArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("GetNicPlainArgs", "datacenterId");
            }
            if ($.serverId == null) {
                throw new MissingRequiredPropertyException("GetNicPlainArgs", "serverId");
            }
            return $;
        }
    }

}
