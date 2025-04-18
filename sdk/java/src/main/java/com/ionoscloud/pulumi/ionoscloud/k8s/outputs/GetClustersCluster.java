// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.k8s.outputs;

import com.ionoscloud.pulumi.ionoscloud.k8s.outputs.GetClustersClusterConfig;
import com.ionoscloud.pulumi.ionoscloud.k8s.outputs.GetClustersClusterMaintenanceWindow;
import com.ionoscloud.pulumi.ionoscloud.k8s.outputs.GetClustersClusterS3Bucket;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@CustomType
public final class GetClustersCluster {
    /**
     * @return Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
     * 
     */
    private List<String> apiSubnetAllowLists;
    /**
     * @return A list of available versions for upgrading the cluster
     * 
     */
    private List<String> availableUpgradeVersions;
    private String caCrt;
    private List<GetClustersClusterConfig> configs;
    private String id;
    private String k8sVersion;
    private String kubeConfig;
    private String location;
    /**
     * @return A maintenance window comprise of a day of the week and a time for maintenance to be allowed
     * 
     */
    private List<GetClustersClusterMaintenanceWindow> maintenanceWindows;
    private String name;
    /**
     * @return The NAT gateway IP of the cluster if the cluster is private.
     * 
     */
    private String natGatewayIp;
    private List<String> nodePools;
    /**
     * @return The node subnet of the cluster, if the cluster is private.
     * 
     */
    private String nodeSubnet;
    /**
     * @return The indicator if the cluster is public or private.
     * 
     */
    private Boolean public_;
    /**
     * @return List of Object Storage bucket configured for K8s usage. For now it contains only an Object Storage bucket used to store K8s API audit logs.
     * 
     */
    private List<GetClustersClusterS3Bucket> s3Buckets;
    private String server;
    private String state;
    private Map<String,String> userTokens;
    /**
     * @return A list of versions that may be used for node pools under this cluster
     * 
     */
    private List<String> viableNodePoolVersions;

