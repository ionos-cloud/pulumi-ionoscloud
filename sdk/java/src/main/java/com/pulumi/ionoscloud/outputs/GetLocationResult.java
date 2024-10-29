// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.outputs.GetLocationCpuArchitecture;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetLocationResult {
    /**
     * @return Array of features and CPU families available in a location
     * 
     */
    private List<GetLocationCpuArchitecture> cpuArchitectures;
    private @Nullable String feature;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return List of image aliases available for the location
     * 
     */
    private List<String> imageAliases;
    private @Nullable String name;

    private GetLocationResult() {}
    /**
     * @return Array of features and CPU families available in a location
     * 
     */
    public List<GetLocationCpuArchitecture> cpuArchitectures() {
        return this.cpuArchitectures;
    }
    public Optional<String> feature() {
        return Optional.ofNullable(this.feature);
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return List of image aliases available for the location
     * 
     */
    public List<String> imageAliases() {
        return this.imageAliases;
    }
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLocationResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetLocationCpuArchitecture> cpuArchitectures;
        private @Nullable String feature;
        private String id;
        private List<String> imageAliases;
        private @Nullable String name;
        public Builder() {}
        public Builder(GetLocationResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.cpuArchitectures = defaults.cpuArchitectures;
    	      this.feature = defaults.feature;
    	      this.id = defaults.id;
    	      this.imageAliases = defaults.imageAliases;
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder cpuArchitectures(List<GetLocationCpuArchitecture> cpuArchitectures) {
            if (cpuArchitectures == null) {
              throw new MissingRequiredPropertyException("GetLocationResult", "cpuArchitectures");
            }
            this.cpuArchitectures = cpuArchitectures;
            return this;
        }
        public Builder cpuArchitectures(GetLocationCpuArchitecture... cpuArchitectures) {
            return cpuArchitectures(List.of(cpuArchitectures));
        }
        @CustomType.Setter
        public Builder feature(@Nullable String feature) {

            this.feature = feature;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetLocationResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder imageAliases(List<String> imageAliases) {
            if (imageAliases == null) {
              throw new MissingRequiredPropertyException("GetLocationResult", "imageAliases");
            }
            this.imageAliases = imageAliases;
            return this;
        }
        public Builder imageAliases(String... imageAliases) {
            return imageAliases(List.of(imageAliases));
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        public GetLocationResult build() {
            final var _resultValue = new GetLocationResult();
            _resultValue.cpuArchitectures = cpuArchitectures;
            _resultValue.feature = feature;
            _resultValue.id = id;
            _resultValue.imageAliases = imageAliases;
            _resultValue.name = name;
            return _resultValue;
        }
    }
}
