// *** WARNING: this file was generated by pulumi. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    public static class GetVcpuServer
    {
        /// <summary>
        /// The **VCPU Server data source** can be used to search for and return existing VCPU servers. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetVcpuServerResult> InvokeAsync(GetVcpuServerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVcpuServerResult>("ionoscloud:index/getVcpuServer:getVcpuServer", args ?? new GetVcpuServerArgs(), options.WithDefaults());

        /// <summary>
        /// The **VCPU Server data source** can be used to search for and return existing VCPU servers. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetVcpuServerResult> Invoke(GetVcpuServerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVcpuServerResult>("ionoscloud:index/getVcpuServer:getVcpuServer", args ?? new GetVcpuServerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVcpuServerArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public string DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// Name of an existing server that you want to search for.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        public GetVcpuServerArgs()
        {
        }
        public static new GetVcpuServerArgs Empty => new GetVcpuServerArgs();
    }

    public sealed class GetVcpuServerInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Datacenter's UUID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// ID of the server you want to search for.
        /// 
        /// `datacenter_id` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Name of an existing server that you want to search for.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public GetVcpuServerInvokeArgs()
        {
        }
        public static new GetVcpuServerInvokeArgs Empty => new GetVcpuServerInvokeArgs();
    }


    [OutputType]
    public sealed class GetVcpuServerResult
    {
        /// <summary>
        /// The availability zone in which the volume should exist
        /// </summary>
        public readonly string AvailabilityZone;
        public readonly string BootCdrom;
        public readonly string BootImage;
        public readonly string BootVolume;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVcpuServerCdromResult> Cdroms;
        /// <summary>
        /// The total number of cores for the server
        /// </summary>
        public readonly int Cores;
        /// <summary>
        /// CPU architecture on which server gets provisioned; not all CPU architectures are available in all datacenter regions; available CPU architectures can be retrieved from the datacenter resource.
        /// </summary>
        public readonly string CpuFamily;
        /// <summary>
        /// The id of the datacenter
        /// </summary>
        public readonly string DatacenterId;
        /// <summary>
        /// The Id of the label
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVcpuServerLabelResult> Labels;
        /// <summary>
        /// Name of the firewall rule
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVcpuServerNicResult> Nics;
        /// <summary>
        /// The amount of memory for the server in MB
        /// </summary>
        public readonly int Ram;
        public readonly string Token;
        /// <summary>
        /// The type of firewall rule
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// Status of the virtual Machine
        /// </summary>
        public readonly string VmState;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVcpuServerVolumeResult> Volumes;

        [OutputConstructor]
        private GetVcpuServerResult(
            string availabilityZone,

            string bootCdrom,

            string bootImage,

            string bootVolume,

            ImmutableArray<Outputs.GetVcpuServerCdromResult> cdroms,

            int cores,

            string cpuFamily,

            string datacenterId,

            string? id,

            ImmutableArray<Outputs.GetVcpuServerLabelResult> labels,

            string? name,

            ImmutableArray<Outputs.GetVcpuServerNicResult> nics,

            int ram,

            string token,

            string type,

            string vmState,

            ImmutableArray<Outputs.GetVcpuServerVolumeResult> volumes)
        {
            AvailabilityZone = availabilityZone;
            BootCdrom = bootCdrom;
            BootImage = bootImage;
            BootVolume = bootVolume;
            Cdroms = cdroms;
            Cores = cores;
            CpuFamily = cpuFamily;
            DatacenterId = datacenterId;
            Id = id;
            Labels = labels;
            Name = name;
            Nics = nics;
            Ram = ram;
            Token = token;
            Type = type;
            VmState = vmState;
            Volumes = volumes;
        }
    }
}
