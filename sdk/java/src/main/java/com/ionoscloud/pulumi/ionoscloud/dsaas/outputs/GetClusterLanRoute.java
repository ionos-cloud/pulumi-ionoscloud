// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dsaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetClusterLanRoute {
    /**
     * @return IPv4 or IPv6 gateway IP for the route
     * 
     */
    private String gateway;
    /**
     * @return IPv4 or IPv6 CIDR to be routed via the interface
     * 
     */
    private String network;

    private GetClusterLanRoute() {}
    /**
     * @return IPv4 or IPv6 gateway IP for the route
     * 
     */
    public String gateway() {
        return this.gateway;
    }
    /**
     * @return IPv4 or IPv6 CIDR to be routed via the interface
     * 
     */
    public String network() {
        return this.network;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetClusterLanRoute defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String gateway;
        private String network;
        public Builder() {}
        public Builder(GetClusterLanRoute defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.gateway = defaults.gateway;
    	      this.network = defaults.network;
        }

        @CustomType.Setter
        public Builder gateway(String gateway) {
            if (gateway == null) {
              throw new MissingRequiredPropertyException("GetClusterLanRoute", "gateway");
            }
            this.gateway = gateway;
            return this;
        }
        @CustomType.Setter
        public Builder network(String network) {
            if (network == null) {
              throw new MissingRequiredPropertyException("GetClusterLanRoute", "network");
            }
            this.network = network;
            return this;
        }
        public GetClusterLanRoute build() {
            final var _resultValue = new GetClusterLanRoute();
            _resultValue.gateway = gateway;
            _resultValue.network = network;
            return _resultValue;
        }
    }
}
