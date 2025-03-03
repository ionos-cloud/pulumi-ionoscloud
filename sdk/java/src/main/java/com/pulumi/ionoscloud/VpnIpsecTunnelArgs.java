// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import com.pulumi.ionoscloud.inputs.VpnIpsecTunnelAuthArgs;
import com.pulumi.ionoscloud.inputs.VpnIpsecTunnelEspArgs;
import com.pulumi.ionoscloud.inputs.VpnIpsecTunnelIkeArgs;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class VpnIpsecTunnelArgs extends com.pulumi.resources.ResourceArgs {

    public static final VpnIpsecTunnelArgs Empty = new VpnIpsecTunnelArgs();

    /**
     * [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
     * items: 1.
     * 
     */
    @Import(name="auth", required=true)
    private Output<VpnIpsecTunnelAuthArgs> auth;

    /**
     * @return [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
     * items: 1.
     * 
     */
    public Output<VpnIpsecTunnelAuthArgs> auth() {
        return this.auth;
    }

    /**
     * [list] The network CIDRs on the &#34;Left&#34; side that are allowed to connect to the IPSec
     * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1.
     * Maximum items: 20.
     * 
     */
    @Import(name="cloudNetworkCidrs", required=true)
    private Output<List<String>> cloudNetworkCidrs;

    /**
     * @return [list] The network CIDRs on the &#34;Left&#34; side that are allowed to connect to the IPSec
     * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1.
     * Maximum items: 20.
     * 
     */
    public Output<List<String>> cloudNetworkCidrs() {
        return this.cloudNetworkCidrs;
    }

    /**
     * [string] The human-readable description of your IPSec Gateway Tunnel.
     * 
     */
    @Import(name="description")
    private @Nullable Output<String> description;

    /**
     * @return [string] The human-readable description of your IPSec Gateway Tunnel.
     * 
     */
    public Optional<Output<String>> description() {
        return Optional.ofNullable(this.description);
    }

    /**
     * [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
     * 
     */
    @Import(name="esps", required=true)
    private Output<List<VpnIpsecTunnelEspArgs>> esps;

    /**
     * @return [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
     * 
     */
    public Output<List<VpnIpsecTunnelEspArgs>> esps() {
        return this.esps;
    }

    /**
     * [string] The ID of the IPSec Gateway that the tunnel belongs to.
     * 
     */
    @Import(name="gatewayId", required=true)
    private Output<String> gatewayId;

    /**
     * @return [string] The ID of the IPSec Gateway that the tunnel belongs to.
     * 
     */
    public Output<String> gatewayId() {
        return this.gatewayId;
    }

    /**
     * [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
     * 
     */
    @Import(name="ike", required=true)
    private Output<VpnIpsecTunnelIkeArgs> ike;

    /**
     * @return [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
     * 
     */
    public Output<VpnIpsecTunnelIkeArgs> ike() {
        return this.ike;
    }

    /**
     * [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
     * gb/lhr, us/ewr, us/las, us/mci, fr/par
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
     * gb/lhr, us/ewr, us/las, us/mci, fr/par
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * [string] The name of the IPSec Gateway Tunnel.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] The name of the IPSec Gateway Tunnel.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [list] The network CIDRs on the &#34;Right&#34; side that are allowed to connect to the IPSec
     * tunnel. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1. Maximum items: 20.
     * 
     */
    @Import(name="peerNetworkCidrs", required=true)
    private Output<List<String>> peerNetworkCidrs;

    /**
     * @return [list] The network CIDRs on the &#34;Right&#34; side that are allowed to connect to the IPSec
     * tunnel. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1. Maximum items: 20.
     * 
     */
    public Output<List<String>> peerNetworkCidrs() {
        return this.peerNetworkCidrs;
    }

    /**
     * [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
     * 
     */
    @Import(name="remoteHost", required=true)
    private Output<String> remoteHost;

    /**
     * @return [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
     * 
     */
    public Output<String> remoteHost() {
        return this.remoteHost;
    }

    private VpnIpsecTunnelArgs() {}

    private VpnIpsecTunnelArgs(VpnIpsecTunnelArgs $) {
        this.auth = $.auth;
        this.cloudNetworkCidrs = $.cloudNetworkCidrs;
        this.description = $.description;
        this.esps = $.esps;
        this.gatewayId = $.gatewayId;
        this.ike = $.ike;
        this.location = $.location;
        this.name = $.name;
        this.peerNetworkCidrs = $.peerNetworkCidrs;
        this.remoteHost = $.remoteHost;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(VpnIpsecTunnelArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private VpnIpsecTunnelArgs $;

        public Builder() {
            $ = new VpnIpsecTunnelArgs();
        }

        public Builder(VpnIpsecTunnelArgs defaults) {
            $ = new VpnIpsecTunnelArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param auth [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
         * items: 1.
         * 
         * @return builder
         * 
         */
        public Builder auth(Output<VpnIpsecTunnelAuthArgs> auth) {
            $.auth = auth;
            return this;
        }

        /**
         * @param auth [string] Properties with all data needed to define IPSec Authentication. Minimum items: 1. Maximum
         * items: 1.
         * 
         * @return builder
         * 
         */
        public Builder auth(VpnIpsecTunnelAuthArgs auth) {
            return auth(Output.of(auth));
        }

        /**
         * @param cloudNetworkCidrs [list] The network CIDRs on the &#34;Left&#34; side that are allowed to connect to the IPSec
         * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1.
         * Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder cloudNetworkCidrs(Output<List<String>> cloudNetworkCidrs) {
            $.cloudNetworkCidrs = cloudNetworkCidrs;
            return this;
        }

        /**
         * @param cloudNetworkCidrs [list] The network CIDRs on the &#34;Left&#34; side that are allowed to connect to the IPSec
         * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1.
         * Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder cloudNetworkCidrs(List<String> cloudNetworkCidrs) {
            return cloudNetworkCidrs(Output.of(cloudNetworkCidrs));
        }

        /**
         * @param cloudNetworkCidrs [list] The network CIDRs on the &#34;Left&#34; side that are allowed to connect to the IPSec
         * tunnel, i.e. the CIDRs within your IONOS Cloud LAN. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1.
         * Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder cloudNetworkCidrs(String... cloudNetworkCidrs) {
            return cloudNetworkCidrs(List.of(cloudNetworkCidrs));
        }

        /**
         * @param description [string] The human-readable description of your IPSec Gateway Tunnel.
         * 
         * @return builder
         * 
         */
        public Builder description(@Nullable Output<String> description) {
            $.description = description;
            return this;
        }

        /**
         * @param description [string] The human-readable description of your IPSec Gateway Tunnel.
         * 
         * @return builder
         * 
         */
        public Builder description(String description) {
            return description(Output.of(description));
        }

        /**
         * @param esps [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder esps(Output<List<VpnIpsecTunnelEspArgs>> esps) {
            $.esps = esps;
            return this;
        }

        /**
         * @param esps [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder esps(List<VpnIpsecTunnelEspArgs> esps) {
            return esps(Output.of(esps));
        }

        /**
         * @param esps [list] Settings for the IPSec SA (ESP) phase. Minimum items: 1. Maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder esps(VpnIpsecTunnelEspArgs... esps) {
            return esps(List.of(esps));
        }

        /**
         * @param gatewayId [string] The ID of the IPSec Gateway that the tunnel belongs to.
         * 
         * @return builder
         * 
         */
        public Builder gatewayId(Output<String> gatewayId) {
            $.gatewayId = gatewayId;
            return this;
        }

        /**
         * @param gatewayId [string] The ID of the IPSec Gateway that the tunnel belongs to.
         * 
         * @return builder
         * 
         */
        public Builder gatewayId(String gatewayId) {
            return gatewayId(Output.of(gatewayId));
        }

        /**
         * @param ike [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder ike(Output<VpnIpsecTunnelIkeArgs> ike) {
            $.ike = ike;
            return this;
        }

        /**
         * @param ike [list] Settings for the initial security exchange phase. Minimum items: 1. Maximum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder ike(VpnIpsecTunnelIkeArgs ike) {
            return ike(Output.of(ike));
        }

        /**
         * @param location [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
         * gb/lhr, us/ewr, us/las, us/mci, fr/par
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location [string] The location of the IPSec Gateway Tunnel. Supported locations: de/fra, de/txl, es/vit,
         * gb/lhr, us/ewr, us/las, us/mci, fr/par
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name [string] The name of the IPSec Gateway Tunnel.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] The name of the IPSec Gateway Tunnel.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param peerNetworkCidrs [list] The network CIDRs on the &#34;Right&#34; side that are allowed to connect to the IPSec
         * tunnel. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1. Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder peerNetworkCidrs(Output<List<String>> peerNetworkCidrs) {
            $.peerNetworkCidrs = peerNetworkCidrs;
            return this;
        }

        /**
         * @param peerNetworkCidrs [list] The network CIDRs on the &#34;Right&#34; side that are allowed to connect to the IPSec
         * tunnel. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1. Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder peerNetworkCidrs(List<String> peerNetworkCidrs) {
            return peerNetworkCidrs(Output.of(peerNetworkCidrs));
        }

        /**
         * @param peerNetworkCidrs [list] The network CIDRs on the &#34;Right&#34; side that are allowed to connect to the IPSec
         * tunnel. Specify &#34;0.0.0.0/0&#34; or &#34;::/0&#34; for all addresses. Minimum items: 1. Maximum items: 20.
         * 
         * @return builder
         * 
         */
        public Builder peerNetworkCidrs(String... peerNetworkCidrs) {
            return peerNetworkCidrs(List.of(peerNetworkCidrs));
        }

        /**
         * @param remoteHost [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
         * 
         * @return builder
         * 
         */
        public Builder remoteHost(Output<String> remoteHost) {
            $.remoteHost = remoteHost;
            return this;
        }

        /**
         * @param remoteHost [string] The remote peer host fully qualified domain name or public IPV4 IP to connect to.
         * 
         * @return builder
         * 
         */
        public Builder remoteHost(String remoteHost) {
            return remoteHost(Output.of(remoteHost));
        }

        public VpnIpsecTunnelArgs build() {
            if ($.auth == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "auth");
            }
            if ($.cloudNetworkCidrs == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "cloudNetworkCidrs");
            }
            if ($.esps == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "esps");
            }
            if ($.gatewayId == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "gatewayId");
            }
            if ($.ike == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "ike");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "location");
            }
            if ($.peerNetworkCidrs == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "peerNetworkCidrs");
            }
            if ($.remoteHost == null) {
                throw new MissingRequiredPropertyException("VpnIpsecTunnelArgs", "remoteHost");
            }
            return $;
        }
    }

}
