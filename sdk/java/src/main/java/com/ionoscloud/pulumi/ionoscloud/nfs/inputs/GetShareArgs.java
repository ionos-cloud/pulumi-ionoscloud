// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ionoscloud.pulumi.ionoscloud.nfs.inputs;

import com.ionoscloud.pulumi.ionoscloud.nfs.inputs.GetShareClientGroupArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class GetShareArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetShareArgs Empty = new GetShareArgs();

    /**
     * The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
     * 
     */
    @Import(name="clientGroups")
    private @Nullable Output<List<GetShareClientGroupArgs>> clientGroups;

    /**
     * @return The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
     * 
     */
    public Optional<Output<List<GetShareClientGroupArgs>>> clientGroups() {
        return Optional.ofNullable(this.clientGroups);
    }

    /**
     * The ID of the Network File Storage cluster.
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return The ID of the Network File Storage cluster.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    @Import(name="gid")
    private @Nullable Output<Integer> gid;

    /**
     * @return The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    public Optional<Output<Integer>> gid() {
        return Optional.ofNullable(this.gid);
    }

    /**
     * ID of the Network File Storage share.
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of the Network File Storage share.
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * The location where the Network File Storage share is located.
     * 
     */
    @Import(name="location")
    private @Nullable Output<String> location;

    /**
     * @return The location where the Network File Storage share is located.
     * 
     */
    public Optional<Output<String>> location() {
        return Optional.ofNullable(this.location);
    }

    /**
     * Name of the Network File Storage share.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the Network File Storage share.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     * 
     */
    @Import(name="partialMatch")
    private @Nullable Output<Boolean> partialMatch;

    /**
     * @return Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
     * 
     */
    public Optional<Output<Boolean>> partialMatch() {
        return Optional.ofNullable(this.partialMatch);
    }

    /**
     * The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
     * 
     */
    @Import(name="quota")
    private @Nullable Output<Integer> quota;

    /**
     * @return The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
     * 
     */
    public Optional<Output<Integer>> quota() {
        return Optional.ofNullable(this.quota);
    }

    /**
     * The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    @Import(name="uid")
    private @Nullable Output<Integer> uid;

    /**
     * @return The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
     * 
     */
    public Optional<Output<Integer>> uid() {
        return Optional.ofNullable(this.uid);
    }

    private GetShareArgs() {}

    private GetShareArgs(GetShareArgs $) {
        this.clientGroups = $.clientGroups;
        this.clusterId = $.clusterId;
        this.gid = $.gid;
        this.id = $.id;
        this.location = $.location;
        this.name = $.name;
        this.partialMatch = $.partialMatch;
        this.quota = $.quota;
        this.uid = $.uid;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetShareArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetShareArgs $;

        public Builder() {
            $ = new GetShareArgs();
        }

        public Builder(GetShareArgs defaults) {
            $ = new GetShareArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clientGroups The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
         * 
         * @return builder
         * 
         */
        public Builder clientGroups(@Nullable Output<List<GetShareClientGroupArgs>> clientGroups) {
            $.clientGroups = clientGroups;
            return this;
        }

        /**
         * @param clientGroups The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
         * 
         * @return builder
         * 
         */
        public Builder clientGroups(List<GetShareClientGroupArgs> clientGroups) {
            return clientGroups(Output.of(clientGroups));
        }

        /**
         * @param clientGroups The groups of clients are the systems connecting to the Network File Storage cluster. Each client group supports the following:
         * 
         * @return builder
         * 
         */
        public Builder clientGroups(GetShareClientGroupArgs... clientGroups) {
            return clientGroups(List.of(clientGroups));
        }

        /**
         * @param clusterId The ID of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId The ID of the Network File Storage cluster.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param gid The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
         * 
         * @return builder
         * 
         */
        public Builder gid(@Nullable Output<Integer> gid) {
            $.gid = gid;
            return this;
        }

        /**
         * @param gid The group ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
         * 
         * @return builder
         * 
         */
        public Builder gid(Integer gid) {
            return gid(Output.of(gid));
        }

        /**
         * @param id ID of the Network File Storage share.
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of the Network File Storage share.
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param location The location where the Network File Storage share is located.
         * 
         * @return builder
         * 
         */
        public Builder location(@Nullable Output<String> location) {
            $.location = location;
            return this;
        }

        /**
         * @param location The location where the Network File Storage share is located.
         * 
         * @return builder
         * 
         */
        public Builder location(String location) {
            return location(Output.of(location));
        }

        /**
         * @param name Name of the Network File Storage share.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the Network File Storage share.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(@Nullable Output<Boolean> partialMatch) {
            $.partialMatch = partialMatch;
            return this;
        }

        /**
         * @param partialMatch Whether partial matching is allowed or not when using the name filter. Defaults to `false`.
         * 
         * @return builder
         * 
         */
        public Builder partialMatch(Boolean partialMatch) {
            return partialMatch(Output.of(partialMatch));
        }

        /**
         * @param quota The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
         * 
         * @return builder
         * 
         */
        public Builder quota(@Nullable Output<Integer> quota) {
            $.quota = quota;
            return this;
        }

        /**
         * @param quota The quota in MiB for the export. The quota can restrict the amount of data that can be stored within the export. The quota can be disabled using `0`.
         * 
         * @return builder
         * 
         */
        public Builder quota(Integer quota) {
            return quota(Output.of(quota));
        }

        /**
         * @param uid The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
         * 
         * @return builder
         * 
         */
        public Builder uid(@Nullable Output<Integer> uid) {
            $.uid = uid;
            return this;
        }

        /**
         * @param uid The user ID that will own the exported directory. If not set, **anonymous** (`512`) will be used.
         * 
         * @return builder
         * 
         */
        public Builder uid(Integer uid) {
            return uid(Output.of(uid));
        }

        public GetShareArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("GetShareArgs", "clusterId");
            }
            return $;
        }
    }

}
