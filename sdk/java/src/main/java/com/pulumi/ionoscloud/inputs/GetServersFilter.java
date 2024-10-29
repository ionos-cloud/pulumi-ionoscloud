// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetServersFilter extends com.pulumi.resources.InvokeArgs {

    public static final GetServersFilter Empty = new GetServersFilter();

    @Import(name="name", required=true)
    private String name;

    public String name() {
        return this.name;
    }

    @Import(name="value", required=true)
    private String value;

    public String value() {
        return this.value;
    }

    private GetServersFilter() {}

    private GetServersFilter(GetServersFilter $) {
        this.name = $.name;
        this.value = $.value;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetServersFilter defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetServersFilter $;

        public Builder() {
            $ = new GetServersFilter();
        }

        public Builder(GetServersFilter defaults) {
            $ = new GetServersFilter(Objects.requireNonNull(defaults));
        }

        public Builder name(String name) {
            $.name = name;
            return this;
        }

        public Builder value(String value) {
            $.value = value;
            return this;
        }

        public GetServersFilter build() {
            if ($.name == null) {
                throw new MissingRequiredPropertyException("GetServersFilter", "name");
            }
            if ($.value == null) {
                throw new MissingRequiredPropertyException("GetServersFilter", "value");
            }
            return $;
        }
    }

}
