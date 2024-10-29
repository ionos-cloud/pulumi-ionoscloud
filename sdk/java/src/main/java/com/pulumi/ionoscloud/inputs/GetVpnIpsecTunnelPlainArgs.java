// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetVpnIpsecTunnelPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetVpnIpsecTunnelPlainArgs Empty = new GetVpnIpsecTunnelPlainArgs();

    /**
     * The ID of the IPSec Gateway that the tunnel belongs to.
     * 
     */
    @Import(name="gatewayId", required=true)
    private String gatewayId;

    /**
     * @return The ID of the IPSec Gateway that the tunnel belongs to.
     * 
     */
    public String gatewayId() {
        return this.gatewayId;
    }

    /**
     * ID of an existing IPSec Gateway Tunnel that you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable String id;

    /**
     * @return ID of an existing IPSec Gateway Tunnel that you want to search for.
     * 
     */
    public Optional<String> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The location of the IPSec Gateway Tunnel.
     * 
     */
    @Import(name="location", required=true)
    private String location;

    /**
     * @return The location of the IPSec Gateway Tunnel.
     * 
     */
    public String location() {
        return this.location;
    }

    /**
     * Name of an existing IPSec Gateway Tunnel that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable String name;

    /**
     * @return Name of an existing IPSec Gateway Tunnel that you want to search for.
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }

    private GetVpnIpsecTunnelPlainArgs() {}

    private GetVpnIpsecTunnelPlainArgs(GetVpnIpsecTunnelPlainArgs $) {
        this.gatewayId = $.gatewayId;
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetVpnIpsecTunnelPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetVpnIpsecTunnelPlainArgs $;

        public Builder() {
            $ = new GetVpnIpsecTunnelPlainArgs();
        }

        public Builder(GetVpnIpsecTunnelPlainArgs defaults) {
            $ = new GetVpnIpsecTunnelPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param gatewayId The ID of the IPSec Gateway that the tunnel belongs to.
         * 
         * @return builder
         * 
         */
        public Builder gatewayId(String gatewayId) {
            $.gatewayId = gatewayId;
            return this;
        }

        /**
         * @param id ID of an existing IPSec Gateway Tunnel that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable String id) {
            $.id = id;
            return this;
        }

        /**
         * @param location The location of the IPSec Gateway Tunnel.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            $.location = location;
            return this;
        }

        /**
         * @param name Name of an existing IPSec Gateway Tunnel that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable String name) {
            $.name = name;
            return this;
        }

        public GetVpnIpsecTunnelPlainArgs build() {
            if ($.gatewayId == null) {
                throw new MissingRequiredPropertyException("GetVpnIpsecTunnelPlainArgs", "gatewayId");
            }
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetVpnIpsecTunnelPlainArgs", "location");
            }
            return $;
        }
    }

}
