// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.vpn.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class WireguardGatewayMaintenanceWindowArgs extends com.pulumi.resources.ResourceArgs {

    public static final WireguardGatewayMaintenanceWindowArgs Empty = new WireguardGatewayMaintenanceWindowArgs();

    /**
     * [string] The name of the week day.
     * 
     */
    @Import(name="dayOfTheWeek", required=true)
    private Output<String> dayOfTheWeek;

    /**
     * @return [string] The name of the week day.
     * 
     */
    public Output<String> dayOfTheWeek() {
        return this.dayOfTheWeek;
    }

    /**
     * [string] Start of the maintenance window in UTC time.
     * 
     */
    @Import(name="time", required=true)
    private Output<String> time;

    /**
     * @return [string] Start of the maintenance window in UTC time.
     * 
     */
    public Output<String> time() {
        return this.time;
    }

    private WireguardGatewayMaintenanceWindowArgs() {}

    private WireguardGatewayMaintenanceWindowArgs(WireguardGatewayMaintenanceWindowArgs $) {
        this.dayOfTheWeek = $.dayOfTheWeek;
        this.time = $.time;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(WireguardGatewayMaintenanceWindowArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private WireguardGatewayMaintenanceWindowArgs $;

        public Builder() {
            $ = new WireguardGatewayMaintenanceWindowArgs();
        }

        public Builder(WireguardGatewayMaintenanceWindowArgs defaults) {
            $ = new WireguardGatewayMaintenanceWindowArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param dayOfTheWeek [string] The name of the week day.
         * 
         * @return builder
         * 
         */
        public Builder dayOfTheWeek(Output<String> dayOfTheWeek) {
            $.dayOfTheWeek = dayOfTheWeek;
            return this;
        }

        /**
         * @param dayOfTheWeek [string] The name of the week day.
         * 
         * @return builder
         * 
         */
        public Builder dayOfTheWeek(String dayOfTheWeek) {
            return dayOfTheWeek(Output.of(dayOfTheWeek));
        }

        /**
         * @param time [string] Start of the maintenance window in UTC time.
         * 
         * @return builder
         * 
         */
        public Builder time(Output<String> time) {
            $.time = time;
            return this;
        }

        /**
         * @param time [string] Start of the maintenance window in UTC time.
         * 
         * @return builder
         * 
         */
        public Builder time(String time) {
            return time(Output.of(time));
        }

        public WireguardGatewayMaintenanceWindowArgs build() {
            if ($.dayOfTheWeek == null) {
                throw new MissingRequiredPropertyException("WireguardGatewayMaintenanceWindowArgs", "dayOfTheWeek");
            }
            if ($.time == null) {
                throw new MissingRequiredPropertyException("WireguardGatewayMaintenanceWindowArgs", "time");
            }
            return $;
        }
    }

}
