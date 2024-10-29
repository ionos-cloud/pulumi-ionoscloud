// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetPgClusterFromBackup {
    /**
     * @return The unique ID of the backup you want to restore.
     * 
     */
    private String backupId;
    /**
     * @return If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.
     * 
     */
    private String recoveryTargetTime;

    private GetPgClusterFromBackup() {}
    /**
     * @return The unique ID of the backup you want to restore.
     * 
     */
    public String backupId() {
        return this.backupId;
    }
    /**
     * @return If this value is supplied as ISO 8601 timestamp, the backup will be replayed up until the given timestamp. If empty, the backup will be applied completely.
     * 
     */
    public String recoveryTargetTime() {
        return this.recoveryTargetTime;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetPgClusterFromBackup defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String backupId;
        private String recoveryTargetTime;
        public Builder() {}
        public Builder(GetPgClusterFromBackup defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.backupId = defaults.backupId;
    	      this.recoveryTargetTime = defaults.recoveryTargetTime;
        }

        @CustomType.Setter
        public Builder backupId(String backupId) {
            if (backupId == null) {
              throw new MissingRequiredPropertyException("GetPgClusterFromBackup", "backupId");
            }
            this.backupId = backupId;
            return this;
        }
        @CustomType.Setter
        public Builder recoveryTargetTime(String recoveryTargetTime) {
            if (recoveryTargetTime == null) {
              throw new MissingRequiredPropertyException("GetPgClusterFromBackup", "recoveryTargetTime");
            }
            this.recoveryTargetTime = recoveryTargetTime;
            return this;
        }
        public GetPgClusterFromBackup build() {
            final var _resultValue = new GetPgClusterFromBackup();
            _resultValue.backupId = backupId;
            _resultValue.recoveryTargetTime = recoveryTargetTime;
            return _resultValue;
        }
    }
}
