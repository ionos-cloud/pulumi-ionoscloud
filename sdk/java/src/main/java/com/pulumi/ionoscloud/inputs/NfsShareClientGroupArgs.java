// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.NfsShareClientGroupNfsArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NfsShareClientGroupArgs extends com.pulumi.resources.ResourceArgs {

    public static final NfsShareClientGroupArgs Empty = new NfsShareClientGroupArgs();

    /**
     * Optional description for the clients groups.
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return Optional description for the clients groups.
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
     * 
     */
    @Import(name="hosts", required=true)
    private Output<List<String>> hosts;

    /**
     * @return A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
     * 
     */
    public Output<List<String>> hosts() {
        return this.hosts;
    }

    /**
     * The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
     * 
     */
    @Import(name="ipNetworks", required=true)
    private Output<List<String>> ipNetworks;

    /**
     * @return The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
     * 
     */
    public Output<List<String>> ipNetworks() {
        return this.ipNetworks;
    }

    /**
     * NFS specific configurations. Each configuration includes:
     * 
     */
    @Import(name="nfs")
    private @Nullable Output<NfsShareClientGroupNfsArgs> nfs;

    /**
     * @return NFS specific configurations. Each configuration includes:
     * 
     */
    public Optional<Output<NfsShareClientGroupNfsArgs>> nfs() {
        return Optional.ofNullable(this.nfs);
    }

    private NfsShareClientGroupArgs() {}

    private NfsShareClientGroupArgs(NfsShareClientGroupArgs $) {
        this.description = $.description;
        this.hosts = $.hosts;
        this.ipNetworks = $.ipNetworks;
        this.nfs = $.nfs;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NfsShareClientGroupArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NfsShareClientGroupArgs $;

        public Builder() {
            $ = new NfsShareClientGroupArgs();
        }

        public Builder(NfsShareClientGroupArgs defaults) {
            $ = new NfsShareClientGroupArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param description Optional description for the clients groups.
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description Optional description for the clients groups.
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param hosts A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
         * 
         * @return builder
         * 
         */
        public Builder hosts(Output<List<String>> hosts) {
            $.hosts = hosts;
            return this;
        }

        /**
         * @param hosts A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
         * 
         * @return builder
         * 
         */
        public Builder hosts(List<String> hosts) {
            return hosts(Output.of(hosts));
        }

        /**
         * @param hosts A singular host allowed to connect to the share. The host can be specified as IP address and can be either IPv4 or IPv6.
         * 
         * @return builder
         * 
         */
        public Builder hosts(String... hosts) {
            return hosts(List.of(hosts));
        }

        /**
         * @param ipNetworks The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
         * 
         * @return builder
         * 
         */
        public Builder ipNetworks(Output<List<String>> ipNetworks) {
            $.ipNetworks = ipNetworks;
            return this;
        }

        /**
         * @param ipNetworks The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
         * 
         * @return builder
         * 
         */
        public Builder ipNetworks(List<String> ipNetworks) {
            return ipNetworks(Output.of(ipNetworks));
        }

        /**
         * @param ipNetworks The allowed host or network to which the export is being shared. The IP address can be either IPv4 or IPv6 and has to be given with CIDR notation.
         * 
         * @return builder
         * 
         */
        public Builder ipNetworks(String... ipNetworks) {
            return ipNetworks(List.of(ipNetworks));
        }

        /**
         * @param nfs NFS specific configurations. Each configuration includes:
         * 
         * @return builder
         * 
         */
        public Builder nfs(@Nullable Output<NfsShareClientGroupNfsArgs> nfs) {
            $.nfs = nfs;
            return this;
        }

        /**
         * @param nfs NFS specific configurations. Each configuration includes:
         * 
         * @return builder
         * 
         */
        public Builder nfs(NfsShareClientGroupNfsArgs nfs) {
            return nfs(Output.of(nfs));
        }

        public NfsShareClientGroupArgs build() {
            if ($.hosts == null) {
                throw new MissingRequiredPropertyException("NfsShareClientGroupArgs", "hosts");
            }
            if ($.ipNetworks == null) {
                throw new MissingRequiredPropertyException("NfsShareClientGroupArgs", "ipNetworks");
            }
            return $;
        }
    }

}
