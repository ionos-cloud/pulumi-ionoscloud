// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.pulumi.ionoscloud.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.ionoscloud.inputs.GroupUserArgs;
import java.lang.Boolean;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GroupState extends com.pulumi.resources.ResourceArgs {

    public static final GroupState Empty = new GroupState();

    /**
     * [Boolean] The group will be allowed to access the activity log.
     * 
     */
    @Import(name="accessActivityLog")
    private @Nullable Output<Boolean> accessActivityLog;

    /**
     * @return [Boolean] The group will be allowed to access the activity log.
     * 
     */
    public Optional<Output<Boolean>> accessActivityLog() {
        return Optional.ofNullable(this.accessActivityLog);
    }

    /**
     * [Boolean]  The group will be allowed to access and manage certificates.
     * 
     */
    @Import(name="accessAndManageCertificates")
    private @Nullable Output<Boolean> accessAndManageCertificates;

    /**
     * @return [Boolean]  The group will be allowed to access and manage certificates.
     * 
     */
    public Optional<Output<Boolean>> accessAndManageCertificates() {
        return Optional.ofNullable(this.accessAndManageCertificates);
    }

    /**
     * [Boolean]  The group will be allowed to access and manage monitoring.
     * 
     */
    @Import(name="accessAndManageMonitoring")
    private @Nullable Output<Boolean> accessAndManageMonitoring;

    /**
     * @return [Boolean]  The group will be allowed to access and manage monitoring.
     * 
     */
    public Optional<Output<Boolean>> accessAndManageMonitoring() {
        return Optional.ofNullable(this.accessAndManageMonitoring);
    }

    /**
     * [Boolean] The group will be allowed to create backup unit privilege.
     * 
     */
    @Import(name="createBackupUnit")
    private @Nullable Output<Boolean> createBackupUnit;

    /**
     * @return [Boolean] The group will be allowed to create backup unit privilege.
     * 
     */
    public Optional<Output<Boolean>> createBackupUnit() {
        return Optional.ofNullable(this.createBackupUnit);
    }

    /**
     * [Boolean] The group will be allowed to create virtual data centers.
     * 
     */
    @Import(name="createDatacenter")
    private @Nullable Output<Boolean> createDatacenter;

    /**
     * @return [Boolean] The group will be allowed to create virtual data centers.
     * 
     */
    public Optional<Output<Boolean>> createDatacenter() {
        return Optional.ofNullable(this.createDatacenter);
    }

    /**
     * [Boolean]  The group will be allowed to create flow log.
     * 
     */
    @Import(name="createFlowLog")
    private @Nullable Output<Boolean> createFlowLog;

    /**
     * @return [Boolean]  The group will be allowed to create flow log.
     * 
     */
    public Optional<Output<Boolean>> createFlowLog() {
        return Optional.ofNullable(this.createFlowLog);
    }

    /**
     * [Boolean] The group will be allowed to create internet access privilege.
     * 
     */
    @Import(name="createInternetAccess")
    private @Nullable Output<Boolean> createInternetAccess;

    /**
     * @return [Boolean] The group will be allowed to create internet access privilege.
     * 
     */
    public Optional<Output<Boolean>> createInternetAccess() {
        return Optional.ofNullable(this.createInternetAccess);
    }

    /**
     * [Boolean]  The group will be allowed to create kubernetes cluster privilege.
     * 
     */
    @Import(name="createK8sCluster")
    private @Nullable Output<Boolean> createK8sCluster;

    /**
     * @return [Boolean]  The group will be allowed to create kubernetes cluster privilege.
     * 
     */
    public Optional<Output<Boolean>> createK8sCluster() {
        return Optional.ofNullable(this.createK8sCluster);
    }

    /**
     * [Boolean] The group will be allowed to create Cross Connects privilege.
     * 
     */
    @Import(name="createPcc")
    private @Nullable Output<Boolean> createPcc;

    /**
     * @return [Boolean] The group will be allowed to create Cross Connects privilege.
     * 
     */
    public Optional<Output<Boolean>> createPcc() {
        return Optional.ofNullable(this.createPcc);
    }

    /**
     * [Boolean] The group will be allowed to create snapshots.
     * 
     */
    @Import(name="createSnapshot")
    private @Nullable Output<Boolean> createSnapshot;

    /**
     * @return [Boolean] The group will be allowed to create snapshots.
     * 
     */
    public Optional<Output<Boolean>> createSnapshot() {
        return Optional.ofNullable(this.createSnapshot);
    }

    /**
     * [Boolean]  Privilege for a group to manage DBaaS related functionality.
     * 
     */
    @Import(name="manageDbaas")
    private @Nullable Output<Boolean> manageDbaas;

    /**
     * @return [Boolean]  Privilege for a group to manage DBaaS related functionality.
     * 
     */
    public Optional<Output<Boolean>> manageDbaas() {
        return Optional.ofNullable(this.manageDbaas);
    }

    /**
     * [string] A name for the group.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return [string] A name for the group.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * [Boolean] The group will be allowed to reserve IP addresses.
     * 
     */
    @Import(name="reserveIp")
    private @Nullable Output<Boolean> reserveIp;

    /**
     * @return [Boolean] The group will be allowed to reserve IP addresses.
     * 
     */
    public Optional<Output<Boolean>> reserveIp() {
        return Optional.ofNullable(this.reserveIp);
    }

    /**
     * [Boolean] The group will have S3 privilege.
     * 
     */
    @Import(name="s3Privilege")
    private @Nullable Output<Boolean> s3Privilege;

    /**
     * @return [Boolean] The group will have S3 privilege.
     * 
     */
    public Optional<Output<Boolean>> s3Privilege() {
        return Optional.ofNullable(this.s3Privilege);
    }

    /**
     * [string] The ID of the specific user to add to the group. Please use user_ids argument since this is **DEPRECATED**
     * 
     * @deprecated
     * Please use user_ids for adding users to the group, since user_id will be removed in the future
     * 
     */
    @Deprecated /* Please use user_ids for adding users to the group, since user_id will be removed in the future */
    @Import(name="userId")
    private @Nullable Output<String> userId;

    /**
     * @return [string] The ID of the specific user to add to the group. Please use user_ids argument since this is **DEPRECATED**
     * 
     * @deprecated
     * Please use user_ids for adding users to the group, since user_id will be removed in the future
     * 
     */
    @Deprecated /* Please use user_ids for adding users to the group, since user_id will be removed in the future */
    public Optional<Output<String>> userId() {
        return Optional.ofNullable(this.userId);
    }

    /**
     * [list] A list of users to add to the group.
     * 
     */
    @Import(name="userIds")
    private @Nullable Output<List<String>> userIds;

    /**
     * @return [list] A list of users to add to the group.
     * 
     */
    public Optional<Output<List<String>>> userIds() {
        return Optional.ofNullable(this.userIds);
    }

    /**
     * List of users - See the User section
     * 
     * **NOTE:** user_id/user_ids field cannot be used at the same time with group_ids field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     * 
     */
    @Import(name="users")
    private @Nullable Output<List<GroupUserArgs>> users;

    /**
     * @return List of users - See the User section
     * 
     * **NOTE:** user_id/user_ids field cannot be used at the same time with group_ids field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
     * 
     */
    public Optional<Output<List<GroupUserArgs>>> users() {
        return Optional.ofNullable(this.users);
    }

    private GroupState() {}

    private GroupState(GroupState $) {
        this.accessActivityLog = $.accessActivityLog;
        this.accessAndManageCertificates = $.accessAndManageCertificates;
        this.accessAndManageMonitoring = $.accessAndManageMonitoring;
        this.createBackupUnit = $.createBackupUnit;
        this.createDatacenter = $.createDatacenter;
        this.createFlowLog = $.createFlowLog;
        this.createInternetAccess = $.createInternetAccess;
        this.createK8sCluster = $.createK8sCluster;
        this.createPcc = $.createPcc;
        this.createSnapshot = $.createSnapshot;
        this.manageDbaas = $.manageDbaas;
        this.name = $.name;
        this.reserveIp = $.reserveIp;
        this.s3Privilege = $.s3Privilege;
        this.userId = $.userId;
        this.userIds = $.userIds;
        this.users = $.users;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GroupState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GroupState $;

        public Builder() {
            $ = new GroupState();
        }

        public Builder(GroupState defaults) {
            $ = new GroupState(Objects.requireNonNull(defaults));
        }

        /**
         * @param accessActivityLog [Boolean] The group will be allowed to access the activity log.
         * 
         * @return builder
         * 
         */
        public Builder accessActivityLog(@Nullable Output<Boolean> accessActivityLog) {
            $.accessActivityLog = accessActivityLog;
            return this;
        }

        /**
         * @param accessActivityLog [Boolean] The group will be allowed to access the activity log.
         * 
         * @return builder
         * 
         */
        public Builder accessActivityLog(Boolean accessActivityLog) {
            return accessActivityLog(Output.of(accessActivityLog));
        }

        /**
         * @param accessAndManageCertificates [Boolean]  The group will be allowed to access and manage certificates.
         * 
         * @return builder
         * 
         */
        public Builder accessAndManageCertificates(@Nullable Output<Boolean> accessAndManageCertificates) {
            $.accessAndManageCertificates = accessAndManageCertificates;
            return this;
        }

        /**
         * @param accessAndManageCertificates [Boolean]  The group will be allowed to access and manage certificates.
         * 
         * @return builder
         * 
         */
        public Builder accessAndManageCertificates(Boolean accessAndManageCertificates) {
            return accessAndManageCertificates(Output.of(accessAndManageCertificates));
        }

        /**
         * @param accessAndManageMonitoring [Boolean]  The group will be allowed to access and manage monitoring.
         * 
         * @return builder
         * 
         */
        public Builder accessAndManageMonitoring(@Nullable Output<Boolean> accessAndManageMonitoring) {
            $.accessAndManageMonitoring = accessAndManageMonitoring;
            return this;
        }

        /**
         * @param accessAndManageMonitoring [Boolean]  The group will be allowed to access and manage monitoring.
         * 
         * @return builder
         * 
         */
        public Builder accessAndManageMonitoring(Boolean accessAndManageMonitoring) {
            return accessAndManageMonitoring(Output.of(accessAndManageMonitoring));
        }

        /**
         * @param createBackupUnit [Boolean] The group will be allowed to create backup unit privilege.
         * 
         * @return builder
         * 
         */
        public Builder createBackupUnit(@Nullable Output<Boolean> createBackupUnit) {
            $.createBackupUnit = createBackupUnit;
            return this;
        }

        /**
         * @param createBackupUnit [Boolean] The group will be allowed to create backup unit privilege.
         * 
         * @return builder
         * 
         */
        public Builder createBackupUnit(Boolean createBackupUnit) {
            return createBackupUnit(Output.of(createBackupUnit));
        }

        /**
         * @param createDatacenter [Boolean] The group will be allowed to create virtual data centers.
         * 
         * @return builder
         * 
         */
        public Builder createDatacenter(@Nullable Output<Boolean> createDatacenter) {
            $.createDatacenter = createDatacenter;
            return this;
        }

        /**
         * @param createDatacenter [Boolean] The group will be allowed to create virtual data centers.
         * 
         * @return builder
         * 
         */
        public Builder createDatacenter(Boolean createDatacenter) {
            return createDatacenter(Output.of(createDatacenter));
        }

        /**
         * @param createFlowLog [Boolean]  The group will be allowed to create flow log.
         * 
         * @return builder
         * 
         */
        public Builder createFlowLog(@Nullable Output<Boolean> createFlowLog) {
            $.createFlowLog = createFlowLog;
            return this;
        }

        /**
         * @param createFlowLog [Boolean]  The group will be allowed to create flow log.
         * 
         * @return builder
         * 
         */
        public Builder createFlowLog(Boolean createFlowLog) {
            return createFlowLog(Output.of(createFlowLog));
        }

        /**
         * @param createInternetAccess [Boolean] The group will be allowed to create internet access privilege.
         * 
         * @return builder
         * 
         */
        public Builder createInternetAccess(@Nullable Output<Boolean> createInternetAccess) {
            $.createInternetAccess = createInternetAccess;
            return this;
        }

        /**
         * @param createInternetAccess [Boolean] The group will be allowed to create internet access privilege.
         * 
         * @return builder
         * 
         */
        public Builder createInternetAccess(Boolean createInternetAccess) {
            return createInternetAccess(Output.of(createInternetAccess));
        }

        /**
         * @param createK8sCluster [Boolean]  The group will be allowed to create kubernetes cluster privilege.
         * 
         * @return builder
         * 
         */
        public Builder createK8sCluster(@Nullable Output<Boolean> createK8sCluster) {
            $.createK8sCluster = createK8sCluster;
            return this;
        }

        /**
         * @param createK8sCluster [Boolean]  The group will be allowed to create kubernetes cluster privilege.
         * 
         * @return builder
         * 
         */
        public Builder createK8sCluster(Boolean createK8sCluster) {
            return createK8sCluster(Output.of(createK8sCluster));
        }

        /**
         * @param createPcc [Boolean] The group will be allowed to create Cross Connects privilege.
         * 
         * @return builder
         * 
         */
        public Builder createPcc(@Nullable Output<Boolean> createPcc) {
            $.createPcc = createPcc;
            return this;
        }

        /**
         * @param createPcc [Boolean] The group will be allowed to create Cross Connects privilege.
         * 
         * @return builder
         * 
         */
        public Builder createPcc(Boolean createPcc) {
            return createPcc(Output.of(createPcc));
        }

        /**
         * @param createSnapshot [Boolean] The group will be allowed to create snapshots.
         * 
         * @return builder
         * 
         */
        public Builder createSnapshot(@Nullable Output<Boolean> createSnapshot) {
            $.createSnapshot = createSnapshot;
            return this;
        }

        /**
         * @param createSnapshot [Boolean] The group will be allowed to create snapshots.
         * 
         * @return builder
         * 
         */
        public Builder createSnapshot(Boolean createSnapshot) {
            return createSnapshot(Output.of(createSnapshot));
        }

        /**
         * @param manageDbaas [Boolean]  Privilege for a group to manage DBaaS related functionality.
         * 
         * @return builder
         * 
         */
        public Builder manageDbaas(@Nullable Output<Boolean> manageDbaas) {
            $.manageDbaas = manageDbaas;
            return this;
        }

        /**
         * @param manageDbaas [Boolean]  Privilege for a group to manage DBaaS related functionality.
         * 
         * @return builder
         * 
         */
        public Builder manageDbaas(Boolean manageDbaas) {
            return manageDbaas(Output.of(manageDbaas));
        }

        /**
         * @param name [string] A name for the group.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name [string] A name for the group.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param reserveIp [Boolean] The group will be allowed to reserve IP addresses.
         * 
         * @return builder
         * 
         */
        public Builder reserveIp(@Nullable Output<Boolean> reserveIp) {
            $.reserveIp = reserveIp;
            return this;
        }

        /**
         * @param reserveIp [Boolean] The group will be allowed to reserve IP addresses.
         * 
         * @return builder
         * 
         */
        public Builder reserveIp(Boolean reserveIp) {
            return reserveIp(Output.of(reserveIp));
        }

        /**
         * @param s3Privilege [Boolean] The group will have S3 privilege.
         * 
         * @return builder
         * 
         */
        public Builder s3Privilege(@Nullable Output<Boolean> s3Privilege) {
            $.s3Privilege = s3Privilege;
            return this;
        }

        /**
         * @param s3Privilege [Boolean] The group will have S3 privilege.
         * 
         * @return builder
         * 
         */
        public Builder s3Privilege(Boolean s3Privilege) {
            return s3Privilege(Output.of(s3Privilege));
        }

        /**
         * @param userId [string] The ID of the specific user to add to the group. Please use user_ids argument since this is **DEPRECATED**
         * 
         * @return builder
         * 
         * @deprecated
         * Please use user_ids for adding users to the group, since user_id will be removed in the future
         * 
         */
        @Deprecated /* Please use user_ids for adding users to the group, since user_id will be removed in the future */
        public Builder userId(@Nullable Output<String> userId) {
            $.userId = userId;
            return this;
        }

        /**
         * @param userId [string] The ID of the specific user to add to the group. Please use user_ids argument since this is **DEPRECATED**
         * 
         * @return builder
         * 
         * @deprecated
         * Please use user_ids for adding users to the group, since user_id will be removed in the future
         * 
         */
        @Deprecated /* Please use user_ids for adding users to the group, since user_id will be removed in the future */
        public Builder userId(String userId) {
            return userId(Output.of(userId));
        }

        /**
         * @param userIds [list] A list of users to add to the group.
         * 
         * @return builder
         * 
         */
        public Builder userIds(@Nullable Output<List<String>> userIds) {
            $.userIds = userIds;
            return this;
        }

        /**
         * @param userIds [list] A list of users to add to the group.
         * 
         * @return builder
         * 
         */
        public Builder userIds(List<String> userIds) {
            return userIds(Output.of(userIds));
        }

        /**
         * @param userIds [list] A list of users to add to the group.
         * 
         * @return builder
         * 
         */
        public Builder userIds(String... userIds) {
            return userIds(List.of(userIds));
        }

        /**
         * @param users List of users - See the User section
         * 
         * **NOTE:** user_id/user_ids field cannot be used at the same time with group_ids field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
         * 
         * @return builder
         * 
         */
        public Builder users(@Nullable Output<List<GroupUserArgs>> users) {
            $.users = users;
            return this;
        }

        /**
         * @param users List of users - See the User section
         * 
         * **NOTE:** user_id/user_ids field cannot be used at the same time with group_ids field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
         * 
         * @return builder
         * 
         */
        public Builder users(List<GroupUserArgs> users) {
            return users(Output.of(users));
        }

        /**
         * @param users List of users - See the User section
         * 
         * **NOTE:** user_id/user_ids field cannot be used at the same time with group_ids field in user resource. Trying to add the same user to the same group in both ways in the same plan will result in a cyclic dependency error.
         * 
         * @return builder
         * 
         */
        public Builder users(GroupUserArgs... users) {
            return users(List.of(users));
        }

        public GroupState build() {
            return $;
        }
    }

}
