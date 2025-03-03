// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetMongoClusterPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetMongoClusterPlainArgs Empty = new GetMongoClusterPlainArgs();

    @Import(name="displayName")
    private @Nullable String displayName;

    public Optional<String> displayName() {
        return Optional.ofNullable(this.displayName);
    }

    @Import(name="id")
    private @Nullable String id;

    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    private GetMongoClusterPlainArgs() {}

    private GetMongoClusterPlainArgs(GetMongoClusterPlainArgs $) {
        this.displayName = $.displayName;
        this.id = $.id;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetMongoClusterPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetMongoClusterPlainArgs $;

        public Builder() {
            $ = new GetMongoClusterPlainArgs();
        }

        public Builder(GetMongoClusterPlainArgs defaults) {
            $ = new GetMongoClusterPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder displayName(@Nullable String displayName) {
            $.displayName = displayName;
            return this;
        }

        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        public GetMongoClusterPlainArgs build() {
            return $;
        }
    }

}
