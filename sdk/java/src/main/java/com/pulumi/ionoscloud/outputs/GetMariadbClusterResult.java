// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetMariadbClusterConnection;
import com.pulumi.ionoscloud.outputs.GetMariadbClusterMaintenanceWindow;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetMariadbClusterResult {
    private List<GetMariadbClusterConnection> connections;
    private Integer cores;
    private @Nullable String displayName;
    private String dnsName;
    private @Nullable String id;
    private Integer instances;
    private @Nullable String location;
    private List<GetMariadbClusterMaintenanceWindow> maintenanceWindows;
    private String mariadbVersion;
    private Integer ram;
    private Integer storageSize;

    private GetMariadbClusterResult() {}
    public List<GetMariadbClusterConnection> connections() {
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
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public Integer instances() {
        return this.instances;
    }
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }
    public List<GetMariadbClusterMaintenanceWindow> maintenanceWindows() {
        return this.maintenanceWindows;
    }
    public String mariadbVersion() {
        return this.mariadbVersion;
    }
    public Integer ram() {
        return this.ram;
    }
    public Integer storageSize() {
        return this.storageSize;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetMariadbClusterResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetMariadbClusterConnection> connections;
        private Integer cores;
        private @Nullable String displayName;
        private String dnsName;
        private @Nullable String id;
        private Integer instances;
        private @Nullable String location;
        private List<GetMariadbClusterMaintenanceWindow> maintenanceWindows;
        private String mariadbVersion;
        private Integer ram;
        private Integer storageSize;
        public Builder() {}
        public Builder(GetMariadbClusterResult defaults) {
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
        public Builder connections(List<GetMariadbClusterConnection> connections) {
            if (connections == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "connections");
            }
            this.connections = connections;
            return this;
        }
        public Builder connections(GetMariadbClusterConnection... connections) {
            return connections(List.of(connections));
        }
        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "cores");
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
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "dnsName");
            }
            this.dnsName = dnsName;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder instances(Integer instances) {
            if (instances == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "instances");
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
        public Builder maintenanceWindows(List<GetMariadbClusterMaintenanceWindow> maintenanceWindows) {
            if (maintenanceWindows == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "maintenanceWindows");
            }
            this.maintenanceWindows = maintenanceWindows;
            return this;
        }
        public Builder maintenanceWindows(GetMariadbClusterMaintenanceWindow... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }
        @CustomType.Setter
        public Builder mariadbVersion(String mariadbVersion) {
            if (mariadbVersion == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "mariadbVersion");
            }
            this.mariadbVersion = mariadbVersion;
            return this;
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder storageSize(Integer storageSize) {
            if (storageSize == null) {
              throw new MissingRequiredPropertyException("GetMariadbClusterResult", "storageSize");
            }
            this.storageSize = storageSize;
            return this;
        }
        public GetMariadbClusterResult build() {
            final var _resultValue = new GetMariadbClusterResult();
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
