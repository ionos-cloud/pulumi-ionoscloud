// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetTargetGroupTarget {
    /**
     * @return Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    private Boolean healthCheckEnabled;
    /**
     * @return The IP of the balanced target VM.
     * 
     */
    private String ip;
    /**
     * @return Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    private Boolean maintenanceEnabled;
    /**
     * @return The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    private Integer port;
    /**
     * @return The proxy protocol version.
     * 
     */
    private String proxyProtocol;
    /**
     * @return Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    private Integer weight;

    private GetTargetGroupTarget() {}
    /**
     * @return Makes the target available only if it accepts periodic health check TCP connection attempts; when turned off, the target is considered always available. The health check only consists of a connection attempt to the address and port of the target. Default is True.
     * 
     */
    public Boolean healthCheckEnabled() {
        return this.healthCheckEnabled;
    }
    /**
     * @return The IP of the balanced target VM.
     * 
     */
    public String ip() {
        return this.ip;
    }
    /**
     * @return Maintenance mode prevents the target from receiving balanced traffic.
     * 
     */
    public Boolean maintenanceEnabled() {
        return this.maintenanceEnabled;
    }
    /**
     * @return The port of the balanced target service; valid range is 1 to 65535.
     * 
     */
    public Integer port() {
        return this.port;
    }
    /**
     * @return The proxy protocol version.
     * 
     */
    public String proxyProtocol() {
        return this.proxyProtocol;
    }
    /**
     * @return Traffic is distributed in proportion to target weight, relative to the combined weight of all targets. A target with higher weight receives a greater share of traffic. Valid range is 0 to 256 and default is 1; targets with weight of 0 do not participate in load balancing but still accept persistent connections. It is best use values in the middle of the range to leave room for later adjustments.
     * 
     */
    public Integer weight() {
        return this.weight;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetTargetGroupTarget defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean healthCheckEnabled;
        private String ip;
        private Boolean maintenanceEnabled;
        private Integer port;
        private String proxyProtocol;
        private Integer weight;
        public Builder() {}
        public Builder(GetTargetGroupTarget defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.healthCheckEnabled = defaults.healthCheckEnabled;
    	      this.ip = defaults.ip;
    	      this.maintenanceEnabled = defaults.maintenanceEnabled;
    	      this.port = defaults.port;
    	      this.proxyProtocol = defaults.proxyProtocol;
    	      this.weight = defaults.weight;
        }

        @CustomType.Setter
        public Builder healthCheckEnabled(Boolean healthCheckEnabled) {
            if (healthCheckEnabled == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "healthCheckEnabled");
            }
            this.healthCheckEnabled = healthCheckEnabled;
            return this;
        }
        @CustomType.Setter
        public Builder ip(String ip) {
            if (ip == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "ip");
            }
            this.ip = ip;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceEnabled(Boolean maintenanceEnabled) {
            if (maintenanceEnabled == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "maintenanceEnabled");
            }
            this.maintenanceEnabled = maintenanceEnabled;
            return this;
        }
        @CustomType.Setter
        public Builder port(Integer port) {
            if (port == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "port");
            }
            this.port = port;
            return this;
        }
        @CustomType.Setter
        public Builder proxyProtocol(String proxyProtocol) {
            if (proxyProtocol == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "proxyProtocol");
            }
            this.proxyProtocol = proxyProtocol;
            return this;
        }
        @CustomType.Setter
        public Builder weight(Integer weight) {
            if (weight == null) {
              throw new MissingRequiredPropertyException("GetTargetGroupTarget", "weight");
            }
            this.weight = weight;
            return this;
        }
        public GetTargetGroupTarget build() {
            final var _resultValue = new GetTargetGroupTarget();
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
