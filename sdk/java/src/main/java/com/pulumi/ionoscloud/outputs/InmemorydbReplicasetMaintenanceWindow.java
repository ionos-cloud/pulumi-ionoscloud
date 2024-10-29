// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class InmemorydbReplicasetMaintenanceWindow {
    /**
     * @return The name of the week day.
     * 
     */
    private String dayOfTheWeek;
    /**
     * @return Start of the maintenance window in UTC time.
     * 
     */
    private String time;

    private InmemorydbReplicasetMaintenanceWindow() {}
    /**
     * @return The name of the week day.
     * 
     */
    public String dayOfTheWeek() {
        return this.dayOfTheWeek;
    }
    /**
     * @return Start of the maintenance window in UTC time.
     * 
     */
    public String time() {
        return this.time;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(InmemorydbReplicasetMaintenanceWindow defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String dayOfTheWeek;
        private String time;
        public Builder() {}
        public Builder(InmemorydbReplicasetMaintenanceWindow defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dayOfTheWeek = defaults.dayOfTheWeek;
    	      this.time = defaults.time;
        }

        @CustomType.Setter
        public Builder dayOfTheWeek(String dayOfTheWeek) {
            if (dayOfTheWeek == null) {
              throw new MissingRequiredPropertyException("InmemorydbReplicasetMaintenanceWindow", "dayOfTheWeek");
            }
            this.dayOfTheWeek = dayOfTheWeek;
            return this;
        }
        @CustomType.Setter
        public Builder time(String time) {
            if (time == null) {
              throw new MissingRequiredPropertyException("InmemorydbReplicasetMaintenanceWindow", "time");
            }
            this.time = time;
            return this;
        }
        public InmemorydbReplicasetMaintenanceWindow build() {
            final var _resultValue = new InmemorydbReplicasetMaintenanceWindow();
            _resultValue.dayOfTheWeek = dayOfTheWeek;
            _resultValue.time = time;
            return _resultValue;
        }
    }
}
