// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Integer;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VpnIpsecTunnelEspArgs extends com.pulumi.resources.ResourceArgs {

    public static final VpnIpsecTunnelEspArgs Empty = new VpnIpsecTunnelEspArgs();

    /**
     * [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
     * values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
     * Default value: `16-MODP4096`.
     * 
     */
    @Import(name="diffieHellmanGroup")
    private @Nullable Output<String> diffieHellmanGroup;

    /**
     * @return [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
     * values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
     * Default value: `16-MODP4096`.
     * 
     */
    public Optional<Output<String>> diffieHellmanGroup() {
        return Optional.ofNullable(this.diffieHellmanGroup);
    }

    /**
     * [string] The encryption algorithm to use for IPSec Encryption. Possible
     * values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
     * `AES256-CCM-12`. Default value: `AES256`.
     * 
     */
    @Import(name="encryptionAlgorithm")
    private @Nullable Output<String> encryptionAlgorithm;

    /**
     * @return [string] The encryption algorithm to use for IPSec Encryption. Possible
     * values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
     * `AES256-CCM-12`. Default value: `AES256`.
     * 
     */
    public Optional<Output<String>> encryptionAlgorithm() {
        return Optional.ofNullable(this.encryptionAlgorithm);
    }

    /**
     * [string] The integrity algorithm to use for IPSec Encryption. Possible
     * values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
     * 
     */
    @Import(name="integrityAlgorithm")
    private @Nullable Output<String> integrityAlgorithm;

    /**
     * @return [string] The integrity algorithm to use for IPSec Encryption. Possible
     * values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
     * 
     */
    public Optional<Output<String>> integrityAlgorithm() {
        return Optional.ofNullable(this.integrityAlgorithm);
    }

    /**
     * [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
     * Default value: `86400`.
     * 
     */
    @Import(name="lifetime")
    private @Nullable Output<Integer> lifetime;

    /**
     * @return [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
     * Default value: `86400`.
     * 
     */
    public Optional<Output<Integer>> lifetime() {
        return Optional.ofNullable(this.lifetime);
    }

    private VpnIpsecTunnelEspArgs() {}

    private VpnIpsecTunnelEspArgs(VpnIpsecTunnelEspArgs $) {
        this.diffieHellmanGroup = $.diffieHellmanGroup;
        this.encryptionAlgorithm = $.encryptionAlgorithm;
        this.integrityAlgorithm = $.integrityAlgorithm;
        this.lifetime = $.lifetime;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VpnIpsecTunnelEspArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VpnIpsecTunnelEspArgs $;

        public Builder() {
            $ = new VpnIpsecTunnelEspArgs();
        }

        public Builder(VpnIpsecTunnelEspArgs defaults) {
            $ = new VpnIpsecTunnelEspArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param diffieHellmanGroup [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
         * values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
         * Default value: `16-MODP4096`.
         * 
         * @return builder
         * 
         */
        public Builder diffieHellmanGroup(@Nullable Output<String> diffieHellmanGroup) {
            $.diffieHellmanGroup = diffieHellmanGroup;
            return this;
        }

        /**
         * @param diffieHellmanGroup [string] The Diffie-Hellman Group to use for IPSec Encryption. Possible
         * values: `15-MODP3072`, `16-MODP4096`, `19-ECP256`, `20-ECP384`, `21-ECP521`, `28-ECP256BP`, `29-ECP384BP`, `30-ECP512BP`.
         * Default value: `16-MODP4096`.
         * 
         * @return builder
         * 
         */
        public Builder diffieHellmanGroup(String diffieHellmanGroup) {
            return diffieHellmanGroup(Output.of(diffieHellmanGroup));
        }

        /**
         * @param encryptionAlgorithm [string] The encryption algorithm to use for IPSec Encryption. Possible
         * values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
         * `AES256-CCM-12`. Default value: `AES256`.
         * 
         * @return builder
         * 
         */
        public Builder encryptionAlgorithm(@Nullable Output<String> encryptionAlgorithm) {
            $.encryptionAlgorithm = encryptionAlgorithm;
            return this;
        }

        /**
         * @param encryptionAlgorithm [string] The encryption algorithm to use for IPSec Encryption. Possible
         * values: `AES128`, `AES256`, `AES128-CTR`, `AES256-CTR`, `AES128-GCM-16`, `AES256-GCM-16`, `AES128-GCM-12`, `AES256-GCM-12`, `AES128-CCM-12`,
         * `AES256-CCM-12`. Default value: `AES256`.
         * 
         * @return builder
         * 
         */
        public Builder encryptionAlgorithm(String encryptionAlgorithm) {
            return encryptionAlgorithm(Output.of(encryptionAlgorithm));
        }

        /**
         * @param integrityAlgorithm [string] The integrity algorithm to use for IPSec Encryption. Possible
         * values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
         * 
         * @return builder
         * 
         */
        public Builder integrityAlgorithm(@Nullable Output<String> integrityAlgorithm) {
            $.integrityAlgorithm = integrityAlgorithm;
            return this;
        }

        /**
         * @param integrityAlgorithm [string] The integrity algorithm to use for IPSec Encryption. Possible
         * values: `SHA256`, `SHA384`, `SHA512`, `AES-XCBC`. Default value: `SHA256`.
         * 
         * @return builder
         * 
         */
        public Builder integrityAlgorithm(String integrityAlgorithm) {
            return integrityAlgorithm(Output.of(integrityAlgorithm));
        }

        /**
         * @param lifetime [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
         * Default value: `86400`.
         * 
         * @return builder
         * 
         */
        public Builder lifetime(@Nullable Output<Integer> lifetime) {
            $.lifetime = lifetime;
            return this;
        }

        /**
         * @param lifetime [string] The phase lifetime in seconds. Minimum value: `3600`. Maximum value: `86400`.
         * Default value: `86400`.
         * 
         * @return builder
         * 
         */
        public Builder lifetime(Integer lifetime) {
            return lifetime(Output.of(lifetime));
        }

        public VpnIpsecTunnelEspArgs build() {
            return $;
        }
    }

}
