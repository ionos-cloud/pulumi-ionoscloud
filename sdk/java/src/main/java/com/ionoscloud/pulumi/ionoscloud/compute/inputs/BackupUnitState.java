// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class BackupUnitState extends com.pulumi.resources.ResourceArgs {

    public static final BackupUnitState Empty = new BackupUnitState();

    /**
     * [string] The email address assigned to the backup unit
     * 
     */
    @Import(name="email")
    private @Nullable Output<String> email;

    /**
     * @return [string] The email address assigned to the backup unit
     * 
     */
    public Optional<Output<String>> email() {
        return Optional.ofNullable(this.email);
    }

    /**
     * The login associated with the backup unit. Derived from the contract number
     * 
     */
    @Import(name="login")
    private @Nullable Output<String> login;

    /**
     * @return The login associated with the backup unit. Derived from the contract number
     * 
     */
    public Optional<Output<String>> login() {
        return Optional.ofNullable(this.login);
    }

    /**
     * [string] The name of the Backup Unit. This argument is immutable.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the Backup Unit. This argument is immutable.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] The desired password for the Backup Unit
     * 
     */
    @Import(name="password")
    private @Nullable Output<String> password;

    /**
     * @return [string] The desired password for the Backup Unit
     * 
     */
    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    private BackupUnitState() {}

    private BackupUnitState(BackupUnitState $) {
        this.email = $.email;
        this.login = $.login;
        this.name = $.name;
        this.password = $.password;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(BackupUnitState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private BackupUnitState $;

        public Builder() {
            $ = new BackupUnitState();
        }

        public Builder(BackupUnitState defaults) {
            $ = new BackupUnitState(Objects.requireNonNull(defaults));
        }

        /**
         * @param email [string] The email address assigned to the backup unit
         * 
         * @return builder
         * 
         */
        public Builder email(@Nullable Output<String> email) {
            $.email = email;
            return this;
        }

        /**
         * @param email [string] The email address assigned to the backup unit
         * 
         * @return builder
         * 
         */
        public Builder email(String email) {
            return email(Output.of(email));
        }

        /**
         * @param login The login associated with the backup unit. Derived from the contract number
         * 
         * @return builder
         * 
         */
        public Builder login(@Nullable Output<String> login) {
            $.login = login;
            return this;
        }

        /**
         * @param login The login associated with the backup unit. Derived from the contract number
         * 
         * @return builder
         * 
         */
        public Builder login(String login) {
            return login(Output.of(login));
        }

        /**
         * @param name [string] The name of the Backup Unit. This argument is immutable.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the Backup Unit. This argument is immutable.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param password [string] The desired password for the Backup Unit
         * 
         * @return builder
         * 
         */
        public Builder password(@Nullable Output<String> password) {
            $.password = password;
            return this;
        }

        /**
         * @param password [string] The desired password for the Backup Unit
         * 
         * @return builder
         * 
         */
        public Builder password(String password) {
            return password(Output.of(password));
        }

        public BackupUnitState build() {
            return $;
        }
    }

}
