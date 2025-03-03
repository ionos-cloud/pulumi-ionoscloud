// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetMariadbClusterConnection {
    /**
     * @return The IP and subnet for your cluster.
     * 
     */
    private String cidr;
    /**
     * @return The datacenter to connect your cluster to.
     * 
     */
    private String datacenterId;
    /**
     * @return The numeric LAN ID to connect your cluster to.
     * 
     */
    private String lanId;

    private GetMariadbClusterConnection() {}
    /**
     * @return The IP and subnet for your cluster.
     * 
     */
    public String cidr() {
        return this.cidr;
    }
    /**
     * @return The datacenter to connect your cluster to.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return The numeric LAN ID to connect your cluster to.
     * 
     */
    public String lanId() {
        return this.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMariadbClusterConnection defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String cidr;
        private String datacenterId;
        private String lanId;
        public Builder() {}
        public Builder(GetMariadbClusterConnection defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cidr = defaults.cidr;
    	      this.datacenterId = defaults.datacenterId;
    	      this.lanId = defaults.lanId;
        }

        @CustomType.Setter
        public Builder cidr(String cidr) {
            if (cidr == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterConnection", "cidr");
            }
            this.cidr = cidr;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterConnection", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder lanId(String lanId) {
            if (lanId == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterConnection", "lanId");
            }
            this.lanId = lanId;
            return this;
        }
        public GetMariadbClusterConnection build() {
            final var _resultValue = new GetMariadbClusterConnection();
            _resultValue.cidr = cidr;
            _resultValue.datacenterId = datacenterId;
            _resultValue.lanId = lanId;
            return _resultValue;
        }
    }
}
