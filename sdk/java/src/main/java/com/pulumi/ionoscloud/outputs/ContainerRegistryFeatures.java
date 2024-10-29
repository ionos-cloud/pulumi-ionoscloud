// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class ContainerRegistryFeatures {
    /**
     * @return [bool] Enables or disables the Vulnerability Scanning feature for the Container Registry. To disable this feature, set the attribute to false when creating the CR resource.
     * 
     * &gt; **⚠ WARNING** `Container Registry Vulnerability Scanning` is a paid feature which is enabled by default, and cannot be turned off after activation. To disable this feature for a Container Registry, ensure `vulnerability_scanning` is set to false on resource creation.
     * 
     */
    private @Nullable Boolean vulnerabilityScanning;

    private ContainerRegistryFeatures() {}
    /**
     * @return [bool] Enables or disables the Vulnerability Scanning feature for the Container Registry. To disable this feature, set the attribute to false when creating the CR resource.
     * 
     * &gt; **⚠ WARNING** `Container Registry Vulnerability Scanning` is a paid feature which is enabled by default, and cannot be turned off after activation. To disable this feature for a Container Registry, ensure `vulnerability_scanning` is set to false on resource creation.
     * 
     */
    public Optional<Boolean> vulnerabilityScanning() {
        return Optional.ofNullable(this.vulnerabilityScanning);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ContainerRegistryFeatures defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean vulnerabilityScanning;
        public Builder() {}
        public Builder(ContainerRegistryFeatures defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.vulnerabilityScanning = defaults.vulnerabilityScanning;
        }

        @CustomType.Setter
        public Builder vulnerabilityScanning(@Nullable Boolean vulnerabilityScanning) {

            this.vulnerabilityScanning = vulnerabilityScanning;
            return this;
        }
        public ContainerRegistryFeatures build() {
            final var _resultValue = new ContainerRegistryFeatures();
            _resultValue.vulnerabilityScanning = vulnerabilityScanning;
            return _resultValue;
        }
    }
}
