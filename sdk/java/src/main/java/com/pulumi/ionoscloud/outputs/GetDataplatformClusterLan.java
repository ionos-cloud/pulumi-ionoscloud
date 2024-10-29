// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetDataplatformClusterLanRoute;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetDataplatformClusterLan {
    /**
     * @return Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is &#39;true&#39;.
     * 
     */
    private Boolean dhcp;
    /**
     * @return The LAN ID of an existing LAN at the related data center
     * 
     */
    private String lanId;
    /**
     * @return An array of additional LANs attached to worker nodes
     * 
     */
    private List<GetDataplatformClusterLanRoute> routes;

    private GetDataplatformClusterLan() {}
    /**
     * @return Indicates if the Kubernetes node pool LAN will reserve an IP using DHCP. The default value is &#39;true&#39;.
     * 
     */
    public Boolean dhcp() {
        return this.dhcp;
    }
    /**
     * @return The LAN ID of an existing LAN at the related data center
     * 
     */
    public String lanId() {
        return this.lanId;
    }
    /**
     * @return An array of additional LANs attached to worker nodes
     * 
     */
    public List<GetDataplatformClusterLanRoute> routes() {
        return this.routes;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetDataplatformClusterLan defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean dhcp;
        private String lanId;
        private List<GetDataplatformClusterLanRoute> routes;
        public Builder() {}
        public Builder(GetDataplatformClusterLan defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dhcp = defaults.dhcp;
    	      this.lanId = defaults.lanId;
    	      this.routes = defaults.routes;
        }

        @CustomType.Setter
        public Builder dhcp(Boolean dhcp) {
            if (dhcp == null) {
              throw new MissingRequiredPropertyException("GetDataplatformClusterLan", "dhcp");
            }
            this.dhcp = dhcp;
            return this;
        }
        @CustomType.Setter
        public Builder lanId(String lanId) {
            if (lanId == null) {
              throw new MissingRequiredPropertyException("GetDataplatformClusterLan", "lanId");
            }
            this.lanId = lanId;
            return this;
        }
        @CustomType.Setter
        public Builder routes(List<GetDataplatformClusterLanRoute> routes) {
            if (routes == null) {
              throw new MissingRequiredPropertyException("GetDataplatformClusterLan", "routes");
            }
            this.routes = routes;
            return this;
        }
        public Builder routes(GetDataplatformClusterLanRoute... routes) {
            return routes(List.of(routes));
        }
        public GetDataplatformClusterLan build() {
            final var _resultValue = new GetDataplatformClusterLan();
            _resultValue.dhcp = dhcp;
            _resultValue.lanId = lanId;
            _resultValue.routes = routes;
            return _resultValue;
        }
    }
}
