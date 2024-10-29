// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class TargetGroupTargetArgs extends com.pulumi.resources.ResourceArgs {

    public static final TargetGroupTargetArgs Empty = new TargetGroupTargetArgs();

    /**
     * [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    @Import(name="healthCheckEnabled")
    private @Nullable Output<Boolean> healthCheckEnabled;

    /**
     * @return [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    public Optional<Output<Boolean>> healthCheckEnabled() {
        return Optional.ofNullable(this.healthCheckEnabled);
    }

    /**
     * [string] The IP of the balanced target VM.
     * 
     */
    @Import(name="ip", required=true)
    private Output<String> ip;

    /**
     * @return [string] The IP of the balanced target VM.
     * 
     */
    public Output<String> ip() {
        return this.ip;
    }

    /**
     * [bool] Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    @Import(name="maintenanceEnabled")
    private @Nullable Output<Boolean> maintenanceEnabled;

    /**
     * @return [bool] Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    public Optional<Output<Boolean>> maintenanceEnabled() {
        return Optional.ofNullable(this.maintenanceEnabled);
    }

    /**
     * [int] The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    @Import(name="port", required=true)
    private Output<Integer> port;

    /**
     * @return [int] The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    public Output<Integer> port() {
        return this.port;
    }

    /**
     * [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
     * 
     */
    @Import(name="proxyProtocol")
    private @Nullable Output<String> proxyProtocol;

    /**
     * @return [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
     * 
     */
    public Optional<Output<String>> proxyProtocol() {
        return Optional.ofNullable(this.proxyProtocol);
    }

    /**
     * [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    @Import(name="weight", required=true)
    private Output<Integer> weight;

    /**
     * @return [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    public Output<Integer> weight() {
        return this.weight;
    }

    private TargetGroupTargetArgs() {}

    private TargetGroupTargetArgs(TargetGroupTargetArgs $) {
        this.healthCheckEnabled = $.healthCheckEnabled;
        this.ip = $.ip;
        this.maintenanceEnabled = $.maintenanceEnabled;
        this.port = $.port;
        this.proxyProtocol = $.proxyProtocol;
        this.weight = $.weight;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(TargetGroupTargetArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private TargetGroupTargetArgs $;

        public Builder() {
            $ = new TargetGroupTargetArgs();
        }

        public Builder(TargetGroupTargetArgs defaults) {
            $ = new TargetGroupTargetArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param healthCheckEnabled [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
         * 
         * @return builder
         * 
         */
        public Builder healthCheckEnabled(@Nullable Output<Boolean> healthCheckEnabled) {
            $.healthCheckEnabled = healthCheckEnabled;
            return this;
        }

        /**
         * @param healthCheckEnabled [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
         * 
         * @return builder
         * 
         */
        public Builder healthCheckEnabled(Boolean healthCheckEnabled) {
            return healthCheckEnabled(Output.of(healthCheckEnabled));
        }

        /**
         * @param ip [string] The IP of the balanced target VM.
         * 
         * @return builder
         * 
         */
        public Builder ip(Output<String> ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ip [string] The IP of the balanced target VM.
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        /**
         * @param maintenanceEnabled [bool] Maintenance mode prevents the target from receiving balanced traffic.
         * 
         * @return builder
         * 
         */
        public Builder maintenanceEnabled(@Nullable Output<Boolean> maintenanceEnabled) {
            $.maintenanceEnabled = maintenanceEnabled;
            return this;
        }

        /**
         * @param maintenanceEnabled [bool] Maintenance mode prevents the target from receiving balanced traffic.
         * 
         * @return builder
         * 
         */
        public Builder maintenanceEnabled(Boolean maintenanceEnabled) {
            return maintenanceEnabled(Output.of(maintenanceEnabled));
        }

        /**
         * @param port [int] The port of the balanced target service; valid range is 1 to 65535.
         * 
         * @return builder
         * 
         */
        public Builder port(Output<Integer> port) {
            $.port = port;
            return this;
        }

        /**
         * @param port [int] The port of the balanced target service; valid range is 1 to 65535.
         * 
         * @return builder
         * 
         */
        public Builder port(Integer port) {
            return port(Output.of(port));
        }

        /**
         * @param proxyProtocol [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
         * 
         * @return builder
         * 
         */
        public Builder proxyProtocol(@Nullable Output<String> proxyProtocol) {
            $.proxyProtocol = proxyProtocol;
            return this;
        }

        /**
         * @param proxyProtocol [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
         * 
         * @return builder
         * 
         */
        public Builder proxyProtocol(String proxyProtocol) {
            return proxyProtocol(Output.of(proxyProtocol));
        }

        /**
         * @param weight [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
         * 
         * @return builder
         * 
         */
        public Builder weight(Output<Integer> weight) {
            $.weight = weight;
            return this;
        }

        /**
         * @param weight [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
         * 
         * @return builder
         * 
         */
        public Builder weight(Integer weight) {
            return weight(Output.of(weight));
        }

        public TargetGroupTargetArgs build() {
            if ($.ip == null) {
                throw new MissingRequiredPropertyException("TargetGroupTargetArgs", "ip");
            }
            if ($.port == null) {
                throw new MissingRequiredPropertyException("TargetGroupTargetArgs", "port");
            }
            if ($.weight == null) {
                throw new MissingRequiredPropertyException("TargetGroupTargetArgs", "weight");
            }
            return $;
        }
    }

}
