// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.dbaas.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetMongoUserRoleArgs extends com.pulumi.resources.ResourceArgs {

    public static final GetMongoUserRoleArgs Empty = new GetMongoUserRoleArgs();

    /**
     * [true] Database on which to apply the role.
     * 
     * **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
     * 
     */
    @Import(name="database", required=true)
    private Output<String> database;

    /**
     * @return [true] Database on which to apply the role.
     * 
     * **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
     * 
     */
    public Output<String> database() {
        return this.database;
    }

    /**
     * [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor and enableSharding.
     * 
     */
    @Import(name="role", required=true)
    private Output<String> role;

    /**
     * @return [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor and enableSharding.
     * 
     */
    public Output<String> role() {
        return this.role;
    }

    private GetMongoUserRoleArgs() {}

    private GetMongoUserRoleArgs(GetMongoUserRoleArgs $) {
        this.database = $.database;
        this.role = $.role;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetMongoUserRoleArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetMongoUserRoleArgs $;

        public Builder() {
            $ = new GetMongoUserRoleArgs();
        }

        public Builder(GetMongoUserRoleArgs defaults) {
            $ = new GetMongoUserRoleArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param database [true] Database on which to apply the role.
         * 
         * **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
         * 
         * @return builder
         * 
         */
        public Builder database(Output<String> database) {
            $.database = database;
            return this;
        }

        /**
         * @param database [true] Database on which to apply the role.
         * 
         * **NOTE:** MongoDb users do not support update at the moment. Changing any attribute will result in the user being re-created.
         * 
         * @return builder
         * 
         */
        public Builder database(String database) {
            return database(Output.of(database));
        }

        /**
         * @param role [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor and enableSharding.
         * 
         * @return builder
         * 
         */
        public Builder role(Output<String> role) {
            $.role = role;
            return this;
        }

        /**
         * @param role [true] Mongodb user role. Examples: read, readWrite, readAnyDatabase, readWriteAnyDatabase, dbAdmin, dbAdminAnyDatabase, clusterMonitor and enableSharding.
         * 
         * @return builder
         * 
         */
        public Builder role(String role) {
            return role(Output.of(role));
        }

        public GetMongoUserRoleArgs build() {
            if ($.database == null) {
                throw new MissingRequiredPropertyException("GetMongoUserRoleArgs", "database");
            }
            if ($.role == null) {
                throw new MissingRequiredPropertyException("GetMongoUserRoleArgs", "role");
            }
            return $;
        }
    }

}
