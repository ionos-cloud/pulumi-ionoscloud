// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cert.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetAutoCertificateArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetAutoCertificateArgs Empty = new GetAutoCertificateArgs();

    /**
     * [string] ID of the auto-certificate you want to search for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return [string] ID of the auto-certificate you want to search for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * [string] The location of the auto-certificate.
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return [string] The location of the auto-certificate.
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * [string] Name of an existing auto-certificate that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] Name of an existing auto-certificate that you want to search for.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    private GetAutoCertificateArgs() {}

    private GetAutoCertificateArgs(GetAutoCertificateArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetAutoCertificateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetAutoCertificateArgs $;

        public Builder() {
            $ = new GetAutoCertificateArgs();
        }

        public Builder(GetAutoCertificateArgs defaults) {
            $ = new GetAutoCertificateArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id [string] ID of the auto-certificate you want to search for.
         * 
         * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id [string] ID of the auto-certificate you want to search for.
         * 
         * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location [string] The location of the auto-certificate.
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location [string] The location of the auto-certificate.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] Name of an existing auto-certificate that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] Name of an existing auto-certificate that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        public GetAutoCertificateArgs build() {
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetAutoCertificateArgs", "location");
            }
            return $;
        }
    }

}
