// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class MongoClusterMaintenanceWindow {
    /**
     * @return [string]
     * 
     */
    private String dayOfTheWeek;
    /**
     * @return [string]
     * 
     */
    private String time;

    private MongoClusterMaintenanceWindow() {}
    /**
     * @return [string]
     * 
     */
    public String dayOfTheWeek() {
        return this.dayOfTheWeek;
    }
    /**
     * @return [string]
     * 
     */
    public String time() {
        return this.time;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(MongoClusterMaintenanceWindow defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String dayOfTheWeek;
        private String time;
        public Builder() {}
        public Builder(MongoClusterMaintenanceWindow defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.dayOfTheWeek = defaults.dayOfTheWeek;
    	      this.time = defaults.time;
        }

        @CustomType.Setter
        public Builder dayOfTheWeek(String dayOfTheWeek) {
            if (dayOfTheWeek == null) {
              throw new MissingRequiredPropertyException("MongoClusterMaintenanceWindow", "dayOfTheWeek");
            }
            this.dayOfTheWeek = dayOfTheWeek;
            return this;
        }
        @CustomType.Setter
        public Builder time(String time) {
            if (time == null) {
              throw new MissingRequiredPropertyException("MongoClusterMaintenanceWindow", "time");
            }
            this.time = time;
            return this;
        }
        public MongoClusterMaintenanceWindow build() {
            final var _resultValue = new MongoClusterMaintenanceWindow();
            _resultValue.dayOfTheWeek = dayOfTheWeek;
            _resultValue.time = time;
            return _resultValue;
        }
    }
}
