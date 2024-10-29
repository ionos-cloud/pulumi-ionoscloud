// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class ContainerRegistryTokenCredentialArgs extends com.pulumi.resources.ResourceArgs {

    public static final ContainerRegistryTokenCredentialArgs Empty = new ContainerRegistryTokenCredentialArgs();

    @Import(name="password", required=true)
    private Output<String> password;

    public Output<String> password() {
        return this.password;
    }

    @Import(name="username", required=true)
    private Output<String> username;

    public Output<String> username() {
        return this.username;
    }

    private ContainerRegistryTokenCredentialArgs() {}

    private ContainerRegistryTokenCredentialArgs(ContainerRegistryTokenCredentialArgs $) {
        this.password = $.password;
        this.username = $.username;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ContainerRegistryTokenCredentialArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ContainerRegistryTokenCredentialArgs $;

        public Builder() {
            $ = new ContainerRegistryTokenCredentialArgs();
        }

        public Builder(ContainerRegistryTokenCredentialArgs defaults) {
            $ = new ContainerRegistryTokenCredentialArgs(Objects.requireNonNull(defaults));
        }

        public Builder password(Output<String> password) {
            $.password = password;
            return this;
        }

        public Builder password(String password) {
            return password(Output.of(password));
        }

        public Builder username(Output<String> username) {
            $.username = username;
            return this;
        }

        public Builder username(String username) {
            return username(Output.of(username));
        }

        public ContainerRegistryTokenCredentialArgs build() {
            if ($.password == null) {
                throw new MissingRequiredPropertyException("ContainerRegistryTokenCredentialArgs", "password");
            }
            if ($.username == null) {
                throw new MissingRequiredPropertyException("ContainerRegistryTokenCredentialArgs", "username");
            }
            return $;
        }
    }

}
