// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class MongoClusterBiConnector {
    /**
     * @return [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
     * 
     */
    private @Nullable Boolean enabled;
    /**
     * @return [string] - The host where this new BI Connector is installed.
     * 
     */
    private @Nullable String host;
    /**
     * @return [string] - Port number used when connecting to this new BI Connector.
     * 
     */
    private @Nullable String port;

    private MongoClusterBiConnector() {}
    /**
     * @return [bool] - The status of the BI Connector. If not set, the BI Connector is disabled.
     * 
     */
    public Optional<Boolean> enabled() {
        return Optional.ofNullable(this.enabled);
    }
    /**
     * @return [string] - The host where this new BI Connector is installed.
     * 
     */
    public Optional<String> host() {
        return Optional.ofNullable(this.host);
    }
    /**
     * @return [string] - Port number used when connecting to this new BI Connector.
     * 
     */
    public Optional<String> port() {
        return Optional.ofNullable(this.port);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(MongoClusterBiConnector defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Boolean enabled;
        private @Nullable String host;
        private @Nullable String port;
        public Builder() {}
        public Builder(MongoClusterBiConnector defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.enabled = defaults.enabled;
    	      this.host = defaults.host;
    	      this.port = defaults.port;
        }

        @CustomType.Setter
        public Builder enabled(@Nullable Boolean enabled) {

            this.enabled = enabled;
            return this;
        }
        @CustomType.Setter
        public Builder host(@Nullable String host) {

            this.host = host;
            return this;
        }
        @CustomType.Setter
        public Builder port(@Nullable String port) {

            this.port = port;
            return this;
        }
        public MongoClusterBiConnector build() {
            final var _resultValue = new MongoClusterBiConnector();
            _resultValue.enabled = enabled;
            _resultValue.host = host;
            _resultValue.port = port;
            return _resultValue;
        }
    }
}
