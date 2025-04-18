// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.k8s.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetClusterS3Bucket {
    /**
     * @return Name of an existing cluster that you want to search for.
     * 
     */
    private String name;

    private GetClusterS3Bucket() {}
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

    public static Builder builder(GetClusterS3Bucket defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String name;
        public Builder() {}
        public Builder(GetClusterS3Bucket defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetClusterS3Bucket", "name");
            }
            this.name = name;
            return this;
        }
        public GetClusterS3Bucket build() {
            final var _resultValue = new GetClusterS3Bucket();
            _resultValue.name = name;
            return _resultValue;
        }
    }
}
