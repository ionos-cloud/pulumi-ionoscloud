// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cert;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class CertificateArgs extends com.pulumi.resources.ResourceArgs {

    public static final CertificateArgs Empty = new CertificateArgs();

    /**
     * [string] The certificate body. Pem encoded. Immutable.
     * 
     */
    @Import(name="certificate", required=true)
    private Output<String> certificate;

    /**
     * @return [string] The certificate body. Pem encoded. Immutable.
     * 
     */
    public Output<String> certificate() {
        return this.certificate;
    }

    /**
     * [string] The certificate chain. Pem encoded. Immutable.
     * 
     */
    @Import(name="certificateChain")
    private @Nullable Output<String> certificateChain;

    /**
     * @return [string] The certificate chain. Pem encoded. Immutable.
     * 
     */
    public Optional<Output<String>> certificateChain() {
        return Optional.ofNullable(this.certificateChain);
    }

    /**
     * [string] The certificate name
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The certificate name
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [string] The certificate private key. Immutable. Sensitive.
     * 
     */
    @Import(name="privateKey", required=true)
    private Output<String> privateKey;

    /**
     * @return [string] The certificate private key. Immutable. Sensitive.
     * 
     */
    public Output<String> privateKey() {
        return this.privateKey;
    }

    private CertificateArgs() {}

    private CertificateArgs(CertificateArgs $) {
        this.certificate = $.certificate;
        this.certificateChain = $.certificateChain;
        this.name = $.name;
        this.privateKey = $.privateKey;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(CertificateArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private CertificateArgs $;

        public Builder() {
            $ = new CertificateArgs();
        }

        public Builder(CertificateArgs defaults) {
            $ = new CertificateArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param certificate [string] The certificate body. Pem encoded. Immutable.
         * 
         * @return builder
         * 
         */
        public Builder certificate(Output<String> certificate) {
            $.certificate = certificate;
            return this;
        }

        /**
         * @param certificate [string] The certificate body. Pem encoded. Immutable.
         * 
         * @return builder
         * 
         */
        public Builder certificate(String certificate) {
            return certificate(Output.of(certificate));
        }

        /**
         * @param certificateChain [string] The certificate chain. Pem encoded. Immutable.
         * 
         * @return builder
         * 
         */
        public Builder certificateChain(@Nullable Output<String> certificateChain) {
            $.certificateChain = certificateChain;
            return this;
        }

        /**
         * @param certificateChain [string] The certificate chain. Pem encoded. Immutable.
         * 
         * @return builder
         * 
         */
        public Builder certificateChain(String certificateChain) {
            return certificateChain(Output.of(certificateChain));
        }

        /**
         * @param name [string] The certificate name
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The certificate name
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param privateKey [string] The certificate private key. Immutable. Sensitive.
         * 
         * @return builder
         * 
         */
        public Builder privateKey(Output<String> privateKey) {
            $.privateKey = privateKey;
            return this;
        }

        /**
         * @param privateKey [string] The certificate private key. Immutable. Sensitive.
         * 
         * @return builder
         * 
         */
        public Builder privateKey(String privateKey) {
            return privateKey(Output.of(privateKey));
        }

        public CertificateArgs build() {
            if ($.certificate == null) {
                throw new MissingRequiredPropertyException("CertificateArgs", "certificate");
            }
            if ($.privateKey == null) {
                throw new MissingRequiredPropertyException("CertificateArgs", "privateKey");
            }
            return $;
        }
    }

}
