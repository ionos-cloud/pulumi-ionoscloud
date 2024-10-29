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
public final class GetServerVolume {
    /**
     * @return The availability zone in which the volume should exist
     * 
     */
    private String availabilityZone;
    /**
     * @return The uuid of the Backup Unit that user has access to
     * 
     */
    private String backupUnitId;
    /**
     * @return The UUID of the attached server.
     * 
     */
    private String bootServer;
    /**
     * @return The bus type of the volume
     * 
     */
    private String bus;
    /**
     * @return Is capable of CPU hot plug (no reboot required)
     * 
     */
    private Boolean cpuHotPlug;
    /**
     * @return The Logical Unit Number (LUN) of the storage volume
     * 
     */
    private Integer deviceNumber;
    /**
     * @return Is capable of Virt-IO drive hot plug (no reboot required)
     * 
     */
    private Boolean discVirtioHotPlug;
    /**
     * @return Is capable of Virt-IO drive hot unplug (no reboot required)
     * 
     */
    private Boolean discVirtioHotUnplug;
    /**
     * @return ID of the server you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    private String id;
    private String imageName;
    /**
     * @return Initial password to be set for installed OS
     * 
     */
    private String imagePassword;
    /**
     * @return OS type of this volume
     * 
     */
    private String licenceType;
    /**
     * @return Name of an existing server that you want to search for.
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
     * @return The PCI slot number of the Nic
     * 
     */
    private Integer pciSlot;
    /**
     * @return Is capable of memory hot plug (no reboot required)
     * 
     */
    private Boolean ramHotPlug;
    /**
     * @return The size of the volume in GB
     * 
     */
    private Integer size;
    /**
     * @return Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key
     * 
     */
    private List<String> sshKeys;
    /**
     * @return The type of firewall rule
     * 
     */
    private String type;
    /**
     * @return The cloud-init configuration for the volume as base64 encoded string
     * 
     */
    private @Nullable String userData;

