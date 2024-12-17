// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Compute
{
    public static class GetVCPUServer
    {
        /// <summary>
        /// The **VCPU Server data source** can be used to search for and return existing VCPU servers. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Task<GetVCPUServerResult> InvokeAsync(GetVCPUServerArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVCPUServerResult>("ionoscloud:compute/getVCPUServer:getVCPUServer", args ?? new GetVCPUServerArgs(), options.WithDefaults());

        /// <summary>
        /// The **VCPU Server data source** can be used to search for and return existing VCPU servers. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetVCPUServerResult> Invoke(GetVCPUServerInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVCPUServerResult>("ionoscloud:compute/getVCPUServer:getVCPUServer", args ?? new GetVCPUServerInvokeArgs(), options.WithDefaults());

        /// <summary>
        /// The **VCPU Server data source** can be used to search for and return existing VCPU servers. 
        /// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
        /// When this happens, please refine your search string so that it is specific enough to return only one result.
        /// 
        /// ## Example Usage
        /// </summary>
        public static Output<GetVCPUServerResult> Invoke(GetVCPUServerInvokeArgs args, InvokeOutputOptions options)
            => global::Pulumi.Deployment.Instance.Invoke<GetVCPUServerResult>("ionoscloud:compute/getVCPUServer:getVCPUServer", args ?? new GetVCPUServerInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVCPUServerArgs : global::Pulumi.InvokeArgs
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

        public GetVCPUServerArgs()
        {
        }
        public static new GetVCPUServerArgs Empty => new GetVCPUServerArgs();
    }

    public sealed class GetVCPUServerInvokeArgs : global::Pulumi.InvokeArgs
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

        public GetVCPUServerInvokeArgs()
        {
        }
        public static new GetVCPUServerInvokeArgs Empty => new GetVCPUServerInvokeArgs();
    }


    [OutputType]
    public sealed class GetVCPUServerResult
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
        public readonly ImmutableArray<Outputs.GetVCPUServerCdromResult> Cdroms;
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
        public readonly ImmutableArray<Outputs.GetVCPUServerLabelResult> Labels;
        /// <summary>
        /// Name of the firewall rule
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// list of
        /// </summary>
        public readonly ImmutableArray<Outputs.GetVCPUServerNicResult> Nics;
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
        public readonly ImmutableArray<Outputs.GetVCPUServerVolumeResult> Volumes;

        [OutputConstructor]
        private GetVCPUServerResult(
            string availabilityZone,

            string bootCdrom,

            string bootImage,

            string bootVolume,

            ImmutableArray<Outputs.GetVCPUServerCdromResult> cdroms,

            int cores,

            string cpuFamily,

            string datacenterId,

            string? id,

            ImmutableArray<Outputs.GetVCPUServerLabelResult> labels,

            string? name,

            ImmutableArray<Outputs.GetVCPUServerNicResult> nics,

            int ram,

            string token,

            string type,

            string vmState,

            ImmutableArray<Outputs.GetVCPUServerVolumeResult> volumes)
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
