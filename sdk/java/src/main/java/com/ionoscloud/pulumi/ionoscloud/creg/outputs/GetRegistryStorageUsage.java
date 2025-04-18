// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.creg.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetRegistryStorageUsage {
    private Integer bytes;
    private String updatedAt;

    private GetRegistryStorageUsage() {}
    public Integer bytes() {
        return this.bytes;
    }
    public String updatedAt() {
        return this.updatedAt;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetRegistryStorageUsage defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Integer bytes;
        private String updatedAt;
        public Builder() {}
        public Builder(GetRegistryStorageUsage defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.bytes = defaults.bytes;
    	      this.updatedAt = defaults.updatedAt;
        }

        @CustomType.Setter
        public Builder bytes(Integer bytes) {
            if (bytes == null) {
              throw new MissingRequiredPropertyException("GetRegistryStorageUsage", "bytes");
            }
            this.bytes = bytes;
            return this;
        }
        @CustomType.Setter
        public Builder updatedAt(String updatedAt) {
            if (updatedAt == null) {
              throw new MissingRequiredPropertyException("GetRegistryStorageUsage", "updatedAt");
            }
            this.updatedAt = updatedAt;
            return this;
        }
        public GetRegistryStorageUsage build() {
            final var _resultValue = new GetRegistryStorageUsage();
            _resultValue.bytes = bytes;
            _resultValue.updatedAt = updatedAt;
            return _resultValue;
        }
    }
}