    private GetServerVolume() {}
    /**
     * @return The availability zone in which the volume should exist
     * 
     */
    public String availabilityZone() {
        return this.availabilityZone;
    }
    /**
     * @return The uuid of the Backup Unit that user has access to
     * 
     */
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
    /**
     * @return The bus type of the volume
     * 
     */
    public String bus() {
        return this.bus;
    }
    /**
     * @return Is capable of CPU hot plug (no reboot required)
     * 
     */
    public Boolean cpuHotPlug() {
        return this.cpuHotPlug;
    }
    /**
     * @return The Logical Unit Number (LUN) of the storage volume
     * 
     */
    public Integer deviceNumber() {
        return this.deviceNumber;
    }
    /**
     * @return Is capable of Virt-IO drive hot plug (no reboot required)
     * 
     */
    public Boolean discVirtioHotPlug() {
        return this.discVirtioHotPlug;
    }
    /**
     * @return Is capable of Virt-IO drive hot unplug (no reboot required)
     * 
     */
    public Boolean discVirtioHotUnplug() {
        return this.discVirtioHotUnplug;
    }
    /**
     * @return ID of the server you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public String id() {
        return this.id;
    }
    public String imageName() {
        return this.imageName;
    }
    /**
     * @return Initial password to be set for installed OS
     * 
     */
    public String imagePassword() {
        return this.imagePassword;
    }
    /**
     * @return OS type of this volume
     * 
     */
    public String licenceType() {
        return this.licenceType;
    }
    /**
     * @return Name of an existing server that you want to search for.
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
     * @return The PCI slot number of the Nic
     * 
     */
    public Integer pciSlot() {
        return this.pciSlot;
    }
    /**
     * @return Is capable of memory hot plug (no reboot required)
     * 
     */
    public Boolean ramHotPlug() {
        return this.ramHotPlug;
    }
    /**
     * @return The size of the volume in GB
     * 
     */
    public Integer size() {
        return this.size;
    }
    /**
     * @return Public SSH keys are set on the image as authorized keys for appropriate SSH login to the instance using the corresponding private key
     * 
     */
    public List<String> sshKeys() {
        return this.sshKeys;
    }
    /**
     * @return The type of firewall rule
     * 
     */
    public String type() {
        return this.type;
    }
    /**
     * @return The cloud-init configuration for the volume as base64 encoded string
     * 
     */
    public Optional<String> userData() {
        return Optional.ofNullable(this.userData);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetServerVolume defaults) {
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
        private String type;
        private @Nullable String userData;
        public Builder() {}
        public Builder(GetServerVolume defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.availabilityZone = defaults.availabilityZone;
    	      this.backupUnitId = defaults.backupUnitId;
    	      this.bootServer = defaults.bootServer;
    	      this.bus = defaults.bus;
    	      this.cpuHotPlug = defaults.cpuHotPlug;
    	      this.deviceNumber = defaults.deviceNumber;
    	      this.discVirtioHotPlug = defaults.discVirtioHotPlug;
    	      this.discVirtioHotUnplug = defaults.discVirtioHotUnplug;
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
    	      this.type = defaults.type;
    	      this.userData = defaults.userData;
        }

        @CustomType.Setter
        public Builder availabilityZone(String availabilityZone) {
            if (availabilityZone == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "availabilityZone");
            }
            this.availabilityZone = availabilityZone;
            return this;
        }
        @CustomType.Setter
        public Builder backupUnitId(String backupUnitId) {
            if (backupUnitId == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "backupUnitId");
            }
            this.backupUnitId = backupUnitId;
            return this;
        }
        @CustomType.Setter
        public Builder bootServer(String bootServer) {
            if (bootServer == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "bootServer");
            }
            this.bootServer = bootServer;
            return this;
        }
        @CustomType.Setter
        public Builder bus(String bus) {
            if (bus == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "bus");
            }
            this.bus = bus;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            if (cpuHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "cpuHotPlug");
            }
            this.cpuHotPlug = cpuHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder deviceNumber(Integer deviceNumber) {
            if (deviceNumber == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "deviceNumber");
            }
            this.deviceNumber = deviceNumber;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            if (discVirtioHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "discVirtioHotPlug");
            }
            this.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            if (discVirtioHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "discVirtioHotUnplug");
            }
            this.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder imageName(String imageName) {
            if (imageName == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "imageName");
            }
            this.imageName = imageName;
            return this;
        }
        @CustomType.Setter
        public Builder imagePassword(String imagePassword) {
            if (imagePassword == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "imagePassword");
            }
            this.imagePassword = imagePassword;
            return this;
        }
        @CustomType.Setter
        public Builder licenceType(String licenceType) {
            if (licenceType == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "licenceType");
            }
            this.licenceType = licenceType;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotPlug(Boolean nicHotPlug) {
            if (nicHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "nicHotPlug");
            }
            this.nicHotPlug = nicHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            if (nicHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "nicHotUnplug");
            }
            this.nicHotUnplug = nicHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder pciSlot(Integer pciSlot) {
            if (pciSlot == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "pciSlot");
            }
            this.pciSlot = pciSlot;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotPlug(Boolean ramHotPlug) {
            if (ramHotPlug == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "ramHotPlug");
            }
            this.ramHotPlug = ramHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder size(Integer size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "size");
            }
            this.size = size;
            return this;
        }
        @CustomType.Setter
        public Builder sshKeys(List<String> sshKeys) {
            if (sshKeys == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "sshKeys");
            }
            this.sshKeys = sshKeys;
            return this;
        }
        public Builder sshKeys(String... sshKeys) {
            return sshKeys(List.of(sshKeys));
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetServerVolume", "type");
            }
            this.type = type;
            return this;
        }
        @CustomType.Setter
        public Builder userData(@Nullable String userData) {

            this.userData = userData;
            return this;
        }
        public GetServerVolume build() {
            final var _resultValue = new GetServerVolume();
            _resultValue.availabilityZone = availabilityZone;
            _resultValue.backupUnitId = backupUnitId;
            _resultValue.bootServer = bootServer;
            _resultValue.bus = bus;
            _resultValue.cpuHotPlug = cpuHotPlug;
            _resultValue.deviceNumber = deviceNumber;
            _resultValue.discVirtioHotPlug = discVirtioHotPlug;
            _resultValue.discVirtioHotUnplug = discVirtioHotUnplug;
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
            _resultValue.type = type;
            _resultValue.userData = userData;
            return _resultValue;
        }
    }
}
