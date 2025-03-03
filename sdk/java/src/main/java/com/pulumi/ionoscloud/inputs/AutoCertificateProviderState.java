// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.AutoCertificateProviderExternalAccountBindingArgs;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class AutoCertificateProviderState extends com.pulumi.resources.ResourceArgs {

    public static final AutoCertificateProviderState Empty = new AutoCertificateProviderState();

    /**
     * The email address of the certificate requester
     * 
     */
    @Import(name="email")
    private @Nullable Output<String> email;

    /**
     * @return The email address of the certificate requester
     * 
     */
    public Optional<Output<String>> email() {
        return Optional.ofNullable(this.email);
    }

    @Import(name="externalAccountBinding")
    private @Nullable Output<AutoCertificateProviderExternalAccountBindingArgs> externalAccountBinding;

    public Optional<Output<AutoCertificateProviderExternalAccountBindingArgs>> externalAccountBinding() {
        return Optional.ofNullable(this.externalAccountBinding);
    }

    /**
     * The location of the certificate provider
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return The location of the certificate provider
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * The name of the certificate provider
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return The name of the certificate provider
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The URL of the certificate provider
     * 
     */
    @Import(name="server")
    private @Nullable Output<String> server;

    /**
     * @return The URL of the certificate provider
     * 
     */
    public Optional<Output<String>> server() {
        return Optional.ofNullable(this.server);
    }

    private AutoCertificateProviderState() {}

    private AutoCertificateProviderState(AutoCertificateProviderState $) {
        this.email = $.email;
        this.externalAccountBinding = $.externalAccountBinding;
        this.location = $.location;
        this.name = $.name;
        this.server = $.server;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(AutoCertificateProviderState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private AutoCertificateProviderState $;

        public Builder() {
            $ = new AutoCertificateProviderState();
        }

        public Builder(AutoCertificateProviderState defaults) {
            $ = new AutoCertificateProviderState(Objects.requireNonNull(defaults));
        }

        /**
         * @param email The email address of the certificate requester
         * 
         * @return builder
         * 
         */
        public Builder email(@Nullable Output<String> email) {
            $.email = email;
            return this;
        }

        /**
         * @param email The email address of the certificate requester
         * 
         * @return builder
         * 
         */
        public Builder email(String email) {
            return email(Output.of(email));
        }

        public Builder externalAccountBinding(@Nullable Output<AutoCertificateProviderExternalAccountBindingArgs> externalAccountBinding) {
            $.externalAccountBinding = externalAccountBinding;
            return this;
        }

        public Builder externalAccountBinding(AutoCertificateProviderExternalAccountBindingArgs externalAccountBinding) {
            return externalAccountBinding(Output.of(externalAccountBinding));
        }

        /**
         * @param location The location of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name The name of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name The name of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param server The URL of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder server(@Nullable Output<String> server) {
            $.server = server;
            return this;
        }

        /**
         * @param server The URL of the certificate provider
         * 
         * @return builder
         * 
         */
        public Builder server(String server) {
            return server(Output.of(server));
        }

        public AutoCertificateProviderState build() {
            return $;
        }
    }

}
