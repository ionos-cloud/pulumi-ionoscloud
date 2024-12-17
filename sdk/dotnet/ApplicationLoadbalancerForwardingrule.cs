// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud
{
    /// <summary>
    /// Manages an **Application Load Balancer Forwarding Rule** on IonosCloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.IO;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ionoscloud = Pulumi.Ionoscloud;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleDatacenter = new Ionoscloud.Compute.Datacenter("exampleDatacenter", new()
    ///     {
    ///         Location = "us/las",
    ///         Description = "datacenter description",
    ///         SecAuthProtection = false,
    ///     });
    /// 
    ///     var example1 = new Ionoscloud.Compute.Lan("example1", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = true,
    ///     });
    /// 
    ///     var example2 = new Ionoscloud.Compute.Lan("example2", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         Public = true,
    ///     });
    /// 
    ///     var exampleApplicationLoadbalancer = new Ionoscloud.ApplicationLoadbalancer("exampleApplicationLoadbalancer", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         ListenerLan = example1.Id,
    ///         Ips = new[]
    ///         {
    ///             "10.12.118.224",
    ///         },
    ///         TargetLan = example2.Id,
    ///         LbPrivateIps = new[]
    ///         {
    ///             "10.13.72.225/24",
    ///         },
    ///     });
    /// 
    ///     //optionally you can add a certificate to the application load balancer
    ///     var cert = new Ionoscloud.Cert.Certificate("cert", new()
    ///     {
    ///         Certificate = File.ReadAllText("path_to_cert"),
    ///         CertificateChain = File.ReadAllText("path_to_cert_chain"),
    ///         PrivateKey = File.ReadAllText("path_to_private_key"),
    ///     });
    /// 
    ///     var exampleApplicationLoadbalancerForwardingrule = new Ionoscloud.ApplicationLoadbalancerForwardingrule("exampleApplicationLoadbalancerForwardingrule", new()
    ///     {
    ///         DatacenterId = exampleDatacenter.Id,
    ///         ApplicationLoadbalancerId = exampleApplicationLoadbalancer.Id,
    ///         Protocol = "HTTP",
    ///         ListenerIp = "10.12.118.224",
    ///         ListenerPort = 8080,
    ///         ClientTimeout = 1000,
    ///         HttpRules = new[]
    ///         {
    ///             new Ionoscloud.Inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs
    ///             {
    ///                 Name = "http_rule",
    ///                 Type = "REDIRECT",
    ///                 DropQuery = true,
    ///                 Location = "www.ionos.com",
    ///                 StatusCode = 301,
    ///                 Conditions = new[]
    ///                 {
    ///                     new Ionoscloud.Inputs.ApplicationLoadbalancerForwardingruleHttpRuleConditionArgs
    ///                     {
    ///                         Type = "HEADER",
    ///                         Condition = "EQUALS",
    ///                         Negate = true,
    ///                         Key = "key",
    ///                         Value = "10.12.120.224/24",
    ///                     },
    ///                 },
    ///             },
    ///             new Ionoscloud.Inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs
    ///             {
    ///                 Name = "http_rule_2",
    ///                 Type = "STATIC",
    ///                 DropQuery = false,
    ///                 StatusCode = 303,
    ///                 ResponseMessage = "Response",
    ///                 ContentType = "text/plain",
    ///                 Conditions = new[]
    ///                 {
    ///                     new Ionoscloud.Inputs.ApplicationLoadbalancerForwardingruleHttpRuleConditionArgs
    ///                     {
    ///                         Type = "QUERY",
    ///                         Condition = "MATCHES",
    ///                         Negate = false,
    ///                         Key = "key",
    ///                         Value = "10.12.120.224/24",
    ///                     },
    ///                 },
    ///             },
    ///         },
    ///         ServerCertificates = new[]
    ///         {
    ///             cert.Id,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Resource Application Load Balancer Forwarding Rule can be imported using the `resource id`, `alb id` and `datacenter id`, e.g.
    /// 
    /// ```sh
    /// $ pulumi import ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule my_application_loadbalancer_forwardingrule {datacenter uuid}/{application_loadbalancer uuid}/{application_loadbalancer_forwardingrule uuid}
    /// ```
    /// </summary>
    [IonoscloudResourceType("ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule")]
    public partial class ApplicationLoadbalancerForwardingrule : global::Pulumi.CustomResource
    {
        /// <summary>
        /// [string] The ID of Application Load Balancer.
        /// </summary>
        [Output("applicationLoadbalancerId")]
        public Output<string> ApplicationLoadbalancerId { get; private set; } = null!;

        /// <summary>
        /// [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
        /// </summary>
        [Output("clientTimeout")]
        public Output<int> ClientTimeout { get; private set; } = null!;

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Output("datacenterId")]
        public Output<string> DatacenterId { get; private set; } = null!;

        /// <summary>
        /// [list] Array of items in that collection
        /// </summary>
        [Output("httpRules")]
        public Output<ImmutableArray<Outputs.ApplicationLoadbalancerForwardingruleHttpRule>> HttpRules { get; private set; } = null!;

        /// <summary>
        /// [string] Listening (inbound) IP.
        /// </summary>
        [Output("listenerIp")]
        public Output<string> ListenerIp { get; private set; } = null!;

        /// <summary>
        /// [int] Listening (inbound) port number; valid range is 1 to 65535.
        /// </summary>
        [Output("listenerPort")]
        public Output<int> ListenerPort { get; private set; } = null!;

        /// <summary>
        /// [string] The name of the Application Load Balancer forwarding rule.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// [list] Array of certificate ids. You can create certificates with the certificate resource.
        /// </summary>
        [Output("serverCertificates")]
        public Output<ImmutableArray<string>> ServerCertificates { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationLoadbalancerForwardingrule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationLoadbalancerForwardingrule(string name, ApplicationLoadbalancerForwardingruleArgs args, CustomResourceOptions? options = null)
            : base("ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule", name, args ?? new ApplicationLoadbalancerForwardingruleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationLoadbalancerForwardingrule(string name, Input<string> id, ApplicationLoadbalancerForwardingruleState? state = null, CustomResourceOptions? options = null)
            : base("ionoscloud:index/applicationLoadbalancerForwardingrule:ApplicationLoadbalancerForwardingrule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationLoadbalancerForwardingrule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationLoadbalancerForwardingrule Get(string name, Input<string> id, ApplicationLoadbalancerForwardingruleState? state = null, CustomResourceOptions? options = null)
        {
            return new ApplicationLoadbalancerForwardingrule(name, id, state, options);
        }
    }

    public sealed class ApplicationLoadbalancerForwardingruleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of Application Load Balancer.
        /// </summary>
        [Input("applicationLoadbalancerId", required: true)]
        public Input<string> ApplicationLoadbalancerId { get; set; } = null!;

        /// <summary>
        /// [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
        /// </summary>
        [Input("clientTimeout")]
        public Input<int>? ClientTimeout { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId", required: true)]
        public Input<string> DatacenterId { get; set; } = null!;

        [Input("httpRules")]
        private InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs>? _httpRules;

        /// <summary>
        /// [list] Array of items in that collection
        /// </summary>
        public InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs> HttpRules
        {
            get => _httpRules ?? (_httpRules = new InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleArgs>());
            set => _httpRules = value;
        }

        /// <summary>
        /// [string] Listening (inbound) IP.
        /// </summary>
        [Input("listenerIp", required: true)]
        public Input<string> ListenerIp { get; set; } = null!;

        /// <summary>
        /// [int] Listening (inbound) port number; valid range is 1 to 65535.
        /// </summary>
        [Input("listenerPort", required: true)]
        public Input<int> ListenerPort { get; set; } = null!;

        /// <summary>
        /// [string] The name of the Application Load Balancer forwarding rule.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("serverCertificates")]
        private InputList<string>? _serverCertificates;

        /// <summary>
        /// [list] Array of certificate ids. You can create certificates with the certificate resource.
        /// </summary>
        public InputList<string> ServerCertificates
        {
            get => _serverCertificates ?? (_serverCertificates = new InputList<string>());
            set => _serverCertificates = value;
        }

        public ApplicationLoadbalancerForwardingruleArgs()
        {
        }
        public static new ApplicationLoadbalancerForwardingruleArgs Empty => new ApplicationLoadbalancerForwardingruleArgs();
    }

    public sealed class ApplicationLoadbalancerForwardingruleState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// [string] The ID of Application Load Balancer.
        /// </summary>
        [Input("applicationLoadbalancerId")]
        public Input<string>? ApplicationLoadbalancerId { get; set; }

        /// <summary>
        /// [int] The maximum time in milliseconds to wait for the client to acknowledge or send data; default is 50,000 (50 seconds).
        /// </summary>
        [Input("clientTimeout")]
        public Input<int>? ClientTimeout { get; set; }

        /// <summary>
        /// [string] The ID of a Virtual Data Center.
        /// </summary>
        [Input("datacenterId")]
        public Input<string>? DatacenterId { get; set; }

        [Input("httpRules")]
        private InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleGetArgs>? _httpRules;

        /// <summary>
        /// [list] Array of items in that collection
        /// </summary>
        public InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleGetArgs> HttpRules
        {
            get => _httpRules ?? (_httpRules = new InputList<Inputs.ApplicationLoadbalancerForwardingruleHttpRuleGetArgs>());
            set => _httpRules = value;
        }

        /// <summary>
        /// [string] Listening (inbound) IP.
        /// </summary>
        [Input("listenerIp")]
        public Input<string>? ListenerIp { get; set; }

        /// <summary>
        /// [int] Listening (inbound) port number; valid range is 1 to 65535.
        /// </summary>
        [Input("listenerPort")]
        public Input<int>? ListenerPort { get; set; }

        /// <summary>
        /// [string] The name of the Application Load Balancer forwarding rule.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// [string] Balancing protocol.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("serverCertificates")]
        private InputList<string>? _serverCertificates;

        /// <summary>
        /// [list] Array of certificate ids. You can create certificates with the certificate resource.
        /// </summary>
        public InputList<string> ServerCertificates
        {
            get => _serverCertificates ?? (_serverCertificates = new InputList<string>());
            set => _serverCertificates = value;
        }

        public ApplicationLoadbalancerForwardingruleState()
        {
        }
        public static new ApplicationLoadbalancerForwardingruleState Empty => new ApplicationLoadbalancerForwardingruleState();
    }
}
