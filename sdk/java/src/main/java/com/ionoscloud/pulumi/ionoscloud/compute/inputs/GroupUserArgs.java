// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.compute.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GroupUserArgs extends com.pulumi.resources.ResourceArgs {

    public static final GroupUserArgs Empty = new GroupUserArgs();

    @Import(name="administrator")
    private @Nullable Output<Boolean> administrator;

    public Optional<Output<Boolean>> administrator() {
        return Optional.ofNullable(this.administrator);
    }

    @Import(name="email")
    private @Nullable Output<String> email;

    public Optional<Output<String>> email() {
        return Optional.ofNullable(this.email);
    }

    @Import(name="firstName")
    private @Nullable Output<String> firstName;

    public Optional<Output<String>> firstName() {
        return Optional.ofNullable(this.firstName);
    }

    @Import(name="forceSecAuth")
    private @Nullable Output<Boolean> forceSecAuth;

    public Optional<Output<Boolean>> forceSecAuth() {
        return Optional.ofNullable(this.forceSecAuth);
    }

    @Import(name="id")
    private @Nullable Output<String> id;

    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    @Import(name="lastName")
    private @Nullable Output<String> lastName;

    public Optional<Output<String>> lastName() {
        return Optional.ofNullable(this.lastName);
    }

    @Import(name="password")
    private @Nullable Output<String> password;

    public Optional<Output<String>> password() {
        return Optional.ofNullable(this.password);
    }

    private GroupUserArgs() {}

    private GroupUserArgs(GroupUserArgs $) {
        this.administrator = $.administrator;
        this.email = $.email;
        this.firstName = $.firstName;
        this.forceSecAuth = $.forceSecAuth;
        this.id = $.id;
        this.lastName = $.lastName;
        this.password = $.password;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GroupUserArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GroupUserArgs $;

        public Builder() {
            $ = new GroupUserArgs();
        }

        public Builder(GroupUserArgs defaults) {
            $ = new GroupUserArgs(Objects.requireNonNull(defaults));
        }

        public Builder administrator(@Nullable Output<Boolean> administrator) {
            $.administrator = administrator;
            return this;
        }

        public Builder administrator(Boolean administrator) {
            return administrator(Output.of(administrator));
        }

        public Builder email(@Nullable Output<String> email) {
            $.email = email;
            return this;
        }

        public Builder email(String email) {
            return email(Output.of(email));
        }

        public Builder firstName(@Nullable Output<String> firstName) {
            $.firstName = firstName;
            return this;
        }

        public Builder firstName(String firstName) {
            return firstName(Output.of(firstName));
        }

        public Builder forceSecAuth(@Nullable Output<Boolean> forceSecAuth) {
            $.forceSecAuth = forceSecAuth;
            return this;
        }

        public Builder forceSecAuth(Boolean forceSecAuth) {
            return forceSecAuth(Output.of(forceSecAuth));
        }

        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        public Builder id(String id) {
            return id(Output.of(id));
        }

        public Builder lastName(@Nullable Output<String> lastName) {
            $.lastName = lastName;
            return this;
        }

        public Builder lastName(String lastName) {
            return lastName(Output.of(lastName));
        }

        public Builder password(@Nullable Output<String> password) {
            $.password = password;
            return this;
        }

        public Builder password(String password) {
            return password(Output.of(password));
        }

        public GroupUserArgs build() {
            return $;
        }
    }

}
