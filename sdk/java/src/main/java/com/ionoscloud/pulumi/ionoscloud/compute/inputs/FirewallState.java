// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class FirewallState extends com.pulumi.resources.ResourceArgs {

    public static final FirewallState Empty = new FirewallState();

    /**
     * [string] The Virtual Data Center ID.
     * 
     */
    @Import(name="datacenterId")
    private @Nullable Output<String> datacenterId;

    /**
     * @return [string] The Virtual Data Center ID.
     * 
     */
    public Optional<Output<String>> datacenterId() {
        return Optional.ofNullable(this.datacenterId);
    }

    /**
     * [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
     * 
     */
    @Import(name="icmpCode")
    private @Nullable Output<String> icmpCode;

    /**
     * @return [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
     * 
     */
    public Optional<Output<String>> icmpCode() {
        return Optional.ofNullable(this.icmpCode);
    }

    /**
     * [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
     * 
     */
    @Import(name="icmpType")
    private @Nullable Output<String> icmpType;

    /**
     * @return [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
     * 
     */
    public Optional<Output<String>> icmpType() {
        return Optional.ofNullable(this.icmpType);
    }

    /**
     * [string] The name of the firewall rule.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the firewall rule.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] The NIC ID.
     * 
     */
    @Import(name="nicId")
    private @Nullable Output<String> nicId;

    /**
     * @return [string] The NIC ID.
     * 
     */
    public Optional<Output<String>> nicId() {
        return Optional.ofNullable(this.nicId);
    }

    /**
     * [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     * 
     */
    @Import(name="portRangeEnd")
    private @Nullable Output<Integer> portRangeEnd;

    /**
     * @return [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     * 
     */
    public Optional<Output<Integer>> portRangeEnd() {
        return Optional.ofNullable(this.portRangeEnd);
    }

    /**
     * [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     * 
     */
    @Import(name="portRangeStart")
    private @Nullable Output<Integer> portRangeStart;

    /**
     * @return [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
     * 
     */
    public Optional<Output<Integer>> portRangeStart() {
        return Optional.ofNullable(this.portRangeStart);
    }

    /**
     * [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
     * 
     */
    @Import(name="protocol")
    private @Nullable Output<String> protocol;

    /**
     * @return [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
     * 
     */
    public Optional<Output<String>> protocol() {
        return Optional.ofNullable(this.protocol);
    }

    /**
     * [string] The Server ID.
     * 
     */
    @Import(name="serverId")
    private @Nullable Output<String> serverId;

    /**
     * @return [string] The Server ID.
     * 
     */
    public Optional<Output<String>> serverId() {
        return Optional.ofNullable(this.serverId);
    }

    /**
     * [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
     * 
     */
    @Import(name="sourceIp")
    private @Nullable Output<String> sourceIp;

    /**
     * @return [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
     * 
     */
    public Optional<Output<String>> sourceIp() {
        return Optional.ofNullable(this.sourceIp);
    }

    /**
     * [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
     * 
     */
    @Import(name="sourceMac")
    private @Nullable Output<String> sourceMac;

    /**
     * @return [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
     * 
     */
    public Optional<Output<String>> sourceMac() {
        return Optional.ofNullable(this.sourceMac);
    }

    /**
     * [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
     * 
     */
    @Import(name="targetIp")
    private @Nullable Output<String> targetIp;

    /**
     * @return [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
     * 
     */
    public Optional<Output<String>> targetIp() {
        return Optional.ofNullable(this.targetIp);
    }

    /**
     * [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    private FirewallState() {}

    private FirewallState(FirewallState $) {
        this.datacenterId = $.datacenterId;
        this.icmpCode = $.icmpCode;
        this.icmpType = $.icmpType;
        this.name = $.name;
        this.nicId = $.nicId;
        this.portRangeEnd = $.portRangeEnd;
        this.portRangeStart = $.portRangeStart;
        this.protocol = $.protocol;
        this.serverId = $.serverId;
        this.sourceIp = $.sourceIp;
        this.sourceMac = $.sourceMac;
        this.targetIp = $.targetIp;
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(FirewallState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private FirewallState $;

        public Builder() {
            $ = new FirewallState();
        }

        public Builder(FirewallState defaults) {
            $ = new FirewallState(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [string] The Virtual Data Center ID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(@Nullable Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] The Virtual Data Center ID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param icmpCode [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
         * 
         * @return builder
         * 
         */
        public Builder icmpCode(@Nullable Output<String> icmpCode) {
            $.icmpCode = icmpCode;
            return this;
        }

        /**
         * @param icmpCode [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
         * 
         * @return builder
         * 
         */
        public Builder icmpCode(String icmpCode) {
            return icmpCode(Output.of(icmpCode));
        }

        /**
         * @param icmpType [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
         * 
         * @return builder
         * 
         */
        public Builder icmpType(@Nullable Output<String> icmpType) {
            $.icmpType = icmpType;
            return this;
        }

        /**
         * @param icmpType [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
         * 
         * @return builder
         * 
         */
        public Builder icmpType(String icmpType) {
            return icmpType(Output.of(icmpType));
        }

        /**
         * @param name [string] The name of the firewall rule.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the firewall rule.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param nicId [string] The NIC ID.
         * 
         * @return builder
         * 
         */
        public Builder nicId(@Nullable Output<String> nicId) {
            $.nicId = nicId;
            return this;
        }

        /**
         * @param nicId [string] The NIC ID.
         * 
         * @return builder
         * 
         */
        public Builder nicId(String nicId) {
            return nicId(Output.of(nicId));
        }

        /**
         * @param portRangeEnd [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
         * 
         * @return builder
         * 
         */
        public Builder portRangeEnd(@Nullable Output<Integer> portRangeEnd) {
            $.portRangeEnd = portRangeEnd;
            return this;
        }

        /**
         * @param portRangeEnd [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
         * 
         * @return builder
         * 
         */
        public Builder portRangeEnd(Integer portRangeEnd) {
            return portRangeEnd(Output.of(portRangeEnd));
        }

        /**
         * @param portRangeStart [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
         * 
         * @return builder
         * 
         */
        public Builder portRangeStart(@Nullable Output<Integer> portRangeStart) {
            $.portRangeStart = portRangeStart;
            return this;
        }

        /**
         * @param portRangeStart [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
         * 
         * @return builder
         * 
         */
        public Builder portRangeStart(Integer portRangeStart) {
            return portRangeStart(Output.of(portRangeStart));
        }

        /**
         * @param protocol [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
         * 
         * @return builder
         * 
         */
        public Builder protocol(@Nullable Output<String> protocol) {
            $.protocol = protocol;
            return this;
        }

        /**
         * @param protocol [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
         * 
         * @return builder
         * 
         */
        public Builder protocol(String protocol) {
            return protocol(Output.of(protocol));
        }

        /**
         * @param serverId [string] The Server ID.
         * 
         * @return builder
         * 
         */
        public Builder serverId(@Nullable Output<String> serverId) {
            $.serverId = serverId;
            return this;
        }

        /**
         * @param serverId [string] The Server ID.
         * 
         * @return builder
         * 
         */
        public Builder serverId(String serverId) {
            return serverId(Output.of(serverId));
        }

        /**
         * @param sourceIp [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
         * 
         * @return builder
         * 
         */
        public Builder sourceIp(@Nullable Output<String> sourceIp) {
            $.sourceIp = sourceIp;
            return this;
        }

        /**
         * @param sourceIp [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
         * 
         * @return builder
         * 
         */
        public Builder sourceIp(String sourceIp) {
            return sourceIp(Output.of(sourceIp));
        }

        /**
         * @param sourceMac [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
         * 
         * @return builder
         * 
         */
        public Builder sourceMac(@Nullable Output<String> sourceMac) {
            $.sourceMac = sourceMac;
            return this;
        }

        /**
         * @param sourceMac [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
         * 
         * @return builder
         * 
         */
        public Builder sourceMac(String sourceMac) {
            return sourceMac(Output.of(sourceMac));
        }

        /**
         * @param targetIp [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
         * 
         * @return builder
         * 
         */
        public Builder targetIp(@Nullable Output<String> targetIp) {
            $.targetIp = targetIp;
            return this;
        }

        /**
         * @param targetIp [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
         * 
         * @return builder
         * 
         */
        public Builder targetIp(String targetIp) {
            return targetIp(Output.of(targetIp));
        }

        /**
         * @param type [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public FirewallState build() {
            return $;
        }
    }

}
