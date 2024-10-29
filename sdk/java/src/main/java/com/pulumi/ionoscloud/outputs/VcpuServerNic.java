// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.VcpuServerNicFirewall;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class VcpuServerNic {
    private @Nullable Integer deviceNumber;
    private @Nullable Boolean dhcp;
    private @Nullable Boolean dhcpv6;
    private @Nullable Boolean firewallActive;
    private @Nullable String firewallType;
    /**
     * @return Allows to define firewall rules inline in the server. See the Firewall section.
     * 
     */
    private @Nullable List<VcpuServerNicFirewall> firewalls;
    private @Nullable String id;
    /**
     * @return Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     * 
     */
    private @Nullable List<String> ips;
    private @Nullable String ipv6CidrBlock;
    private @Nullable List<String> ipv6Ips;
    private Integer lan;
    private @Nullable String mac;
    /**
     * @return [string] The name of the server.
     * 
     */
    private @Nullable String name;
    private @Nullable Integer pciSlot;

    private VcpuServerNic() {}
    public Optional<Integer> deviceNumber() {
        return Optional.ofNullable(this.deviceNumber);
    }
    public Optional<Boolean> dhcp() {
        return Optional.ofNullable(this.dhcp);
    }
    public Optional<Boolean> dhcpv6() {
        return Optional.ofNullable(this.dhcpv6);
    }
    public Optional<Boolean> firewallActive() {
        return Optional.ofNullable(this.firewallActive);
    }
    public Optional<String> firewallType() {
        return Optional.ofNullable(this.firewallType);
    }
    /**
     * @return Allows to define firewall rules inline in the server. See the Firewall section.
     * 
     */
    public List<VcpuServerNicFirewall> firewalls() {
        return this.firewalls == null ? List.of() : this.firewalls;
    }
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return Collection of IP addresses assigned to a nic. Explicitly assigned public IPs need to come from reserved IP blocks, Passing value null or empty array will assign an IP address automatically.
     * 
     */
    public List<String> ips() {
        return this.ips == null ? List.of() : this.ips;
    }
    public Optional<String> ipv6CidrBlock() {
        return Optional.ofNullable(this.ipv6CidrBlock);
    }
    public List<String> ipv6Ips() {
        return this.ipv6Ips == null ? List.of() : this.ipv6Ips;
    }
    public Integer lan() {
        return this.lan;
    }
    public Optional<String> mac() {
        return Optional.ofNullable(this.mac);
    }
    /**
     * @return [string] The name of the server.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    public Optional<Integer> pciSlot() {
        return Optional.ofNullable(this.pciSlot);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(VcpuServerNic defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Integer deviceNumber;
        private @Nullable Boolean dhcp;
        private @Nullable Boolean dhcpv6;
        private @Nullable Boolean firewallActive;
        private @Nullable String firewallType;
        private @Nullable List<VcpuServerNicFirewall> firewalls;
        private @Nullable String id;
        private @Nullable List<String> ips;
        private @Nullable String ipv6CidrBlock;
        private @Nullable List<String> ipv6Ips;
        private Integer lan;
        private @Nullable String mac;
        private @Nullable String name;
        private @Nullable Integer pciSlot;
        public Builder() {}
        public Builder(VcpuServerNic defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.deviceNumber = defaults.deviceNumber;
    	      this.dhcp = defaults.dhcp;
    	      this.dhcpv6 = defaults.dhcpv6;
    	      this.firewallActive = defaults.firewallActive;
    	      this.firewallType = defaults.firewallType;
    	      this.firewalls = defaults.firewalls;
    	      this.id = defaults.id;
    	      this.ips = defaults.ips;
    	      this.ipv6CidrBlock = defaults.ipv6CidrBlock;
    	      this.ipv6Ips = defaults.ipv6Ips;
    	      this.lan = defaults.lan;
    	      this.mac = defaults.mac;
    	      this.name = defaults.name;
    	      this.pciSlot = defaults.pciSlot;
        }

        @CustomType.Setter
        public Builder deviceNumber(@Nullable Integer deviceNumber) {

            this.deviceNumber = deviceNumber;
            return this;
        }
        @CustomType.Setter
        public Builder dhcp(@Nullable Boolean dhcp) {

            this.dhcp = dhcp;
            return this;
        }
        @CustomType.Setter
        public Builder dhcpv6(@Nullable Boolean dhcpv6) {

            this.dhcpv6 = dhcpv6;
            return this;
        }
        @CustomType.Setter
        public Builder firewallActive(@Nullable Boolean firewallActive) {

            this.firewallActive = firewallActive;
            return this;
        }
        @CustomType.Setter
        public Builder firewallType(@Nullable String firewallType) {

            this.firewallType = firewallType;
            return this;
        }
        @CustomType.Setter
        public Builder firewalls(@Nullable List<VcpuServerNicFirewall> firewalls) {

            this.firewalls = firewalls;
            return this;
        }
        public Builder firewalls(VcpuServerNicFirewall... firewalls) {
            return firewalls(List.of(firewalls));
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder ips(@Nullable List<String> ips) {

            this.ips = ips;
            return this;
        }
        public Builder ips(String... ips) {
            return ips(List.of(ips));
        }
        @CustomType.Setter
        public Builder ipv6CidrBlock(@Nullable String ipv6CidrBlock) {

            this.ipv6CidrBlock = ipv6CidrBlock;
            return this;
        }
        @CustomType.Setter
        public Builder ipv6Ips(@Nullable List<String> ipv6Ips) {

            this.ipv6Ips = ipv6Ips;
            return this;
        }
        public Builder ipv6Ips(String... ipv6Ips) {
            return ipv6Ips(List.of(ipv6Ips));
        }
        @CustomType.Setter
        public Builder lan(Integer lan) {
            if (lan == null) {
              throw new MissingRequiredPropertyException("VcpuServerNic", "lan");
            }
            this.lan = lan;
            return this;
        }
        @CustomType.Setter
        public Builder mac(@Nullable String mac) {

            this.mac = mac;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder pciSlot(@Nullable Integer pciSlot) {

            this.pciSlot = pciSlot;
            return this;
        }
        public VcpuServerNic build() {
            final var _resultValue = new VcpuServerNic();
            _resultValue.deviceNumber = deviceNumber;
            _resultValue.dhcp = dhcp;
            _resultValue.dhcpv6 = dhcpv6;
            _resultValue.firewallActive = firewallActive;
            _resultValue.firewallType = firewallType;
            _resultValue.firewalls = firewalls;
            _resultValue.id = id;
            _resultValue.ips = ips;
            _resultValue.ipv6CidrBlock = ipv6CidrBlock;
            _resultValue.ipv6Ips = ipv6Ips;
            _resultValue.lan = lan;
            _resultValue.mac = mac;
            _resultValue.name = name;
            _resultValue.pciSlot = pciSlot;
            return _resultValue;
        }
    }
}
