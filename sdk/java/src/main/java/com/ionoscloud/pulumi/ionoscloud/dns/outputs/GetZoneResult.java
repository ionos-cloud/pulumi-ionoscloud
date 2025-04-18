// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dns.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetZoneResult {
    /**
     * @return The description of the DNS Zone.
     * 
     */
    private String description;
    /**
     * @return Indicates if the DNS Zone is activated or not.
     * 
     */
    private Boolean enabled;
    /**
     * @return The UUID of the DNS Zone.
     * 
     */
    private String id;
    /**
     * @return The name of the DNS Zone.
     * 
     */
    private String name;
    /**
     * @return A list of available name servers.
     * 
     */
    private List<String> nameservers;
    private @Nullable Boolean partialMatch;

    private GetZoneResult() {}
    /**
     * @return The description of the DNS Zone.
     * 
     */
    public String description() {
        return this.description;
    }
    /**
     * @return Indicates if the DNS Zone is activated or not.
     * 
     */
    public Boolean enabled() {
        return this.enabled;
    }
    /**
     * @return The UUID of the DNS Zone.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The name of the DNS Zone.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return A list of available name servers.
     * 
     */
    public List<String> nameservers() {
        return this.nameservers;
    }
    public Optional<Boolean> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetZoneResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String description;
        private Boolean enabled;
        private String id;
        private String name;
        private List<String> nameservers;
        private @Nullable Boolean partialMatch;
        public Builder() {}
        public Builder(GetZoneResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.description = defaults.description;
    	      this.enabled = defaults.enabled;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.nameservers = defaults.nameservers;
    	      this.partialMatch = defaults.partialMatch;
        }

        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetZoneResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder enabled(Boolean enabled) {
            if (enabled == null) {
              throw new MissingRequiredPropertyException("GetZoneResult", "enabled");
            }
            this.enabled = enabled;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetZoneResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetZoneResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder nameservers(List<String> nameservers) {
            if (nameservers == null) {
              throw new MissingRequiredPropertyException("GetZoneResult", "nameservers");
            }
            this.nameservers = nameservers;
            return this;
        }
        public Builder nameservers(String... nameservers) {
            return nameservers(List.of(nameservers));
        }
        @CustomType.Setter
        public Builder partialMatch(@Nullable Boolean partialMatch) {

            this.partialMatch = partialMatch;
            return this;
        }
        public GetZoneResult build() {
            final var _resultValue = new GetZoneResult();
            _resultValue.description = description;
            _resultValue.enabled = enabled;
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.nameservers = nameservers;
            _resultValue.partialMatch = partialMatch;
            return _resultValue;
        }
    }
}
