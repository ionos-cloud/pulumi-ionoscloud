// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetVpnIpsecGatewayArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetVpnIpsecGatewayArgs Empty = new GetVpnIpsecGatewayArgs();

    /**
     * ID of an existing IPSec Gateway that you want to search for.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of an existing IPSec Gateway that you want to search for.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The location of the IPSec Gateway.
     * 
     */
    @Import(name="location", required=true)
    private Output<String> location;

    /**
     * @return The location of the IPSec Gateway.
     * 
     */
    public Output<String> location() {
        return this.location;
    }

    /**
     * Name of an existing IPSec Gateway that you want to search for.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of an existing IPSec Gateway that you want to search for.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * The IKE version that is permitted for the VPN tunnels.
     * 
     */
    @Import(name="version")
    private @Nullable Output<String> version;

    /**
     * @return The IKE version that is permitted for the VPN tunnels.
     * 
     */
    public Optional<Output<String>> version() {
        return Optional.ofNullable(this.version);
    }

    private GetVpnIpsecGatewayArgs() {}

    private GetVpnIpsecGatewayArgs(GetVpnIpsecGatewayArgs $) {
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
        this.version = $.version;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetVpnIpsecGatewayArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetVpnIpsecGatewayArgs $;

        public Builder() {
            $ = new GetVpnIpsecGatewayArgs();
        }

        public Builder(GetVpnIpsecGatewayArgs defaults) {
            $ = new GetVpnIpsecGatewayArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of an existing IPSec Gateway that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of an existing IPSec Gateway that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location The location of the IPSec Gateway.
         * 
         * @return builder
         * 
         */
        public Builder location(Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location of the IPSec Gateway.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name Name of an existing IPSec Gateway that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of an existing IPSec Gateway that you want to search for.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param version The IKE version that is permitted for the VPN tunnels.
         * 
         * @return builder
         * 
         */
        public Builder version(@Nullable Output<String> version) {
            $.version = version;
            return this;
        }

        /**
         * @param version The IKE version that is permitted for the VPN tunnels.
         * 
         * @return builder
         * 
         */
        public Builder version(String version) {
            return version(Output.of(version));
        }

        public GetVpnIpsecGatewayArgs build() {
            if ($.location == null) {
                throw new MissingRequiredPropertyException("GetVpnIpsecGatewayArgs", "location");
            }
            return $;
        }
    }

}
