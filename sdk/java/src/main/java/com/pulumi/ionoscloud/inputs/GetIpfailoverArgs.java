// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetIpfailoverArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetIpfailoverArgs Empty = new GetIpfailoverArgs();

    /**
     * The ID of the datacenter containing the ip failover datasource
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return The ID of the datacenter containing the ip failover datasource
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * The reserved IP address to be used in the IP failover group.
     * 
     */
    @Import(name="ip", required=true)
    private Output<String> ip;

    /**
     * @return The reserved IP address to be used in the IP failover group.
     * 
     */
    public Output<String> ip() {
        return this.ip;
    }

    /**
     * The ID of a LAN.
     * 
     */
    @Import(name="lanId", required=true)
    private Output<String> lanId;

    /**
     * @return The ID of a LAN.
     * 
     */
    public Output<String> lanId() {
        return this.lanId;
    }

    private GetIpfailoverArgs() {}

    private GetIpfailoverArgs(GetIpfailoverArgs $) {
        this.datacenterId = $.datacenterId;
        this.ip = $.ip;
        this.lanId = $.lanId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetIpfailoverArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetIpfailoverArgs $;

        public Builder() {
            $ = new GetIpfailoverArgs();
        }

        public Builder(GetIpfailoverArgs defaults) {
            $ = new GetIpfailoverArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId The ID of the datacenter containing the ip failover datasource
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId The ID of the datacenter containing the ip failover datasource
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param ip The reserved IP address to be used in the IP failover group.
         * 
         * @return builder
         * 
         */
        public Builder ip(Output<String> ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ip The reserved IP address to be used in the IP failover group.
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        /**
         * @param lanId The ID of a LAN.
         * 
         * @return builder
         * 
         */
        public Builder lanId(Output<String> lanId) {
            $.lanId = lanId;
            return this;
        }

        /**
         * @param lanId The ID of a LAN.
         * 
         * @return builder
         * 
         */
        public Builder lanId(String lanId) {
            return lanId(Output.of(lanId));
        }

        public GetIpfailoverArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("GetIpfailoverArgs", "datacenterId");
            }
            if ($.ip == null) {
                throw new MissingRequiredPropertyException("GetIpfailoverArgs", "ip");
            }
            if ($.lanId == null) {
                throw new MissingRequiredPropertyException("GetIpfailoverArgs", "lanId");
            }
            return $;
        }
    }

}
