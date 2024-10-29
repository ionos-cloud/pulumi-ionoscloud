// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetCubeServerCdrom;
import com.pulumi.ionoscloud.outputs.GetCubeServerNic;
import com.pulumi.ionoscloud.outputs.GetCubeServerVolume;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetCubeServerResult {
    /**
     * @return The availability zone in which the volume should exist
     * 
     */
    private String availabilityZone;
    private String bootCdrom;
    private String bootImage;
    private String bootVolume;
    /**
     * @return list of
     * 
     */
    private List<GetCubeServerCdrom> cdroms;
    private Integer cores;
    private String cpuFamily;
    /**
     * @return The id of the datacenter
     * 
     */
    private String datacenterId;
    /**
     * @return Id of the firewall rule
     * 
     */
    private @Nullable String id;
    /**
     * @return Name of the firewall rule
     * 
     */
    private @Nullable String name;
    /**
     * @return list of
     * 
     */
    private List<GetCubeServerNic> nics;
    private Integer ram;
    /**
     * @return The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     * 
     */
    private @Nullable String templateUuid;
    private String token;
    /**
     * @return Status of the virtual Machine
     * 
     */
    private String vmState;
    /**
     * @return list of
     * 
     */
    private List<GetCubeServerVolume> volumes;

    private GetCubeServerResult() {}
    /**
     * @return The availability zone in which the volume should exist
     * 
     */
    public String availabilityZone() {
        return this.availabilityZone;
    }
    public String bootCdrom() {
        return this.bootCdrom;
    }
    public String bootImage() {
        return this.bootImage;
    }
    public String bootVolume() {
        return this.bootVolume;
    }
    /**
     * @return list of
     * 
     */
    public List<GetCubeServerCdrom> cdroms() {
        return this.cdroms;
    }
    public Integer cores() {
        return this.cores;
    }
    public String cpuFamily() {
        return this.cpuFamily;
    }
    /**
     * @return The id of the datacenter
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }
    /**
     * @return Id of the firewall rule
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return Name of the firewall rule
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return list of
     * 
     */
    public List<GetCubeServerNic> nics() {
        return this.nics;
    }
    public Integer ram() {
        return this.ram;
    }
    /**
     * @return The UUID of the template for creating a CUBE server; the available templates for CUBE servers can be found on the templates resource
     * 
     */
    public Optional<String> templateUuid() {
        return Optional.ofNullable(this.templateUuid);
    }
    public String token() {
        return this.token;
    }
    /**
     * @return Status of the virtual Machine
     * 
     */
    public String vmState() {
        return this.vmState;
    }
    /**
     * @return list of
     * 
     */
    public List<GetCubeServerVolume> volumes() {
        return this.volumes;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCubeServerResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String availabilityZone;
        private String bootCdrom;
        private String bootImage;
        private String bootVolume;
        private List<GetCubeServerCdrom> cdroms;
        private Integer cores;
        private String cpuFamily;
        private String datacenterId;
        private @Nullable String id;
        private @Nullable String name;
        private List<GetCubeServerNic> nics;
        private Integer ram;
        private @Nullable String templateUuid;
        private String token;
        private String vmState;
        private List<GetCubeServerVolume> volumes;
        public Builder() {}
        public Builder(GetCubeServerResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.availabilityZone = defaults.availabilityZone;
    	      this.bootCdrom = defaults.bootCdrom;
    	      this.bootImage = defaults.bootImage;
    	      this.bootVolume = defaults.bootVolume;
    	      this.cdroms = defaults.cdroms;
    	      this.cores = defaults.cores;
    	      this.cpuFamily = defaults.cpuFamily;
    	      this.datacenterId = defaults.datacenterId;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.nics = defaults.nics;
    	      this.ram = defaults.ram;
    	      this.templateUuid = defaults.templateUuid;
    	      this.token = defaults.token;
    	      this.vmState = defaults.vmState;
    	      this.volumes = defaults.volumes;
        }

        @CustomType.Setter
        public Builder availabilityZone(String availabilityZone) {
            if (availabilityZone == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "availabilityZone");
            }
            this.availabilityZone = availabilityZone;
            return this;
        }
        @CustomType.Setter
        public Builder bootCdrom(String bootCdrom) {
            if (bootCdrom == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "bootCdrom");
            }
            this.bootCdrom = bootCdrom;
            return this;
        }
        @CustomType.Setter
        public Builder bootImage(String bootImage) {
            if (bootImage == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "bootImage");
            }
            this.bootImage = bootImage;
            return this;
        }
        @CustomType.Setter
        public Builder bootVolume(String bootVolume) {
            if (bootVolume == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "bootVolume");
            }
            this.bootVolume = bootVolume;
            return this;
        }
        @CustomType.Setter
        public Builder cdroms(List<GetCubeServerCdrom> cdroms) {
            if (cdroms == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "cdroms");
            }
            this.cdroms = cdroms;
            return this;
        }
        public Builder cdroms(GetCubeServerCdrom... cdroms) {
            return cdroms(List.of(cdroms));
        }
        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder cpuFamily(String cpuFamily) {
            if (cpuFamily == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "cpuFamily");
            }
            this.cpuFamily = cpuFamily;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "datacenterId");
            }
            this.datacenterId = datacenterId;
            return this;
        }
        @CustomType.Setter
        public Builder id(@Nullable String id) {

            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nics(List<GetCubeServerNic> nics) {
            if (nics == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "nics");
            }
            this.nics = nics;
            return this;
        }
        public Builder nics(GetCubeServerNic... nics) {
            return nics(List.of(nics));
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder templateUuid(@Nullable String templateUuid) {

            this.templateUuid = templateUuid;
            return this;
        }
        @CustomType.Setter
        public Builder token(String token) {
            if (token == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "token");
            }
            this.token = token;
            return this;
        }
        @CustomType.Setter
        public Builder vmState(String vmState) {
            if (vmState == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "vmState");
            }
            this.vmState = vmState;
            return this;
        }
        @CustomType.Setter
        public Builder volumes(List<GetCubeServerVolume> volumes) {
            if (volumes == null) {
              throw new MissingRequiredPropertyException("GetCubeServerResult", "volumes");
            }
            this.volumes = volumes;
            return this;
        }
        public Builder volumes(GetCubeServerVolume... volumes) {
            return volumes(List.of(volumes));
        }
        public GetCubeServerResult build() {
            final var _resultValue = new GetCubeServerResult();
            _resultValue.availabilityZone = availabilityZone;
            _resultValue.bootCdrom = bootCdrom;
            _resultValue.bootImage = bootImage;
            _resultValue.bootVolume = bootVolume;
            _resultValue.cdroms = cdroms;
            _resultValue.cores = cores;
            _resultValue.cpuFamily = cpuFamily;
            _resultValue.datacenterId = datacenterId;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.nics = nics;
            _resultValue.ram = ram;
            _resultValue.templateUuid = templateUuid;
            _resultValue.token = token;
            _resultValue.vmState = vmState;
            _resultValue.volumes = volumes;
            return _resultValue;
        }
    }
}
