// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.nsg;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class DatacenterNsgSelectionArgs extends com.pulumi.resources.ResourceArgs {

    public static final DatacenterNsgSelectionArgs Empty = new DatacenterNsgSelectionArgs();

    /**
     * [string] The ID of a Virtual Data Center.
     * 
     */
    @Import(name="datacenterId", required=true)
    private Output<String> datacenterId;

    /**
     * @return [string] The ID of a Virtual Data Center.
     * 
     */
    public Output<String> datacenterId() {
        return this.datacenterId;
    }

    /**
     * [string] The ID of a Network Security Group.
     * 
     */
    @Import(name="nsgId", required=true)
    private Output<String> nsgId;

    /**
     * @return [string] The ID of a Network Security Group.
     * 
     */
    public Output<String> nsgId() {
        return this.nsgId;
    }

    private DatacenterNsgSelectionArgs() {}

    private DatacenterNsgSelectionArgs(DatacenterNsgSelectionArgs $) {
        this.datacenterId = $.datacenterId;
        this.nsgId = $.nsgId;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(DatacenterNsgSelectionArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private DatacenterNsgSelectionArgs $;

        public Builder() {
            $ = new DatacenterNsgSelectionArgs();
        }

        public Builder(DatacenterNsgSelectionArgs defaults) {
            $ = new DatacenterNsgSelectionArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param datacenterId [string] The ID of a Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(Output<String> datacenterId) {
            $.datacenterId = datacenterId;
            return this;
        }

        /**
         * @param datacenterId [string] The ID of a Virtual Data Center.
         * 
         * @return builder
         * 
         */
        public Builder datacenterId(String datacenterId) {
            return datacenterId(Output.of(datacenterId));
        }

        /**
         * @param nsgId [string] The ID of a Network Security Group.
         * 
         * @return builder
         * 
         */
        public Builder nsgId(Output<String> nsgId) {
            $.nsgId = nsgId;
            return this;
        }

        /**
         * @param nsgId [string] The ID of a Network Security Group.
         * 
         * @return builder
         * 
         */
        public Builder nsgId(String nsgId) {
            return nsgId(Output.of(nsgId));
        }

        public DatacenterNsgSelectionArgs build() {
            if ($.datacenterId == null) {
                throw new MissingRequiredPropertyException("DatacenterNsgSelectionArgs", "datacenterId");
            }
            if ($.nsgId == null) {
                throw new MissingRequiredPropertyException("DatacenterNsgSelectionArgs", "nsgId");
            }
            return $;
        }
    }

}
