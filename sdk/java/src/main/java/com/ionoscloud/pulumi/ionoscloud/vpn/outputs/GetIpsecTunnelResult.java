// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.vpn.outputs;

import com.ionoscloud.pulumi.ionoscloud.vpn.outputs.GetIpsecTunnelAuth;
import com.ionoscloud.pulumi.ionoscloud.vpn.outputs.GetIpsecTunnelEsp;
import com.ionoscloud.pulumi.ionoscloud.vpn.outputs.GetIpsecTunnelIke;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class GetIpsecTunnelResult {
    private List<GetIpsecTunnelAuth> auths;
    private List<String> cloudNetworkCidrs;
    private String description;
    private List<GetIpsecTunnelEsp> esps;
    private String gatewayId;
    private String id;
    private List<GetIpsecTunnelIke> ikes;
    private @Nullable String location;
    private String name;
    private List<String> peerNetworkCidrs;
    private String remoteHost;

    private GetIpsecTunnelResult() {}
    public List<GetIpsecTunnelAuth> auths() {
        return this.auths;
    }
    public List<String> cloudNetworkCidrs() {
        return this.cloudNetworkCidrs;
    }
    public String description() {
        return this.description;
    }
    public List<GetIpsecTunnelEsp> esps() {
        return this.esps;
    }
    public String gatewayId() {
        return this.gatewayId;
    }
    public String id() {
        return this.id;
    }
    public List<GetIpsecTunnelIke> ikes() {
        return this.ikes;
    }
    public Optional<String> location() {
        return Optional.ofNullable(this.location);
    }
    public String name() {
        return this.name;
    }
    public List<String> peerNetworkCidrs() {
        return this.peerNetworkCidrs;
    }
    public String remoteHost() {
        return this.remoteHost;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetIpsecTunnelResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private List<GetIpsecTunnelAuth> auths;
        private List<String> cloudNetworkCidrs;
        private String description;
        private List<GetIpsecTunnelEsp> esps;
        private String gatewayId;
        private String id;
        private List<GetIpsecTunnelIke> ikes;
        private @Nullable String location;
        private String name;
        private List<String> peerNetworkCidrs;
        private String remoteHost;
        public Builder() {}
        public Builder(GetIpsecTunnelResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.auths = defaults.auths;
    	      this.cloudNetworkCidrs = defaults.cloudNetworkCidrs;
    	      this.description = defaults.description;
    	      this.esps = defaults.esps;
    	      this.gatewayId = defaults.gatewayId;
    	      this.id = defaults.id;
    	      this.ikes = defaults.ikes;
    	      this.location = defaults.location;
    	      this.name = defaults.name;
    	      this.peerNetworkCidrs = defaults.peerNetworkCidrs;
    	      this.remoteHost = defaults.remoteHost;
        }

        @CustomType.Setter
        public Builder auths(List<GetIpsecTunnelAuth> auths) {
            if (auths == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "auths");
            }
            this.auths = auths;
            return this;
        }
        public Builder auths(GetIpsecTunnelAuth... auths) {
            return auths(List.of(auths));
        }
        @CustomType.Setter
        public Builder cloudNetworkCidrs(List<String> cloudNetworkCidrs) {
            if (cloudNetworkCidrs == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "cloudNetworkCidrs");
            }
            this.cloudNetworkCidrs = cloudNetworkCidrs;
            return this;
        }
        public Builder cloudNetworkCidrs(String... cloudNetworkCidrs) {
            return cloudNetworkCidrs(List.of(cloudNetworkCidrs));
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder esps(List<GetIpsecTunnelEsp> esps) {
            if (esps == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "esps");
            }
            this.esps = esps;
            return this;
        }
        public Builder esps(GetIpsecTunnelEsp... esps) {
            return esps(List.of(esps));
        }
        @CustomType.Setter
        public Builder gatewayId(String gatewayId) {
            if (gatewayId == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "gatewayId");
            }
            this.gatewayId = gatewayId;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder ikes(List<GetIpsecTunnelIke> ikes) {
            if (ikes == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "ikes");
            }
            this.ikes = ikes;
            return this;
        }
        public Builder ikes(GetIpsecTunnelIke... ikes) {
            return ikes(List.of(ikes));
        }
        @CustomType.Setter
        public Builder location(@Nullable String location) {

            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder peerNetworkCidrs(List<String> peerNetworkCidrs) {
            if (peerNetworkCidrs == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "peerNetworkCidrs");
            }
            this.peerNetworkCidrs = peerNetworkCidrs;
            return this;
        }
        public Builder peerNetworkCidrs(String... peerNetworkCidrs) {
            return peerNetworkCidrs(List.of(peerNetworkCidrs));
        }
        @CustomType.Setter
        public Builder remoteHost(String remoteHost) {
            if (remoteHost == null) {
              throw new MissingRequiredPropertyException("GetIpsecTunnelResult", "remoteHost");
            }
            this.remoteHost = remoteHost;
            return this;
        }
        public GetIpsecTunnelResult build() {
            final var _resultValue = new GetIpsecTunnelResult();
            _resultValue.auths = auths;
            _resultValue.cloudNetworkCidrs = cloudNetworkCidrs;
            _resultValue.description = description;
            _resultValue.esps = esps;
            _resultValue.gatewayId = gatewayId;
            _resultValue.id = id;
            _resultValue.ikes = ikes;
            _resultValue.location = location;
            _resultValue.name = name;
            _resultValue.peerNetworkCidrs = peerNetworkCidrs;
            _resultValue.remoteHost = remoteHost;
            return _resultValue;
        }
    }
}
