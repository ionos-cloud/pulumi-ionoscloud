// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.creg.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class RegistryStorageUsage {
    private @Nullable Integer bytes;
    private @Nullable String updatedAt;

    private RegistryStorageUsage() {}
    public Optional<Integer> bytes() {
        return Optional.ofNullable(this.bytes);
    }
    public Optional<String> updatedAt() {
        return Optional.ofNullable(this.updatedAt);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RegistryStorageUsage defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Integer bytes;
        private @Nullable String updatedAt;
        public Builder() {}
        public Builder(RegistryStorageUsage defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.bytes = defaults.bytes;
    	      this.updatedAt = defaults.updatedAt;
        }

        @CustomType.Setter
        public Builder bytes(@Nullable Integer bytes) {

            this.bytes = bytes;
            return this;
        }
        @CustomType.Setter
        public Builder updatedAt(@Nullable String updatedAt) {

            this.updatedAt = updatedAt;
            return this;
        }
        public RegistryStorageUsage build() {
            final var _resultValue = new RegistryStorageUsage();
            _resultValue.bytes = bytes;
            _resultValue.updatedAt = updatedAt;
            return _resultValue;
        }
    }
}
