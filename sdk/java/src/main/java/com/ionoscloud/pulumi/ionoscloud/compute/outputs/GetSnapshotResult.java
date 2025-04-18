// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetSnapshotResult {
    /**
     * @return Is capable of CPU hot plug (no reboot required)
     * 
     */
    private Boolean cpuHotPlug;
    /**
     * @return Is capable of CPU hot unplug (no reboot required)
     * 
     */
    private Boolean cpuHotUnplug;
    /**
     * @return Human readable description
     * 
     */
    private String description;
    /**
     * @return Is capable of SCSI drive hot plug (no reboot required)
     * 
     */
    private Boolean discScsiHotPlug;
    /**
     * @return Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    private Boolean discScsiHotUnplug;
    /**
     * @return Is capable of Virt-IO drive hot plug (no reboot required)
     * 
     */
    private Boolean discVirtioHotPlug;
    /**
     * @return Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    private Boolean discVirtioHotUnplug;
    /**
     * @return UUID of the snapshot
     * 
     */
    private String id;
    /**
     * @return OS type of this Snapshot
     * 
     */
    private String licenceType;
    /**
     * @return Location of that image/snapshot
     * 
     */
    private String location;
    /**
     * @return The name of the snapshot.
     * 
     */
    private String name;
    /**
     * @return Is capable of nic hot plug (no reboot required)
     * 
     */
    private Boolean nicHotPlug;
    /**
     * @return Is capable of nic hot unplug (no reboot required)
     * 
     */
    private Boolean nicHotUnplug;
    /**
     * @return Is capable of memory hot plug (no reboot required)
     * 
     */
    private Boolean ramHotPlug;
    /**
     * @return Is capable of memory hot unplug (no reboot required)
     * 
     */
    private Boolean ramHotUnplug;
    /**
     * @return Boolean value representing if the snapshot requires extra protection e.g. two factor protection
     * 
     */
    private Boolean secAuthProtection;
    /**
     * @return The size of the image in GB
     * 
     */
    private Integer size;

    private GetSnapshotResult() {}
    /**
     * @return Is capable of CPU hot plug (no reboot required)
     * 
     */
    public Boolean cpuHotPlug() {
        return this.cpuHotPlug;
    }
    /**
     * @return Is capable of CPU hot unplug (no reboot required)
     * 
     */
    public Boolean cpuHotUnplug() {
        return this.cpuHotUnplug;
    }
    /**
     * @return Human readable description
     * 
     */
    public String description() {
        return this.description;
    }
    /**
     * @return Is capable of SCSI drive hot plug (no reboot required)
     * 
     */
    public Boolean discScsiHotPlug() {
        return this.discScsiHotPlug;
    }
    /**
     * @return Is capable of SCSI drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    public Boolean discScsiHotUnplug() {
        return this.discScsiHotUnplug;
    }
    /**
     * @return Is capable of Virt-IO drive hot plug (no reboot required)
     * 
     */
    public Boolean discVirtioHotPlug() {
        return this.discVirtioHotPlug;
    }
    /**
     * @return Is capable of Virt-IO drive hot unplug (no reboot required). This works only for non-Windows virtual Machines.
     * 
     */
    public Boolean discVirtioHotUnplug() {
        return this.discVirtioHotUnplug;
    }
    /**
     * @return UUID of the snapshot
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return OS type of this Snapshot
     * 
     */
    public String licenceType() {
        return this.licenceType;
    }
    /**
     * @return Location of that image/snapshot
     * 
     */
    public String location() {
        return this.location;
    }
    /**
     * @return The name of the snapshot.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Is capable of nic hot plug (no reboot required)
     * 
     */
    public Boolean nicHotPlug() {
        return this.nicHotPlug;
    }
    /**
     * @return Is capable of nic hot unplug (no reboot required)
     * 
     */
    public Boolean nicHotUnplug() {
        return this.nicHotUnplug;
    }
    /**
     * @return Is capable of memory hot plug (no reboot required)
     * 
     */
    public Boolean ramHotPlug() {
        return this.ramHotPlug;
    }
    /**
     * @return Is capable of memory hot unplug (no reboot required)
     * 
     */
    public Boolean ramHotUnplug() {
        return this.ramHotUnplug;
    }
    /**
     * @return Boolean value representing if the snapshot requires extra protection e.g. two factor protection
     * 
     */
    public Boolean secAuthProtection() {
        return this.secAuthProtection;
    }
    /**
     * @return The size of the image in GB
     * 
     */
    public Integer size() {
        return this.size;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetSnapshotResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean cpuHotPlug;
        private Boolean cpuHotUnplug;
        private String description;
        private Boolean discScsiHotPlug;
        private Boolean discScsiHotUnplug;
        private Boolean discVirtioHotPlug;
        private Boolean discVirtioHotUnplug;
        private String id;
        private String licenceType;
        private String location;
        private String name;
        private Boolean nicHotPlug;
        private Boolean nicHotUnplug;
        private Boolean ramHotPlug;
        private Boolean ramHotUnplug;
        private Boolean secAuthProtection;
        private Integer size;
        public Builder() {}
        public Builder(GetSnapshotResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cpuHotPlug = defaults.cpuHotPlug;
    	      this.cpuHotUnplug = defaults.cpuHotUnplug;
    	      this.description = defaults.description;
    	      this.discScsiHotPlug = defaults.discScsiHotPlug;
    	      this.discScsiHotUnplug = defaults.discScsiHotUnplug;
    	      this.discVirtioHotPlug = defaults.discVirtioHotPlug;
    	      this.discVirtioHotUnplug = defaults.discVirtioHotUnplug;
    	      this.id = defaults.id;
    	      this.licenceType = defaults.licenceType;
    	      this.location = defaults.location;
    	      this.name = defaults.name;
    	      this.nicHotPlug = defaults.nicHotPlug;
    	      this.nicHotUnplug = defaults.nicHotUnplug;
    	      this.ramHotPlug = defaults.ramHotPlug;
    	      this.ramHotUnplug = defaults.ramHotUnplug;
    	      this.secAuthProtection = defaults.secAuthProtection;
    	      this.size = defaults.size;
        }

        @CustomType.Setter
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            if (cpuHotPlug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "cpuHotPlug");
            }
            this.cpuHotPlug = cpuHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotUnplug(Boolean cpuHotUnplug) {
            if (cpuHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "cpuHotUnplug");
            }
            this.cpuHotUnplug = cpuHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotPlug(Boolean discScsiHotPlug) {
            if (discScsiHotPlug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "discScsiHotPlug");
            }
            this.discScsiHotPlug = discScsiHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotUnplug(Boolean discScsiHotUnplug) {
            if (discScsiHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "discScsiHotUnplug");
            }
            this.discScsiHotUnplug = discScsiHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            if (discVirtioHotPlug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "discVirtioHotPlug");
            }
            this.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            if (discVirtioHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "discVirtioHotUnplug");
            }
            this.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder licenceType(String licenceType) {
            if (licenceType == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "licenceType");
            }
            this.licenceType = licenceType;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotPlug(Boolean nicHotPlug) {
            if (nicHotPlug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "nicHotPlug");
            }
            this.nicHotPlug = nicHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            if (nicHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "nicHotUnplug");
            }
            this.nicHotUnplug = nicHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotPlug(Boolean ramHotPlug) {
            if (ramHotPlug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "ramHotPlug");
            }
            this.ramHotPlug = ramHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotUnplug(Boolean ramHotUnplug) {
            if (ramHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "ramHotUnplug");
            }
            this.ramHotUnplug = ramHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder secAuthProtection(Boolean secAuthProtection) {
            if (secAuthProtection == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "secAuthProtection");
            }
            this.secAuthProtection = secAuthProtection;
            return this;
        }
        @CustomType.Setter
        public Builder size(Integer size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetSnapshotResult", "size");
            }
            this.size = size;
            return this;
        }
        public GetSnapshotResult build() {
            final var _resultValue = new GetSnapshotResult();
            _resultValue.cpuHotPlug = cpuHotPlug;
            _resultValue.cpuHotUnplug = cpuHotUnplug;
            _resultValue.description = description;
            _resultValue.discScsiHotPlug = discScsiHotPlug;
            _resultValue.discScsiHotUnplug = discScsiHotUnplug;
            _resultValue.discVirtioHotPlug = discVirtioHotPlug;
            _resultValue.discVirtioHotUnplug = discVirtioHotUnplug;
            _resultValue.id = id;
            _resultValue.licenceType = licenceType;
            _resultValue.location = location;
            _resultValue.name = name;
            _resultValue.nicHotPlug = nicHotPlug;
            _resultValue.nicHotUnplug = nicHotUnplug;
            _resultValue.ramHotPlug = ramHotPlug;
            _resultValue.ramHotUnplug = ramHotUnplug;
            _resultValue.secAuthProtection = secAuthProtection;
            _resultValue.size = size;
            return _resultValue;
        }
    }
}
