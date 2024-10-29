// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class K8sNodePoolMaintenanceWindowArgs extends com.pulumi.resources.ResourceArgs {

    public static final K8sNodePoolMaintenanceWindowArgs Empty = new K8sNodePoolMaintenanceWindowArgs();

    /**
     * [string] Day of the week when maintenance is allowed
     * 
     */
    @Import(name="dayOfTheWeek", required=true)
    private Output<String> dayOfTheWeek;

    /**
     * @return [string] Day of the week when maintenance is allowed
     * 
     */
    public Output<String> dayOfTheWeek() {
        return this.dayOfTheWeek;
    }

    /**
     * [string] A clock time in the day when maintenance is allowed
     * 
     */
    @Import(name="time", required=true)
    private Output<String> time;

    /**
     * @return [string] A clock time in the day when maintenance is allowed
     * 
     */
    public Output<String> time() {
        return this.time;
    }

    private K8sNodePoolMaintenanceWindowArgs() {}

    private K8sNodePoolMaintenanceWindowArgs(K8sNodePoolMaintenanceWindowArgs $) {
        this.dayOfTheWeek = $.dayOfTheWeek;
        this.time = $.time;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(K8sNodePoolMaintenanceWindowArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private K8sNodePoolMaintenanceWindowArgs $;

        public Builder() {
            $ = new K8sNodePoolMaintenanceWindowArgs();
        }

        public Builder(K8sNodePoolMaintenanceWindowArgs defaults) {
            $ = new K8sNodePoolMaintenanceWindowArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dayOfTheWeek [string] Day of the week when maintenance is allowed
         * 
         * @return builder
         * 
         */
        public Builder dayOfTheWeek(Output<String> dayOfTheWeek) {
            $.dayOfTheWeek = dayOfTheWeek;
            return this;
        }

        /**
         * @param dayOfTheWeek [string] Day of the week when maintenance is allowed
         * 
         * @return builder
         * 
         */
        public Builder dayOfTheWeek(String dayOfTheWeek) {
            return dayOfTheWeek(Output.of(dayOfTheWeek));
        }

        /**
         * @param time [string] A clock time in the day when maintenance is allowed
         * 
         * @return builder
         * 
         */
        public Builder time(Output<String> time) {
            $.time = time;
            return this;
        }

        /**
         * @param time [string] A clock time in the day when maintenance is allowed
         * 
         * @return builder
         * 
         */
        public Builder time(String time) {
            return time(Output.of(time));
        }

        public K8sNodePoolMaintenanceWindowArgs build() {
            if ($.dayOfTheWeek == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolMaintenanceWindowArgs", "dayOfTheWeek");
            }
            if ($.time == null) {
                throw new MissingRequiredPropertyException("K8sNodePoolMaintenanceWindowArgs", "time");
            }
            return $;
        }
    }

}
