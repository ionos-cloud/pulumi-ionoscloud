// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetSnapshotPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetSnapshotPlainArgs Empty = new GetSnapshotPlainArgs();

    /**
     * UUID of an existing snapshot that you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return UUID of an existing snapshot that you want to search for.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * Existing snapshot&#39;s location.
     * 
     */
    @Import(name="location")
    private @Nullable String location;

    /**
     * @return Existing snapshot&#39;s location.
     * 
     */
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * Name of an existing snapshot that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing snapshot that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The size of the snapshot to look for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
     * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
     * When this happens, please refine your search string so that it is specific enough to return only one result.
     * 
     */
    @Import(name="size")
    private @Nullable Integer size;

    /**
     * @return The size of the snapshot to look for.
     * 
     * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
     * Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
     * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
     * When this happens, please refine your search string so that it is specific enough to return only one result.
     * 
     */
    public Optional<Integer> size() {
        return Optional.ofNullable(this.size);
    }

    private GetSnapshotPlainArgs() {}

    private GetSnapshotPlainArgs(GetSnapshotPlainArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
        this.size = $.size;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetSnapshotPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetSnapshotPlainArgs $;

        public Builder() {
            $ = new GetSnapshotPlainArgs();
        }

        public Builder(GetSnapshotPlainArgs defaults) {
            $ = new GetSnapshotPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id UUID of an existing snapshot that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param location Existing snapshot&#39;s location.
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable String location) {
            $.location = location;
            return this;
        }

        /**
         * @param name Name of an existing snapshot that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        /**
         * @param size The size of the snapshot to look for.
         * 
         * Either `name` or `id` must be provided. If none, or both are provided, the datasource will return an error.
         * Additionally, you can add `location` and `size` along with the `name` argument for a more refined search.
         * If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
         * When this happens, please refine your search string so that it is specific enough to return only one result.
         * 
         * @return builder
         * 
         */
        public Builder size(@Nullable Integer size) {
            $.size = size;
            return this;
        }

        public GetSnapshotPlainArgs build() {
            return $;
        }
    }

}
