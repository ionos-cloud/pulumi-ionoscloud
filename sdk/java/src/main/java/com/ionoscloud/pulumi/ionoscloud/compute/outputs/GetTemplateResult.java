// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetTemplateResult {
    /**
     * @return The CPU cores count
     * 
     */
    private Double cores;
    /**
     * @return Id of template
     * 
     */
    private String id;
    /**
     * @return Name of template
     * 
     */
    private String name;
    /**
     * @return The RAM size in MB
     * 
     */
    private Double ram;
    /**
     * @return The storage size in GB
     * 
     */
    private Double storageSize;

    private GetTemplateResult() {}
    /**
     * @return The CPU cores count
     * 
     */
    public Double cores() {
        return this.cores;
    }
    /**
     * @return Id of template
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Name of template
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return The RAM size in MB
     * 
     */
    public Double ram() {
        return this.ram;
    }
    /**
     * @return The storage size in GB
     * 
     */
    public Double storageSize() {
        return this.storageSize;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetTemplateResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Double cores;
        private String id;
        private String name;
        private Double ram;
        private Double storageSize;
        public Builder() {}
        public Builder(GetTemplateResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cores = defaults.cores;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.ram = defaults.ram;
    	      this.storageSize = defaults.storageSize;
        }

        @CustomType.Setter
        public Builder cores(Double cores) {
            if (cores == null) {
              throw new MissingRequiredPropertyException("GetTemplateResult", "cores");
            }
            this.cores = cores;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetTemplateResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetTemplateResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder ram(Double ram) {
            if (ram == null) {
              throw new MissingRequiredPropertyException("GetTemplateResult", "ram");
            }
            this.ram = ram;
            return this;
        }
        @CustomType.Setter
        public Builder storageSize(Double storageSize) {
            if (storageSize == null) {
              throw new MissingRequiredPropertyException("GetTemplateResult", "storageSize");
            }
            this.storageSize = storageSize;
            return this;
        }
        public GetTemplateResult build() {
            final var _resultValue = new GetTemplateResult();
            _resultValue.cores = cores;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.ram = ram;
            _resultValue.storageSize = storageSize;
            return _resultValue;
        }
    }
}
