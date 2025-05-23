// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.inputs;

import com.ionoscloud.pulumi.ionoscloud.dbaas.inputs.InMemoryDBReplicaSetCredentialsHashedPasswordArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class InMemoryDBReplicaSetCredentialsArgs extends com.pulumi.resources.ResourceArgs {

    public static final InMemoryDBReplicaSetCredentialsArgs Empty = new InMemoryDBReplicaSetCredentialsArgs();

    /**
     * [object] The hashed password for a InMemoryDB user.
     * 
     */
    @Import(name="hashedPassword")
    private @Nullable Output<InMemoryDBReplicaSetCredentialsHashedPasswordArgs> hashedPassword;

    /**
     * @return [object] The hashed password for a InMemoryDB user.
     * 
     */
    public Optional<Output<InMemoryDBReplicaSetCredentialsHashedPasswordArgs>> hashedPassword() {
        return Optional.ofNullable(this.hashedPassword);
    }

    /**
     * [string] The password for a InMemoryDB user, this is a field that is marked as `Sensitive`.
     * 
     */
    @Import(name="plainTextPassword")
    private @Nullable Output<String> plainTextPassword;

    /**
     * @return [string] The password for a InMemoryDB user, this is a field that is marked as `Sensitive`.
     * 
     */
    public Optional<Output<String>> plainTextPassword() {
        return Optional.ofNullable(this.plainTextPassword);
    }

    /**
     * [string] The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
     * 
     */
    @Import(name="username", required=true)
    private Output<String> username;

    /**
     * @return [string] The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
     * 
     */
    public Output<String> username() {
        return this.username;
    }

    private InMemoryDBReplicaSetCredentialsArgs() {}

    private InMemoryDBReplicaSetCredentialsArgs(InMemoryDBReplicaSetCredentialsArgs $) {
        this.hashedPassword = $.hashedPassword;
        this.plainTextPassword = $.plainTextPassword;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InMemoryDBReplicaSetCredentialsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InMemoryDBReplicaSetCredentialsArgs $;

        public Builder() {
            $ = new InMemoryDBReplicaSetCredentialsArgs();
        }

        public Builder(InMemoryDBReplicaSetCredentialsArgs defaults) {
            $ = new InMemoryDBReplicaSetCredentialsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param hashedPassword [object] The hashed password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder hashedPassword(@Nullable Output<InMemoryDBReplicaSetCredentialsHashedPasswordArgs> hashedPassword) {
            $.hashedPassword = hashedPassword;
            return this;
        }

        /**
         * @param hashedPassword [object] The hashed password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder hashedPassword(InMemoryDBReplicaSetCredentialsHashedPasswordArgs hashedPassword) {
            return hashedPassword(Output.of(hashedPassword));
        }

        /**
         * @param plainTextPassword [string] The password for a InMemoryDB user, this is a field that is marked as `Sensitive`.
         * 
         * @return builder
         * 
         */
        public Builder plainTextPassword(@Nullable Output<String> plainTextPassword) {
            $.plainTextPassword = plainTextPassword;
            return this;
        }

        /**
         * @param plainTextPassword [string] The password for a InMemoryDB user, this is a field that is marked as `Sensitive`.
         * 
         * @return builder
         * 
         */
        public Builder plainTextPassword(String plainTextPassword) {
            return plainTextPassword(Output.of(plainTextPassword));
        }

        /**
         * @param username [string] The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
         * 
         * @return builder
         * 
         */
        public Builder username(Output<String> username) {
            $.username = username;
            return this;
        }

        /**
         * @param username [string] The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
         * 
         * @return builder
         * 
         */
        public Builder username(String username) {
            return username(Output.of(username));
        }

        public InMemoryDBReplicaSetCredentialsArgs build() {
            if ($.username == null) {
                throw new MissingRequiredPropertyException("InMemoryDBReplicaSetCredentialsArgs", "username");
            }
            return $;
        }
    }

}
