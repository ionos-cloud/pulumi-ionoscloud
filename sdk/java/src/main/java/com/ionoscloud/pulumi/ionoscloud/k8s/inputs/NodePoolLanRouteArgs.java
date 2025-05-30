// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.k8s.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class NodePoolLanRouteArgs extends com.pulumi.resources.ResourceArgs {

    public static final NodePoolLanRouteArgs Empty = new NodePoolLanRouteArgs();

    /**
     * [string] IPv4 or IPv6 Gateway IP for the route
     * 
     */
    @Import(name="gatewayIp", required=true)
    private Output<String> gatewayIp;

    /**
     * @return [string] IPv4 or IPv6 Gateway IP for the route
     * 
     */
    public Output<String> gatewayIp() {
        return this.gatewayIp;
    }

    /**
     * [string] IPv4 or IPv6 CIDR to be routed via the interface
     * 
     */
    @Import(name="network", required=true)
    private Output<String> network;

    /**
     * @return [string] IPv4 or IPv6 CIDR to be routed via the interface
     * 
     */
    public Output<String> network() {
        return this.network;
    }

    private NodePoolLanRouteArgs() {}

    private NodePoolLanRouteArgs(NodePoolLanRouteArgs $) {
        this.gatewayIp = $.gatewayIp;
        this.network = $.network;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NodePoolLanRouteArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NodePoolLanRouteArgs $;

        public Builder() {
            $ = new NodePoolLanRouteArgs();
        }

        public Builder(NodePoolLanRouteArgs defaults) {
            $ = new NodePoolLanRouteArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param gatewayIp [string] IPv4 or IPv6 Gateway IP for the route
         * 
         * @return builder
         * 
         */
        public Builder gatewayIp(Output<String> gatewayIp) {
            $.gatewayIp = gatewayIp;
            return this;
        }

        /**
         * @param gatewayIp [string] IPv4 or IPv6 Gateway IP for the route
         * 
         * @return builder
         * 
         */
        public Builder gatewayIp(String gatewayIp) {
            return gatewayIp(Output.of(gatewayIp));
        }

        /**
         * @param network [string] IPv4 or IPv6 CIDR to be routed via the interface
         * 
         * @return builder
         * 
         */
        public Builder network(Output<String> network) {
            $.network = network;
            return this;
        }

        /**
         * @param network [string] IPv4 or IPv6 CIDR to be routed via the interface
         * 
         * @return builder
         * 
         */
        public Builder network(String network) {
            return network(Output.of(network));
        }

        public NodePoolLanRouteArgs build() {
            if ($.gatewayIp == null) {
                throw new MissingRequiredPropertyException("NodePoolLanRouteArgs", "gatewayIp");
            }
            if ($.network == null) {
                throw new MissingRequiredPropertyException("NodePoolLanRouteArgs", "network");
            }
            return $;
        }
    }

}
