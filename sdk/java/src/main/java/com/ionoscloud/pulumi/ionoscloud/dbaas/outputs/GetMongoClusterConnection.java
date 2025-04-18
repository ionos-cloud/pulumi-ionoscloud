// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetMongoClusterConnection {
    /**
     * @return The list of IPs and subnet for your cluster.
     *           Note the following unavailable IP ranges:
     *           10.233.64.0/18
     *           10.233.0.0/18
     *           10.233.114.0/24
     *  example: [192.168.1.100/24, 192.168.1.101/24]
     * 
     */
    private List<String> cidrLists;
    /**
     * @return The datacenter to connect your cluster to.
     * 
     */
    private String datacenterId;
    /**
     * @return The LAN to connect your cluster to.
     * 
     */
    private String lanId;

    private GetMongoClusterConnection() {}
    /**
     * @return The list of IPs and subnet for your cluster.
     *           Note the following unavailable IP ranges:
     *           10.233.64.0/18
     *           10.233.0.0/18
     *           10.233.114.0/24
     *  example: [192.168.1.100/24, 192.168.1.101/24]
     * 
     */
    public List<String> cidrLists() {
        return this.cidrLists;
    }
    /**
     * @return The datacenter to connect your cluster to.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return The LAN to connect your cluster to.
     * 
     */
    public String lanId() {
        return this.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMongoClusterConnection defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> cidrLists;
        private String datacenterId;
        private String lanId;
        public Builder() {}
        public Builder(GetMongoClusterConnection defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cidrLists = defaults.cidrLists;
    	      this.datacenterId = defaults.datacenterId;
    	      this.lanId = defaults.lanId;
        }

        @CustomType.Setter
        public Builder cidrLists(List<String> cidrLists) {
            if (cidrLists == null) {
              throw new MissingRequiredPropertyException("GetMongoClusterConnection", "cidrLists");
            }
            this.cidrLists = cidrLists;
            return this;
        }
        public Builder cidrLists(String... cidrLists) {
            return cidrLists(List.of(cidrLists));
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetMongoClusterConnection", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder lanId(String lanId) {
            if (lanId == null) {
              throw new MissingRequiredPropertyException("GetMongoClusterConnection", "lanId");
            }
            this.lanId = lanId;
            return this;
        }
        public GetMongoClusterConnection build() {
            final var _resultValue = new GetMongoClusterConnection();
            _resultValue.cidrLists = cidrLists;
            _resultValue.datacenterId = datacenterId;
            _resultValue.lanId = lanId;
            return _resultValue;
        }
    }
}
