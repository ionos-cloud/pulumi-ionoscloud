// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class VCPUServerLabelArgs extends com.pulumi.resources.ResourceArgs {

    public static final VCPUServerLabelArgs Empty = new VCPUServerLabelArgs();

    @Import(name="key", required=true)
    private Output<String> key;

    public Output<String> key() {
        return this.key;
    }

    @Import(name="value", required=true)
    private Output<String> value;

    public Output<String> value() {
        return this.value;
    }

    private VCPUServerLabelArgs() {}

    private VCPUServerLabelArgs(VCPUServerLabelArgs $) {
        this.key = $.key;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VCPUServerLabelArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VCPUServerLabelArgs $;

        public Builder() {
            $ = new VCPUServerLabelArgs();
        }

        public Builder(VCPUServerLabelArgs defaults) {
            $ = new VCPUServerLabelArgs(Objects.requireNonNull(defaults));
        }

        public Builder key(Output<String> key) {
            $.key = key;
            return this;
        }

        public Builder key(String key) {
            return key(Output.of(key));
        }

        public Builder value(Output<String> value) {
            $.value = value;
            return this;
        }

        public Builder value(String value) {
            return value(Output.of(value));
        }

        public VCPUServerLabelArgs build() {
            if ($.key == null) {
                throw new MissingRequiredPropertyException("VCPUServerLabelArgs", "key");
            }
            if ($.value == null) {
                throw new MissingRequiredPropertyException("VCPUServerLabelArgs", "value");
            }
            return $;
        }
    }

}
