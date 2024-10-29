// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetServersServerVolume {
    private String availabilityZone;
    private String backupUnitId;
    /**
     * @return The UUID of the attached server.
     * 
     */
    private String bootServer;
    private String bus;
    private Boolean cpuHotPlug;
    private Integer deviceNumber;
    private Boolean discVirtioHotPlug;
    private Boolean discVirtioHotUnplug;
    private String diskType;
    private String id;
    private String imageName;
    private String imagePassword;
    private String licenceType;
    private String name;
    private Boolean nicHotPlug;
    private Boolean nicHotUnplug;
    private Integer pciSlot;
    private Boolean ramHotPlug;
    private Integer size;
    private List<String> sshKeys;
    private @Nullable String userData;

    private GetServersServerVolume() {}
    public String availabilityZone() {
        return this.availabilityZone;
    }
    public String backupUnitId() {
        return this.backupUnitId;
    }
    /**
     * @return The UUID of the attached server.
     * 
     */
    public String bootServer() {
        return this.bootServer;
    }
    public String bus() {
        return this.bus;
    }
    public Boolean cpuHotPlug() {
        return this.cpuHotPlug;
    }
    public Integer deviceNumber() {
        return this.deviceNumber;
    }
    public Boolean discVirtioHotPlug() {
        return this.discVirtioHotPlug;
    }
    public Boolean discVirtioHotUnplug() {
        return this.discVirtioHotUnplug;
    }
    public String diskType() {
        return this.diskType;
    }
    public String id() {
        return this.id;
    }
    public String imageName() {
        return this.imageName;
    }
    public String imagePassword() {
        return this.imagePassword;
    }
    public String licenceType() {
        return this.licenceType;
    }
    public String name() {
        return this.name;
    }
    public Boolean nicHotPlug() {
        return this.nicHotPlug;
    }
    public Boolean nicHotUnplug() {
        return this.nicHotUnplug;
    }
    public Integer pciSlot() {
        return this.pciSlot;
    }
    public Boolean ramHotPlug() {
        return this.ramHotPlug;
    }
    public Integer size() {
        return this.size;
    }
    public List<String> sshKeys() {
        return this.sshKeys;
    }
    public Optional<String> userData() {
        return Optional.ofNullable(this.userData);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetServersServerVolume defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String availabilityZone;
        private String backupUnitId;
        private String bootServer;
        private String bus;
        private Boolean cpuHotPlug;
        private Integer deviceNumber;
        private Boolean discVirtioHotPlug;
        private Boolean discVirtioHotUnplug;
        private String diskType;
        private String id;
        private String imageName;
        private String imagePassword;
        private String licenceType;
        private String name;
        private Boolean nicHotPlug;
        private Boolean nicHotUnplug;
        private Integer pciSlot;
        private Boolean ramHotPlug;
        private Integer size;
        private List<String> sshKeys;
        private @Nullable String userData;
        public Builder() {}
        public Builder(GetServersServerVolume defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.availabilityZone = defaults.availabilityZone;
    	      this.backupUnitId = defaults.backupUnitId;
    	      this.bootServer = defaults.bootServer;
    	      this.bus = defaults.bus;
    	      this.cpuHotPlug = defaults.cpuHotPlug;
    	      this.deviceNumber = defaults.deviceNumber;
    	      this.discVirtioHotPlug = defaults.discVirtioHotPlug;
    	      this.discVirtioHotUnplug = defaults.discVirtioHotUnplug;
    	      this.diskType = defaults.diskType;
    	      this.id = defaults.id;
    	      this.imageName = defaults.imageName;
    	      this.imagePassword = defaults.imagePassword;
    	      this.licenceType = defaults.licenceType;
    	      this.name = defaults.name;
    	      this.nicHotPlug = defaults.nicHotPlug;
    	      this.nicHotUnplug = defaults.nicHotUnplug;
    	      this.pciSlot = defaults.pciSlot;
    	      this.ramHotPlug = defaults.ramHotPlug;
    	      this.size = defaults.size;
    	      this.sshKeys = defaults.sshKeys;
    	      this.userData = defaults.userData;
        }

        @CustomType.Setter
        public Builder availabilityZone(String availabilityZone) {
            if (availabilityZone == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "availabilityZone");
            }
            this.availabilityZone = availabilityZone;
            return this;
        }
        @CustomType.Setter
        public Builder backupUnitId(String backupUnitId) {
            if (backupUnitId == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "backupUnitId");
            }
            this.backupUnitId = backupUnitId;
            return this;
        }
        @CustomType.Setter
        public Builder bootServer(String bootServer) {
            if (bootServer == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "bootServer");
            }
            this.bootServer = bootServer;
            return this;
        }
        @CustomType.Setter
        public Builder bus(String bus) {
            if (bus == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "bus");
            }
            this.bus = bus;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            if (cpuHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "cpuHotPlug");
            }
            this.cpuHotPlug = cpuHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder deviceNumber(Integer deviceNumber) {
            if (deviceNumber == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "deviceNumber");
            }
            this.deviceNumber = deviceNumber;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            if (discVirtioHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "discVirtioHotPlug");
            }
            this.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            if (discVirtioHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "discVirtioHotUnplug");
            }
            this.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder diskType(String diskType) {
            if (diskType == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "diskType");
            }
            this.diskType = diskType;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder imageName(String imageName) {
            if (imageName == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "imageName");
            }
            this.imageName = imageName;
            return this;
        }
        @CustomType.Setter
        public Builder imagePassword(String imagePassword) {
            if (imagePassword == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "imagePassword");
            }
            this.imagePassword = imagePassword;
            return this;
        }
        @CustomType.Setter
        public Builder licenceType(String licenceType) {
            if (licenceType == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "licenceType");
            }
            this.licenceType = licenceType;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotPlug(Boolean nicHotPlug) {
            if (nicHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "nicHotPlug");
            }
            this.nicHotPlug = nicHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            if (nicHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "nicHotUnplug");
            }
            this.nicHotUnplug = nicHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder pciSlot(Integer pciSlot) {
            if (pciSlot == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "pciSlot");
            }
            this.pciSlot = pciSlot;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotPlug(Boolean ramHotPlug) {
            if (ramHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "ramHotPlug");
            }
            this.ramHotPlug = ramHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder size(Integer size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "size");
            }
            this.size = size;
            return this;
        }
        @CustomType.Setter
        public Builder sshKeys(List<String> sshKeys) {
            if (sshKeys == null) {
              throw new MissingRequiredPropertyException("GetServersServerVolume", "sshKeys");
            }
            this.sshKeys = sshKeys;
            return this;
        }
        public Builder sshKeys(String... sshKeys) {
            return sshKeys(List.of(sshKeys));
        }
        @CustomType.Setter
        public Builder userData(@Nullable String userData) {

            this.userData = userData;
            return this;
        }
        public GetServersServerVolume build() {
            final var _resultValue = new GetServersServerVolume();
            _resultValue.availabilityZone = availabilityZone;
            _resultValue.backupUnitId = backupUnitId;
            _resultValue.bootServer = bootServer;
            _resultValue.bus = bus;
            _resultValue.cpuHotPlug = cpuHotPlug;
            _resultValue.deviceNumber = deviceNumber;
            _resultValue.discVirtioHotPlug = discVirtioHotPlug;
            _resultValue.discVirtioHotUnplug = discVirtioHotUnplug;
            _resultValue.diskType = diskType;
            _resultValue.id = id;
            _resultValue.imageName = imageName;
            _resultValue.imagePassword = imagePassword;
            _resultValue.licenceType = licenceType;
            _resultValue.name = name;
            _resultValue.nicHotPlug = nicHotPlug;
            _resultValue.nicHotUnplug = nicHotUnplug;
            _resultValue.pciSlot = pciSlot;
            _resultValue.ramHotPlug = ramHotPlug;
            _resultValue.size = size;
            _resultValue.sshKeys = sshKeys;
            _resultValue.userData = userData;
            return _resultValue;
        }
    }
}
