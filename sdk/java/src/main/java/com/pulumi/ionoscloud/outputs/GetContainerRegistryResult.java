// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetContainerRegistryFeature;
import com.pulumi.ionoscloud.outputs.GetContainerRegistryGarbageCollectionSchedule;
import com.pulumi.ionoscloud.outputs.GetContainerRegistryMaintenanceWindow;
import com.pulumi.ionoscloud.outputs.GetContainerRegistryStorageUsage;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetContainerRegistryResult {
    /**
     * @return The subnet CIDRs that are allowed to connect to the registry.  Specify &#34;a.b.c.d/32&#34; for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
     * 
     */
    private List<String> apiSubnetAllowLists;
    private List<GetContainerRegistryFeature> features;
    private List<GetContainerRegistryGarbageCollectionSchedule> garbageCollectionSchedules;
    private String hostname;
    /**
     * @return Id of the container registry.
     * 
     */
    private @Nullable String id;
    private @Nullable String location;
    private List<GetContainerRegistryMaintenanceWindow> maintenanceWindows;
    /**
     * @return The name of the container registry.
     * 
     */
    private @Nullable String name;
    private @Nullable Boolean partialMatch;
    private List<GetContainerRegistryStorageUsage> storageUsages;

    private GetContainerRegistryResult() {}
    /**
     * @return The subnet CIDRs that are allowed to connect to the registry.  Specify &#34;a.b.c.d/32&#34; for an individual IP address. __Note__: If this list is empty or not set, there are no restrictions.
     * 
     */
    public List<String> apiSubnetAllowLists() {
        return this.apiSubnetAllowLists;
    }
    public List<GetContainerRegistryFeature> features() {
        return this.features;
    }
    public List<GetContainerRegistryGarbageCollectionSchedule> garbageCollectionSchedules() {
        return this.garbageCollectionSchedules;
    }
    public String hostname() {
        return this.hostname;
    }
    /**
     * @return Id of the container registry.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }
    public List<GetContainerRegistryMaintenanceWindow> maintenanceWindows() {
        return this.maintenanceWindows;
    }
    /**
     * @return The name of the container registry.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    public Optional<Boolean> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }
    public List<GetContainerRegistryStorageUsage> storageUsages() {
        return this.storageUsages;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetContainerRegistryResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> apiSubnetAllowLists;
        private List<GetContainerRegistryFeature> features;
        private List<GetContainerRegistryGarbageCollectionSchedule> garbageCollectionSchedules;
        private String hostname;
        private @Nullable String id;
        private @Nullable String location;
        private List<GetContainerRegistryMaintenanceWindow> maintenanceWindows;
        private @Nullable String name;
        private @Nullable Boolean partialMatch;
        private List<GetContainerRegistryStorageUsage> storageUsages;
        public Builder() {}
        public Builder(GetContainerRegistryResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.apiSubnetAllowLists = defaults.apiSubnetAllowLists;
    	      this.features = defaults.features;
    	      this.garbageCollectionSchedules = defaults.garbageCollectionSchedules;
    	      this.hostname = defaults.hostname;
    	      this.id = defaults.id;
    	      this.location = defaults.location;
    	      this.maintenanceWindows = defaults.maintenanceWindows;
    	      this.name = defaults.name;
    	      this.partialMatch = defaults.partialMatch;
    	      this.storageUsages = defaults.storageUsages;
        }

        @CustomType.Setter
        public Builder apiSubnetAllowLists(List<String> apiSubnetAllowLists) {
            if (apiSubnetAllowLists == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "apiSubnetAllowLists");
            }
            this.apiSubnetAllowLists = apiSubnetAllowLists;
            return this;
        }
        public Builder apiSubnetAllowLists(String... apiSubnetAllowLists) {
            return apiSubnetAllowLists(List.of(apiSubnetAllowLists));
        }
        @CustomType.Setter
        public Builder features(List<GetContainerRegistryFeature> features) {
            if (features == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "features");
            }
            this.features = features;
            return this;
        }
        public Builder features(GetContainerRegistryFeature... features) {
            return features(List.of(features));
        }
        @CustomType.Setter
        public Builder garbageCollectionSchedules(List<GetContainerRegistryGarbageCollectionSchedule> garbageCollectionSchedules) {
            if (garbageCollectionSchedules == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "garbageCollectionSchedules");
            }
            this.garbageCollectionSchedules = garbageCollectionSchedules;
            return this;
        }
        public Builder garbageCollectionSchedules(GetContainerRegistryGarbageCollectionSchedule... garbageCollectionSchedules) {
            return garbageCollectionSchedules(List.of(garbageCollectionSchedules));
        }
        @CustomType.Setter
        public Builder hostname(String hostname) {
            if (hostname == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "hostname");
            }
            this.hostname = hostname;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder location(@Nullable String location) {

            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder maintenanceWindows(List<GetContainerRegistryMaintenanceWindow> maintenanceWindows) {
            if (maintenanceWindows == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "maintenanceWindows");
            }
            this.maintenanceWindows = maintenanceWindows;
            return this;
        }
        public Builder maintenanceWindows(GetContainerRegistryMaintenanceWindow... maintenanceWindows) {
            return maintenanceWindows(List.of(maintenanceWindows));
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder partialMatch(@Nullable Boolean partialMatch) {

            this.partialMatch = partialMatch;
            return this;
        }
        @CustomType.Setter
        public Builder storageUsages(List<GetContainerRegistryStorageUsage> storageUsages) {
            if (storageUsages == null) {
              throw new MissingRequiredPropertyException("GetContainerRegistryResult", "storageUsages");
            }
            this.storageUsages = storageUsages;
            return this;
        }
        public Builder storageUsages(GetContainerRegistryStorageUsage... storageUsages) {
            return storageUsages(List.of(storageUsages));
        }
        public GetContainerRegistryResult build() {
            final var _resultValue = new GetContainerRegistryResult();
            _resultValue.apiSubnetAllowLists = apiSubnetAllowLists;
            _resultValue.features = features;
            _resultValue.garbageCollectionSchedules = garbageCollectionSchedules;
            _resultValue.hostname = hostname;
            _resultValue.id = id;
            _resultValue.location = location;
            _resultValue.maintenanceWindows = maintenanceWindows;
            _resultValue.name = name;
            _resultValue.partialMatch = partialMatch;
            _resultValue.storageUsages = storageUsages;
            return _resultValue;
        }
    }
}
