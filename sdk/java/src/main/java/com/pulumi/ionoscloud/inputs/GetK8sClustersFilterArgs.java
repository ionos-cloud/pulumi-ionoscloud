// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetK8sClustersFilterArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetK8sClustersFilterArgs Empty = new GetK8sClustersFilterArgs();

    @Import(name="name", required=true)
    private Output<String> name;

    public Output<String> name() {
        return this.name;
    }

    @Import(name="value", required=true)
    private Output<String> value;

    public Output<String> value() {
        return this.value;
    }

    private GetK8sClustersFilterArgs() {}

    private GetK8sClustersFilterArgs(GetK8sClustersFilterArgs $) {
        this.name = $.name;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetK8sClustersFilterArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetK8sClustersFilterArgs $;

        public Builder() {
            $ = new GetK8sClustersFilterArgs();
        }

        public Builder(GetK8sClustersFilterArgs defaults) {
            $ = new GetK8sClustersFilterArgs(Objects.requireNonNull(defaults));
        }

        public Builder name(Output<String> name) {
            $.name = name;
            return this;
        }

        public Builder name(String name) {
            return name(Output.of(name));
        }

        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        public Builder value(String value) {
            return value(Output.of(value));
        }

        public GetK8sClustersFilterArgs build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetK8sClustersFilterArgs", "name");
            }
            if ($.value == null) {
                throw new MissingRequiredPropertyException("GetK8sClustersFilterArgs", "value");
            }
            return $;
        }
    }

}
