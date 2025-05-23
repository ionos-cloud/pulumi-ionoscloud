// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class InMemoryDBReplicaSetCredentialsHashedPasswordArgs extends com.pulumi.resources.ResourceArgs {

    public static final InMemoryDBReplicaSetCredentialsHashedPasswordArgs Empty = new InMemoryDBReplicaSetCredentialsHashedPasswordArgs();

    /**
     * [string] The value can be only: &#34;SHA-256&#34;.
     * 
     */
    @Import(name="algorithm", required=true)
    private Output<String> algorithm;

    /**
     * @return [string] The value can be only: &#34;SHA-256&#34;.
     * 
     */
    public Output<String> algorithm() {
        return this.algorithm;
    }

    /**
     * [string] The hashed password.
     * 
     */
    @Import(name="hash", required=true)
    private Output<String> hash;

    /**
     * @return [string] The hashed password.
     * 
     */
    public Output<String> hash() {
        return this.hash;
    }

    private InMemoryDBReplicaSetCredentialsHashedPasswordArgs() {}

    private InMemoryDBReplicaSetCredentialsHashedPasswordArgs(InMemoryDBReplicaSetCredentialsHashedPasswordArgs $) {
        this.algorithm = $.algorithm;
        this.hash = $.hash;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(InMemoryDBReplicaSetCredentialsHashedPasswordArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private InMemoryDBReplicaSetCredentialsHashedPasswordArgs $;

        public Builder() {
            $ = new InMemoryDBReplicaSetCredentialsHashedPasswordArgs();
        }

        public Builder(InMemoryDBReplicaSetCredentialsHashedPasswordArgs defaults) {
            $ = new InMemoryDBReplicaSetCredentialsHashedPasswordArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param algorithm [string] The value can be only: &#34;SHA-256&#34;.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(Output<String> algorithm) {
            $.algorithm = algorithm;
            return this;
        }

        /**
         * @param algorithm [string] The value can be only: &#34;SHA-256&#34;.
         * 
         * @return builder
         * 
         */
        public Builder algorithm(String algorithm) {
            return algorithm(Output.of(algorithm));
        }

        /**
         * @param hash [string] The hashed password.
         * 
         * @return builder
         * 
         */
        public Builder hash(Output<String> hash) {
            $.hash = hash;
            return this;
        }

        /**
         * @param hash [string] The hashed password.
         * 
         * @return builder
         * 
         */
        public Builder hash(String hash) {
            return hash(Output.of(hash));
        }

        public InMemoryDBReplicaSetCredentialsHashedPasswordArgs build() {
            if ($.algorithm == null) {
                throw new MissingRequiredPropertyException("InMemoryDBReplicaSetCredentialsHashedPasswordArgs", "algorithm");
            }
            if ($.hash == null) {
                throw new MissingRequiredPropertyException("InMemoryDBReplicaSetCredentialsHashedPasswordArgs", "hash");
            }
            return $;
        }
    }

}
