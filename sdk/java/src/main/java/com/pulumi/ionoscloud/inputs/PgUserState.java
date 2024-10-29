// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class PgUserState extends com.pulumi.resources.ResourceArgs {

    public static final PgUserState Empty = new PgUserState();

    @Import(name="clusterId")
    private @Nullable Output<String> clusterId;

    public Optional<Output<String>> clusterId() {
        return Optional.ofNullable(this.clusterId);
    }

    /**
     * Describes whether this user is a system user or not. A system user cannot be updated or deleted.
     * 
     */
    @Import(name="isSystemUser")
    private @Nullable Output<Boolean> isSystemUser;

    /**
     * @return Describes whether this user is a system user or not. A system user cannot be updated or deleted.
     * 
     */
    public Optional<Output<Boolean>> isSystemUser() {
        return Optional.ofNullable(this.isSystemUser);
    }

    @Import(name="password")
    private @Nullable Output<String> password;

    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    @Import(name="username")
    private @Nullable Output<String> username;

    public Optional<Output<String>> username() {
        return Optional.ofNullable(this.username);
    }

    private PgUserState() {}

    private PgUserState(PgUserState $) {
        this.clusterId = $.clusterId;
        this.isSystemUser = $.isSystemUser;
        this.password = $.password;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(PgUserState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private PgUserState $;

        public Builder() {
            $ = new PgUserState();
        }

        public Builder(PgUserState defaults) {
            $ = new PgUserState(Objects.requireNonNull(defaults));
        }

        public Builder clusterId(@Nullable Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param isSystemUser Describes whether this user is a system user or not. A system user cannot be updated or deleted.
         * 
         * @return builder
         * 
         */
        public Builder isSystemUser(@Nullable Output<Boolean> isSystemUser) {
            $.isSystemUser = isSystemUser;
            return this;
        }

        /**
         * @param isSystemUser Describes whether this user is a system user or not. A system user cannot be updated or deleted.
         * 
         * @return builder
         * 
         */
        public Builder isSystemUser(Boolean isSystemUser) {
            return isSystemUser(Output.of(isSystemUser));
        }

        public Builder password(@Nullable Output<String> password) {
            $.password = password;
            return this;
        }

        public Builder password(String password) {
            return password(Output.of(password));
        }

        public Builder username(@Nullable Output<String> username) {
            $.username = username;
            return this;
        }

        public Builder username(String username) {
            return username(Output.of(username));
        }

        public PgUserState build() {
            return $;
        }
    }

}
