// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class LanIpFailoverArgs extends com.pulumi.resources.ResourceArgs {

    public static final LanIpFailoverArgs Empty = new LanIpFailoverArgs();

    @Import(name="ip")
    private @Nullable Output<String> ip;

    public Optional<Output<String>> ip() {
        return Optional.ofNullable(this.ip);
    }

    @Import(name="nicUuid")
    private @Nullable Output<String> nicUuid;

    public Optional<Output<String>> nicUuid() {
        return Optional.ofNullable(this.nicUuid);
    }

    private LanIpFailoverArgs() {}

    private LanIpFailoverArgs(LanIpFailoverArgs $) {
        this.ip = $.ip;
        this.nicUuid = $.nicUuid;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(LanIpFailoverArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private LanIpFailoverArgs $;

        public Builder() {
            $ = new LanIpFailoverArgs();
        }

        public Builder(LanIpFailoverArgs defaults) {
            $ = new LanIpFailoverArgs(Objects.requireNonNull(defaults));
        }

        public Builder ip(@Nullable Output<String> ip) {
            $.ip = ip;
            return this;
        }

        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        public Builder nicUuid(@Nullable Output<String> nicUuid) {
            $.nicUuid = nicUuid;
            return this;
        }

        public Builder nicUuid(String nicUuid) {
            return nicUuid(Output.of(nicUuid));
        }

        public LanIpFailoverArgs build() {
            return $;
        }
    }

}
