// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetPrivateCrossconnectPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetPrivateCrossconnectPlainArgs Empty = new GetPrivateCrossconnectPlainArgs();

    /**
     * Description of cross connect
     * 
     */
    @Import(name="description")
    private @Nullable String description;

    /**
     * @return Description of cross connect
     * 
     */
    public Optional<String> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * ID of the cross connect you want to search for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of the cross connect you want to search for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Name of an existing cross connect that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing cross connect that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetPrivateCrossconnectPlainArgs() {}

    private GetPrivateCrossconnectPlainArgs(GetPrivateCrossconnectPlainArgs $) {
        this.description = $.description;
        this.id = $.id;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetPrivateCrossconnectPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetPrivateCrossconnectPlainArgs $;

        public Builder() {
            $ = new GetPrivateCrossconnectPlainArgs();
        }

        public Builder(GetPrivateCrossconnectPlainArgs defaults) {
            $ = new GetPrivateCrossconnectPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param description Description of cross connect
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable String description) {
            $.description = description;
            return this;
        }

        /**
         * @param id ID of the cross connect you want to search for.
         * 
         * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param name Name of an existing cross connect that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetPrivateCrossconnectPlainArgs build() {
            return $;
        }
    }

}
