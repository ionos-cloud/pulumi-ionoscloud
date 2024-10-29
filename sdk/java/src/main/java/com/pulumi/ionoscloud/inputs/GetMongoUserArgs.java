// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.GetMongoUserRoleArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetMongoUserArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetMongoUserArgs Empty = new GetMongoUserArgs();

    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    public Output<String> clusterId() {
        return this.clusterId;
    }

    @Import(name="database")
    private @Nullable Output<String> database;

    public Optional<Output<String>> database() {
        return Optional.ofNullable(this.database);
    }

    @Import(name="id")
    private @Nullable Output<String> id;

    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="roles")
    private @Nullable Output<List<GetMongoUserRoleArgs>> roles;

    public Optional<Output<List<GetMongoUserRoleArgs>>> roles() {
        return Optional.ofNullable(this.roles);
    }

    @Import(name="username", required=true)
    private Output<String> username;

    public Output<String> username() {
        return this.username;
    }

    private GetMongoUserArgs() {}

    private GetMongoUserArgs(GetMongoUserArgs $) {
        this.clusterId = $.clusterId;
        this.database = $.database;
        this.id = $.id;
        this.roles = $.roles;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetMongoUserArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetMongoUserArgs $;

        public Builder() {
            $ = new GetMongoUserArgs();
        }

        public Builder(GetMongoUserArgs defaults) {
            $ = new GetMongoUserArgs(Objects.requireNonNull(defaults));
        }

        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        public Builder database(@Nullable Output<String> database) {
            $.database = database;
            return this;
        }

        public Builder database(String database) {
            return database(Output.of(database));
        }

        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        public Builder id(String id) {
            return id(Output.of(id));
        }

        public Builder roles(@Nullable Output<List<GetMongoUserRoleArgs>> roles) {
            $.roles = roles;
            return this;
        }

        public Builder roles(List<GetMongoUserRoleArgs> roles) {
            return roles(Output.of(roles));
        }

        public Builder roles(GetMongoUserRoleArgs... roles) {
            return roles(List.of(roles));
        }

        public Builder username(Output<String> username) {
            $.username = username;
            return this;
        }

        public Builder username(String username) {
            return username(Output.of(username));
        }

        public GetMongoUserArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("GetMongoUserArgs", "clusterId");
            }
            if ($.username == null) {
                throw new MissingRequiredPropertyException("GetMongoUserArgs", "username");
            }
            return $;
        }
    }

}