    private GetClustersCluster() {}
    /**
     * @return Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.
     * 
     */
    public List<String> apiSubnetAllowLists() {
        return this.apiSubnetAllowLists;
    }
    /**
     * @return A list of available versions for upgrading the cluster
     * 
     */
    public List<String> availableUpgradeVersions() {
        return this.availableUpgradeVersions;
    }
    public String caCrt() {
        return this.caCrt;
    }
    public List<GetClustersClusterConfig> configs() {
        return this.configs;
    }
    public String id() {
        return this.id;
    }
    public String k8sVersion() {
        return this.k8sVersion;
    }
    public String kubeConfig() {
        return this.kubeConfig;
    }
    public String location() {
        return this.location;
    }
    /**
     * @return A maintenance window comprise of a day of the week and a time for maintenance to be allowed
     * 
     */
    public List<GetClustersClusterMaintenanceWindow> maintenanceWindows() {
        return this.maintenanceWindows;
    }
    public String name() {
        return this.name;
    }
    /**
     * @return The NAT gateway IP of the cluster if the cluster is private.
     * 
     */
    public String natGatewayIp() {
        return this.natGatewayIp;
    }
    public List<String> nodePools() {
        return this.nodePools;
    }
    /**
     * @return The node subnet of the cluster, if the cluster is private.
     * 
     */
    public String nodeSubnet() {
        return this.nodeSubnet;
    }
    /**
     * @return The indicator if the cluster is public or private.
     * 
     */
    public Boolean public_() {
        return this.public_;
    }
    /**
     * @return List of Object Storage bucket configured for K8s usage. For now it contains only an Object Storage bucket used to store K8s API audit logs.
     * 
     */
    public List<GetClustersClusterS3Bucket> s3Buckets() {
        return this.s3Buckets;
    }
    public String server() {
        return this.server;
    }
    public String state() {
        return this.state;
    }
    public Map<String,String> userTokens() {
        return this.userTokens;
    }
    /**
     * @return A list of versions that may be used for node pools under this cluster
     * 
     */
    public List<String> viableNodePoolVersions() {
        return this.viableNodePoolVersions;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetClustersCluster defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> apiSubnetAllowLists;
        private List<String> availableUpgradeVersions;
        private String caCrt;
        private List<GetClustersClusterConfig> configs;
        private String id;
        private String k8sVersion;
        private String kubeConfig;
        private String location;
        private List<GetClustersClusterMaintenanceWindow> maintenanceWindows;
        private String name;
        private String natGatewayIp;
        private List<String> nodePools;
        private String nodeSubnet;
        private Boolean public_;
        private List<GetClustersClusterS3Bucket> s3Buckets;
        private String server;
        private String state;
        private Map<String,String> userTokens;
        private List<String> viableNodePoolVersions;
        public Builder() {}
        public Builder(GetClustersCluster defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.apiSubnetAllowLists = defaults.apiSubnetAllowLists;
    	      this.availableUpgradeVersions = defaults.availableUpgradeVersions;
    	      this.caCrt = defaults.caCrt;
    	      this.configs = defaults.configs;
    	      this.id = defaults.id;
    	      this.k8sVersion = defaults.k8sVersion;
    	      this.kubeConfig = defaults.kubeConfig;
    	      this.location = defaults.location;
    	      this.maintenanceWindows = defaults.maintenanceWindows;
    	      this.name = defaults.name;
    	      this.natGatewayIp = defaults.natGatewayIp;
    	      this.nodePools = defaults.nodePools;
    	      this.nodeSubnet = defaults.nodeSubnet;
    	      this.public_ = defaults.public_;
    	      this.s3Buckets = defaults.s3Buckets;
    	      this.server = defaults.server;
    	      this.state = defaults.state;
    	      this.userTokens = defaults.userTokens;
    	      this.viableNodePoolVersions = defaults.viableNodePoolVersions;
        }

        @CustomType.Setter
        public Builder apiSubnetAllowLists(List<String> apiSubnetAllowLists) {
            if (apiSubnetAllowLists == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "apiSubnetAllowLists");
            }
            this.apiSubnetAllowLists = apiSubnetAllowLists;
            return this;
        }
        public Builder apiSubnetAllowLists(String... apiSubnetAllowLists) {
            return apiSubnetAllowLists(List.of(apiSubnetAllowLists));
        }
        @CustomType.Setter
        public Builder availableUpgradeVersions(List<String> availableUpgradeVersions) {
            if (availableUpgradeVersions == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "availableUpgradeVersions");
            }
            this.availableUpgradeVersions = availableUpgradeVersions;
            return this;
        }
        public Builder availableUpgradeVersions(String... availableUpgradeVersions) {
            return availableUpgradeVersions(List.of(availableUpgradeVersions));
        }
        @CustomType.Setter
        public Builder caCrt(String caCrt) {
            if (caCrt == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "caCrt");
            }
            this.caCrt = caCrt;
            return this;
        }
        @CustomType.Setter
        public Builder configs(List<GetClustersClusterConfig> configs) {
            if (configs == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "configs");
            }
            this.configs = configs;
            return this;
        }
        public Builder configs(GetClustersClusterConfig... configs) {
            return configs(List.of(configs));
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder k8sVersion(String k8sVersion) {
            if (k8sVersion == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "k8sVersion");
            }
            this.k8sVersion = k8sVersion;
            return this;
        }
        @CustomType.Setter
        public Builder kubeConfig(String kubeConfig) {
            if (kubeConfig == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "kubeConfig");
            }
            this.kubeConfig = kubeConfig;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceWindows(List<GetClustersClusterMaintenanceWindow> maintenanceWindows) {
            if (maintenanceWindows == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "maintenanceWindows");
            }
            this.maintenanceWindows = maintenanceWindows;
            return this;
        }
        public Builder maintenanceWindows(GetClustersClusterMaintenanceWindow... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder natGatewayIp(String natGatewayIp) {
            if (natGatewayIp == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "natGatewayIp");
            }
            this.natGatewayIp = natGatewayIp;
            return this;
        }
        @CustomType.Setter
        public Builder nodePools(List<String> nodePools) {
            if (nodePools == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "nodePools");
            }
            this.nodePools = nodePools;
            return this;
        }
        public Builder nodePools(String... nodePools) {
            return nodePools(List.of(nodePools));
        }
        @CustomType.Setter
        public Builder nodeSubnet(String nodeSubnet) {
            if (nodeSubnet == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "nodeSubnet");
            }
            this.nodeSubnet = nodeSubnet;
            return this;
        }
        @CustomType.Setter("public")
        public Builder public_(Boolean public_) {
            if (public_ == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "public_");
            }
            this.public_ = public_;
            return this;
        }
        @CustomType.Setter
        public Builder s3Buckets(List<GetClustersClusterS3Bucket> s3Buckets) {
            if (s3Buckets == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "s3Buckets");
            }
            this.s3Buckets = s3Buckets;
            return this;
        }
        public Builder s3Buckets(GetClustersClusterS3Bucket... s3Buckets) {
            return s3Buckets(List.of(s3Buckets));
        }
        @CustomType.Setter
        public Builder server(String server) {
            if (server == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "server");
            }
            this.server = server;
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            if (state == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "state");
            }
            this.state = state;
            return this;
        }
        @CustomType.Setter
        public Builder userTokens(Map<String,String> userTokens) {
            if (userTokens == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "userTokens");
            }
            this.userTokens = userTokens;
            return this;
        }
        @CustomType.Setter
        public Builder viableNodePoolVersions(List<String> viableNodePoolVersions) {
            if (viableNodePoolVersions == null) {
              throw new MissingRequiredPropertyException("GetClustersCluster", "viableNodePoolVersions");
            }
            this.viableNodePoolVersions = viableNodePoolVersions;
            return this;
        }
        public Builder viableNodePoolVersions(String... viableNodePoolVersions) {
            return viableNodePoolVersions(List.of(viableNodePoolVersions));
        }
        public GetClustersCluster build() {
            final var _resultValue = new GetClustersCluster();
            _resultValue.apiSubnetAllowLists = apiSubnetAllowLists;
            _resultValue.availableUpgradeVersions = availableUpgradeVersions;
            _resultValue.caCrt = caCrt;
            _resultValue.configs = configs;
            _resultValue.id = id;
            _resultValue.k8sVersion = k8sVersion;
            _resultValue.kubeConfig = kubeConfig;
            _resultValue.location = location;
            _resultValue.maintenanceWindows = maintenanceWindows;
            _resultValue.name = name;
            _resultValue.natGatewayIp = natGatewayIp;
            _resultValue.nodePools = nodePools;
            _resultValue.nodeSubnet = nodeSubnet;
            _resultValue.public_ = public_;
            _resultValue.s3Buckets = s3Buckets;
            _resultValue.server = server;
            _resultValue.state = state;
            _resultValue.userTokens = userTokens;
            _resultValue.viableNodePoolVersions = viableNodePoolVersions;
            return _resultValue;
        }
    }
}
