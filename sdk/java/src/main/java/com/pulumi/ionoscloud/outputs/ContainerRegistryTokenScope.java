// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class ContainerRegistryTokenScope {
    /**
     * @return [string] Example: [&#34;pull&#34;, &#34;push&#34;, &#34;delete&#34;]
     * 
     */
    private List<String> actions;
    /**
     * @return [string]
     * 
     */
    private String name;
    /**
     * @return [string]
     * 
     */
    private String type;

    private ContainerRegistryTokenScope() {}
    /**
     * @return [string] Example: [&#34;pull&#34;, &#34;push&#34;, &#34;delete&#34;]
     * 
     */
    public List<String> actions() {
        return this.actions;
    }
    /**
     * @return [string]
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return [string]
     * 
     */
    public String type() {
        return this.type;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(ContainerRegistryTokenScope defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<String> actions;
        private String name;
        private String type;
        public Builder() {}
        public Builder(ContainerRegistryTokenScope defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.actions = defaults.actions;
    	      this.name = defaults.name;
    	      this.type = defaults.type;
        }

        @CustomType.Setter
        public Builder actions(List<String> actions) {
            if (actions == null) {
              throw new MissingRequiredPropertyException("ContainerRegistryTokenScope", "actions");
            }
            this.actions = actions;
            return this;
        }
        public Builder actions(String... actions) {
            return actions(List.of(actions));
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("ContainerRegistryTokenScope", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("ContainerRegistryTokenScope", "type");
            }
            this.type = type;
            return this;
        }
        public ContainerRegistryTokenScope build() {
            final var _resultValue = new ContainerRegistryTokenScope();
            _resultValue.actions = actions;
            _resultValue.name = name;
            _resultValue.type = type;
            return _resultValue;
        }
    }
}
