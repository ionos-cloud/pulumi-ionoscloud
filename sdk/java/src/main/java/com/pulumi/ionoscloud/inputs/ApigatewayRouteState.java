// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.ApigatewayRouteUpstreamArgs;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ApigatewayRouteState extends com.pulumi.resources.ResourceArgs {

    public static final ApigatewayRouteState Empty = new ApigatewayRouteState();

    /**
     * [string] The ID of the API Gateway that the route belongs to.
     * 
     */
    @Import(name="gatewayId")
    private @Nullable Output<String> gatewayId;

    /**
     * @return [string] The ID of the API Gateway that the route belongs to.
     * 
     */
    public Optional<Output<String>> gatewayId() {
        return Optional.ofNullable(this.gatewayId);
    }

    /**
     * [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
     * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
     * 
     */
    @Import(name="methods")
    private @Nullable Output<List<String>> methods;

    /**
     * @return [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
     * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
     * 
     */
    public Optional<Output<List<String>>> methods() {
        return Optional.ofNullable(this.methods);
    }

    /**
     * [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [list] The paths that the route should match. Minimum items: 1.
     * 
     */
    @Import(name="paths")
    private @Nullable Output<List<String>> paths;

    /**
     * @return [list] The paths that the route should match. Minimum items: 1.
     * 
     */
    public Optional<Output<List<String>>> paths() {
        return Optional.ofNullable(this.paths);
    }

    /**
     * [string] This field specifies the protocol used by the ingress to route traffic to the backend
     * service. Default value: `http`.
     * 
     */
    @Import(name="type")
    private @Nullable Output<String> type;

    /**
     * @return [string] This field specifies the protocol used by the ingress to route traffic to the backend
     * service. Default value: `http`.
     * 
     */
    public Optional<Output<String>> type() {
        return Optional.ofNullable(this.type);
    }

    /**
     * Upstreams information of the API Gateway Route. Minimum items: 1.
     * 
     */
    @Import(name="upstreams")
    private @Nullable Output<List<ApigatewayRouteUpstreamArgs>> upstreams;

    /**
     * @return Upstreams information of the API Gateway Route. Minimum items: 1.
     * 
     */
    public Optional<Output<List<ApigatewayRouteUpstreamArgs>>> upstreams() {
        return Optional.ofNullable(this.upstreams);
    }

    /**
     * [bool] To enable websocket support. Default value: `false`.
     * 
     */
    @Import(name="websocket")
    private @Nullable Output<Boolean> websocket;

    /**
     * @return [bool] To enable websocket support. Default value: `false`.
     * 
     */
    public Optional<Output<Boolean>> websocket() {
        return Optional.ofNullable(this.websocket);
    }

    private ApigatewayRouteState() {}

    private ApigatewayRouteState(ApigatewayRouteState $) {
        this.gatewayId = $.gatewayId;
        this.methods = $.methods;
        this.name = $.name;
        this.paths = $.paths;
        this.type = $.type;
        this.upstreams = $.upstreams;
        this.websocket = $.websocket;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ApigatewayRouteState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ApigatewayRouteState $;

        public Builder() {
            $ = new ApigatewayRouteState();
        }

        public Builder(ApigatewayRouteState defaults) {
            $ = new ApigatewayRouteState(Objects.requireNonNull(defaults));
        }

        /**
         * @param gatewayId [string] The ID of the API Gateway that the route belongs to.
         * 
         * @return builder
         * 
         */
        public Builder gatewayId(@Nullable Output<String> gatewayId) {
            $.gatewayId = gatewayId;
            return this;
        }

        /**
         * @param gatewayId [string] The ID of the API Gateway that the route belongs to.
         * 
         * @return builder
         * 
         */
        public Builder gatewayId(String gatewayId) {
            return gatewayId(Output.of(gatewayId));
        }

        /**
         * @param methods [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
         * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
         * 
         * @return builder
         * 
         */
        public Builder methods(@Nullable Output<List<String>> methods) {
            $.methods = methods;
            return this;
        }

        /**
         * @param methods [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
         * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
         * 
         * @return builder
         * 
         */
        public Builder methods(List<String> methods) {
            return methods(Output.of(methods));
        }

        /**
         * @param methods [list] The HTTP methods that the route should match. Minimum items: 1. Possible values: `GET`,
         * `POST`, `PUT`, `DELETE`, `PATCH`, `OPTIONS`, `HEAD`, `CONNECT`, `TRACE`.
         * 
         * @return builder
         * 
         */
        public Builder methods(String... methods) {
            return methods(List.of(methods));
        }

        /**
         * @param name [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] Name of the API Gateway Route. Only alphanumeric characters are allowed.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param paths [list] The paths that the route should match. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder paths(@Nullable Output<List<String>> paths) {
            $.paths = paths;
            return this;
        }

        /**
         * @param paths [list] The paths that the route should match. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder paths(List<String> paths) {
            return paths(Output.of(paths));
        }

        /**
         * @param paths [list] The paths that the route should match. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder paths(String... paths) {
            return paths(List.of(paths));
        }

        /**
         * @param type [string] This field specifies the protocol used by the ingress to route traffic to the backend
         * service. Default value: `http`.
         * 
         * @return builder
         * 
         */
        public Builder type(@Nullable Output<String> type) {
            $.type = type;
            return this;
        }

        /**
         * @param type [string] This field specifies the protocol used by the ingress to route traffic to the backend
         * service. Default value: `http`.
         * 
         * @return builder
         * 
         */
        public Builder type(String type) {
            return type(Output.of(type));
        }

        /**
         * @param upstreams Upstreams information of the API Gateway Route. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder upstreams(@Nullable Output<List<ApigatewayRouteUpstreamArgs>> upstreams) {
            $.upstreams = upstreams;
            return this;
        }

        /**
         * @param upstreams Upstreams information of the API Gateway Route. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder upstreams(List<ApigatewayRouteUpstreamArgs> upstreams) {
            return upstreams(Output.of(upstreams));
        }

        /**
         * @param upstreams Upstreams information of the API Gateway Route. Minimum items: 1.
         * 
         * @return builder
         * 
         */
        public Builder upstreams(ApigatewayRouteUpstreamArgs... upstreams) {
            return upstreams(List.of(upstreams));
        }

        /**
         * @param websocket [bool] To enable websocket support. Default value: `false`.
         * 
         * @return builder
         * 
         */
        public Builder websocket(@Nullable Output<Boolean> websocket) {
            $.websocket = websocket;
            return this;
        }

        /**
         * @param websocket [bool] To enable websocket support. Default value: `false`.
         * 
         * @return builder
         * 
         */
        public Builder websocket(Boolean websocket) {
            return websocket(Output.of(websocket));
        }

        public ApigatewayRouteState build() {
            return $;
        }
    }

}
