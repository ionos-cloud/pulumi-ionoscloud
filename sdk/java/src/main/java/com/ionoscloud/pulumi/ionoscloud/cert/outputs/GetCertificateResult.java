// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.cert.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetCertificateResult {
    /**
     * @return Certificate body.
     * 
     */
    private String certificate;
    /**
     * @return Certificate chain.
     * 
     */
    private String certificateChain;
    /**
     * @return The id of the certificate.
     * 
     */
    private String id;
    /**
     * @return The name of the certificate.
     * 
     */
    private String name;

    private GetCertificateResult() {}
    /**
     * @return Certificate body.
     * 
     */
    public String certificate() {
        return this.certificate;
    }
    /**
     * @return Certificate chain.
     * 
     */
    public String certificateChain() {
        return this.certificateChain;
    }
    /**
     * @return The id of the certificate.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The name of the certificate.
     * 
     */
    public String name() {
        return this.name;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCertificateResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String certificate;
        private String certificateChain;
        private String id;
        private String name;
        public Builder() {}
        public Builder(GetCertificateResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.certificate = defaults.certificate;
    	      this.certificateChain = defaults.certificateChain;
    	      this.id = defaults.id;
    	      this.name = defaults.name;
        }

        @CustomType.Setter
        public Builder certificate(String certificate) {
            if (certificate == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "certificate");
            }
            this.certificate = certificate;
            return this;
        }
        @CustomType.Setter
        public Builder certificateChain(String certificateChain) {
            if (certificateChain == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "certificateChain");
            }
            this.certificateChain = certificateChain;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetCertificateResult", "name");
            }
            this.name = name;
            return this;
        }
        public GetCertificateResult build() {
            final var _resultValue = new GetCertificateResult();
            _resultValue.certificate = certificate;
            _resultValue.certificateChain = certificateChain;
            _resultValue.id = id;
            _resultValue.name = name;
            return _resultValue;
        }
    }
}
