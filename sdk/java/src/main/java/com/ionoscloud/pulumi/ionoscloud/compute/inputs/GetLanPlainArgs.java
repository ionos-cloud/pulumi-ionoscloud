// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetLanPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetLanPlainArgs Empty = new GetLanPlainArgs();

    /**
     * Datacenter&#39;s UUID.
     * 
     */
    @Import(name="datacenterId", required=true)
    private String datacenterId;

    /**
     * @return Datacenter&#39;s UUID.
     * 
     */
    public String datacenterId() {
        return this.datacenterId;
    }

    /**
     * ID of the lan you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of the lan you want to search for.
     * 
     * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing lan that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing lan that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetLanPlainArgs() {}

    private GetLanPlainArgs(GetLanPlainArgs $) {
        this.datacenterId = $.datacenterId;
        this.id = $.id;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetLanPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetLanPlainArgs $;

        public Builder() {
            $ = new GetLanPlainArgs();
        }

        public Builder(GetLanPlainArgs defaults) {
            $ = new GetLanPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId Datacenter&#39;s UUID.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param id ID of the lan you want to search for.
         * 
         * `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param name Name of an existing lan that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetLanPlainArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("GetLanPlainArgs", "datacenterId");
            }
            return $;
        }
    }

}
