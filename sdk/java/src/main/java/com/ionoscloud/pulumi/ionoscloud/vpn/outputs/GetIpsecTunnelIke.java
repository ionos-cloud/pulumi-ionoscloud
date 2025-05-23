// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.vpn.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetIpsecTunnelIke {
    /**
     * @return The Diffie-Hellman Group to use for IPSec Encryption.
     * 
     */
    private String diffieHellmanGroup;
    /**
     * @return The encryption algorithm to use for IPSec Encryption.
     * 
     */
    private String encryptionAlgorithm;
    /**
     * @return The integrity algorithm to use for IPSec Encryption.
     * 
     */
    private String integrityAlgorithm;
    /**
     * @return The phase lifetime in seconds.
     * 
     */
    private Integer lifetime;

    private GetIpsecTunnelIke() {}
    /**
     * @return The Diffie-Hellman Group to use for IPSec Encryption.
     * 
     */
    public String diffieHellmanGroup() {
        return this.diffieHellmanGroup;
    }
    /**
     * @return The encryption algorithm to use for IPSec Encryption.
     * 
     */
    public String encryptionAlgorithm() {
        return this.encryptionAlgorithm;
    }
    /**
     * @return The integrity algorithm to use for IPSec Encryption.
     * 
     */
    public String integrityAlgorithm() {
        return this.integrityAlgorithm;
    }
    /**
     * @return The phase lifetime in seconds.
     * 
     */
    public Integer lifetime() {
        return this.lifetime;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetIpsecTunnelIke defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String diffieHellmanGroup;
        private String encryptionAlgorithm;
        private String integrityAlgorithm;
        private Integer lifetime;
        public Builder() {}
        public Builder(GetIpsecTunnelIke defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.diffieHellmanGroup = defaults.diffieHellmanGroup;
    	      this.encryptionAlgorithm = defaults.encryptionAlgorithm;
    	      this.integrityAlgorithm = defaults.integrityAlgorithm;
    	      this.lifetime = defaults.lifetime;
        }

        @CustomType.Setter
        public Builder diffieHellmanGroup(String diffieHellmanGroup) {
            if (diffieHellmanGroup == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelIke", "diffieHellmanGroup");
            }
            this.diffieHellmanGroup = diffieHellmanGroup;
            return this;
        }
        @CustomType.Setter
        public Builder encryptionAlgorithm(String encryptionAlgorithm) {
            if (encryptionAlgorithm == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelIke", "encryptionAlgorithm");
            }
            this.encryptionAlgorithm = encryptionAlgorithm;
            return this;
        }
        @CustomType.Setter
        public Builder integrityAlgorithm(String integrityAlgorithm) {
            if (integrityAlgorithm == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelIke", "integrityAlgorithm");
            }
            this.integrityAlgorithm = integrityAlgorithm;
            return this;
        }
        @CustomType.Setter
        public Builder lifetime(Integer lifetime) {
            if (lifetime == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelIke", "lifetime");
            }
            this.lifetime = lifetime;
            return this;
        }
        public GetIpsecTunnelIke build() {
            final var _resultValue = new GetIpsecTunnelIke();
            _resultValue.diffieHellmanGroup = diffieHellmanGroup;
            _resultValue.encryptionAlgorithm = encryptionAlgorithm;
            _resultValue.integrityAlgorithm = integrityAlgorithm;
            _resultValue.lifetime = lifetime;
            return _resultValue;
        }
    }
}
