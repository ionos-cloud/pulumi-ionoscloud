// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetAutoCertificateProviderPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetAutoCertificateProviderPlainArgs Empty = new GetAutoCertificateProviderPlainArgs();

    @Import(name="id")
    private @Nullable String id;

    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="location", required=true)
    private String location;

    public String location() {
        return this.location;
    }

    @Import(name="name")
    private @Nullable String name;

    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetAutoCertificateProviderPlainArgs() {}

    private GetAutoCertificateProviderPlainArgs(GetAutoCertificateProviderPlainArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetAutoCertificateProviderPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetAutoCertificateProviderPlainArgs $;

        public Builder() {
            $ = new GetAutoCertificateProviderPlainArgs();
        }

        public Builder(GetAutoCertificateProviderPlainArgs defaults) {
            $ = new GetAutoCertificateProviderPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        public Builder location(String location) {
            $.location = location;
            return this;
        }

        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetAutoCertificateProviderPlainArgs build() {
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetAutoCertificateProviderPlainArgs", "location");
            }
            return $;
        }
    }

}
