// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetNfsShareClientGroupNfArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetNfsShareClientGroupNfArgs Empty = new GetNfsShareClientGroupNfArgs();

    /**
     * The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
     * 
     */
    @Import(name="squash", required=true)
    private Output<String> squash;

    /**
     * @return The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
     * 
     */
    public Output<String> squash() {
        return this.squash;
    }

    private GetNfsShareClientGroupNfArgs() {}

    private GetNfsShareClientGroupNfArgs(GetNfsShareClientGroupNfArgs $) {
        this.squash = $.squash;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetNfsShareClientGroupNfArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetNfsShareClientGroupNfArgs $;

        public Builder() {
            $ = new GetNfsShareClientGroupNfArgs();
        }

        public Builder(GetNfsShareClientGroupNfArgs defaults) {
            $ = new GetNfsShareClientGroupNfArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param squash The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
         * 
         * @return builder
         * 
         */
        public Builder squash(Output<String> squash) {
            $.squash = squash;
            return this;
        }

        /**
         * @param squash The squash mode for the export. The squash mode can be: none - No squash mode. no mapping, root-anonymous - Map root user to anonymous uid, all-anonymous - Map all users to anonymous uid.
         * 
         * @return builder
         * 
         */
        public Builder squash(String squash) {
            return squash(Output.of(squash));
        }

        public GetNfsShareClientGroupNfArgs build() {
            if ($.squash == null) {
                throw new MissingRequiredPropertyException("GetNfsShareClientGroupNfArgs", "squash");
            }
            return $;
        }
    }

}
