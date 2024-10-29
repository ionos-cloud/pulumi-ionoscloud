// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ServerNicFirewallArgs extends com.pulumi.resources.ResourceArgs {

    public static final ServerNicFirewallArgs Empty = new ServerNicFirewallArgs();

    @Import(name="icmpCode")
    private @Nullable Output<String> icmpCode;

    public Optional<Output<String>> icmpCode() {
        return Optional.ofNullable(this.icmpCode);
    }

    @Import(name="icmpType")
    private @Nullable Output<String> icmpType;

    public Optional<Output<String>> icmpType() {
        return Optional.ofNullable(this.icmpType);
    }

    @Import(name="id")
    private @Nullable Output<String> id;

    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * [string] The name of the server.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the server.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    @Import(name="portRangeEnd")
    private @Nullable Output<Integer> portRangeEnd;

    public Optional<Output<Integer>> portRangeEnd() {
        return Optional.ofNullable(this.portRangeEnd);
    }

    @Import(name="portRangeStart")
    private @Nullable Output<Integer> portRangeStart;

    public Optional<Output<Integer>> portRangeStart() {
        return Optional.ofNullable(this.portRangeStart);
    }

    @Import(name="protocol", required=true)
    private Output<String> protocol;

    public Output<String> protocol() {
        return this.protocol;
    }

    @Import(name="sourceIp")
    private @Nullable Output<String> sourceIp;

    public Optional<Output<String>> sourceIp() {
        return Optional.ofNullable(this.sourceIp);
    }

    @Import(name="sourceMac")
    private @Nullable Output<String> sourceMac;

    public Optional<Output<String>> sourceMac() {
        return Optional.ofNullable(this.sourceMac);
    }

    @Import(name="targetIp")
    private @Nullable Output<String> targetIp;

    public Optional<Output<String>> targetIp() {
        return Optional.ofNullable(this.targetIp);
    }

    /**
     * (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    private ServerNicFirewallArgs() {}

    private ServerNicFirewallArgs(ServerNicFirewallArgs $) {
        this.icmpCode = $.icmpCode;
        this.icmpType = $.icmpType;
        this.id = $.id;
        this.name = $.name;
        this.portRangeEnd = $.portRangeEnd;
        this.portRangeStart = $.portRangeStart;
        this.protocol = $.protocol;
        this.sourceIp = $.sourceIp;
        this.sourceMac = $.sourceMac;
        this.targetIp = $.targetIp;
        this.type = $.type;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ServerNicFirewallArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ServerNicFirewallArgs $;

        public Builder() {
            $ = new ServerNicFirewallArgs();
        }

        public Builder(ServerNicFirewallArgs defaults) {
            $ = new ServerNicFirewallArgs(Objects.requireNonNull(defaults));
        }

        public Builder icmpCode(@Nullable Output<String> icmpCode) {
            $.icmpCode = icmpCode;
            return this;
        }

        public Builder icmpCode(String icmpCode) {
            return icmpCode(Output.of(icmpCode));
        }

        public Builder icmpType(@Nullable Output<String> icmpType) {
            $.icmpType = icmpType;
            return this;
        }

        public Builder icmpType(String icmpType) {
            return icmpType(Output.of(icmpType));
        }

        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param name [string] The name of the server.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the server.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder portRangeEnd(@Nullable Output<Integer> portRangeEnd) {
            $.portRangeEnd = portRangeEnd;
            return this;
        }

        public Builder portRangeEnd(Integer portRangeEnd) {
            return portRangeEnd(Output.of(portRangeEnd));
        }

        public Builder portRangeStart(@Nullable Output<Integer> portRangeStart) {
            $.portRangeStart = portRangeStart;
            return this;
        }

        public Builder portRangeStart(Integer portRangeStart) {
            return portRangeStart(Output.of(portRangeStart));
        }

        public Builder protocol(Output<String> protocol) {
            $.protocol = protocol;
            return this;
        }

        public Builder protocol(String protocol) {
            return protocol(Output.of(protocol));
        }

        public Builder sourceIp(@Nullable Output<String> sourceIp) {
            $.sourceIp = sourceIp;
            return this;
        }

        public Builder sourceIp(String sourceIp) {
            return sourceIp(Output.of(sourceIp));
        }

        public Builder sourceMac(@Nullable Output<String> sourceMac) {
            $.sourceMac = sourceMac;
            return this;
        }

        public Builder sourceMac(String sourceMac) {
            return sourceMac(Output.of(sourceMac));
        }

        public Builder targetIp(@Nullable Output<String> targetIp) {
            $.targetIp = targetIp;
            return this;
        }

        public Builder targetIp(String targetIp) {
            return targetIp(Output.of(targetIp));
        }

        /**
         * @param type (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type (Computed)[string] Server usages: [ENTERPRISE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/virtual-servers) or [CUBE](https://docs.ionos.com/cloud/compute-engine/virtual-servers/cloud-cubes). This property is immutable.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        public ServerNicFirewallArgs build() {
            if ($.protocol == null) {
                throw new MissingRequiredPropertyException("ServerNicFirewallArgs", "protocol");
            }
            return $;
        }
    }

}
