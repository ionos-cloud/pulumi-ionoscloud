// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.ionoscloud.pulumi.ionoscloud.dbaas.outputs.GetMariaDBClusterConnection;
import com.ionoscloud.pulumi.ionoscloud.dbaas.outputs.GetMariaDBClusterMaintenanceWindow;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetMariaDBClusterResult {
    /**
     * @return The network connection for your cluster. Only one connection is allowed.
     * 
     */
    private List<GetMariaDBClusterConnection> connections;
    /**
     * @return [int] The number of CPU cores per instance.
     * 
     */
    private Integer cores;
    /**
     * @return [string] The friendly name of your cluster.
     * 
     */
    private String displayName;
    /**
     * @return [string] The DNS name pointing to your cluster.
     * 
     */
    private String dnsName;
    private String id;
    /**
     * @return [int] The total number of instances in the cluster (one primary and n-1 secondary).
     * 
     */
    private Integer instances;
    private @Nullable String location;
    /**
     * @return A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    private List<GetMariaDBClusterMaintenanceWindow> maintenanceWindows;
    /**
     * @return [string] The MariaDB version of your cluster.
     * 
     */
    private String mariadbVersion;
    /**
     * @return [int] The amount of memory per instance in gigabytes (GB).
     * 
     */
    private Integer ram;
    /**
     * @return [int] The amount of storage per instance in gigabytes (GB).
     * 
     */
    private Integer storageSize;

    private GetMariaDBClusterResult() {}
    /**
     * @return The network connection for your cluster. Only one connection is allowed.
     * 
     */
    public List<GetMariaDBClusterConnection> connections() {
        return this.connections;
    }
    /**
     * @return [int] The number of CPU cores per instance.
     * 
     */
    public Integer cores() {
        return this.cores;
    }
    /**
     * @return [string] The friendly name of your cluster.
     * 
     */
    public String displayName() {
        return this.displayName;
    }
    /**
     * @return [string] The DNS name pointing to your cluster.
     * 
     */
    public String dnsName() {
        return this.dnsName;
    }
    public String id() {
        return this.id;
    }
    /**
     * @return [int] The total number of instances in the cluster (one primary and n-1 secondary).
     * 
     */
    public Integer instances() {
        return this.instances;
    }
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }
    /**
     * @return A weekly 4 hour-long window, during which maintenance might occur.
     * 
     */
    public List<GetMariaDBClusterMaintenanceWindow> maintenanceWindows() {
        return this.maintenanceWindows;
    }
    /**
     * @return [string] The MariaDB version of your cluster.
     * 
     */
    public String mariadbVersion() {
        return this.mariadbVersion;
    }
    /**
     * @return [int] The amount of memory per instance in gigabytes (GB).
     * 
     */
    public Integer ram() {
        return this.ram;
    }
    /**
     * @return [int] The amount of storage per instance in gigabytes (GB).
     * 
     */
    public Integer storageSize() {
        return this.storageSize;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMariaDBClusterResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetMariaDBClusterConnection> connections;
        private Integer cores;
        private String displayName;
        private String dnsName;
        private String id;
        private Integer instances;
        private @Nullable String location;
        private List<GetMariaDBClusterMaintenanceWindow> maintenanceWindows;
        private String mariadbVersion;
        private Integer ram;
        private Integer storageSize;
        public Builder() {}
        public Builder(GetMariaDBClusterResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.connections = defaults.connections;
    	      this.cores = defaults.cores;
    	      this.displayName = defaults.displayName;
    	      this.dnsName = defaults.dnsName;
    	      this.id = defaults.id;
    	      this.instances = defaults.instances;
    	      this.location = defaults.location;
    	      this.maintenanceWindows = defaults.maintenanceWindows;
    	      this.mariadbVersion = defaults.mariadbVersion;
    	      this.ram = defaults.ram;
    	      this.storageSize = defaults.storageSize;
        }

        @CustomType.Setter
        public Builder connections(List<GetMariaDBClusterConnection> connections) {
            if (connections == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "connections");
            }
            this.connections = connections;
            return this;
        }
        public Builder connections(GetMariaDBClusterConnection... connections) {
            return connections(List.of(connections));
        }
        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder displayName(String displayName) {
            if (displayName == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "displayName");
            }
            this.displayName = displayName;
            return this;
        }
        @CustomType.Setter
        public Builder dnsName(String dnsName) {
            if (dnsName == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "dnsName");
            }
            this.dnsName = dnsName;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder instances(Integer instances) {
            if (instances == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "instances");
            }
            this.instances = instances;
            return this;
        }
        @CustomType.Setter
        public Builder location(@Nullable String location) {

            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceWindows(List<GetMariaDBClusterMaintenanceWindow> maintenanceWindows) {
            if (maintenanceWindows == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "maintenanceWindows");
            }
            this.maintenanceWindows = maintenanceWindows;
            return this;
        }
        public Builder maintenanceWindows(GetMariaDBClusterMaintenanceWindow... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }
        @CustomType.Setter
        public Builder mariadbVersion(String mariadbVersion) {
            if (mariadbVersion == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "mariadbVersion");
            }
            this.mariadbVersion = mariadbVersion;
            return this;
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder storageSize(Integer storageSize) {
            if (storageSize == null) {
              throw new MissingRequiredPropertyException("GetMariaDBClusterResult", "storageSize");
            }
            this.storageSize = storageSize;
            return this;
        }
        public GetMariaDBClusterResult build() {
            final var _resultValue = new GetMariaDBClusterResult();
            _resultValue.connections = connections;
            _resultValue.cores = cores;
            _resultValue.displayName = displayName;
            _resultValue.dnsName = dnsName;
            _resultValue.id = id;
            _resultValue.instances = instances;
            _resultValue.location = location;
            _resultValue.maintenanceWindows = maintenanceWindows;
            _resultValue.mariadbVersion = mariadbVersion;
            _resultValue.ram = ram;
            _resultValue.storageSize = storageSize;
            return _resultValue;
        }
    }
}
