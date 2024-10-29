// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Map;
import java.util.Objects;

@CustomType
public final class GetK8sClustersClusterConfigContext {
    private Map<String,String> context;
    private String name;

    private GetK8sClustersClusterConfigContext() {}
    public Map<String,String> context() {
        return this.context;
    }
    public String name() {
        return this.name;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetK8sClustersClusterConfigContext defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Map<String,String> context;
        private String name;
        public Builder() {}
        public Builder(GetK8sClustersClusterConfigContext defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.context = defaults.context;
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder context(Map<String,String> context) {
            if (context == null) {
              throw new MissingRequiredPropertyException("GetK8sClustersClusterConfigContext", "context");
            }
            this.context = context;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetK8sClustersClusterConfigContext", "name");
            }
            this.name = name;
            return this;
        }
        public GetK8sClustersClusterConfigContext build() {
            final var _resultValue = new GetK8sClustersClusterConfigContext();
            _resultValue.context = context;
            _resultValue.name = name;
            return _resultValue;
        }
    }
}
