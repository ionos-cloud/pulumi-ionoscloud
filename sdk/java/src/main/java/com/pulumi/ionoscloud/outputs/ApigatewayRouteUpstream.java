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
public final class ApigatewayRouteUpstream {
    /**
     * @return [string] The host of the upstream.
     * 
     */
    private String host;
    /**
     * @return [string] The load balancer algorithm. Default value: `roundrobin`.
     * 
     */
    private @Nullable String loadbalancer;
    /**
     * @return [int] The port of the upstream. Default value: `80`.
     * 
     */
    private @Nullable Integer port;
    /**
     * @return [string] The target URL of the upstream. Default value: `http`.
     * 
     */
    private @Nullable String scheme;
    /**
     * @return [int] Weight with which to split traffic to the upstream. Default value: `100`.
     * 
     */
    private @Nullable Integer weight;

    private ApigatewayRouteUpstream() {}
    /**
     * @return [string] The host of the upstream.
     * 
     */
    public String host() {
        return this.host;
    }
    /**
     * @return [string] The load balancer algorithm. Default value: `roundrobin`.
     * 
     */
    public Optional<String> loadbalancer() {
        return Optional.ofNullable(this.loadbalancer);
    }
    /**
     * @return [int] The port of the upstream. Default value: `80`.
     * 
     */
    public Optional<Integer> port() {
        return Optional.ofNullable(this.port);
    }
    /**
     * @return [string] The target URL of the upstream. Default value: `http`.
     * 
     */
    public Optional<String> scheme() {
        return Optional.ofNullable(this.scheme);
    }
    /**
     * @return [int] Weight with which to split traffic to the upstream. Default value: `100`.
     * 
     */
    public Optional<Integer> weight() {
        return Optional.ofNullable(this.weight);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ApigatewayRouteUpstream defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String host;
        private @Nullable String loadbalancer;
        private @Nullable Integer port;
        private @Nullable String scheme;
        private @Nullable Integer weight;
        public Builder() {}
        public Builder(ApigatewayRouteUpstream defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.host = defaults.host;
    	      this.loadbalancer = defaults.loadbalancer;
    	      this.port = defaults.port;
    	      this.scheme = defaults.scheme;
    	      this.weight = defaults.weight;
        }

        @CustomType.Setter
        public Builder host(String host) {
            if (host == null) {
              throw new MissingRequiredPropertyException("ApigatewayRouteUpstream", "host");
            }
            this.host = host;
            return this;
        }
        @CustomType.Setter
        public Builder loadbalancer(@Nullable String loadbalancer) {

            this.loadbalancer = loadbalancer;
            return this;
        }
        @CustomType.Setter
        public Builder port(@Nullable Integer port) {

            this.port = port;
            return this;
        }
        @CustomType.Setter
        public Builder scheme(@Nullable String scheme) {

            this.scheme = scheme;
            return this;
        }
        @CustomType.Setter
        public Builder weight(@Nullable Integer weight) {

            this.weight = weight;
            return this;
        }
        public ApigatewayRouteUpstream build() {
            final var _resultValue = new ApigatewayRouteUpstream();
            _resultValue.host = host;
            _resultValue.loadbalancer = loadbalancer;
            _resultValue.port = port;
            _resultValue.scheme = scheme;
            _resultValue.weight = weight;
            return _resultValue;
        }
    }
}
