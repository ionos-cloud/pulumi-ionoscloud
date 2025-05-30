// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Compute
{
    /// <summary>
    /// Manages a set of **Firewall Rules** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Ionoscloud.Pulumi.Ionoscloud;
    /// using Random = Pulumi.Random;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var example = new Ionoscloud.Compute.Datacenter("example", new()
    ///     {
    ///         Name = "Datacenter Example",
    ///         Location = "us/las",
    ///         Description = "Datacenter Description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var exampleIPBlock = new Ionoscloud.Compute.IPBlock("example", new()
    ///     {
    ///         Location = example.Location,
    ///         Size = 2,
    ///         Name = "IP Block Example",
    ///     });
    /// 
    ///     var serverImagePassword = new Random.Index.Password("server_image_password", new()
    ///     {
    ///         Length = 16,
    ///         Special = false,
    ///     });
    /// 
    ///     var exampleServer = new Ionoscloud.Compute.Server("example", new()
    ///     {
    ///         Name = "Server Example",
    ///         DatacenterId = example.Id,
    ///         Cores = 1,
    ///         Ram = 1024,
    ///         AvailabilityZone = "ZONE_1",
    ///         CpuFamily = "INTEL_XEON",
    ///         ImageName = "Ubuntu-20.04",
    ///         ImagePassword = serverImagePassword.Result,
    ///         Volume = new Ionoscloud.Compute.Inputs.ServerVolumeArgs
    ///         {
    ///             Name = "system",
    ///             Size = 14,
    ///             DiskType = "SSD",
    ///         },
    ///         Nic = new Ionoscloud.Compute.Inputs.ServerNicArgs
    ///         {
    ///             Lan = 1,
    ///             Dhcp = true,
    ///             FirewallActive = true,
    ///         },
    ///     });
    /// 
    ///     var exampleNic = new Ionoscloud.Compute.Nic("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         ServerId = exampleServer.Id,
    ///         Lan = 2,
    ///         Dhcp = true,
    ///         FirewallActive = true,
    ///         Name = "Nic Example",
    ///     });
    /// 
    ///     var exampleFirewall = new Ionoscloud.Compute.Firewall("example", new()
    ///     {
    ///         DatacenterId = example.Id,
    ///         ServerId = exampleServer.Id,
    ///         NicId = exampleNic.Id,
    ///         Protocol = "ICMP",
    ///         Name = "Firewall Example",
    ///         SourceMac = "00:0a:95:9d:68:16",
    ///         SourceIp = exampleIPBlock.Ips.Apply(ips =&gt; ips[0]),
    ///         TargetIp = exampleIPBlock.Ips.Apply(ips =&gt; ips[1]),
    ///         IcmpType = "1",
    ///         IcmpCode = "8",
    ///         Type = "INGRESS",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Firewall can be imported using the `resource id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:compute/firewall:Firewall myfwruledatacenter uuid/server uuid/nic uuid/firewall uuid
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:compute/firewall:Firewall")]
    public partial class Firewall : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The Virtual Data Center ID.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        /// </summary>
        [Output("icmpCode")]
        public Output<string?> IcmpCode { get; private set; } = null!;

        /// <summary>
        /// [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        /// </summary>
        [Output("icmpType")]
        public Output<string?> IcmpType { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the firewall rule.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] The NIC ID.
        /// </summary>
        [Output("nicId")]
        public Output<string> NicId { get; private set; } = null!;

        /// <summary>
        /// [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Output("portRangeEnd")]
        public Output<int?> PortRangeEnd { get; private set; } = null!;

        /// <summary>
        /// [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Output("portRangeStart")]
        public Output<int?> PortRangeStart { get; private set; } = null!;

        /// <summary>
        /// [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// [string] The Server ID.
        /// </summary>
        [Output("serverId")]
        public Output<string> ServerId { get; private set; } = null!;

        /// <summary>
        /// [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        /// </summary>
        [Output("sourceIp")]
        public Output<string> SourceIp { get; private set; } = null!;

        /// <summary>
        /// [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        /// </summary>
        [Output("sourceMac")]
        public Output<string?> SourceMac { get; private set; } = null!;

        /// <summary>
        /// [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        /// </summary>
        [Output("targetIp")]
        public Output<string> TargetIp { get; private set; } = null!;

        /// <summary>
        /// [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a Firewall resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Firewall(string name, FirewallArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/firewall:Firewall", name, args ?? new FirewallArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Firewall(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:compute/firewall:Firewall", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Firewall resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Firewall Get(string name, Input<string> id, FirewallState? state = null, CustomResourceOptions? options = null)
        {
            return new Firewall(name, id, state, options);
        }
    }

    public sealed class FirewallArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The Virtual Data Center ID.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        /// <summary>
        /// [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        /// </summary>
        [Input("icmpCode")]
        public Input<string>? IcmpCode { get; set; }

        /// <summary>
        /// [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        /// </summary>
        [Input("icmpType")]
        public Input<string>? IcmpType { get; set; }

        /// <summary>
        /// [string] The name of the firewall rule.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The NIC ID.
        /// </summary>
        [Input("nicId", required: true)]
        public Input<string> NicId { get; set; } = null!;

        /// <summary>
        /// [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeEnd")]
        public Input<int>? PortRangeEnd { get; set; }

        /// <summary>
        /// [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeStart")]
        public Input<int>? PortRangeStart { get; set; }

        /// <summary>
        /// [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// [string] The Server ID.
        /// </summary>
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        /// <summary>
        /// [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        /// </summary>
        [Input("sourceIp")]
        public Input<string>? SourceIp { get; set; }

        /// <summary>
        /// [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        /// </summary>
        [Input("sourceMac")]
        public Input<string>? SourceMac { get; set; }

        /// <summary>
        /// [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        /// </summary>
        [Input("targetIp")]
        public Input<string>? TargetIp { get; set; }

        /// <summary>
        /// [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public FirewallArgs()
        {
        }
        public static new FirewallArgs Empty => new FirewallArgs();
    }

    public sealed class FirewallState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The Virtual Data Center ID.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        /// <summary>
        /// [int] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen.
        /// </summary>
        [Input("icmpCode")]
        public Input<string>? IcmpCode { get; set; }

        /// <summary>
        /// [string] Defines the allowed code (from 0 to 254) if protocol ICMP is chosen. Value null allows all codes.
        /// </summary>
        [Input("icmpType")]
        public Input<string>? IcmpType { get; set; }

        /// <summary>
        /// [string] The name of the firewall rule.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] The NIC ID.
        /// </summary>
        [Input("nicId")]
        public Input<string>? NicId { get; set; }

        /// <summary>
        /// [int] Defines the end range of the allowed port (from 1 to 65534) if the protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeEnd")]
        public Input<int>? PortRangeEnd { get; set; }

        /// <summary>
        /// [int] Defines the start range of the allowed port (from 1 to 65534) if protocol TCP or UDP is chosen. Leave portRangeStart and portRangeEnd null to allow all ports.
        /// </summary>
        [Input("portRangeStart")]
        public Input<int>? PortRangeStart { get; set; }

        /// <summary>
        /// [string] The protocol for the rule: TCP, UDP, ICMP, ANY. Property cannot be modified after creation (disallowed in update requests).
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// [string] The Server ID.
        /// </summary>
        [Input("serverId")]
        public Input<string>? ServerId { get; set; }

        /// <summary>
        /// [string] Only traffic originating from the respective IPv4 address is allowed. Value null allows all source IPs.
        /// </summary>
        [Input("sourceIp")]
        public Input<string>? SourceIp { get; set; }

        /// <summary>
        /// [string] Only traffic originating from the respective MAC address is allowed. Valid format: aa:bb:cc:dd:ee:ff. Value null allows all source MAC address. Valid format: aa:bb:cc:dd:ee:ff.
        /// </summary>
        [Input("sourceMac")]
        public Input<string>? SourceMac { get; set; }

        /// <summary>
        /// [string] In case the target NIC has multiple IP addresses, only traffic directed to the respective IP address of the NIC is allowed. Value null allows all target IPs.
        /// </summary>
        [Input("targetIp")]
        public Input<string>? TargetIp { get; set; }

        /// <summary>
        /// [string] The type of firewall rule. If is not specified, it will take the default value INGRESS.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public FirewallState()
        {
        }
        public static new FirewallState Empty => new FirewallState();
    }
}
