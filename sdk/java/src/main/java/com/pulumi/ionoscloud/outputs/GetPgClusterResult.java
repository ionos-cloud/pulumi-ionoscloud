// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetPgClusterConnection;
import com.pulumi.ionoscloud.outputs.GetPgClusterConnectionPooler;
import com.pulumi.ionoscloud.outputs.GetPgClusterFromBackup;
import com.pulumi.ionoscloud.outputs.GetPgClusterMaintenanceWindow;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetPgClusterResult {
    private String backupLocation;
    private List<GetPgClusterConnectionPooler> connectionPoolers;
    private List<GetPgClusterConnection> connections;
    private Integer cores;
    private @Nullable String displayName;
    private String dnsName;
    private List<GetPgClusterFromBackup> fromBackups;
    private @Nullable String id;
    private Integer instances;
    private String location;
    private List<GetPgClusterMaintenanceWindow> maintenanceWindows;
    private String postgresVersion;
    private Integer ram;
    private Integer storageSize;
    private String storageType;
    private String synchronizationMode;

    private GetPgClusterResult() {}
    public String backupLocation() {
        return this.backupLocation;
    }
    public List<GetPgClusterConnectionPooler> connectionPoolers() {
        return this.connectionPoolers;
    }
    public List<GetPgClusterConnection> connections() {
        return this.connections;
    }
    public Integer cores() {
        return this.cores;
    }
    public Optional<String> displayName() {
        return Optional.ofNullable(this.displayName);
    }
    public String dnsName() {
        return this.dnsName;
    }
    public List<GetPgClusterFromBackup> fromBackups() {
        return this.fromBackups;
    }
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public Integer instances() {
        return this.instances;
    }
    public String location() {
        return this.location;
    }
    public List<GetPgClusterMaintenanceWindow> maintenanceWindows() {
        return this.maintenanceWindows;
    }
    public String postgresVersion() {
        return this.postgresVersion;
    }
    public Integer ram() {
        return this.ram;
    }
    public Integer storageSize() {
        return this.storageSize;
    }
    public String storageType() {
        return this.storageType;
    }
    public String synchronizationMode() {
        return this.synchronizationMode;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetPgClusterResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String backupLocation;
        private List<GetPgClusterConnectionPooler> connectionPoolers;
        private List<GetPgClusterConnection> connections;
        private Integer cores;
        private @Nullable String displayName;
        private String dnsName;
        private List<GetPgClusterFromBackup> fromBackups;
        private @Nullable String id;
        private Integer instances;
        private String location;
        private List<GetPgClusterMaintenanceWindow> maintenanceWindows;
        private String postgresVersion;
        private Integer ram;
        private Integer storageSize;
        private String storageType;
        private String synchronizationMode;
        public Builder() {}
        public Builder(GetPgClusterResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.backupLocation = defaults.backupLocation;
    	      this.connectionPoolers = defaults.connectionPoolers;
    	      this.connections = defaults.connections;
    	      this.cores = defaults.cores;
    	      this.displayName = defaults.displayName;
    	      this.dnsName = defaults.dnsName;
    	      this.fromBackups = defaults.fromBackups;
    	      this.id = defaults.id;
    	      this.instances = defaults.instances;
    	      this.location = defaults.location;
    	      this.maintenanceWindows = defaults.maintenanceWindows;
    	      this.postgresVersion = defaults.postgresVersion;
    	      this.ram = defaults.ram;
    	      this.storageSize = defaults.storageSize;
    	      this.storageType = defaults.storageType;
    	      this.synchronizationMode = defaults.synchronizationMode;
        }

        @CustomType.Setter
        public Builder backupLocation(String backupLocation) {
            if (backupLocation == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "backupLocation");
            }
            this.backupLocation = backupLocation;
            return this;
        }
        @CustomType.Setter
        public Builder connectionPoolers(List<GetPgClusterConnectionPooler> connectionPoolers) {
            if (connectionPoolers == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "connectionPoolers");
            }
            this.connectionPoolers = connectionPoolers;
            return this;
        }
        public Builder connectionPoolers(GetPgClusterConnectionPooler... connectionPoolers) {
            return connectionPoolers(List.of(connectionPoolers));
        }
        @CustomType.Setter
        public Builder connections(List<GetPgClusterConnection> connections) {
            if (connections == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "connections");
            }
            this.connections = connections;
            return this;
        }
        public Builder connections(GetPgClusterConnection... connections) {
            return connections(List.of(connections));
        }
        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder displayName(@Nullable String displayName) {

            this.displayName = displayName;
            return this;
        }
        @CustomType.Setter
        public Builder dnsName(String dnsName) {
            if (dnsName == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "dnsName");
            }
            this.dnsName = dnsName;
            return this;
        }
        @CustomType.Setter
        public Builder fromBackups(List<GetPgClusterFromBackup> fromBackups) {
            if (fromBackups == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "fromBackups");
            }
            this.fromBackups = fromBackups;
            return this;
        }
        public Builder fromBackups(GetPgClusterFromBackup... fromBackups) {
            return fromBackups(List.of(fromBackups));
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder instances(Integer instances) {
            if (instances == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "instances");
            }
            this.instances = instances;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceWindows(List<GetPgClusterMaintenanceWindow> maintenanceWindows) {
            if (maintenanceWindows == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "maintenanceWindows");
            }
            this.maintenanceWindows = maintenanceWindows;
            return this;
        }
        public Builder maintenanceWindows(GetPgClusterMaintenanceWindow... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }
        @CustomType.Setter
        public Builder postgresVersion(String postgresVersion) {
            if (postgresVersion == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "postgresVersion");
            }
            this.postgresVersion = postgresVersion;
            return this;
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder storageSize(Integer storageSize) {
            if (storageSize == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "storageSize");
            }
            this.storageSize = storageSize;
            return this;
        }
        @CustomType.Setter
        public Builder storageType(String storageType) {
            if (storageType == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "storageType");
            }
            this.storageType = storageType;
            return this;
        }
        @CustomType.Setter
        public Builder synchronizationMode(String synchronizationMode) {
            if (synchronizationMode == null) {
              throw new MissingRequiredPropertyException("GetPgClusterResult", "synchronizationMode");
            }
            this.synchronizationMode = synchronizationMode;
            return this;
        }
        public GetPgClusterResult build() {
            final var _resultValue = new GetPgClusterResult();
            _resultValue.backupLocation = backupLocation;
            _resultValue.connectionPoolers = connectionPoolers;
            _resultValue.connections = connections;
            _resultValue.cores = cores;
            _resultValue.displayName = displayName;
            _resultValue.dnsName = dnsName;
            _resultValue.fromBackups = fromBackups;
            _resultValue.id = id;
            _resultValue.instances = instances;
            _resultValue.location = location;
            _resultValue.maintenanceWindows = maintenanceWindows;
            _resultValue.postgresVersion = postgresVersion;
            _resultValue.ram = ram;
            _resultValue.storageSize = storageSize;
            _resultValue.storageType = storageType;
            _resultValue.synchronizationMode = synchronizationMode;
            return _resultValue;
        }
    }
}
