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
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetImageResult {
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
     * @return description of the image
     * 
     */
    private @Nullable String description;
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
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    private @Nullable String imageAlias;
    /**
     * @return List of image aliases mapped for this Image
     * 
     */
    private List<String> imageAliases;
    /**
     * @return OS type of this Image
     * 
     */
    private String licenceType;
    /**
     * @return Location of that image/snapshot.
     * 
     */
    private @Nullable String location;
    /**
     * @return name of the image
     * 
     */
    private @Nullable String name;
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
     * @return The size of the image in GB
     * 
     */
    private Double size;
    /**
     * @return This indicates the type of image
     * 
     */
    private @Nullable String type;
    private @Nullable String version;

    private GetImageResult() {}
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
     * @return description of the image
     * 
     */
    public Optional<String> description() {
        return Optional.ofNullable(this.description);
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
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    public Optional<String> imageAlias() {
        return Optional.ofNullable(this.imageAlias);
    }
    /**
     * @return List of image aliases mapped for this Image
     * 
     */
    public List<String> imageAliases() {
        return this.imageAliases;
    }
    /**
     * @return OS type of this Image
     * 
     */
    public String licenceType() {
        return this.licenceType;
    }
    /**
     * @return Location of that image/snapshot.
     * 
     */
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }
    /**
     * @return name of the image
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
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
     * @return The size of the image in GB
     * 
     */
    public Double size() {
        return this.size;
    }
    /**
     * @return This indicates the type of image
     * 
     */
    public Optional<String> type() {
        return Optional.ofNullable(this.type);
    }
    public Optional<String> version() {
        return Optional.ofNullable(this.version);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetImageResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String cloudInit;
        private Boolean cpuHotPlug;
        private Boolean cpuHotUnplug;
        private @Nullable String description;
        private Boolean discScsiHotPlug;
        private Boolean discScsiHotUnplug;
        private Boolean discVirtioHotPlug;
        private Boolean discVirtioHotUnplug;
        private String id;
        private @Nullable String imageAlias;
        private List<String> imageAliases;
        private String licenceType;
        private @Nullable String location;
        private @Nullable String name;
        private Boolean nicHotPlug;
        private Boolean nicHotUnplug;
        private Boolean public_;
        private Boolean ramHotPlug;
        private Boolean ramHotUnplug;
        private Double size;
        private @Nullable String type;
        private @Nullable String version;
        public Builder() {}
        public Builder(GetImageResult defaults) {
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
    	      this.imageAlias = defaults.imageAlias;
    	      this.imageAliases = defaults.imageAliases;
    	      this.licenceType = defaults.licenceType;
    	      this.location = defaults.location;
    	      this.name = defaults.name;
    	      this.nicHotPlug = defaults.nicHotPlug;
    	      this.nicHotUnplug = defaults.nicHotUnplug;
    	      this.public_ = defaults.public_;
    	      this.ramHotPlug = defaults.ramHotPlug;
    	      this.ramHotUnplug = defaults.ramHotUnplug;
    	      this.size = defaults.size;
    	      this.type = defaults.type;
    	      this.version = defaults.version;
        }

        @CustomType.Setter
        public Builder cloudInit(String cloudInit) {
            if (cloudInit == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "cloudInit");
            }
            this.cloudInit = cloudInit;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotPlug(Boolean cpuHotPlug) {
            if (cpuHotPlug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "cpuHotPlug");
            }
            this.cpuHotPlug = cpuHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder cpuHotUnplug(Boolean cpuHotUnplug) {
            if (cpuHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "cpuHotUnplug");
            }
            this.cpuHotUnplug = cpuHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder description(@Nullable String description) {

            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotPlug(Boolean discScsiHotPlug) {
            if (discScsiHotPlug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "discScsiHotPlug");
            }
            this.discScsiHotPlug = discScsiHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discScsiHotUnplug(Boolean discScsiHotUnplug) {
            if (discScsiHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "discScsiHotUnplug");
            }
            this.discScsiHotUnplug = discScsiHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotPlug(Boolean discVirtioHotPlug) {
            if (discVirtioHotPlug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "discVirtioHotPlug");
            }
            this.discVirtioHotPlug = discVirtioHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder discVirtioHotUnplug(Boolean discVirtioHotUnplug) {
            if (discVirtioHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "discVirtioHotUnplug");
            }
            this.discVirtioHotUnplug = discVirtioHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder imageAlias(@Nullable String imageAlias) {

            this.imageAlias = imageAlias;
            return this;
        }
        @CustomType.Setter
        public Builder imageAliases(List<String> imageAliases) {
            if (imageAliases == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "imageAliases");
            }
            this.imageAliases = imageAliases;
            return this;
        }
        public Builder imageAliases(String... imageAliases) {
            return imageAliases(List.of(imageAliases));
        }
        @CustomType.Setter
        public Builder licenceType(String licenceType) {
            if (licenceType == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "licenceType");
            }
            this.licenceType = licenceType;
            return this;
        }
        @CustomType.Setter
        public Builder location(@Nullable String location) {

            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotPlug(Boolean nicHotPlug) {
            if (nicHotPlug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "nicHotPlug");
            }
            this.nicHotPlug = nicHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder nicHotUnplug(Boolean nicHotUnplug) {
            if (nicHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "nicHotUnplug");
            }
            this.nicHotUnplug = nicHotUnplug;
            return this;
        }
        @CustomType.Setter("public")
        public Builder public_(Boolean public_) {
            if (public_ == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "public_");
            }
            this.public_ = public_;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotPlug(Boolean ramHotPlug) {
            if (ramHotPlug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "ramHotPlug");
            }
            this.ramHotPlug = ramHotPlug;
            return this;
        }
        @CustomType.Setter
        public Builder ramHotUnplug(Boolean ramHotUnplug) {
            if (ramHotUnplug == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "ramHotUnplug");
            }
            this.ramHotUnplug = ramHotUnplug;
            return this;
        }
        @CustomType.Setter
        public Builder size(Double size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetImageResult", "size");
            }
            this.size = size;
            return this;
        }
        @CustomType.Setter
        public Builder type(@Nullable String type) {

            this.type = type;
            return this;
        }
        @CustomType.Setter
        public Builder version(@Nullable String version) {

            this.version = version;
            return this;
        }
        public GetImageResult build() {
            final var _resultValue = new GetImageResult();
            _resultValue.cloudInit = cloudInit;
            _resultValue.cpuHotPlug = cpuHotPlug;
            _resultValue.cpuHotUnplug = cpuHotUnplug;
            _resultValue.description = description;
            _resultValue.discScsiHotPlug = discScsiHotPlug;
            _resultValue.discScsiHotUnplug = discScsiHotUnplug;
            _resultValue.discVirtioHotPlug = discVirtioHotPlug;
            _resultValue.discVirtioHotUnplug = discVirtioHotUnplug;
            _resultValue.id = id;
            _resultValue.imageAlias = imageAlias;
            _resultValue.imageAliases = imageAliases;
            _resultValue.licenceType = licenceType;
            _resultValue.location = location;
            _resultValue.name = name;
            _resultValue.nicHotPlug = nicHotPlug;
            _resultValue.nicHotUnplug = nicHotUnplug;
            _resultValue.public_ = public_;
            _resultValue.ramHotPlug = ramHotPlug;
            _resultValue.ramHotUnplug = ramHotUnplug;
            _resultValue.size = size;
            _resultValue.type = type;
            _resultValue.version = version;
            return _resultValue;
        }
    }
}
