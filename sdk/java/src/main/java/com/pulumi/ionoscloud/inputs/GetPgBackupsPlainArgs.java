// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetPgBackupsPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetPgBackupsPlainArgs Empty = new GetPgBackupsPlainArgs();

    @Import(name="clusterId", required=true)
    private String clusterId;

    public String clusterId() {
        return this.clusterId;
    }

    private GetPgBackupsPlainArgs() {}

    private GetPgBackupsPlainArgs(GetPgBackupsPlainArgs $) {
        this.clusterId = $.clusterId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetPgBackupsPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetPgBackupsPlainArgs $;

        public Builder() {
            $ = new GetPgBackupsPlainArgs();
        }

        public Builder(GetPgBackupsPlainArgs defaults) {
            $ = new GetPgBackupsPlainArgs(Objects.requireNonNull(defaults));
        }

        public Builder clusterId(String clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        public GetPgBackupsPlainArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("GetPgBackupsPlainArgs", "clusterId");
            }
            return $;
        }
    }

}
