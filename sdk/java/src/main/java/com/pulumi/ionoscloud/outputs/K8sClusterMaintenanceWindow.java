// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class K8sClusterMaintenanceWindow {
    /**
     * @return [string] Day of the week when maintenance is allowed
     * 
     */
    private String dayOfTheWeek;
    /**
     * @return [string] A clock time in the day when maintenance is allowed
     * 
     */
    private String time;

    private K8sClusterMaintenanceWindow() {}
    /**
     * @return [string] Day of the week when maintenance is allowed
     * 
     */
    public String dayOfTheWeek() {
        return this.dayOfTheWeek;
    }
    /**
     * @return [string] A clock time in the day when maintenance is allowed
     * 
     */
    public String time() {
        return this.time;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(K8sClusterMaintenanceWindow defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String dayOfTheWeek;
        private String time;
        public Builder() {}
        public Builder(K8sClusterMaintenanceWindow defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dayOfTheWeek = defaults.dayOfTheWeek;
    	      this.time = defaults.time;
        }

        @CustomType.Setter
        public Builder dayOfTheWeek(String dayOfTheWeek) {
            if (dayOfTheWeek == null) {
              throw new MissingRequiredPropertyException("K8sClusterMaintenanceWindow", "dayOfTheWeek");
            }
            this.dayOfTheWeek = dayOfTheWeek;
            return this;
        }
        @CustomType.Setter
        public Builder time(String time) {
            if (time == null) {
              throw new MissingRequiredPropertyException("K8sClusterMaintenanceWindow", "time");
            }
            this.time = time;
            return this;
        }
        public K8sClusterMaintenanceWindow build() {
            final var _resultValue = new K8sClusterMaintenanceWindow();
            _resultValue.dayOfTheWeek = dayOfTheWeek;
            _resultValue.time = time;
            return _resultValue;
        }
    }
}
