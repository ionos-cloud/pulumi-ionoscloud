// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetK8sClusterS3Bucket {
    /**
     * @return Name of an existing cluster that you want to search for.
     * 
     */
    private String name;

    private GetK8sClusterS3Bucket() {}
    /**
     * @return Name of an existing cluster that you want to search for.
     * 
     */
    public String name() {
        return this.name;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetK8sClusterS3Bucket defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String name;
        public Builder() {}
        public Builder(GetK8sClusterS3Bucket defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetK8sClusterS3Bucket", "name");
            }
            this.name = name;
            return this;
        }
        public GetK8sClusterS3Bucket build() {
            final var _resultValue = new GetK8sClusterS3Bucket();
            _resultValue.name = name;
            return _resultValue;
        }
    }
}
