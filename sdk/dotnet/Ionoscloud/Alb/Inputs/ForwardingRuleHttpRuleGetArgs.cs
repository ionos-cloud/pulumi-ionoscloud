// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Ionoscloud.Pulumi.Ionoscloud.Alb.Inputs
{

    public sealed class ForwardingRuleHttpRuleGetArgs : global::Pulumi.ResourceArgs
    {
        [Input("conditions")]
        private InputList<Inputs.ForwardingRuleHttpRuleConditionGetArgs>? _conditions;

        /// <summary>
        /// [list] - An array of items in the collection.The action is only performed if each and every condition is met; if no conditions are set, the rule will always be performed.
        /// </summary>
        public InputList<Inputs.ForwardingRuleHttpRuleConditionGetArgs> Conditions
        {
            get => _conditions ?? (_conditions = new InputList<Inputs.ForwardingRuleHttpRuleConditionGetArgs>());
            set => _conditions = value;
        }

        /// <summary>
        /// [string] Valid only for STATIC actions.
        /// </summary>
        [Input("contentType")]
        public Input<string>? ContentType { get; set; }

        /// <summary>
        /// [bool] Default is false; valid only for REDIRECT actions.
        /// </summary>
        [Input("dropQuery")]
        public Input<bool>? DropQuery { get; set; }

        /// <summary>
        /// [string] The location for redirecting; mandatory and valid only for REDIRECT actions.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// [string] The unique name of the Application Load Balancer HTTP rule.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// [string] The response message of the request; mandatory for STATIC action.
        /// </summary>
        [Input("responseMessage")]
        public Input<string>? ResponseMessage { get; set; }

        /// <summary>
        /// [int] Valid only for REDIRECT and STATIC actions. For REDIRECT actions, default is 301 and possible values are 301, 302, 303, 307, and 308. For STATIC actions, default is 503 and valid range is 200 to 599.
        /// </summary>
        [Input("statusCode")]
        public Input<int>? StatusCode { get; set; }

        /// <summary>
        /// [string] The UUID of the target group; mandatory for FORWARD action.
        /// </summary>
        [Input("targetGroup")]
        public Input<string>? TargetGroup { get; set; }

        /// <summary>
        /// [string] Type of the Http Rule.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ForwardingRuleHttpRuleGetArgs()
        {
        }
        public static new ForwardingRuleHttpRuleGetArgs Empty => new ForwardingRuleHttpRuleGetArgs();
    }
}
