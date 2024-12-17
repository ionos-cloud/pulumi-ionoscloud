// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ionoscloud

import (
	"context"
	"reflect"

	"github.com/ionos-cloud/pulumi-ionoscloud/sdk/go/ionoscloud/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The **NAT Gateway Rule data source** can be used to search for and return existing NAT Gateway Rules.
// If a single match is found, it will be returned. If your search results in multiple matches, an error will be returned.
// When this happens, please refine your search string so that it is specific enough to return only one result.
//
// ## Example Usage
func GetNatgatewayRule(ctx *pulumi.Context, args *GetNatgatewayRuleArgs, opts ...pulumi.InvokeOption) (*GetNatgatewayRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetNatgatewayRuleResult
	err := ctx.Invoke("ionoscloud:index/getNatgatewayRule:getNatgatewayRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNatgatewayRule.
type GetNatgatewayRuleArgs struct {
	// Datacenter's UUID.
	DatacenterId string `pulumi:"datacenterId"`
	// ID of the NAT gateway rule you want to search for.
	//
	// Both `datacenterId` and `natgatewayId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id *string `pulumi:"id"`
	// Name of an existing NAT gateway rule that you want to search for.
	Name *string `pulumi:"name"`
	// Nat Gateway's UUID.
	NatgatewayId string `pulumi:"natgatewayId"`
}

// A collection of values returned by getNatgatewayRule.
type GetNatgatewayRuleResult struct {
	DatacenterId string `pulumi:"datacenterId"`
	// Id of the NAT gateway rule
	Id *string `pulumi:"id"`
	// Name of the NAT gateway rule
	Name         *string `pulumi:"name"`
	NatgatewayId string  `pulumi:"natgatewayId"`
	// Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
	Protocol string `pulumi:"protocol"`
	// Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource
	PublicIp string `pulumi:"publicIp"`
	// Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
	SourceSubnet string `pulumi:"sourceSubnet"`
	// Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port
	TargetPortRanges []GetNatgatewayRuleTargetPortRange `pulumi:"targetPortRanges"`
	// Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
	TargetSubnet string `pulumi:"targetSubnet"`
	// ype of the NAT gateway rule.
	Type string `pulumi:"type"`
}

func GetNatgatewayRuleOutput(ctx *pulumi.Context, args GetNatgatewayRuleOutputArgs, opts ...pulumi.InvokeOption) GetNatgatewayRuleResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetNatgatewayRuleResultOutput, error) {
			args := v.(GetNatgatewayRuleArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ionoscloud:index/getNatgatewayRule:getNatgatewayRule", args, GetNatgatewayRuleResultOutput{}, options).(GetNatgatewayRuleResultOutput), nil
		}).(GetNatgatewayRuleResultOutput)
}

// A collection of arguments for invoking getNatgatewayRule.
type GetNatgatewayRuleOutputArgs struct {
	// Datacenter's UUID.
	DatacenterId pulumi.StringInput `pulumi:"datacenterId"`
	// ID of the NAT gateway rule you want to search for.
	//
	// Both `datacenterId` and `natgatewayId` and either `name` or `id` must be provided. If none, or both of `name` and `id` are provided, the datasource will return an error.
	Id pulumi.StringPtrInput `pulumi:"id"`
	// Name of an existing NAT gateway rule that you want to search for.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Nat Gateway's UUID.
	NatgatewayId pulumi.StringInput `pulumi:"natgatewayId"`
}

func (GetNatgatewayRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNatgatewayRuleArgs)(nil)).Elem()
}

// A collection of values returned by getNatgatewayRule.
type GetNatgatewayRuleResultOutput struct{ *pulumi.OutputState }

func (GetNatgatewayRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetNatgatewayRuleResult)(nil)).Elem()
}

func (o GetNatgatewayRuleResultOutput) ToGetNatgatewayRuleResultOutput() GetNatgatewayRuleResultOutput {
	return o
}

func (o GetNatgatewayRuleResultOutput) ToGetNatgatewayRuleResultOutputWithContext(ctx context.Context) GetNatgatewayRuleResultOutput {
	return o
}

func (o GetNatgatewayRuleResultOutput) DatacenterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.DatacenterId }).(pulumi.StringOutput)
}

// Id of the NAT gateway rule
func (o GetNatgatewayRuleResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Name of the NAT gateway rule
func (o GetNatgatewayRuleResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o GetNatgatewayRuleResultOutput) NatgatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.NatgatewayId }).(pulumi.StringOutput)
}

// Protocol of the NAT gateway rule. Defaults to ALL. If protocol is 'ICMP' then targetPortRange start and end cannot be set.
func (o GetNatgatewayRuleResultOutput) Protocol() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.Protocol }).(pulumi.StringOutput)
}

// Public IP address of the NAT gateway rule. Specifies the address used for masking outgoing packets source address field. Should be one of the customer reserved IP address already configured on the NAT gateway resource
func (o GetNatgatewayRuleResultOutput) PublicIp() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.PublicIp }).(pulumi.StringOutput)
}

// Source subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets source IP address.
func (o GetNatgatewayRuleResultOutput) SourceSubnet() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.SourceSubnet }).(pulumi.StringOutput)
}

// Target port range of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on destination port. If none is provided, rule will match any port
func (o GetNatgatewayRuleResultOutput) TargetPortRanges() GetNatgatewayRuleTargetPortRangeArrayOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) []GetNatgatewayRuleTargetPortRange { return v.TargetPortRanges }).(GetNatgatewayRuleTargetPortRangeArrayOutput)
}

// Target or destination subnet of the NAT gateway rule. For SNAT rules it specifies which packets this translation rule applies to based on the packets destination IP address. If none is provided, rule will match any address.
func (o GetNatgatewayRuleResultOutput) TargetSubnet() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.TargetSubnet }).(pulumi.StringOutput)
}

// ype of the NAT gateway rule.
func (o GetNatgatewayRuleResultOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v GetNatgatewayRuleResult) string { return v.Type }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetNatgatewayRuleResultOutput{})
}
