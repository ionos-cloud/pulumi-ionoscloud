// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class IpblockIpConsumerArgs extends com.pulumi.resources.ResourceArgs {

    public static final IpblockIpConsumerArgs Empty = new IpblockIpConsumerArgs();

    @Import(name="datacenterId")
    private @Nullable Output<String> datacenterId;

    public Optional<Output<String>> datacenterId() {
        return Optional.ofNullable(this.datacenterId);
    }

    @Import(name="datacenterName")
    private @Nullable Output<String> datacenterName;

    public Optional<Output<String>> datacenterName() {
        return Optional.ofNullable(this.datacenterName);
    }

    @Import(name="ip")
    private @Nullable Output<String> ip;

    public Optional<Output<String>> ip() {
        return Optional.ofNullable(this.ip);
    }

    @Import(name="k8sClusterUuid")
    private @Nullable Output<String> k8sClusterUuid;

    public Optional<Output<String>> k8sClusterUuid() {
        return Optional.ofNullable(this.k8sClusterUuid);
    }

    @Import(name="k8sNodepoolUuid")
    private @Nullable Output<String> k8sNodepoolUuid;

    public Optional<Output<String>> k8sNodepoolUuid() {
        return Optional.ofNullable(this.k8sNodepoolUuid);
    }

    @Import(name="mac")
    private @Nullable Output<String> mac;

    public Optional<Output<String>> mac() {
        return Optional.ofNullable(this.mac);
    }

    @Import(name="nicId")
    private @Nullable Output<String> nicId;

    public Optional<Output<String>> nicId() {
        return Optional.ofNullable(this.nicId);
    }

    @Import(name="serverId")
    private @Nullable Output<String> serverId;

    public Optional<Output<String>> serverId() {
        return Optional.ofNullable(this.serverId);
    }

    @Import(name="serverName")
    private @Nullable Output<String> serverName;

    public Optional<Output<String>> serverName() {
        return Optional.ofNullable(this.serverName);
    }

    private IpblockIpConsumerArgs() {}

    private IpblockIpConsumerArgs(IpblockIpConsumerArgs $) {
        this.datacenterId = $.datacenterId;
        this.datacenterName = $.datacenterName;
        this.ip = $.ip;
        this.k8sClusterUuid = $.k8sClusterUuid;
        this.k8sNodepoolUuid = $.k8sNodepoolUuid;
        this.mac = $.mac;
        this.nicId = $.nicId;
        this.serverId = $.serverId;
        this.serverName = $.serverName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(IpblockIpConsumerArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private IpblockIpConsumerArgs $;

        public Builder() {
            $ = new IpblockIpConsumerArgs();
        }

        public Builder(IpblockIpConsumerArgs defaults) {
            $ = new IpblockIpConsumerArgs(Objects.requireNonNull(defaults));
        }

        public Builder datacenterId(@Nullable Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        public Builder datacenterName(@Nullable Output<String> datacenterName) {
            $.datacenterName = datacenterName;
            return this;
        }

        public Builder datacenterName(String datacenterName) {
            return datacenterName(Output.of(datacenterName));
        }

        public Builder ip(@Nullable Output<String> ip) {
            $.ip = ip;
            return this;
        }

        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        public Builder k8sClusterUuid(@Nullable Output<String> k8sClusterUuid) {
            $.k8sClusterUuid = k8sClusterUuid;
            return this;
        }

        public Builder k8sClusterUuid(String k8sClusterUuid) {
            return k8sClusterUuid(Output.of(k8sClusterUuid));
        }

        public Builder k8sNodepoolUuid(@Nullable Output<String> k8sNodepoolUuid) {
            $.k8sNodepoolUuid = k8sNodepoolUuid;
            return this;
        }

        public Builder k8sNodepoolUuid(String k8sNodepoolUuid) {
            return k8sNodepoolUuid(Output.of(k8sNodepoolUuid));
        }

        public Builder mac(@Nullable Output<String> mac) {
            $.mac = mac;
            return this;
        }

        public Builder mac(String mac) {
            return mac(Output.of(mac));
        }

        public Builder nicId(@Nullable Output<String> nicId) {
            $.nicId = nicId;
            return this;
        }

        public Builder nicId(String nicId) {
            return nicId(Output.of(nicId));
        }

        public Builder serverId(@Nullable Output<String> serverId) {
            $.serverId = serverId;
            return this;
        }

        public Builder serverId(String serverId) {
            return serverId(Output.of(serverId));
        }

        public Builder serverName(@Nullable Output<String> serverName) {
            $.serverName = serverName;
            return this;
        }

        public Builder serverName(String serverName) {
            return serverName(Output.of(serverName));
        }

        public IpblockIpConsumerArgs build() {
            return $;
        }
    }

}
