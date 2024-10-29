// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Double;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetVcpuServerCdrom {
    /**
     * @return Cloud init compatibility
     * 
     */
    private String cloudInit;
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
     * @return Description of cdrom
     * 
     */
    private String description;
    /**
     * @return Is capable of SCSI drive hot plug (no reboot required)
     * 
     */
    private Boolean discScsiHotPlug;
    /**
     * @return Is capable of SCSI drive hot unplug (no reboot required)
     * 
     */
    private Boolean discScsiHotUnplug;
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
    /**
     * @return List of image aliases mapped for this Image
     * 
     */
    private List<String> imageAliases;
    /**
     * @return Type of image
     * 
     */
    private String imageType;
    /**
     * @return OS type of this volume
     * 
     */
    private String licenceType;
    /**
     * @return Location of that image/snapshot
     * 
     */
    private String location;
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
     * @return Indicates if the image is part of the public repository or not
     * 
     */
    private Boolean public_;
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
     * @return The size of the volume in GB
     * 
     */
    private Double size;

    private GetVcpuServerCdrom() {}
    /**
     * @return Cloud init compatibility
     * 
     */
    public String cloudInit() {
        return this.cloudInit;
    }
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
     * @return Description of cdrom
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
     * @return Is capable of SCSI drive hot unplug (no reboot required)
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
    /**
     * @return List of image aliases mapped for this Image
     * 
     */
    public List<String> imageAliases() {
        return this.imageAliases;
    }
    /**
     * @return Type of image
     * 
     */
    public String imageType() {
        return this.imageType;
    }
    /**
     * @return OS type of this volume
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
     * @return Indicates if the image is part of the public repository or not
     * 
     */
    public Boolean public_() {
        return this.public_;
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
     * @return The size of the volume in GB
     * 
     */
    public Double size() {
        return this.size;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVcpuServerCdrom defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String cloudInit;
        private Boolean cpuHotPlug;
        private Boolean cpuHotUnplug;
        private String description;
        private Boolean discScsiHotPlug;
        private Boolean discScsiHotUnplug;
        private Boolean discVirtioHotPlug;
        private Boolean discVirtioHotUnplug;
        private String id;
        private List<String> imageAliases;
        private String imageType;
        private String licenceType;
        private String location;
        private String name;
        private Boolean nicHotPlug;
        private Boolean nicHotUnplug;
        private Boolean public_;
        private Boolean ramHotPlug;
        private Boolean ramHotUnplug;
        private Double size;
        public Builder() {}
        public Builder(GetVcpuServerCdrom defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cloudInit = defaults.cloudInit;
    	      this.cpuHotPlug = defaults.cpuHotPlug;
    	      this.cpuHotUnplug = defaults.cpuHotUnplug;
    	      this.description = defaults.description;
    	      this.discScsiHotPlug = defaults.discScsiHotPlug;
    	      this.discScsiHotUnplug = defaults.discScsiHotUnplug;
    	      this.discVirtioHotPlug = defaults.discVirtioHotPlug;
    	      this.discVirtioHotUnplug = defaults.discVirtioHotUnplug;
    	      this.id = defaults.id;
    	      this.imageAliases = defaults.imageAliases;
    	      this.imageType = defaults.imageType;
    	      this.licenceType = defaults.licenceType;
    	      this.location = defaults.location;
    	      this.name = defaults.name;
    	      this.nicHotPlug = defaults.nicHotPlug;
    	      this.nicHotUnplug = defaults.nicHotUnplug;
    	      this.public_ = defaults.public_;
    	      this.ramHotPlug = defaults.ramHotPlug;
    	      this.ramHotUnplug = defaults.ramHotUnplug;
    	      this.size = defaults.size;
        }

        @CustomType.Setter
        public Builder cloudInit(String cloudInit) {
            if (cloudInit == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "cloudInit");
            }
            this.cloudInit = cloudInit;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            if (cpuHotPlug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "cpuHotPlug");
            }
            this.cpuHotPlug = cpuHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotUnplug(Boolean cpuHotUnplug) {
            if (cpuHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "cpuHotUnplug");
            }
            this.cpuHotUnplug = cpuHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotPlug(Boolean discScsiHotPlug) {
            if (discScsiHotPlug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "discScsiHotPlug");
            }
            this.discScsiHotPlug = discScsiHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotUnplug(Boolean discScsiHotUnplug) {
            if (discScsiHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "discScsiHotUnplug");
            }
            this.discScsiHotUnplug = discScsiHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            if (discVirtioHotPlug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "discVirtioHotPlug");
            }
            this.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            if (discVirtioHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "discVirtioHotUnplug");
            }
            this.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder imageAliases(List<String> imageAliases) {
            if (imageAliases == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "imageAliases");
            }
            this.imageAliases = imageAliases;
            return this;
        }
        public Builder imageAliases(String... imageAliases) {
            return imageAliases(List.of(imageAliases));
        }
        @CustomType.Setter
        public Builder imageType(String imageType) {
            if (imageType == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "imageType");
            }
            this.imageType = imageType;
            return this;
        }
        @CustomType.Setter
        public Builder licenceType(String licenceType) {
            if (licenceType == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "licenceType");
            }
            this.licenceType = licenceType;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotPlug(Boolean nicHotPlug) {
            if (nicHotPlug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "nicHotPlug");
            }
            this.nicHotPlug = nicHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            if (nicHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "nicHotUnplug");
            }
            this.nicHotUnplug = nicHotUnplug;
            return this;
        }
        @CustomType.Setter("public")
        public Builder public_(Boolean public_) {
            if (public_ == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "public_");
            }
            this.public_ = public_;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotPlug(Boolean ramHotPlug) {
            if (ramHotPlug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "ramHotPlug");
            }
            this.ramHotPlug = ramHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotUnplug(Boolean ramHotUnplug) {
            if (ramHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "ramHotUnplug");
            }
            this.ramHotUnplug = ramHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder size(Double size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerCdrom", "size");
            }
            this.size = size;
            return this;
        }
        public GetVcpuServerCdrom build() {
            final var _resultValue = new GetVcpuServerCdrom();
            _resultValue.cloudInit = cloudInit;
            _resultValue.cpuHotPlug = cpuHotPlug;
            _resultValue.cpuHotUnplug = cpuHotUnplug;
            _resultValue.description = description;
            _resultValue.discScsiHotPlug = discScsiHotPlug;
            _resultValue.discScsiHotUnplug = discScsiHotUnplug;
            _resultValue.discVirtioHotPlug = discVirtioHotPlug;
            _resultValue.discVirtioHotUnplug = discVirtioHotUnplug;
            _resultValue.id = id;
            _resultValue.imageAliases = imageAliases;
            _resultValue.imageType = imageType;
            _resultValue.licenceType = licenceType;
            _resultValue.location = location;
            _resultValue.name = name;
            _resultValue.nicHotPlug = nicHotPlug;
            _resultValue.nicHotUnplug = nicHotUnplug;
            _resultValue.public_ = public_;
            _resultValue.ramHotPlug = ramHotPlug;
            _resultValue.ramHotUnplug = ramHotUnplug;
            _resultValue.size = size;
            return _resultValue;
        }
    }
}
