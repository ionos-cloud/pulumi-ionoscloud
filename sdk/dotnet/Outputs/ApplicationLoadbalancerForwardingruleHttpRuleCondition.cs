// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ionoscloud.Outputs
{

    [OutputType]
    public sealed class ApplicationLoadbalancerForwardingruleHttpRuleCondition
    {
        /// <summary>
        /// [string] Matching rule for the HTTP rule condition attribute; mandatory for HEADER, PATH, QUERY, METHOD, HOST, and COOKIE types; must be null when type is SOURCE_IP.
        /// </summary>
        public readonly string? Condition;
        /// <summary>
        /// [string] Must be null when type is PATH, METHOD, HOST, or SOURCE_IP. Key can only be set when type is COOKIES, HEADER, or QUERY.
        /// </summary>
        public readonly string? Key;
        /// <summary>
        /// [bool] Specifies whether the condition is negated or not; the default is False.
        /// </summary>
        public readonly bool? Negate;
        /// <summary>
        /// [string] Type of the Http Rule condition.
        /// </summary>
        public readonly string Type;
        /// <summary>
        /// [string] Mandatory for conditions CONTAINS, EQUALS, MATCHES, STARTS_WITH, ENDS_WITH; must be null when condition is EXISTS; should be a valid CIDR if provided and if type is SOURCE_IP.
        /// </summary>
        public readonly string? Value;

        [OutputConstructor]
        private ApplicationLoadbalancerForwardingruleHttpRuleCondition(
            string? condition,

            string? key,

            bool? negate,

            string type,

            string? value)
        {
            Condition = condition;
            Key = key;
            Negate = negate;
            Type = type;
            Value = value;
        }
    }
}
