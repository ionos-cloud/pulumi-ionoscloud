// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MongoClusterBiConnectorArgs extends com.pulumi.resources.ResourceArgs {

    public static final MongoClusterBiConnectorArgs Empty = new MongoClusterBiConnectorArgs();

    /**
     * [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
     * 
     */
    @Import(name="enabled")
    private @Nullable Output<Boolean> enabled;

    /**
     * @return [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
     * 
     */
    public Optional<Output<Boolean>> enabled() {
        return Optional.ofNullable(this.enabled);
    }

    /**
     * [string] - The host where this new BI Connector is installed.
     * 
     */
    @Import(name="host")
    private @Nullable Output<String> host;

    /**
     * @return [string] - The host where this new BI Connector is installed.
     * 
     */
    public Optional<Output<String>> host() {
        return Optional.ofNullable(this.host);
    }

    /**
     * [string] - Port number used when connecting to this new BI Connector.
     * 
     */
    @Import(name="port")
    private @Nullable Output<String> port;

    /**
     * @return [string] - Port number used when connecting to this new BI Connector.
     * 
     */
    public Optional<Output<String>> port() {
        return Optional.ofNullable(this.port);
    }

    private MongoClusterBiConnectorArgs() {}

    private MongoClusterBiConnectorArgs(MongoClusterBiConnectorArgs $) {
        this.enabled = $.enabled;
        this.host = $.host;
        this.port = $.port;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MongoClusterBiConnectorArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MongoClusterBiConnectorArgs $;

        public Builder() {
            $ = new MongoClusterBiConnectorArgs();
        }

        public Builder(MongoClusterBiConnectorArgs defaults) {
            $ = new MongoClusterBiConnectorArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param enabled [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
         * 
         * @return builder
         * 
         */
        public Builder enabled(@Nullable Output<Boolean> enabled) {
            $.enabled = enabled;
            return this;
        }

        /**
         * @param enabled [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
         * 
         * @return builder
         * 
         */
        public Builder enabled(Boolean enabled) {
            return enabled(Output.of(enabled));
        }

        /**
         * @param host [string] - The host where this new BI Connector is installed.
         * 
         * @return builder
         * 
         */
        public Builder host(@Nullable Output<String> host) {
            $.host = host;
            return this;
        }

        /**
         * @param host [string] - The host where this new BI Connector is installed.
         * 
         * @return builder
         * 
         */
        public Builder host(String host) {
            return host(Output.of(host));
        }

        /**
         * @param port [string] - Port number used when connecting to this new BI Connector.
         * 
         * @return builder
         * 
         */
        public Builder port(@Nullable Output<String> port) {
            $.port = port;
            return this;
        }

        /**
         * @param port [string] - Port number used when connecting to this new BI Connector.
         * 
         * @return builder
         * 
         */
        public Builder port(String port) {
            return port(Output.of(port));
        }

        public MongoClusterBiConnectorArgs build() {
            return $;
        }
    }

}
