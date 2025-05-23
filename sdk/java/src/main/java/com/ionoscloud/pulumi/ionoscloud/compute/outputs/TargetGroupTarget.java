// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class TargetGroupTarget {
    /**
     * @return [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    private @Nullable Boolean healthCheckEnabled;
    /**
     * @return [string] The IP of the balanced target VM.
     * 
     */
    private String ip;
    /**
     * @return [bool] Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    private @Nullable Boolean maintenanceEnabled;
    /**
     * @return [int] The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    private Integer port;
    /**
     * @return [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
     * 
     */
    private @Nullable String proxyProtocol;
    /**
     * @return [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    private Integer weight;

    private TargetGroupTarget() {}
    /**
     * @return [bool] Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    public Optional<Boolean> healthCheckEnabled() {
        return Optional.ofNullable(this.healthCheckEnabled);
    }
    /**
     * @return [string] The IP of the balanced target VM.
     * 
     */
    public String ip() {
        return this.ip;
    }
    /**
     * @return [bool] Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    public Optional<Boolean> maintenanceEnabled() {
        return Optional.ofNullable(this.maintenanceEnabled);
    }
    /**
     * @return [int] The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    public Integer port() {
        return this.port;
    }
    /**
     * @return [string] The proxy protocol version. Accepted values are `none`, `v1`, `v2`, `v2ssl`. If unspecified, the default value of `none` is used.
     * 
     */
    public Optional<String> proxyProtocol() {
        return Optional.ofNullable(this.proxyProtocol);
    }
    /**
     * @return [int] Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    public Integer weight() {
        return this.weight;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(TargetGroupTarget defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean healthCheckEnabled;
        private String ip;
        private @Nullable Boolean maintenanceEnabled;
        private Integer port;
        private @Nullable String proxyProtocol;
        private Integer weight;
        public Builder() {}
        public Builder(TargetGroupTarget defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.healthCheckEnabled = defaults.healthCheckEnabled;
    	      this.ip = defaults.ip;
    	      this.maintenanceEnabled = defaults.maintenanceEnabled;
    	      this.port = defaults.port;
    	      this.proxyProtocol = defaults.proxyProtocol;
    	      this.weight = defaults.weight;
        }

        @CustomType.Setter
        public Builder healthCheckEnabled(@Nullable Boolean healthCheckEnabled) {

            this.healthCheckEnabled = healthCheckEnabled;
            return this;
        }
        @CustomType.Setter
        public Builder ip(String ip) {
            if (ip == null) {
              throw new MissingRequiredPropertyException("TargetGroupTarget", "ip");
            }
            this.ip = ip;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceEnabled(@Nullable Boolean maintenanceEnabled) {

            this.maintenanceEnabled = maintenanceEnabled;
            return this;
        }
        @CustomType.Setter
        public Builder port(Integer port) {
            if (port == null) {
              throw new MissingRequiredPropertyException("TargetGroupTarget", "port");
            }
            this.port = port;
            return this;
        }
        @CustomType.Setter
        public Builder proxyProtocol(@Nullable String proxyProtocol) {

            this.proxyProtocol = proxyProtocol;
            return this;
        }
        @CustomType.Setter
        public Builder weight(Integer weight) {
            if (weight == null) {
              throw new MissingRequiredPropertyException("TargetGroupTarget", "weight");
            }
            this.weight = weight;
            return this;
        }
        public TargetGroupTarget build() {
            final var _resultValue = new TargetGroupTarget();
            _resultValue.healthCheckEnabled = healthCheckEnabled;
            _resultValue.ip = ip;
            _resultValue.maintenanceEnabled = maintenanceEnabled;
            _resultValue.port = port;
            _resultValue.proxyProtocol = proxyProtocol;
            _resultValue.weight = weight;
            return _resultValue;
        }
    }
}
