// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.InmemorydbReplicasetCredentialsHashedPasswordArgs;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class InmemorydbReplicasetCredentialsArgs extends com.pulumi.resources.ResourceArgs {

    public static final InmemorydbReplicasetCredentialsArgs Empty = new InmemorydbReplicasetCredentialsArgs();

    /**
     * The hashed password for a InMemoryDB user.
     * 
     */
    @Import(name="hashedPassword")
    private @Nullable Output<InmemorydbReplicasetCredentialsHashedPasswordArgs> hashedPassword;

    /**
     * @return The hashed password for a InMemoryDB user.
     * 
     */
    public Optional<Output<InmemorydbReplicasetCredentialsHashedPasswordArgs>> hashedPassword() {
        return Optional.ofNullable(this.hashedPassword);
    }

    /**
     * The password for a InMemoryDB user.
     * 
     */
    @Import(name="plainTextPassword")
    private @Nullable Output<String> plainTextPassword;

    /**
     * @return The password for a InMemoryDB user.
     * 
     */
    public Optional<Output<String>> plainTextPassword() {
        return Optional.ofNullable(this.plainTextPassword);
    }

    /**
     * The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
     * 
     */
    @Import(name="username", required=true)
    private Output<String> username;

    /**
     * @return The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
     * 
     */
    public Output<String> username() {
        return this.username;
    }

    private InmemorydbReplicasetCredentialsArgs() {}

    private InmemorydbReplicasetCredentialsArgs(InmemorydbReplicasetCredentialsArgs $) {
        this.hashedPassword = $.hashedPassword;
        this.plainTextPassword = $.plainTextPassword;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InmemorydbReplicasetCredentialsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InmemorydbReplicasetCredentialsArgs $;

        public Builder() {
            $ = new InmemorydbReplicasetCredentialsArgs();
        }

        public Builder(InmemorydbReplicasetCredentialsArgs defaults) {
            $ = new InmemorydbReplicasetCredentialsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param hashedPassword The hashed password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder hashedPassword(@Nullable Output<InmemorydbReplicasetCredentialsHashedPasswordArgs> hashedPassword) {
            $.hashedPassword = hashedPassword;
            return this;
        }

        /**
         * @param hashedPassword The hashed password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder hashedPassword(InmemorydbReplicasetCredentialsHashedPasswordArgs hashedPassword) {
            return hashedPassword(Output.of(hashedPassword));
        }

        /**
         * @param plainTextPassword The password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder plainTextPassword(@Nullable Output<String> plainTextPassword) {
            $.plainTextPassword = plainTextPassword;
            return this;
        }

        /**
         * @param plainTextPassword The password for a InMemoryDB user.
         * 
         * @return builder
         * 
         */
        public Builder plainTextPassword(String plainTextPassword) {
            return plainTextPassword(Output.of(plainTextPassword));
        }

        /**
         * @param username The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
         * 
         * @return builder
         * 
         */
        public Builder username(Output<String> username) {
            $.username = username;
            return this;
        }

        /**
         * @param username The username for the initial InMemoryDB user. Some system usernames are restricted (e.g. &#39;admin&#39;, &#39;standby&#39;).
         * 
         * @return builder
         * 
         */
        public Builder username(String username) {
            return username(Output.of(username));
        }

        public InmemorydbReplicasetCredentialsArgs build() {
            if ($.username == null) {
                throw new MissingRequiredPropertyException("InmemorydbReplicasetCredentialsArgs", "username");
            }
            return $;
        }
    }

}
