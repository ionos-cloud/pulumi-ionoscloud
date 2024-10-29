// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetVcpuServerCdrom;
import com.pulumi.ionoscloud.outputs.GetVcpuServerLabel;
import com.pulumi.ionoscloud.outputs.GetVcpuServerNic;
import com.pulumi.ionoscloud.outputs.GetVcpuServerVolume;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetVcpuServerResult {
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
    private List<GetVcpuServerCdrom> cdroms;
    /**
     * @return The total number of cores for the server
     * 
     */
    private Integer cores;
    /**
     * @return CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
     * 
     */
    private String cpuFamily;
    /**
     * @return The id of the datacenter
     * 
     */
    private String datacenterId;
    /**
     * @return The Id of the label
     * 
     */
    private @Nullable String id;
    /**
     * @return list of
     * 
     */
    private List<GetVcpuServerLabel> labels;
    /**
     * @return Name of the firewall rule
     * 
     */
    private @Nullable String name;
    /**
     * @return list of
     * 
     */
    private List<GetVcpuServerNic> nics;
    /**
     * @return The amount of memory for the server in MB
     * 
     */
    private Integer ram;
    private String token;
    /**
     * @return The type of firewall rule
     * 
     */
    private String type;
    /**
     * @return Status of the virtual Machine
     * 
     */
    private String vmState;
    /**
     * @return list of
     * 
     */
    private List<GetVcpuServerVolume> volumes;

    private GetVcpuServerResult() {}
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
    public List<GetVcpuServerCdrom> cdroms() {
        return this.cdroms;
    }
    /**
     * @return The total number of cores for the server
     * 
     */
    public Integer cores() {
        return this.cores;
    }
    /**
     * @return CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
     * 
     */
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
     * @return The Id of the label
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }
    /**
     * @return list of
     * 
     */
    public List<GetVcpuServerLabel> labels() {
        return this.labels;
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
    public List<GetVcpuServerNic> nics() {
        return this.nics;
    }
    /**
     * @return The amount of memory for the server in MB
     * 
     */
    public Integer ram() {
        return this.ram;
    }
    public String token() {
        return this.token;
    }
    /**
     * @return The type of firewall rule
     * 
     */
    public String type() {
        return this.type;
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
    public List<GetVcpuServerVolume> volumes() {
        return this.volumes;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVcpuServerResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String availabilityZone;
        private String bootCdrom;
        private String bootImage;
        private String bootVolume;
        private List<GetVcpuServerCdrom> cdroms;
        private Integer cores;
        private String cpuFamily;
        private String datacenterId;
        private @Nullable String id;
        private List<GetVcpuServerLabel> labels;
        private @Nullable String name;
        private List<GetVcpuServerNic> nics;
        private Integer ram;
        private String token;
        private String type;
        private String vmState;
        private List<GetVcpuServerVolume> volumes;
        public Builder() {}
        public Builder(GetVcpuServerResult defaults) {
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
    	      this.labels = defaults.labels;
    	      this.name = defaults.name;
    	      this.nics = defaults.nics;
    	      this.ram = defaults.ram;
    	      this.token = defaults.token;
    	      this.type = defaults.type;
    	      this.vmState = defaults.vmState;
    	      this.volumes = defaults.volumes;
        }

        @CustomType.Setter
        public Builder availabilityZone(String availabilityZone) {
            if (availabilityZone == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "availabilityZone");
            }
            this.availabilityZone = availabilityZone;
            return this;
        }
        @CustomType.Setter
        public Builder bootCdrom(String bootCdrom) {
            if (bootCdrom == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "bootCdrom");
            }
            this.bootCdrom = bootCdrom;
            return this;
        }
        @CustomType.Setter
        public Builder bootImage(String bootImage) {
            if (bootImage == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "bootImage");
            }
            this.bootImage = bootImage;
            return this;
        }
        @CustomType.Setter
        public Builder bootVolume(String bootVolume) {
            if (bootVolume == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "bootVolume");
            }
            this.bootVolume = bootVolume;
            return this;
        }
        @CustomType.Setter
        public Builder cdroms(List<GetVcpuServerCdrom> cdroms) {
            if (cdroms == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "cdroms");
            }
            this.cdroms = cdroms;
            return this;
        }
        public Builder cdroms(GetVcpuServerCdrom... cdroms) {
            return cdroms(List.of(cdroms));
        }
        @CustomType.Setter
        public Builder cores(Integer cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder cpuFamily(String cpuFamily) {
            if (cpuFamily == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "cpuFamily");
            }
            this.cpuFamily = cpuFamily;
            return this;
        }
        @CustomType.Setter
        public Builder datacenterId(String datacenterId) {
            if (datacenterId == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "datacenterId");
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
        public Builder labels(List<GetVcpuServerLabel> labels) {
            if (labels == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "labels");
            }
            this.labels = labels;
            return this;
        }
        public Builder labels(GetVcpuServerLabel... labels) {
            return labels(List.of(labels));
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nics(List<GetVcpuServerNic> nics) {
            if (nics == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "nics");
            }
            this.nics = nics;
            return this;
        }
        public Builder nics(GetVcpuServerNic... nics) {
            return nics(List.of(nics));
        }
        @CustomType.Setter
        public Builder ram(Integer ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder token(String token) {
            if (token == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "token");
            }
            this.token = token;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "type");
            }
            this.type = type;
            return this;
        }
        @CustomType.Setter
        public Builder vmState(String vmState) {
            if (vmState == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "vmState");
            }
            this.vmState = vmState;
            return this;
        }
        @CustomType.Setter
        public Builder volumes(List<GetVcpuServerVolume> volumes) {
            if (volumes == null) {
              throw new MissingRequiredPropertyException("GetVcpuServerResult", "volumes");
            }
            this.volumes = volumes;
            return this;
        }
        public Builder volumes(GetVcpuServerVolume... volumes) {
            return volumes(List.of(volumes));
        }
        public GetVcpuServerResult build() {
            final var _resultValue = new GetVcpuServerResult();
            _resultValue.availabilityZone = availabilityZone;
            _resultValue.bootCdrom = bootCdrom;
            _resultValue.bootImage = bootImage;
            _resultValue.bootVolume = bootVolume;
            _resultValue.cdroms = cdroms;
            _resultValue.cores = cores;
            _resultValue.cpuFamily = cpuFamily;
            _resultValue.datacenterId = datacenterId;
            _resultValue.id = id;
            _resultValue.labels = labels;
            _resultValue.name = name;
            _resultValue.nics = nics;
            _resultValue.ram = ram;
            _resultValue.token = token;
            _resultValue.type = type;
            _resultValue.vmState = vmState;
            _resultValue.volumes = volumes;
            return _resultValue;
        }
    }
}
