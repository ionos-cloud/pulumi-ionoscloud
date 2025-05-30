// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetPSQLDatabasesDatabase {
    /**
     * @return [string] The ID of the database.
     * 
     */
    private String id;
    /**
     * @return [string] The name of the database.
     * 
     */
    private String name;
    /**
     * @return [string] Filter using a specific owner.
     * 
     */
    private String owner;

    private GetPSQLDatabasesDatabase() {}
    /**
     * @return [string] The ID of the database.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return [string] The name of the database.
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return [string] Filter using a specific owner.
     * 
     */
    public String owner() {
        return this.owner;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetPSQLDatabasesDatabase defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String id;
        private String name;
        private String owner;
        public Builder() {}
        public Builder(GetPSQLDatabasesDatabase defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.owner = defaults.owner;
        }

        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetPSQLDatabasesDatabase", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetPSQLDatabasesDatabase", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder owner(String owner) {
            if (owner == null) {
              throw new MissingRequiredPropertyException("GetPSQLDatabasesDatabase", "owner");
            }
            this.owner = owner;
            return this;
        }
        public GetPSQLDatabasesDatabase build() {
            final var _resultValue = new GetPSQLDatabasesDatabase();
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.owner = owner;
            return _resultValue;
        }
    }
}
