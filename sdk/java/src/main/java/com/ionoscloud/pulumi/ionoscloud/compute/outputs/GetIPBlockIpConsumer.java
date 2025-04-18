// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetIPBlockIpConsumer {
    private String datacenterId;
    private String datacenterName;
    private String ip;
    private String k8sClusterUuid;
    private String k8sNodepoolUuid;
    private String mac;
    private String nicId;
    private String serverId;
    private String serverName;

    private GetIPBlockIpConsumer() {}
    public String datacenterId() {
        return this.datacenterId;
    }
    public String datacenterName() {
        return this.datacenterName;
    }
    public String ip() {
        return this.ip;
    }
    public String k8sClusterUuid() {
        return this.k8sClusterUuid;
    }
    public String k8sNodepoolUuid() {
        return this.k8sNodepoolUuid;
    }
    public String mac() {
        return this.mac;
    }
    public String nicId() {
        return this.nicId;
    }
    public String serverId() {
        return this.serverId;
    }
    public String serverName() {
        return this.serverName;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetIPBlockIpConsumer defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String datacenterId;
        private String datacenterName;
        private String ip;
        private String k8sClusterUuid;
        private String k8sNodepoolUuid;
        private String mac;
        private String nicId;
        private String serverId;
        private String serverName;
        public Builder() {}
        public Builder(GetIPBlockIpConsumer defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.datacenterId = defaults.datacenterId;
    	      this.datacenterName = defaults.datacenterName;
    	      this.ip = defaults.ip;
    	      this.k8sClusterUuid = defaults.k8sClusterUuid;
    	      this.k8sNodepoolUuid = defaults.k8sNodepoolUuid;
    	      this.mac = defaults.mac;
    	      this.nicId = defaults.nicId;
    	      this.serverId = defaults.serverId;
    	      this.serverName = defaults.serverName;
        }

        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterName(String datacenterName) {
            if (datacenterName == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "datacenterName");
            }
            this.datacenterName = datacenterName;
            return this;
        }
        @CustomType.Setter
        public Builder ip(String ip) {
            if (ip == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "ip");
            }
            this.ip = ip;
            return this;
        }
        @CustomType.Setter
        public Builder k8sClusterUuid(String k8sClusterUuid) {
            if (k8sClusterUuid == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "k8sClusterUuid");
            }
            this.k8sClusterUuid = k8sClusterUuid;
            return this;
        }
        @CustomType.Setter
        public Builder k8sNodepoolUuid(String k8sNodepoolUuid) {
            if (k8sNodepoolUuid == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "k8sNodepoolUuid");
            }
            this.k8sNodepoolUuid = k8sNodepoolUuid;
            return this;
        }
        @CustomType.Setter
        public Builder mac(String mac) {
            if (mac == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "mac");
            }
            this.mac = mac;
            return this;
        }
        @CustomType.Setter
        public Builder nicId(String nicId) {
            if (nicId == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "nicId");
            }
            this.nicId = nicId;
            return this;
        }
        @CustomType.Setter
        public Builder serverId(String serverId) {
            if (serverId == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "serverId");
            }
            this.serverId = serverId;
            return this;
        }
        @CustomType.Setter
        public Builder serverName(String serverName) {
            if (serverName == null) {
              throw new MissingRequiredPropertyException("GetIPBlockIpConsumer", "serverName");
            }
            this.serverName = serverName;
            return this;
        }
        public GetIPBlockIpConsumer build() {
            final var _resultValue = new GetIPBlockIpConsumer();
            _resultValue.datacenterId = datacenterId;
            _resultValue.datacenterName = datacenterName;
            _resultValue.ip = ip;
            _resultValue.k8sClusterUuid = k8sClusterUuid;
            _resultValue.k8sNodepoolUuid = k8sNodepoolUuid;
            _resultValue.mac = mac;
            _resultValue.nicId = nicId;
            _resultValue.serverId = serverId;
            _resultValue.serverName = serverName;
            return _resultValue;
        }
    }
}
