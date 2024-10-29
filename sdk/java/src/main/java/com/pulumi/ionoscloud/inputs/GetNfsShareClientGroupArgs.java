// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.GetNfsShareClientGroupNfArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;


public final class GetNfsShareClientGroupArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetNfsShareClientGroupArgs Empty = new GetNfsShareClientGroupArgs();

    /**
     * Optional description for the clients groups.
     * 
     */
    @Import(name="description", required=true)
    private Output<String> description;

    /**
     * @return Optional description for the clients groups.
     * 
     */
    public Output<String> description() {
        return this.description;
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
     * The NFS configuration for the client group. Each NFS configuration supports the following:
     * 
     */
    @Import(name="nfs", required=true)
    private Output<List<GetNfsShareClientGroupNfArgs>> nfs;

    /**
     * @return The NFS configuration for the client group. Each NFS configuration supports the following:
     * 
     */
    public Output<List<GetNfsShareClientGroupNfArgs>> nfs() {
        return this.nfs;
    }

    private GetNfsShareClientGroupArgs() {}

    private GetNfsShareClientGroupArgs(GetNfsShareClientGroupArgs $) {
        this.description = $.description;
        this.hosts = $.hosts;
        this.ipNetworks = $.ipNetworks;
        this.nfs = $.nfs;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetNfsShareClientGroupArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetNfsShareClientGroupArgs $;

        public Builder() {
            $ = new GetNfsShareClientGroupArgs();
        }

        public Builder(GetNfsShareClientGroupArgs defaults) {
            $ = new GetNfsShareClientGroupArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param description Optional description for the clients groups.
         * 
         * @return builder
         * 
         */
        public Builder description(Output<String> description) {
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
         * @param nfs The NFS configuration for the client group. Each NFS configuration supports the following:
         * 
         * @return builder
         * 
         */
        public Builder nfs(Output<List<GetNfsShareClientGroupNfArgs>> nfs) {
            $.nfs = nfs;
            return this;
        }

        /**
         * @param nfs The NFS configuration for the client group. Each NFS configuration supports the following:
         * 
         * @return builder
         * 
         */
        public Builder nfs(List<GetNfsShareClientGroupNfArgs> nfs) {
            return nfs(Output.of(nfs));
        }

        /**
         * @param nfs The NFS configuration for the client group. Each NFS configuration supports the following:
         * 
         * @return builder
         * 
         */
        public Builder nfs(GetNfsShareClientGroupNfArgs... nfs) {
            return nfs(List.of(nfs));
        }

        public GetNfsShareClientGroupArgs build() {
            if ($.description == null) {
                throw new MissingRequiredPropertyException("GetNfsShareClientGroupArgs", "description");
            }
            if ($.hosts == null) {
                throw new MissingRequiredPropertyException("GetNfsShareClientGroupArgs", "hosts");
            }
            if ($.ipNetworks == null) {
                throw new MissingRequiredPropertyException("GetNfsShareClientGroupArgs", "ipNetworks");
            }
            if ($.nfs == null) {
                throw new MissingRequiredPropertyException("GetNfsShareClientGroupArgs", "nfs");
            }
            return $;
        }
    }

}
