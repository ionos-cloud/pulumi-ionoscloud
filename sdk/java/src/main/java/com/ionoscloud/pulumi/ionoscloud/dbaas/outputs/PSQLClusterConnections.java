// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class PSQLClusterConnections {
    /**
     * @return [true] The IP and subnet for the database. Note the following unavailable IP ranges: 10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. Please enter in the correct format like IP/Subnet, exp: 192.168.10.0/24. See [Private IPs](https://www.ionos.com/help/server-cloud-infrastructure/private-network/private-ip-address-ranges/) and [Configuring the network](https://docs.ionos.com/cloud/compute-engine/networks/how-tos/configure-networks).
     * 
     */
    private String cidr;
    /**
     * @return [true] The datacenter to connect your cluster to.
     * 
     */
    private String datacenterId;
    /**
     * @return [true] The LAN to connect your cluster to.
     * 
     */
    private String lanId;

    private PSQLClusterConnections() {}
    /**
     * @return [true] The IP and subnet for the database. Note the following unavailable IP ranges: 10.233.64.0/18, 10.233.0.0/18, 10.233.114.0/24. Please enter in the correct format like IP/Subnet, exp: 192.168.10.0/24. See [Private IPs](https://www.ionos.com/help/server-cloud-infrastructure/private-network/private-ip-address-ranges/) and [Configuring the network](https://docs.ionos.com/cloud/compute-engine/networks/how-tos/configure-networks).
     * 
     */
    public String cidr() {
        return this.cidr;
    }
    /**
     * @return [true] The datacenter to connect your cluster to.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return [true] The LAN to connect your cluster to.
     * 
     */
    public String lanId() {
        return this.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(PSQLClusterConnections defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String cidr;
        private String datacenterId;
        private String lanId;
        public Builder() {}
        public Builder(PSQLClusterConnections defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cidr = defaults.cidr;
    	      this.datacenterId = defaults.datacenterId;
    	      this.lanId = defaults.lanId;
        }

        @CustomType.Setter
        public Builder cidr(String cidr) {
            if (cidr == null) {
              throw new MissingRequiredPropertyException("PSQLClusterConnections", "cidr");
            }
            this.cidr = cidr;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("PSQLClusterConnections", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder lanId(String lanId) {
            if (lanId == null) {
              throw new MissingRequiredPropertyException("PSQLClusterConnections", "lanId");
            }
            this.lanId = lanId;
            return this;
        }
        public PSQLClusterConnections build() {
            final var _resultValue = new PSQLClusterConnections();
            _resultValue.cidr = cidr;
            _resultValue.datacenterId = datacenterId;
            _resultValue.lanId = lanId;
            return _resultValue;
        }
    }
}
