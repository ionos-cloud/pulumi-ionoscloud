// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute.Outputs
{

    [OutputType]
    public sealed class GetServersServerResult
    {
        public readonly string AvailabilityZone;
        public readonly string BootCdrom;
        public readonly string BootImage;
        public readonly string BootVolume;
        public readonly ImmutableArray<Outputs.GetServersServerCdromResult> Cdroms;
        public readonly int Cores;
        public readonly string CpuFamily;
        public readonly string Hostname;
        /// <summary>
        /// The unique ID of the server.
        /// </summary>
        public readonly string Id;
        public readonly ImmutableArray<Outputs.GetServersServerLabelResult> Labels;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.GetServersServerNicResult> Nics;
        public readonly int Ram;
        public readonly string? TemplateUuid;
        public readonly string Token;
        public readonly string Type;
        public readonly string VmState;
        public readonly ImmutableArray<Outputs.GetServersServerVolumeResult> Volumes;

        [OutputConstructor]
        private GetServersServerResult(
            string availabilityZone,

            string bootCdrom,

            string bootImage,

            string bootVolume,

            ImmutableArray<Outputs.GetServersServerCdromResult> cdroms,

            int cores,

            string cpuFamily,

            string hostname,

            string id,

            ImmutableArray<Outputs.GetServersServerLabelResult> labels,

            string? name,

            ImmutableArray<Outputs.GetServersServerNicResult> nics,

            int ram,

            string? templateUuid,

            string token,

            string type,

            string vmState,

            ImmutableArray<Outputs.GetServersServerVolumeResult> volumes)
        {
            AvailabilityZone = availabilityZone;
            BootCdrom = bootCdrom;
            BootImage = bootImage;
            BootVolume = bootVolume;
            Cdroms = cdroms;
            Cores = cores;
            CpuFamily = cpuFamily;
            Hostname = hostname;
            Id = id;
            Labels = labels;
            Name = name;
            Nics = nics;
            Ram = ram;
            TemplateUuid = templateUuid;
            Token = token;
            Type = type;
            VmState = vmState;
            Volumes = volumes;
        }
    }
}
