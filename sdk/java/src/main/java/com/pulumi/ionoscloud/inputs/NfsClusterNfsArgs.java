// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NfsClusterNfsArgs extends com.pulumi.resources.ResourceArgs {

    public static final NfsClusterNfsArgs Empty = new NfsClusterNfsArgs();

    /**
     * The minimum supported version of the NFS cluster. Supported values: `4.2`. Default is `4.2`.
     * 
     */
    @Import(name="minVersion")
    private @Nullable Output<String> minVersion;

    /**
     * @return The minimum supported version of the NFS cluster. Supported values: `4.2`. Default is `4.2`.
     * 
     */
    public Optional<Output<String>> minVersion() {
        return Optional.ofNullable(this.minVersion);
    }

    private NfsClusterNfsArgs() {}

    private NfsClusterNfsArgs(NfsClusterNfsArgs $) {
        this.minVersion = $.minVersion;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NfsClusterNfsArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NfsClusterNfsArgs $;

        public Builder() {
            $ = new NfsClusterNfsArgs();
        }

        public Builder(NfsClusterNfsArgs defaults) {
            $ = new NfsClusterNfsArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param minVersion The minimum supported version of the NFS cluster. Supported values: `4.2`. Default is `4.2`.
         * 
         * @return builder
         * 
         */
        public Builder minVersion(@Nullable Output<String> minVersion) {
            $.minVersion = minVersion;
            return this;
        }

        /**
         * @param minVersion The minimum supported version of the NFS cluster. Supported values: `4.2`. Default is `4.2`.
         * 
         * @return builder
         * 
         */
        public Builder minVersion(String minVersion) {
            return minVersion(Output.of(minVersion));
        }

        public NfsClusterNfsArgs build() {
            return $;
        }
    }

}
